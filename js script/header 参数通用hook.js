(function () {
    // 头部参数 请求对象当中的 设胃请求头部参数
   var org = window.XMLHttpRequest.prototype.setRequestHeader;
   window.XMLHttpRequest.prototype.setRequestHeader = function (key, value) {
       // 关键字 在请求当中发现有键是Authorization 断点
       if (key == 'Authorization') {
            debugger;
        }
       return org.apply(this, arguments);
   }
})();
