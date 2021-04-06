const order = ['demo1', 'demo2', 'demo3']

Page({
  onShareAppMessage() {
    return {
      title: 'swiper',
      path: 'page/component/pages/swiper/swiper',

      title: 'scroll-view',
      path: 'page/component/pages/scroll-view/scroll-view'
    }
  },

  data: {
    lists:[],
    indicatorDots: true,
    toView: 'green'
    
  },

  onLoad: function (options) {
    wx.request({
      url: 'http://127.0.0.1:8000/api/courses/home/',
      success: (res)=>{
        console.log(res.data.recommended_courses)
        this.setData({
          lists:res.data.recommended_courses
        })
      }
    })
  },
  

  

})