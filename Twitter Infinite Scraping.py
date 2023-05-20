# import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup


# Celebrity that we are looking for
celebrity = 'The Rock'

# Specify the path to the chromedriver executable
driver_path = 'C:/Web Scraping course/chromedriver.exe'

# Create a Service object
service = Service(driver_path)

# Create a Chrome WebDriver instance
driver = webdriver.Chrome(service=service)


# Twitter login
driver.get('https://twitter.com/i/flow/login')
time.sleep(10)
login = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')
login.send_keys('your email id')
next_button = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div').click()
time.sleep(5)
password_box = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')
password_box.send_keys('your password')
login_button = driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')
login_button.click()


# Searching for celebrity in person tab.
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')))
search = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input')
search.send_keys(celebrity)
search.send_keys(Keys.ENTER)
time.sleep(5)
people = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[1]/div[1]/div[2]/nav/div/div[2]/div/div[3]/a/div/div').click()
time.sleep(5)
profile = driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span').click()
time.sleep(5)


# using BeautifulSoup to extract the tweets from the starting till the end using infinite scrolling.
last_height = driver.execute_script('return document.body.scrollHeight')
tweets = []
while True:
    html_source = driver.execute_script("return document.documentElement.outerHTML")
    time.sleep(1)
    soup = BeautifulSoup(html_source, 'lxml')
    time.sleep(1)
    postings = soup.find_all('div', class_ = 'css-901oao r-1nao33i r-37j5jr r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0')
    for post in postings:
        tweets.append(post.text)
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(2)
    tweets2 = list(set(tweets))
    if len(tweets2) > 200:
        break
    new_height = driver.execute_script('return document.body.scrollHeight')
    if new_height == last_height:
        break
    last_height = new_height
	
	
tweets = list(set(tweets)) # removing duplicate tweets
df = pd.DataFrame(tweets, columns = ['Tweets'])
df.to_excel('tweets.xlsx')