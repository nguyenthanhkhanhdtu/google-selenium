from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument('--no-sandbox')
driver = webdriver.Chrome(executable_path='/usr/bin/google-chrome')
driver.get("https://www.google.com/search?q=paypal.com")
results_list = driver.find_elements_by_tag_name('cite')
options = webdriver.ChromeOptions()
options.add_argument(f'--user-data-dir={user_data_dir_path}')
options.add_argument(f'--profile-directory={profile_dir_name}')

chrome_service = fs.Service(executable_path='/usr/bin/chromedriver')
driver = webdriver.Chrome(options=options, service=chrome_service)
#driver.get(url)
driver.execute_script(`window.open('${url}');`)

time.sleep(30)
driver.close()