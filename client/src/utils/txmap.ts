import {ref} from "vue";
export const mapContainer = ref()
export function initMap() {
    let TMap = (window as any).TMap;
    const init = () => {
        //定义地图中心点坐标
        let center = new TMap.LatLng(39.984120, 116.307484)
        console.log(center)
        //定义map变量，调用 TMap.Map() 构造函数创建地图
        let map = new TMap.Map(document.getElementById('mapContainer'), {
            center: center,//设置地图中心点坐标
            zoom: 17.2,   //设置地图缩放级别
        });

    }
}
