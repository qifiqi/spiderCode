// 先保留原 constructor
// 1. 比如判断是否有该debugger词语，替换为同等长度的空格（避免判断长度）
Function.prototype.constructor_ = Function.prototype.constructor;
Function.prototype.constructor = function (a) {
    // 如果参数为 debugger，就返回空方法
    if(a.indexOf('debugger') !== -1) {
        a = a.replace(
            /debugger/,''
        )
        console.log(a)
    }
    // 如果参数不为 debugger，还是返回原方法
    return Function.prototype.constructor_(a);
}


Function.prototype.constructor.toString = function () {
    return 'function Function() { [native code] }';
};
// };true; //这里是添加条件断点内容



// 2. 如果是定时器的debugger采用以下语句
// 先保留原定时器
var setInterval_ = setInterval
setInterval = function (func, time){
    // 如果时间参数为 0x7d0，就返回空方法
    // 当然也可以不判断，直接返回空，有很多种写法
    if(time == 0x7d0)
    {
        return function () {};
    }
    // 如果时间参数不为 0x7d0，还是返回原方法
    return setInterval_(func, time)
}

// eval("debugger;");
