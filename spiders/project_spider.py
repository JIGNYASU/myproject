import scrapy
import csv
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class ProjectSpider(scrapy.Spider):
    name = 'project'
    start_urls = ['https://hprera.nic.in/PublicDashboard']

    def parse(self, response):
        # Set up Selenium WebDriver
        chrome_options = Options()
        chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
        driver = webdriver.Chrome(options=chrome_options)

        try:
            # Open the webpage using Selenium
            driver.get(response.url)

            # Use WebDriverWait to wait until the form rows are present
            form_rows = WebDriverWait(driver, 20).until(
                EC.presence_of_all_elements_located((By.XPATH, '//*[@id="reg-Projects"]/div/div'))
            )

            # Iterate over each form row
            for form_row in form_rows:
                # Extract the project name from each form row
                project_name = form_row.find_element(By.XPATH, '//*[@id="reg-Projects"]/div/div/div[1]/div/div/span[1]').text

                # Click on the link to open the Application Preview page
                application_link = form_row.find_element(By.XPATH, '//*[@id="reg-Projects"]/div/div/div[1]/div/div/a')
                application_link.click()

                # Wait for the Application Preview page to load
                WebDriverWait(driver, 20).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]'))
                )

                # Extract additional details from the Application Preview page
                name = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]').text
                pan_number = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[6]/td[2]/span').text
                gstin_number = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[13]/td[2]/span').text
                permanent_address = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[12]/td[2]/span').text

                # Print the extracted details
                logging.info(f"Project Name: {project_name}")
                logging.info(f"Name: {name}")
                logging.info(f"PAN No.: {pan_number}")
                logging.info(f"GSTIN No.: {gstin_number}")
                logging.info(f"Permanent Address: {permanent_address}")

                # Write the details to a CSV file
                csv_filename = 'project_details.csv'
                file_exists = os.path.isfile(csv_filename)

                with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
                    fieldnames = ['Project Name', 'Name', 'PAN No.', 'GSTIN No.', 'Permanent Address']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    # Write header only if the file is empty or doesn't exist
                    if not file_exists or csvfile.tell() == 0:
                        writer.writeheader()

                    writer.writerow({
                        'Project Name': project_name,
                        'Name': name,
                        'PAN No.': pan_number,
                        'GSTIN No.': gstin_number,
                        'Permanent Address': permanent_address
                    })

                # Go back to the main page
                driver.back()

        except Exception as e:
            logging.error(f"An error occurred: {e}")

        finally:
            # Close the Selenium WebDriver
            driver.quit()
