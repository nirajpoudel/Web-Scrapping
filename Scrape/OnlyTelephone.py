from selenium import webdriver

path = "/home/niraj/Documents/chromedriver_linux64/chromedriver"

driver = webdriver.Chrome(path)

file = "Contact.txt"
open_file = open(file,"a",encoding='utf-8')

word ="Telephone"

for i in range(605968970,605969100):
    driver.get("http://202.166.205.172:8080/ird/{}".format(i))
    txt = driver.find_element_by_xpath("html").text
    #list_of_words = txt.split(" ")
    #print(list(list_of_words))
    #tex1 = driver.get_attribute("Telephone")
    if word in txt:
        before_keyword, keyword, after_keyword = txt.partition(word)
        only_phone = after_keyword[3:13]
        if only_phone.isdigit():
            print("\nPhone number of pan number({}) is: ".format(i) + str(only_phone))
            open_file.write("Phone number of pan number({}) is: ".format(i) + str(only_phone)+"\n\n")
            print("\nSuccessfully written to file")
        else:
            pass
    else:
        pass
