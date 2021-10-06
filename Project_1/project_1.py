# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import datetime
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("D:\ChromeDriver_94\chromedriver.exe")

print("Enter the starting date: ")
startDate = input()
startDateList = startDate.split('.')

print("Enter the end date: ")
endDate = input()
endDateList = endDate.split('.')

date1 = datetime.date(int(startDateList[2]), int(startDateList[1]), int(startDateList[0]))
date2 = datetime.date(int(endDateList[2]), int(endDateList[1]), int(endDateList[0]))

file = open("Currancy.txt", 'a')

while date1 != date2:
    #driver.get("https://finance.liga.net/ua/currency/cash/currency/usd/filter/" + str(date1))
    driver.get("https://minfin.com.ua/ua/currency/banks/" + str(date1))
    #currency_USD = driver.find_element_by_xpath('/html/body/main/div/div[1]/div/div[4]/table/tbody/tr[7]/td[2]')
    currency_USD = driver.find_element_by_xpath('/html/body/main/div/div/div[1]/div/section[2]/div[2]/div[2]/table/tbody/tr[1]/td[2]')
    #currency_USD = driver.find_element_by_class_name("1633459645")
    file.write(str(date1) + ": " + currency_USD.text + "\n")
    print(currency_USD.text)
    date1 += datetime.timedelta(days = 1)
file.close()
driver.close()
