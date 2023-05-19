# import libraries
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from bs4 import BeautifulSoup
import regex as re

# Chrome driver
driver = webdriver.Chrome('C:/Web Scraping course/chromedriver.exe')

# Directly enter your desired url and login manually and avoid security verifications.
driver.get('https://www.linkedin.com/')
time.sleep(10)

signin = driver.find_element(By.XPATH, '/html/body/nav/div/a[2]')
signin.click()
time.sleep(2)

email = driver.find_element(By.XPATH, '//*[@id="username"]')
email.send_keys('your login id')
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys('your password')
sign_in = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in.send_keys(Keys.ENTER)
time.sleep(5)

# dictionary with the job details
job_list = {'job_link' : [], 'job_role' : [], 'company' : [], 'location' : []}

# to get the last date.
a = str(soup.find_all('ul', class_ = 'artdeco-pagination__pages artdeco-pagination__pages--number')[0].find_all('li')[-1])
last_page = re.search(r'data-test-pagination-page-btn=\"([0-9]+)', a).group(1)

# BeautifulSoup to extract the attributes.
# Selenium to navigate to next page.
for i in range(1, int(last_page)):
    time.sleep(5)
    html_source = driver.execute_script("return document.documentElement.outerHTML")
    soup = BeautifulSoup(html_source, 'lxml')
    time.sleep(2)
    postings = soup.find_all('div', class_ = 'flex-grow-1 artdeco-entity-lockup__content ember-view')
    for post in postings:
        job_list['job_role'].append(post.find('a').text.strip())
        job_list['job_link'].append('https://www.linkedin.com'+ post.find('a').get('href'))
        job_list['company'].append(post.find('span', class_ = 'job-card-container__primary-description').text.strip())
        job_list['location'].append(post.find('li', class_ = 'job-card-container__metadata-item').text.strip())
    if (i != int(last_page)):
        a = soup.find('li', {'data-test-pagination-page-btn' : str(i+1)})
        if a:
            next_page_ember = re.search(r'ember[0-9]+', str(a)).group()
        else:
            b = str(soup.find_all('li', class_ = 'artdeco-pagination__indicator artdeco-pagination__indicator--number ember-view'))
            next_page_ember = 'ember'+re.search(r'([0-9]+)"><button aria-label="Page '+str(i+1)+'"', b).group(1)    
        driver.find_element(By.XPATH, '//*[@id="'+ str(next_page_ember) + '"]').click()
		
# Dict to DataFrame
import pandas as pd
job_openings = pd.DataFrame(job_list)

# Creating xlsx sheet
job_openings.to_excel('LinkedIn Job Openings.xlsx')