//index.js
//获取应用实例
const app = getApp()

Page({
  data: {
    option1: [
      { text: '城市', value: "" },
      { text: '北京', value: "010" },
      { text: '广州', value: "050020" },
      { text: '上海', value: "020" },
      { text: '深圳', value: "050090" },
      { text: '武汉', value: "170020" },
      { text: '杭州', value: "070020"},
    ],
    option2: [
      { text: '薪水', value: "" },
      { text: '10-15万', value: "10$15" },
      { text: '15-20万', value: "15$20" },
      { text: '20-30万', value: "20$30" },
      { text: '30-50万', value: "30$50" },
    ],
    option3: [
      { text: '典型行业', value: "" },
      { text: 'Java后端', value: 'java' },
      { text: '数据挖掘', value: '数据挖掘' },
      { text: '图像算法工程师', value: '图像算法工程师' },
      { text: '互联网产品经理', value: '互联网产品经理' },
    ],
    curPage:0,
    city: "",
    salary: '',
    keyword:'',
    key:'',
    value:"",
    jobs:[]
  },
  onLoad:function(){
    this.setData({
      key:'java'
    })
    this.getJob()
    this.setData({
      key:''
    })
  },

  getspecialjob(){
    console.log(this.data.key)
    wx.request({
      url: 'http://khany.top:5000/Getjob',
      method: 'GET',
      data: {
        'key': this.data.keyword,
        'curPage': this.data.curPage,
        'city': this.data.city,
        'salary': this.data.salary
      },
      success:res=>{
         if (res.data.length != 0) {
          // 重置一下当前长度
          this.data.jobs = []
          console.log(res)
          for (let item of res.data) {
              this.data.jobs.push({
                  title : item.title,
                  company: item.company,
                  require_list:item.require_list,
              })
          }

          console.log(this.data.jobs)
          this.setData({
              jobs: this.data.jobs,
          })
          console.log(this.data.jobs)
          console.log(this.data.jobs.length)
      }
    }
    })
  },

  getJob:function(){
    console.log(this.data.key)
    wx.request({
      url: 'http://khany.top:5000/Getjob',
      method: 'GET',
      data: {
        'key': this.data.key,
        'curPage': this.data.curPage,
        'city': this.data.city,
        'salary': this.data.salary
      },
      success:res=>{
         if (res.data.length != 0) {
          // 重置一下当前长度
          this.data.jobs = []
          console.log(res)
          for (let item of res.data) {
              this.data.jobs.push({
                  title : item.title,
                  company: item.company,
                  require_list:item.require_list,
              })
          }

          console.log(this.data.jobs)
          this.setData({
              jobs: this.data.jobs,
          })
          console.log(this.data.jobs)
          console.log(this.data.jobs.length)
      }
    }
  })

},

  search(event){
    let value = event.detail
    console.log(value)
    this.setData({
        key: value
    })
    // wx.showLoading({
    //     title: '搜索中',
    // })
    this.getJob()
  }
})


