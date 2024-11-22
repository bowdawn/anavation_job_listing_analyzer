from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import json
import time
import concurrent.futures
from tqdm import tqdm 
import os

def init_driver():
    driver = webdriver.Chrome()
    return driver

def extract_job_content(job_data):
    driver = init_driver()
    job_url = job_data['link']
    try:
        driver.get(job_url)
        time.sleep(3)  
        content_element = driver.find_element(By.CLASS_NAME, "content")
        content = content_element.text.strip() if content_element else "Content not found"
        job_data['content'] = content 
    except Exception as e:
        job_data['content'] = f"Error: {str(e)}"
    finally:
        driver.quit()
    return job_data

html_file = "./generated/anavation_job_openings.html"
with open(html_file, "r", encoding="utf-8") as file:
    page_source = file.read()
soup = BeautifulSoup(page_source, "html.parser")

job_listings = []

for team_section in soup.find_all('ul', class_='lever-team'):
    team_name = team_section.find('h4', class_='lever-team-title').text.strip()
    for job_item in team_section.find_all('li', class_='lever-job'):
        job_data = {
            'team': team_name,
            'title': job_item.find('a', class_='lever-job-title').text.strip(),
            'link': job_item.find('a', class_='lever-job-title')['href'],
            'location': job_item.find('span', class_='lever-job-tag').text.strip(),
            'department': job_item['data-department'],
            'work_type': job_item['data-work-type'],
            'content': '' 
        }
        job_listings.append(job_data)

with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    results = list(tqdm(executor.map(extract_job_content, job_listings), total=len(job_listings), desc="Extracting Content"))

directory_path = "./generated"
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

output_file = 'job_listings_with_content.json'
file_path = os.path.join(directory_path, output_file)

with open(file_path, "w", encoding="utf-8") as file:
    json.dump(results, file, indent=4)

print(f"Data has been successfully extracted and saved to {output_file}")
