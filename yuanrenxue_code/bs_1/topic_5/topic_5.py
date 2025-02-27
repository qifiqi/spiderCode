import time

import requests

import execjs

data = []
def req(page):
    _t = time.time()
    m_t = int(_t * 1000)
    f_t = int(_t) * 1000
    topic_5 = execjs.compile(open("./m_f_md5.js", 'r').read())

    m_md5 = topic_5.call('md5', m_t, -389564586, -660478335, -405537848, 1)
    t_md5 = topic_5.call('md5', f_t, 8821003647, -172015004, 461512024, 1)
    _pr = f'{t_md5},0dd63dd002dfe444989f6b3823ebe3fb,cfbe95009118734323925a1333c3dd0d,874fd36c99ac55352d31b578c344c6cc,{m_md5}'
    _aes = topic_5.call('aes', _pr, str(m_t))

    headers = {
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-language": "zh-CN,zh;q=0.9",
        "cache-control": "no-cache",
        "pragma": "no-cache",
        "priority": "u=0, i",
        "referer": "https://match.yuanrenxue.cn/match/5",
        "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "\"macOS\"",
        "sec-fetch-dest": "empty",
        "cookie":f"m={m_md5}; RM4hZBv0dDon443M={_aes}",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
        "x-requested-with": "XMLHttpRequest"
    }
    url = "https://match.yuanrenxue.cn/api/match/5"
    params = {
        "page": page,
        "m": m_t,
        "f": f_t
    }
    response = requests.get(url, headers=headers, params=params)
    json_data = response.json()
    data.extend(json_data['data'])
    print(json_data)


if __name__ == '__main__':
    from collections import Counter

    for i in range(1, 6):
        req(i)

    _data = sorted(data,key=lambda x:x['value'],reverse=True)

    print(sum([i['value'] for i in _data[:5]]))
