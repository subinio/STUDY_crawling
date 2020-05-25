import requests
from bs4 import BeautifulSoup

#response = requests.get('https://www.acmicpc.net/problem/tags')                ##응답 객체
#response = requests.get('https://www.acmicpc.net/problem/tags').ok             ##사용 가능한지 확인
#response = requests.get('https://www.acmicpc.net/problem/tags').status_code    ##응답 상태 코드
#response = requests.get('https://www.acmicpc.net/problem/tags').content        ##응답받은 원본 데이터들
response = requests.get('https://www.acmicpc.net/problem/tags').text                           ##응답받은 문자형식의 데이터들

#print(response)


##html 코드 전체 가져오기
soup = BeautifulSoup(response, 'html.parser')    

#print(soup)


# 원하는 부분을 겨냥
tags = soup.select('.table-responsive tbody tr a[href*=problem]')

## a[속성*=str]  --> a태그 중 속성에 str문자열이 포함된 모든 태그를 의미


##파싱
for x in tags:
    print(x.text)




