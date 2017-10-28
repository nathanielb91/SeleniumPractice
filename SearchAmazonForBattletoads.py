""" This code loads Chrome, searches amazon.com for a video game,
and prints out the product names along with their price """

from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get('https://www.amazon.com')

# get the search textbox
search_field = driver.find_element_by_id('twotabsearchtextbox')
search_field.clear()

# enter search keyword and submit
search_field.send_keys('battletoads')
search_field.submit()

# assign elements to variables
prices = driver.find_elements_by_xpath("//div/div/div/div[2]/div[2]/div[1]/div[2]/div/a/span[2]")
names = driver.find_elements_by_xpath("//div/div/div/div[2]/div[1]/div[1]/a/h2")


# iterate through each element and print the product name and it's price
for i in range(len(prices)):
    print names[i].text  + " : " + prices[i].text

# exit Chrome
driver.close()
