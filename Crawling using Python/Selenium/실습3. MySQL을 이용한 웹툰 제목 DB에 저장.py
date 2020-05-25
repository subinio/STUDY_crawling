import pymysql                      #필요한 모듈
from selenium import webdriver
import time 

#DB연결에 필요한 정보들
conn = pymysql.connect(
    host='localhost',
    user= 'root',
    password='0000',     ## mysql 비밀번호
    db='webtoon',           ## DB table 이름
    charset='utf8'
)

cursor = conn.cursor()   ## DB에 연결된 객체

#크롬 드라이버로 크롤러 객체 설정
driver = webdriver.Chrome('C:\chromedriver.exe')                   ## chromedriver.exe 파일 위치
home = 'https://comic.naver.com/webtoon/list.nhn?titleId=318995&weekday=fri'
driver.get(home)                                                ## 크롤링 할 웹페이지 설정
time.sleep(2)

titles = driver.find_elements_by_css_selector('td.title a')     ## 태그를 통해 긁어오기

print(titles)

for title in titles:
    print(title.text)
    print(title.get_attribute('href'))
    SQL = "INSERT INTO `new_table`(`text1`,`text2`) VALUES('%s', '%s')" % (title.text, title.get_attribute('href'))
    cursor.execute(SQL)

conn.commit()       ## DB연결 닫기





##################################################################

# 여기서 mysql과 데이터베이스와 테이블을 미리 생성해 주어야 한다.

# cmd혹은 bash 에서 mysql root 접속 후 mysql의 root계정에 들어간 후 

# 아래와 같은 순서로 sql문 입력

# CREATE DATABASE webtoon default CHARACTER SET UTF8;
# use webtoon;
# CREATE TABLE new_table (text1 VARCHAR(1000), text2 VARCHAR(1000));

