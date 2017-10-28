"""This code loads Chrome and searches for 'best deep dish in chicago'.
    Inspired by website 'Let me Google that for you' (lmgtfy)"""


from selenium import webdriver
import time
driver = webdriver.Chrome()
url = 'http://www.google.com'
driver.get(url)

def lmgtfy():

    searchBar_textField = driver.find_element_by_xpath('//*[@id="lst-ib"]')
    #searchButton = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[3]/center/input[1]')


    searchBar_textField.send_keys('best deep dish in chicago')
    time.sleep(1)
    #searchButton.click()
    searchBar_textField.submit()


lmgtfy()

