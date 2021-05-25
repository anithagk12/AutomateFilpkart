import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
import csv


class Flipkart():

    def __init__(self):

        self.current_path = 'C://Users//Admin//Desktop//driver'
        self.url = 'https://www.flipkart.com'
        self.driver_path = os.path.join('C://Users//Admin//Desktop//driver', 'chromedriver')
        self.driver = webdriver.Chrome(self.driver_path)

    def page_load(self):

        self.driver.get(self.url)
        login_pop = self.driver.find_element(By.XPATH,'//*[@class="_2KpZ6l _2doB4z"]')
        login_pop.click()
        print('pop-up closed')
        pass
        search_field = self.driver.find_element(By.XPATH,'//*[@class="_3704LK"]')
        search_field.send_keys('Iphone' + '\n')
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@title="Mobiles"]').click()
        time.sleep(5)
        select = Select(self.driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/div[1]/div[2]/div[1]/div/section[2]/div[4]/div[3]/select'))
        select.select_by_visible_text("₹30000")
        time.sleep(5)
        self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[1]/div/div/div[2]/div[3]').click()
        page_html = self.driver.page_source
        self.soup = BeautifulSoup(page_html, 'html.parser')

    def create_csv_file(self):
        rowHeaders = ["Device name", "Storage_details", "Price", "Rating"]
        self.file_csv = open('Flipkart_output.csv', 'w', newline='', encoding='utf-8')
        self.mycsv = csv.DictWriter(self.file_csv, fieldnames=rowHeaders)
       
        self.mycsv.writeheader()

    def data_scrap(self):

        first_page_mobiles = (self.soup.find_all('div', class_='_1YokD2 _3Mn1Gg'))
        for i in first_page_mobiles:
            Device = self.driver.find_element(By.XPATH,'//*[@class="_4rR01T"]')
            Device_Name= Device.text
            price_detail = self.driver.find_element(By.XPATH,'//*[@class="_30jeq3 _1_WHN1"]')
            price = price_detail.text
            Storage = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[3]/ul/li[1]')
            Storage_detail = Storage.text
            price_details = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[2]/div[1]/div/div[1]')
            price = price_details.text
            Rating_details = self.driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[2]/span[2]/span/span[1]')
            Rating = Rating_details.text
            self.mycsv.writerow({"Device name": Device_Name, "Storage_details": Storage_detail, "Price": price, "Rating": Rating})

    def tearDown(self):        
        self.driver.quit()
        self.file_csv.close()

if __name__ == "__main__":

    Flipkart = Flipkart()
    Flipkart.page_load()
    Flipkart.create_csv_file()
    Flipkart.data_scrap()
    Flipkart.tearDown()
    print("Task completed")