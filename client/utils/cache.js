
// 获取缓存信息
function getInfo() {
  try {
    return wx.getStorageInfoSync()
  }
  catch (e) {
    console.log('cache.getInfo:', e)
  }
}

// 在缓存中通过key 获取 一个值 
function read(key) {
  try {
    var value = wx.getStorageSync(key)
    return value
  }
  catch (e) {
    console.log('cache.read:', e)
  }
}

// 返回所有缓存
function readAll() {
  try {
    var cache = {}
    var res = getInfo()
    if (res && res.keys.length) {
      res.keys.forEach(function (key) {
        var value = wx.getStorageSync(key)
        if (value != undefined) cache[key] = value;
      })
      return cache
    }
    return // undefined
  }
  catch (e) {
    console.log('cache.readAll', e)
  }
}

// 写入一个缓存
function write(key, value) {
  try {
    wx.setStorageSync(key, value)
  }
  catch (e) {
    console.log('cache.write', e)
  }
}

// 将字典写入（更新）到缓存
function writeFromDict(dict) {
  try {
    dict.forEach(function (key) {
      var value = dict[key]
      if (value) writeCache(key, value)
    })
  }
  catch (e) {
    console.log('cache.writeFromDict', e)
  }
}

// 删除一条缓存数据
function remove(key) {
  try {
    wx.removeStorageSync(key)
  }
  catch (e) {
    console.log('cache.remove:', e)
  }
}

// 删除（清除）所有缓存数据
function removeAll() {
  try {
    wx.clearStorageSync()
  }
  catch (e) {
    console.log('cache.removeAll: error', e)
  }
}



module.exports = {
  // 缓存操作函数（同步）
  getInfo: getInfo,
  write: write,
  writeFromDict: writeFromDict,
  read: read,
  readAll: readAll,
  remove: remove,
  removeAll: removeAll
}