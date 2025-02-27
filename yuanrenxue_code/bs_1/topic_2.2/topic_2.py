import time

import requests

import execjs

ctx = execjs.compile(open('topic_2.js').read())

aa = 0


def topci_2():
    global aa
    for i in range(1,6):
        # ctx = execjs.compile(open('md5_mg.js').read())
        t = int(time.time() * 1000)
        print(t)
        result = ctx.call("aa", t)
        headers = {
            "accept": "application/json, text/javascript, */*; q=0.01",
            "accept-language": "zh-CN,zh;q=0.9",
            "priority": "u=0, i",
            "referer": "https://match.yuanrenxue.cn/match/2",
            "sec-ch-ua": "\"Not(A:Brand\";v=\"99\", \"Google Chrome\";v=\"133\", \"Chromium\";v=\"133\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "cookie":f"m={result}|{t}",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
            "x-requested-with": "XMLHttpRequest"
        }
        url = "https://match.yuanrenxue.cn/api/match/2"
        params = {
            "page": i
        }
        response = requests.get(url, headers=headers, params=params)
        a = sum([i['value'] for i in response.json()['data']])
        aa += a
        print(a)

if __name__ == '__main__':
    topci_2()
    print(aa)