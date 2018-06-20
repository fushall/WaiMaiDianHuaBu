//app.js
import me from 'utils/me.js';
import cache from 'utils/cache.js';

App({
  onLaunch: function () {
    let app = this
    let shops = cache.read('shops')
    if (shops) {
      app.globalData.shops = shops
    } else {
      app.globalData.shops = [{
        name: '正在更新数据...',
        phonenumbers: ['23333333'],
        description: '描述',
        categories: null
      }]
    }
    // 获取数据
    wx.request({
      url: 'https://tesnot.nmxxy.cn/shops',
      success: function (res) {
        wx.showToast({
          title: '数据更新成功',
          icon: 'success',
          duration: 850
        })
        app.globalData.shops = res.data
        // 存入缓存
        cache.write('shops', res.data)
      }
    })

    wx.login({
      success: function (res) {
        let code = res.code
        wx.request({
          url: 'https://tesnot.nmxxy.cn/login/',
          data: { js_code: res.code },
          method: 'POST',
          success: function (res) {
            let openid = res.data.openid
            let cookie = res.header['Set-Cookie']
            me.writeCookie(cookie)

          }
        })
      }
    })
    // 登录
   
  },
  globalData: {
    userInfo: null,
    currentShop: null,
    shops: null

  }
})