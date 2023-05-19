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

## Contributions
Contributions are welcome! If you find any issues or want to enhance the functionality, feel free to open a pull request.
