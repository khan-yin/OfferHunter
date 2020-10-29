// pages/social/social.js
// import uCharts from '../../ucharts/u-charts'
// import VCharts from 'v-charts'
// import wxcharts from '../../echarts/wxcharts'

let wxCharts = require('../../echarts/wxcharts.js'); // 引入wx-charts.js文件

let columnChart = null;
Page({
  /**
   * 页面的初始数据
   */
  data: {
    imageUrl:[
      "../../static/img/qq.jpg",
      "../../static/img/bytedance.jpg",
      "../../static/img/ms.jpg"
    ],
    listData:[],
    current:'links',
    indicatorDots: true,
    vertical: false,
    autoplay: false,
    interval: 2000,
    duration: 500,
    newList:[
      {
        title:"JAVA程序员就业真的很难吗？",
        like: 999,
        comments:999,
        time: "2020/10/20",
        author: "这个是老话题了，Java程序员远远没有饱和，年薪10万+元是很正常的一个薪酬水平。现在Java程序员挺多的...",
        imgUrl: "https://pic4.zhimg.com/v2-22a87eaee322d4b8f6d421975a134241_1440w.jpg?source=172ae18b",
        isTop:true
      },
      {
        title:"2020年，web前端还好找工作吗？",
        like: 999,
        comments:999,
        time: "2020/10/20",
        author: "一个寒假回来，好几个同学都来问我或者自己开始学起了前端，前端入门虽然简单，但是想要做好很难,再这几年 MVVM 框架的大肆流行...",
        imgUrl: "https://pic2.zhimg.com/v2-0c3c367d8a30ff47ca0309a12342b1fc.webp",
        isTop:true
      },
      {
        title:"吴恩达的机器学习课程质量如何？",
        like: 999,
        comments:999,
        time: "2020/10/20",
        author: "吴恩达的机器学习课程笼统的讲可以说有两门课，一门是Cousera上的课程Machine Learning | Coursera，一门是斯坦福大学的课程CS229: Machine Learning。",
        imgUrl: "https://pic2.zhimg.com/80/v2-a4056e591abd322590b53eec85cecb9a_720w.jpg?source=1940ef5c",
        isTop:false
      },
      {
        title:"计算机视觉是否已经进入瓶颈期？",
        like: 999,
        comments:999,
        time: "2020/10/20",
        author: "谢邀, 其实这个问题也是我近段时间一直在思考的问题. 昨天刚在组里做了个ECCV'16 Recap, 我的观点是：计算机视觉在人工智能和深度学习的大背景下方兴未艾",
        imgUrl: "https://pic3.zhimg.com/80/v2-6b5a2e93b36f744f7521d9dab1d13aeb_720w.jpg?source=1940ef5c",
        isTop:false
        
      },
      {
        title:"在网易有道做语音算法工程师是一种怎样的体验？",
        like: 999,
        comments:999,
        time: "2020/10/20",
        author: "说起网易有道与AI语音技术相关的产品，大家或许都不陌生，许多人可能不会想到，有道AI语音背后的团队非常年轻：成立不到两年，大部分都是应届生，来自知名语音实验室，或者海外高校深造项目。",
        imgUrl: "https://pic4.zhimg.com/80/v2-2853ba74d69368a74c07c9fc76aa5e14_720w.jpg",
        isTop:false
        
      },
    ],
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
      columnChart = new wxCharts({
      canvasId: 'columnCanvas',
      type: 'column',
      animation: true,
      categories: ["Java后端","数据挖掘","图像算法工程师","互联网产品经理"],
      series: [{
          name: '就业岗位',
          data: [18234,15230,8934,13425],
          format: function (val, name) {
              return val;
          }
      }],
      yAxis: {
          format: function (val) {
              return val;
          },
          title: '从业人数',
          min: 0
      },
      xAxis: {
          disableGrid: false,
          type: 'calibration'
      },
      extra: {
          column: {
              width: 15
          }
      },
      width: 350,
      height: 200,
    });
  },
  
})
