// JavaScript eval() 函数的作用是计算 JavaScript 字符串，并把它作为脚本代码来执行。如果参数是一个表达式，eval() 函数将执行表达式。如果参数是 Javascript 语句，eval() 将执行 Javascript 语句，经常被用来动态执行 JS。以下代码执行后，之后所有的 eval() 操作都会在控制台打印输出将要执行的 JS 源码：
(function() {
    // 保存原始方法
    window.__cr_eval = window.eval;
    // 重写 eval
    var myeval = function(src) {
        console.log(src);
        console.log("=============== eval end ===============");
        debugger;
        return window.__cr_eval(src);
    }
    // 屏蔽 JS 中对原生函数 native 属性的检测
    var _myeval = myeval.bind(null);
    _myeval.toString = window.__cr_eval.toString;
    Object.defineProperty(window, 'eval', {
        value: _myeval
    });
})();
