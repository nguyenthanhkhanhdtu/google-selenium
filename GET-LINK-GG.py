import csv
from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import itertools
import random
listlong = []
            
driver = webdriver.Chrome('D:/Tools/chromedriver.exe')
driver.get('https://www.google.com/search?q=&num=200&start=0&sourceid=chrome')
time.sleep(random.randint(10,11))
search_input = driver.find_element_by_name('q')
search_input.send_keys('site:paypal.com AND VN')
time.sleep(3)
search_input.send_keys(Keys.RETURN)
time.sleep(3)
            # grab all linkedin profiles from first page at Google
profiles = driver.find_elements_by_xpath('//*[@class="r"]/a[1]')
time.sleep(8)
profiles = [profile.get_attribute('href') for profile in profiles]
listprof = profiles.copy()
listlong.extend(listprof)
print(profiles)
print("f1")
print(listprof)
print("f2")
print(listlong)
print("f3")
driver.quit()