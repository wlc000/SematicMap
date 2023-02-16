<template>
  <a-layout style="width: 79vw">
    <a-layout>
      <a-layout-content>
        <div id="container"></div>
      </a-layout-content>
      <a-layout-sider>
        <a-row @click="selectPathMode">
          <a-button>
            选择路径
          </a-button>
        </a-row>
        <a-row>
          <a-button @click="exitSelectPathMode">
            退出选择
          </a-button>
        </a-row>
        <a-row>
          <a-button @click="onSubmit">
            确认选择
          </a-button>
        </a-row>
        <a-row>
          <a-button @click="onReset">
            重新选择
          </a-button>
        </a-row>
        <div>
          <span>已选路径id：</span>
          {{ this.selectedPathList }}
        </div>
        <div>
          <span>可选路径id：</span>
          {{ this.selectedAble }}
        </div>
        <br><br><br><br>
        <div>
          <span>预测结果：</span>
          {{ this.prediction }}
        </div>
      </a-layout-sider>
    </a-layout>
  </a-layout>


</template>

<script lang="js">
import AMapLoader from '@amap/amap-jsapi-loader';
import {ref, shallowRef} from 'vue'
import mapJson from '../assets/edge.json'
import relationJson from '../assets/relation.json'
import axios from 'axios';
export default {
  name: "MapContainer",
  setup() {
    const map = shallowRef(null);
    const geojson = shallowRef(null);
    // 选择路径算法
    const selectedPathList = ref([])
    const selectedAble = ref([])
    const startPath = ref(null)
    const endPath = ref(null)
    const prediction = ref('无')
    return {
      map,
      geojson,
      selectedPathList,
      selectedAble,
      startPath,
      endPath,
      prediction
    }
  },
  methods: {
    initMap() {
      AMapLoader.load({
        key: "cd786e577c42a988bfb74d9f194235f5",             // 申请好的Web端开发者Key，首次调用 load 时必填
        version: "2.0",      // 指定要加载的 JSAPI 的版本，缺省时默认为 1.4.15
        plugins: ['AMap.Scale', 'AMap.GeoJSON', 'AMap.Polyline', 'AMap.OverlayGroup', 'AMap.InfoWindow'],       // 需要使用的的插件列表，如比例尺'AMap.Scale'等
      }).then((AMap) => {
        this.map = new AMap.Map("container", {  //设置地图容器id
          viewMode: "3D",    //是否为3D地图模式
          zoom: 7,           //初始化地图级别
          center: [-8.640433, 41.1670937], //初始化地图中心点位置
        });
        this.loadGeoJson()
      }).catch((e) => {
        console.log(e)
      })
    },
    loadGeoJson() {
      // load geojson
      let line_id = 0
      this.geojson = new AMap.GeoJSON({
        geoJSON: mapJson,
        getPolyline: function (geojson, lnglats) {
          return new AMap.Polyline({
            path: lnglats,
            strokeColor: "blue",
            strokeWeight: 4,
            strokeOpacity: 0.9,
            zIndex: 50,
            bubble: true,
            extData: {
              id: line_id++
            }
          })
        }
      })
      // console.log(this.geojson)
      this.bindClickEvent()
      this.map.add(this.geojson)
      // 缩放地图到合适的视野级别
      this.map.setFitView()
    },
    bindClickEvent() {
      let PolyLines = this.geojson.getOverlays()
      for (let o in PolyLines) {
        PolyLines[o].on('click', this.showInfoView)
      }
    },
    refPath() {
      let PolyLines = this.geojson.getOverlays()
      for (let o in PolyLines) {
        let e = PolyLines[o]
        let id = e.getExtData()["id"]
        if (this.selectedPathList.includes(id)) {
          e.setOptions({
            strokeColor: 'black'
          })
          e.off('click', this.selectOnePath)
          e.show()
        } else if (this.selectedAble.includes(id)) {
          e.setOptions({
            strokeColor: 'green'
          })
          e.show()
        } else {
          e.hide()
        }
      }
    },
    bindSelectEvent() {
      let PolyLines = this.geojson.getOverlays()
      for (let o in PolyLines) {
        PolyLines[o].on('click', this.selectOnePath)
      }
    },
    unbindSelectEvent() {
      let PolyLines = this.geojson.getOverlays()
      for (let o in PolyLines) {
        PolyLines[o].off('click', this.selectOnePath)
      }
    },
    showInfoView(e) {
      //构建信息窗体中显示的内容
      let info = [];
      info.push("<br>路段</br>")
      info.push("<p>id:" + e.target.getExtData()["id"] + "</p>")
      info.push("<p class='input-item'>点击位置经度:" + e.lnglat.getLng() + ", 纬度:" + e.lnglat.getLat() + "</p>")

      let infoWindow = new AMap.InfoWindow({
        content: info.join("")  //使用默认信息窗体框样式，显示信息内容
      });
      infoWindow.open(this.map, this.map.getCenter());
    },
    selectOnePath(e) {
      let id = e.target.getExtData()["id"]
      this.selectedPathList.push(id)
      this.selectedAble = relationJson[id]
      this.refPath()
    },
    selectPathMode() {
      // this.selectedPathList = []
      // this.selectedAble = []
      this.startPath = null
      this.endPath = null
      this.bindSelectEvent()
    },
    exitSelectPathMode() {
      this.unbindSelectEvent()
    },
    onSubmit() {
      this.prediction = '(请稍等)'
      const path = 'http://localhost:5000/eta';
      let payload = {
        path:this.selectedPathList,
      }
      axios.post(path,payload)
          .then((res) => {
              this.prediction = res.data.prediction;
          })
          .catch((error) => {
              // eslint-disable-next-line
              console.error(error);
          });
    },
    onReset() {
      this.prediction = '无'
      this.selectedPathList = []
      this.selectedAble = []
      this.initMap()
    }
  },
  mounted() {
    //DOM初始化完成进行地图初始化
    this.initMap()
    //this.loadGeoJson();
  }
}
</script>

<style scoped>
#container {
  padding: 0px;
  margin: 0px;
  width: 70vw;
  height: 800px;
}

.ant-layout-sider {
  background: #f9f9f9;
}
</style>
