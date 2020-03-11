# -*- coding: utf-8 -*-
import urllib
import requests
import json

def tencent(msg):
    APPID = '2129956076'
    APPKEY = 'HZSbkoSOYR4rk4Ft'
    url = 'https://api.ai.qq.com/fcgi-bin/nlp/nlp_textchat'
    params = {
        'app_id': APPID,
        'time_stamp': str(int(time.time())),
        'nonce_str': ''.join(random.choice(string.ascii_letters + string.digits) for x in range(16)),
        'session': '10000'.encode('utf-8'),
        'question': msg.encode('utf-8')
    }
    sign_before = ''
    for key in sorted(params):
        
        sign_before += '{}={}&'.format(key, urllib.quote(params[key], safe=''))
        
    sign_before += 'app_key={}'.format(APPKEY)
​
    
    sign = hashlib.md5(sign_before.encode('UTF-8')).hexdigest().upper()
    params['sign'] = sign
    
    html = requests.post(url, data=params).json()
    return html['data']['answer']
msg= '我好看吗'
print("原话>>", msg)
res = tencent(msg)
print("腾讯>>", res)
