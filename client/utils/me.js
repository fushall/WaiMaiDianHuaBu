"use strict;"

import cache from 'cache.js'

/*
  登陆，
  个人信息，
 */

function writeCookie(cookie) {
  cache.write('cookie', cookie)
}
function readCookie() {
  return cache.read('cookie')
}

function setHeaderCookie() {
  return {
    Cookie: readCookie()
  }
}


module.exports = {
  writeCookie: writeCookie,
  setHeaderCookie: setHeaderCookie
}