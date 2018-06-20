// pages/shops/shops.js
Page({

  /**
   * 页面的初始数据
   */
  data: {
    shops: null
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
  },
  /**
   * 列表项单击
   */
  kindToggle: function(event) {
    // 取shops列表的index
    let index = event.currentTarget.id
    let currentShop = this.data.shops[index]
    let opened = this.data.shops[index].isopen //点击时是否是打开状态
    // 当处于闭合状态的时候，这时候点击，设置状态成打开
    for (let shop of this.data.shops) {
      shop.isopen = false
    }
    // 如果点开了某个店铺，就设置当前店铺为点开的那个
    if (!opened) { // 如果点击时是打开状态，再点击就应该关闭 
      this.data.shops[index].isopen = true
    } 
    let app = getApp()
    // 设置当前店铺
    app.globalData.currentShop = currentShop
    // 更新数据
    this.setData({shops:this.data.shops})
  },
  dial: function(event) {
    let phoneNumber = event.currentTarget.id
    wx.showActionSheet({
      itemList: ['拨号', '复制'],
      success: function (res) {
        if (res.tapIndex == 0) {
          // 拨号
          wx.makePhoneCall({
            phoneNumber: phoneNumber
          })
          wx.showToast({
            title: '请稍后',
            icon: 'loading',
            duration: 1500
          })
        } else {
          // 复制
          wx.setClipboardData({
            data: phoneNumber,
            success: function(res) {
              console.log(res)
              wx.showToast({
                title: '复制成功',
                icon: 'success',
                duration: 850 
              })
            }  
          })
        }
      }
    })
  },
  gotoShop: function(event) {
    
  },
  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {

  },

  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
    //  把全局变量存储的 shops 引用到当前页面
    let app = getApp()
    this.data.shops = app.globalData.shops
    this.setData({ shops: this.data.shops })
    console.log(this.data.shops)
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  
  },

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  
  },

  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  }
})