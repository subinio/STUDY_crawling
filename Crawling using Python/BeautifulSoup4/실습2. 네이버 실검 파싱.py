import requests
from bs4 import BeautifulSoup

## 응답객체
response = requests.get('https://www.naver.com').text   

##html 코드 전체 가져오기
soup = BeautifulSoup(response, 'html.parser')    

# 원하는 부분을 겨냥
tags = soup.select('span.ah_k')

##파싱
for x in tags:
    print(x.text)




