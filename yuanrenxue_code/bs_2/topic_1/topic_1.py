import requests
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import hashlib
import time

from Crypto.Util.Padding import pad
from Crypto.Cipher import AES


def gets(d):
    e = int(time.time())
    g = '666yuanrenxue66'

    key = hashlib.md5(g.encode()).digest()  # 使用 MD5 生成 16 字节的密钥
    cipher = AES.new(key, AES.MODE_ECB)
    data = str(e) + str(d)
    padded_data = pad(data.encode(), AES.block_size)
    h = cipher.encrypt(padded_data)
    print(h.decode('utf-8'))
    md5 = hashlib.md5()
    md5.update(h)
    token = md5.hexdigest()

    j = {
        'page': str(d),
        'token': token,
        'now': e
    }
    return j



# for i in range(1,6):
#     print(requests.post(url='https://match2023.yuanrenxue.cn/api/match2023/1', data=gets(i)).text)
#     break