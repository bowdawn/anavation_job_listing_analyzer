import os
from selenium import webdriver
import time


directory_path = "./generated"
if not os.path.exists(directory_path):
    os.makedirs(directory_path)
driver = webdriver.Chrome()
try:
    url = "https://anavationllc.com/careers/#job-openings"
    driver.get(url)
    time.sleep(5)
    page_source = driver.page_source
    file_path = os.path.join(directory_path, "anavation_job_openings.html")
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(page_source)
    print(f"HTML content saved to '{file_path}'.")
finally:
    driver.quit()
