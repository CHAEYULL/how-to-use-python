#pip3 install requests
#sudo pip install requests
#sudo pip3 install requests
import requests
#pip install bs4
from bs4 import BeautifulSoup
import json
import time

data = requests.get('https://api-gateway.coinone.co.kr/exchange/chart/v1/KRW/ETH?lastDt=1689249600000&interval=1H&1710126620947')

딕셔너리 = json.loads(data.content)
for i in range(100):
    시간 = 딕셔너리['body']['candles'][i]['dt']
    realTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(시간/1000)) 
    print(realTime)

