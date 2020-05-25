from selenium import webdriver
import time 

#크롬 드라이버로 크롤러 객체 설정
driver = webdriver.Chrome('C:\chromedriver.exe')                ## chromedriver.exe 파일 위치
home = 'https://comic.naver.com/webtoon/list.nhn?titleId=318995&weekday=fri'
driver.get(home)                                                ## 크롤링 할 웹페이지 설정
time.sleep(2)

for i in range(5):              ## 페이지 수
    titles = driver.find_elements_by_css_selector('td.title a')     ## 태그를 통해 긁어오기
    button = driver.find_element_by_css_selector('a.next')

    for title in titles:
        print(title.text)
        
    button.click()    ##다음 페이지로 이동 버튼 클릭 
   
