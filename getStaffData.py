from selenium import webdriver  # 웹수집 자동화를 위한 크롬 드라이버 호출
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
# browser = webdriver.Chrome(options=options)
driver = webdriver.Chrome(r'/Applications/chromedriver')  # 크롬 드라이버 경로 설정

driver.get("https://info.sunmoon.ac.kr/PageN/content/activity_10.aspx?ca=001")

week = driver.find_element_by_class_name("tit_day")
print(week.text)

date = []
menu = []

for i in range(1,10,2):
  q = '//*[@id="tabCon1"]/div/table/tbody[1]/tr['+str(i)+']/th'
  q2 = '//*[@id="tabCon1"]/div/table/tbody[1]/tr['+str(i)+']/td[2]'
  mon = driver.find_element_by_xpath(q)
  print(mon.text)
  date.append(mon.text)
  content = driver.find_element_by_xpath(q2).text.split("\n")
  menu.append(content)
print("menu =>>> ",menu)
df = pd.DataFrame(date)
df.columns = ['date']
df['menu'] = menu
df.to_csv("staff.csv", encoding='utf-8')