(function () {
    var open = window.XMLHttpRequest.prototype.open;
    window.XMLHttpRequest.prototype.open = function (method, url, async) {
        if (url.indexOf("login") != -1) {
            debugger;
        }
        return open.apply(this, arguments);
    };
})();
