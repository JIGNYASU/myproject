import scrapy
import csv
import logging
import random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class ProjectSpider(scrapy.Spider):
    name = 'project1'
    start_urls = ['https://hprera.nic.in/PublicDashboard']
    


    def parse(self, response):
        # Set up Selenium WebDriver
        chrome_options = Options()
        #chrome_options.add_argument('--headless')  # Run Chrome in headless mode (no GUI)
        chrome_options.add_argument('--no-sandbox')
        random_port = random.randint(49152, 65535)
        chrome_options.add_argument(f'--remote-debugging-port={random_port}')
        driver = webdriver.Chrome(options=chrome_options)

        try:
            # Open the webpage using Selenium
            driver.get(response.url)

            # Use WebDriverWait to wait until the form rows are present
            form_rows = WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.XPATH, '//*[@id="reg-Projects"]/div/div'))
            )

            # Iterate over each form row
            for form_row in form_rows:
                #PROJECT1>>>>
                project_name1 = form_row.find_element(By.XPATH, '//*[@id="reg-Projects"]/div/div/div[1]/div/div/span[1]').text

                # Click on the link to open the Application Preview page
                application_link1 = form_row.find_element(By.XPATH, '//*[@id="reg-Projects"]/div/div/div[1]/div/div/a')
                application_link1.click()

                # Wait for the Application Preview page to load
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]'))
                )

                # Extract additional details from the Application Preview page
                name1 = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]').text
                pan_number1 = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[7]/td[2]/span').text
                gstin_number1 = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[8]/td[2]/span').text
                permanent_address1 = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[14]/td[2]/span').text

                # Print the extracted details
                logging.info(f"Project Name: {project_name1}")
                logging.info(f"Name: {name1}")
                logging.info(f"PAN No.: {pan_number1}")
                logging.info(f"GSTIN No.: {gstin_number1}")
                logging.info(f"Permanent Address: {permanent_address1}")

                entry_data = [{
                    'Project Name': project_name1,
                    'Name': name1,
                    'PAN No.': pan_number1,
                    'GSTIN No.': gstin_number1,
                    'Permanent Address': permanent_address1,
                }]

                # initializing CSV file
                csv_filename = 'project_details.csv'
                file_exists = os.path.isfile(csv_filename)

                with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
                    fieldnames = ['Project Name', 'Name', 'PAN No.', 'GSTIN No.', 'Permanent Address']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    # Write header only if the file is empty or doesn't exist
                    if not file_exists or csvfile.tell() == 0:
                        writer.writeheader()

                    # Write data for the current row
                    writer.writerows(entry_data)

                #Click on the link to close the Application Preview page and go back to main menu
                #close_link = form_row.find_element(By.XPATH, '//*[@id="modal-data-display-tab_project_main"]/div/div/div[3]/button')
                #close_link.click()

            #driver.back()

            driver.get(response.url)
            # Use WebDriverWait to wait until the form rows are present
            form_rows = WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.XPATH, '//*[@id="reg-Projects"]/div/div'))
            )

        
            for form_row in form_rows:
                #PROJECT2>>>>
                WebDriverWait(driver, 30).until(
                    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="reg-Projects"]/div/div/div[2]/div/div/span[1]'))
                )

                project_name2 = form_row.find_element(By.XPATH, '//*[@id="reg-Projects"]/div/div/div[2]/div/div/span[1]').text

                # Click on the link to open the Application Preview page
                application_link2 = form_row.find_element(By.XPATH, '//*[@id="reg-Projects"]/div/div/div[2]/div/div/a')
                application_link2.click()

                # Wait for the Application Preview page to load
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]'))
                )

                # Extract additional details from the Application Preview page
                name2 = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]').text
                pan_number2 = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[6]/td[2]/span').text
                gstin_number2 = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[8]/td[2]/span').text
                permanent_address2 = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[14]/td[2]/span').text

                # Print the extracted details
                logging.info(f"Project Name: {project_name2}")
                logging.info(f"Name: {name2}")
                logging.info(f"PAN No.: {pan_number2}")
                logging.info(f"GSTIN No.: {gstin_number2}")
                logging.info(f"Permanent Address: {permanent_address2}")

                entry_data2 = [{
                    'Project Name': project_name2,
                    'Name': name2,
                    'PAN No.': pan_number2,
                    'GSTIN No.': gstin_number2,
                    'Permanent Address': permanent_address2,
                }]

                # initializing CSV file
                csv_filename = 'project_details.csv'
                file_exists = os.path.isfile(csv_filename)

                with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
                    fieldnames = ['Project Name', 'Name', 'PAN No.', 'GSTIN No.', 'Permanent Address']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    # Write header only if the file is empty or doesn't exist
                    if not file_exists or csvfile.tell() == 0:
                        writer.writeheader()

                    # Write data for the current row
                    writer.writerows(entry_data2)

            driver.get(response.url)
            # Use WebDriverWait to wait until the form rows are present
            form_rows = WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.XPATH, '//*[@id="reg-Projects"]/div/div'))
            )

        
            for form_row in form_rows:
                #PROJECT3>>>>
                WebDriverWait(driver, 30).until(
                    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="reg-Projects"]/div/div/div[2]/div/div/span[1]'))
                )

                project_name3 = form_row.find_element(By.XPATH, '//*[@id="reg-Projects"]/div/div/div[3]/div/div/span[1]').text

                # Click on the link to open the Application Preview page
                application_link3 = form_row.find_element(By.XPATH, '//*[@id="reg-Projects"]/div/div/div[3]/div/div/a')
                application_link3.click()

                # Wait for the Application Preview page to load
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]'))
                )

                # Extract additional details from the Application Preview page
                name3 = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]').text
                pan_number3 = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[6]/td[2]/span').text
                gstin_number3 = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[8]/td[2]/span').text
                permanent_address3 = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[14]/td[2]/span').text

                # Print the extracted details
                logging.info(f"Project Name: {project_name3}")
                logging.info(f"Name: {name3}")
                logging.info(f"PAN No.: {pan_number3}")
                logging.info(f"GSTIN No.: {gstin_number3}")
                logging.info(f"Permanent Address: {permanent_address3}")

                entry_data3 = [{
                    'Project Name': project_name3,
                    'Name': name3,
                    'PAN No.': pan_number3,
                    'GSTIN No.': gstin_number3,
                    'Permanent Address': permanent_address3,
                }]

                # initializing CSV file
                csv_filename = 'project_details.csv'
                file_exists = os.path.isfile(csv_filename)

                with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
                    fieldnames = ['Project Name', 'Name', 'PAN No.', 'GSTIN No.', 'Permanent Address']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    # Write header only if the file is empty or doesn't exist
                    if not file_exists or csvfile.tell() == 0:
                        writer.writeheader()

                    # Write data for the current row
                    writer.writerows(entry_data3)

            driver.get(response.url)
            # Use WebDriverWait to wait until the form rows are present
            form_rows = WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.XPATH, '//*[@id="reg-Projects"]/div/div'))
            )

        
            for form_row in form_rows:
                #PROJECT4>>>>
                WebDriverWait(driver, 30).until(
                    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="reg-Projects"]/div/div/div[2]/div/div/span[1]'))
                )

                project_name4 = form_row.find_element(By.XPATH, '//*[@id="reg-Projects"]/div/div/div[4]/div/div/span[1]').text

                # Click on the link to open the Application Preview page
                application_link4 = form_row.find_element(By.XPATH, '//*[@id="reg-Projects"]/div/div/div[4]/div/div/a')
                application_link4.click()

                # Wait for the Application Preview page to load
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]'))
                )

                # Extract additional details from the Application Preview page
                name4 = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]').text
                pan_number4 = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[6]/td[2]/span').text
                gstin_number4 = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[8]/td[2]/span').text
                permanent_address4 = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[14]/td[2]/span').text

                # Print the extracted details
                logging.info(f"Project Name: {project_name4}")
                logging.info(f"Name: {name4}")
                logging.info(f"PAN No.: {pan_number4}")
                logging.info(f"GSTIN No.: {gstin_number4}")
                logging.info(f"Permanent Address: {permanent_address4}")

                entry_data4 = [{
                    'Project Name': project_name4,
                    'Name': name4,
                    'PAN No.': pan_number4,
                    'GSTIN No.': gstin_number4,
                    'Permanent Address': permanent_address4,
                }]

                # initializing CSV file
                csv_filename = 'project_details.csv'
                file_exists = os.path.isfile(csv_filename)

                with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
                    fieldnames = ['Project Name', 'Name', 'PAN No.', 'GSTIN No.', 'Permanent Address']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    # Write header only if the file is empty or doesn't exist
                    if not file_exists or csvfile.tell() == 0:
                        writer.writeheader()

                    # Write data for the current row
                    writer.writerows(entry_data4)

            driver.get(response.url)
            # Use WebDriverWait to wait until the form rows are present
            form_rows = WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located((By.XPATH, '//*[@id="reg-Projects"]/div/div'))
            )

        
            for form_row in form_rows:
                #PROJECT5>>>>
                WebDriverWait(driver, 30).until(
                    EC.presence_of_all_elements_located((By.XPATH, '//*[@id="reg-Projects"]/div/div/div[2]/div/div/span[1]'))
                )

                project_name5 = form_row.find_element(By.XPATH, '//*[@id="reg-Projects"]/div/div/div[5]/div/div/span[1]').text

                # Click on the link to open the Application Preview page
                application_link5 = form_row.find_element(By.XPATH, '//*[@id="reg-Projects"]/div/div/div[5]/div/div/a')
                application_link5.click()

                # Wait for the Application Preview page to load
                WebDriverWait(driver, 30).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]'))
                )

                # Extract additional details from the Application Preview page
                name5 = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]').text
                pan_number5 = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[7]/td[2]/span').text
                gstin_number5 = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[8]/td[2]/span').text
                permanent_address5 = driver.find_element(By.XPATH, '//*[@id="project-menu-html"]/div[2]/div[1]/div/table/tbody/tr[14]/td[2]/span').text

                # Print the extracted details
                logging.info(f"Project Name: {project_name5}")
                logging.info(f"Name: {name5}")
                logging.info(f"PAN No.: {pan_number5}")
                logging.info(f"GSTIN No.: {gstin_number5}")
                logging.info(f"Permanent Address: {permanent_address5}")

                entry_data5 = [{
                    'Project Name': project_name5,
                    'Name': name5,
                    'PAN No.': pan_number5,
                    'GSTIN No.': gstin_number5,
                    'Permanent Address': permanent_address5,
                }]

                # initializing CSV file
                csv_filename = 'project_details.csv'
                file_exists = os.path.isfile(csv_filename)

                with open(csv_filename, 'a', newline='', encoding='utf-8') as csvfile:
                    fieldnames = ['Project Name', 'Name', 'PAN No.', 'GSTIN No.', 'Permanent Address']
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

                    # Write header only if the file is empty or doesn't exist
                    if not file_exists or csvfile.tell() == 0:
                        writer.writeheader()

                    # Write data for the current row
                    writer.writerows(entry_data5)


        except Exception as e:
            logging.error(f"An error occurred: {e}")

        finally:
            # Close the Selenium WebDriver
            driver.quit()
