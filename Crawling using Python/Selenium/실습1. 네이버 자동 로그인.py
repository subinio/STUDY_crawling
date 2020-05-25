from selenium import webdriver
import time 

#크롬 드라이버로 크롤러 객체 설정
driver = webdriver.Chrome('C:\chromedriver.exe')                ## chromedriver.exe 파일 위치
driver.get('https://nid.naver.com/nidlogin.login')              ## 크롤링 할 웹페이지 설정 (네이버 로그인 페이지)
time.sleep(0.5)

driver.find_element_by_css_selector('input#id').send_keys('본인의 아이디를 입력하세요')     ## 아이디 입력
time.sleep(1)
driver.find_element_by_css_selector('input#pw').send_keys('본인의 비밀번호를 입력하세요')     ## 비밀번호 입력
time.sleep(1)
driver.find_element_by_css_selector('input.btn_global').click()

