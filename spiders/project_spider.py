import scrapy
import csv
import logging
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

            # Use WebDriverWait to wait until the main form row is present
            main_form_row = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="reg-Projects"]/div/div'))
            )

            # Extract entries within the main form row
            entries = main_form_row.find_elements(By.XPATH, '//*[@id="reg-Projects"]/div/div')

            # Limit to the first 5 entries
            for index, entry in enumerate(entries[:5], start=1):
                # Extract the project name from the entry
                project_name = entry.find_element(By.XPATH, '//*[@id="reg-Projects"]/div/div/div[1]/div/div/span[1]').text

                # Print the project name
                logging.info(f"Project Name ({index}): {project_name}")

                # Click on the link to open the Application Preview page
                application_link = entry.find_element(By.XPATH, '//*[@id="reg-Projects"]/div/div/div[1]/div/div/a')
                application_link.click()

                # Wait for the Application Preview page to load
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]'))
                )

                # Extract additional details from the Application Preview page
                name = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]').text
                pan_number = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[6]/td[2]/span').text
                gstin_number = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[13]/td[2]/span').text
                permanent_address = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[12]/td[2]/span').text

                # Print the extracted details
                logging.info(f"Name: {name}")
                logging.info(f"PAN No.: {pan_number}")
                logging.info(f"GSTIN No.: {gstin_number}")
                logging.info(f"Permanent Address: {permanent_address}")

                # Write the details to a CSV file
                with open('project_details.csv', 'a', newline='', encoding='utf-8') as csvfile:
                    fieldnames = ['Project Name', 'Name', 'PAN No.', 'GSTIN No.', 'Permanent Address']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    # Write header only if the file is empty
                    if csvfile.tell() == 0:
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
