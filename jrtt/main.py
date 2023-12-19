import requests
import execjs
cook = '__ac_signature=_02B4Z6wo00f01U7VpuQAAIDCc3y8ece7lcVO9aJAADbQ50; tt_webid=7312051802298746431; ttcid=72039574dd31445faa4bd6a59dd71a5735; s_v_web_id=verify_lq3qiz1u_OA5IbjKH_KAlL_4fnz_ArJ4_ryGU7mZNe1UB; local_city_cache=%E8%A5%BF%E5%AE%89; _ga=GA1.1.237048523.1702469741; csrftoken=73a6ed13015297b9ebeba9dd7bd1e677; msToken=P0rmJdeot5T7l2dge0ma4MR8uKidFiV3uOei_xp-P4y2ZpJccaArgImySr9GmuhwwcpuNNe_49E7WYlKkxA9K2J62R5tY1xGFvymdq42; _ga_QEHZPBE5HH=GS1.1.1702995822.5.1.1702996166.0.0.0; tt_scid=Zx7cuNwk.CqgxwslVepFOx01ECDStAfDnlykz3UjAXSmnAKyFzG0sjBGw6NqRSfHc205; ttwid=1%7C67PbDBTA9bpdV3ysvzTCb_PgoldQYdmmctHWFw-sqpU%7C1702996166%7C3dec8b6fce1db3f9ea9acab78efecc65a4d272c44e9cc52c55d82b92ab83bcf9'
headers = {
    "authority": "www.toutiao.com",
    "accept": "application/json, text/plain, */*",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "referer": "https://www.toutiao.com/?source=m_redirect&W2atIF=1",
    "sec-ch-ua": "\"Not_A Brand\";v=\"8\", \"Chromium\";v=\"120\", \"Google Chrome\";v=\"120\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    'Cookie':cook,
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}
with open('jrtt.js', 'r', encoding='utf-8') as f:
    jstext = f.read()

ctx = execjs.compile(jstext)
a = 'https://www.toutiao.com/hot-event/hot-board/?origin=toutiao_pc'
result = ctx.call('get_signature', cook,a)
_signature = result
url = "https://www.toutiao.com/hot-event/hot-board/"
params = {
    "origin": "toutiao_pc",
    "_signature": _signature
}
response = requests.get(url, headers=headers, params=params)

print(response.text)
print(response)