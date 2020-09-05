from selenium import webdriver
path = "/home/niraj/Documents/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(path)

file = "Information.txt"
open_file = open(file,"a",encoding='utf-8')

output =''


for i in range(605968970,605969999):
    driver.get("http://202.166.205.172:8080/ird/{}".format(i))
    txt = driver.find_element_by_xpath("html").text
    print(txt)

    if txt == '{"Message":"An error has occurred."}':
        pass
    else:
        open_file.write(txt+"\n\n"+"----------------------------------------*---------------------------------------------\n")
        print("file written")
