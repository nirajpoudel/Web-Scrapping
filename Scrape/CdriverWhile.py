from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

path = "/home/niraj/Documents/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(path)
driver.get("http://nepal.gov.np:8080/NationalPortal/irdService")

file = "UserInfo.txt"
open_file = open(file,"a",encoding='utf-8')
#open_file.write('Address,PAN,Nepali name,English name,Registration date,Taypayer type,Taxpayer description,Taxpayer sub type,Business S. no,Vat registration date,Taxpayer description')



for value in range(605968970,605969999):
    search = driver.find_element_by_id("panNo")
    search.send_keys(value)
    time.sleep(0.01)
    search.send_keys(Keys.RETURN)

    link = driver.find_element_by_id("panNo_btn")
    link.click()
    time.sleep(0.01)
    search.clear()


    table = driver.find_element_by_id("myTable_detail")
    text_outcome = table.text
    print(text_outcome)
    if text_outcome == "":
        pass
    else:
        open_file.write(text_outcome+"\n\n"+"----------------------------------------*---------------------------------------------\n")
        print("file written")

open_file.close()
