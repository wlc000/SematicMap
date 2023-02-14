<script setup lang="ts">
import HelloWorld from './components/HelloWorld.vue'
import * as echarts from 'echarts'
import {EChartsType} from "echarts";
import {onMounted, Ref, ref} from "vue";
import MapContainer from "./components/MapContainer.vue";

const main_k: Ref<any> = ref()
let showChart = () => {
  // 获取DOM元素并且进行初始化
  let myChart: EChartsType;
  myChart = echarts.init(main_k.value);
  // 创建图标
  myChart.setOption({
    title: {
      text: 'ECharts 入门示例'
    },
    tooltip: {},
    xAxis: {
      data: ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
    },
    yAxis: {},
    series: [
      {
        name: '销量',
        type: 'bar',
        data: [5, 20, 36, 10, 10, 20]
      }
    ]
  })
  console.log(myChart)
}
</script>

<template>
<!--  <button @click="showChart()">点击展示图表</button>-->
<!--  <div ref="main_k" style="width: 100%; height: 40vh">HELLO</div>-->
  <MapContainer></MapContainer>
</template>

<style>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
}

.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}

.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}

#app{
  margin-left: 0;
  margin-right: 0;
}
</style>
