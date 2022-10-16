from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
#input your username
username=""
#input your password
password=""
#source website
url="https://example.com"
#set your browser
driver=webdriver.Chrome()
#reach url data
driver.get(url)
#a little time for website fully load
time.sleep(2)
#find username input form path example
user=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div[4]/div/div/div/div[1]/div[1]/input")
#send matching username
user.send_keys(username)
time.sleep(1)
#find password input form path example
pssw=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div[4]/div/div/div/div[1]/div[2]/input")
#send matching password
pssw.send_keys(password)
time.sleep(1)
#find login button path exapmle
btn=driver.find_element(By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div[4]/div/div/div/div[4]/button").click()
time.sleep(5)
#close the page
driver.close()
