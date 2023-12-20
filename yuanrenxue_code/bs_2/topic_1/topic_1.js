
call = function(d) {
    var e = Date['now']()
      , f = a('crypto-js')
      , g = '666yuanrenxue66'
      , h = f['AES']['encrypt'](e + String(d), g, {
        'mode': f['mode']['ECB'],
        'padding': f['pad']['Pkcs7']
    })
      , i = '/api/match2023/1'
      , j = {
        'page': String(d),
        'token': f['MD5'](h['toString']())['toString'](),
        'now': e
    };
    $['ajax']({
        'url': i,
        'dataType': 'json',
        'async': !![],
        'data': j,
        'type': 'POST',
        'beforeSend': function(k) {},
        'success': function(k) {
            k = k['data'];
            let l = '';
            $['each'](k, function(m, n) {
                l += '<td>' + n['value'] + '</td>';
            }),
            $('.number')['text']('')['append'](l),
            $('.page-message')['removeClass']('active'),
            $('.page-message')['eq'](parseInt(d) - 0x1)['addClass']('active');
        },
        'complete': function() {},
        'error': function() {
            failedAlert('请求失败了，生而为虫，我很抱歉~'),
            $('.page-message')['removeClass']('active'),
            $('.page-message')['eq'](0x0)['addClass']('active');
        }
    });
}
d = 1-5