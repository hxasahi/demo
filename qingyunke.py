import urllib
import json
import requests

def qingyunke(msg):
    url = 'http://api.qingyunke.com/api.php?key=free&appid=0&msg={}'.format(urllib.quote(msg))
    html = requests.get(url)
    print('')
    print(html.json()["content"])

while 1 :
    print('')
    msg = raw_input("[tips]==> Please enter:")
    if msg == quit :
        break
    qingyunke(msg)
    
    
    
