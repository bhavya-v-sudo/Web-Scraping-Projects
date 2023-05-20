# Web-Scraping-Projects

# Project - 1: 
# LinkedIn Web Scraper

This Python script allows you to scrape job openings from LinkedIn based on a job search link. It automatically collects job details such as job titles, company names, job roles, and job locations and saves them in an Excel sheet from first page till the last page.

## Installation

Clone the repository:

   git clone https://github.com/bhavya-v-sudo/Web-Scraping-Projects.git
   
## Usage:

1. Enter your LinkedIn job search link when Chrome driver is prompted.

2. The script will automatically scrape all pages of job openings and collects job details from the pages.

3. Once the scraping is complete, an Excel file named job_openings.xlsx will be generated in the project directory containing the collected job details.

## Notes:
1. This script uses Selenium and BeautifulSoup libraries to scrape LinkedIn job details. It requires a compatible WebDriver for your browser (e.g., ChromeDriver for Chrome). Ensure that you have the appropriate WebDriver installed and configured correctly.

2. The script may take some time to complete depending on the number of job openings and pages to scrape.


# Project - 2
# Twitter Web Scraping Project

This project focuses on scraping tweets from Twitter by scrolling till the end of the page using Selenium and Beautiful Soup.

## Project Overview

The goal of this project is to extract tweets from Twitter by simulating scrolling till the end of the page. Twitter's HTML structure dynamically loads new tweets as the user scrolls down. To overcome this, we utilize Selenium, a browser automation tool, to automate the scrolling process and obtain all the tweets. Beautiful Soup, a Python library, is used for parsing and extracting the desired information from the HTML.

## Prerequisites

To run this project, you need to have the following installed:

1. Python
2. Selenium
3. ChromeDriver

Note: Make sure to download the appropriate version of ChromeDriver that matches your Chrome browser version. ChromeDriver acts as a bridge between Selenium and the Chrome browser.

## Usage

The script will automate the scrolling process until all tweets are loaded. The extracted tweets will be stored in an excel or processed further according to your implementation.

# Contributions
Contributions are welcome! If you find any issues or want to enhance the functionality, feel free to open a pull request.
