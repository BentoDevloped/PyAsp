from selenium import webdriver
import time

driver = webdriver.Safari()

driver.get(r'https://forli.commercialisti.it/albo')

time.sleep(100)
