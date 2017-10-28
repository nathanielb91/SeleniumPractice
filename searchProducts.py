"""This code opens Chrome, loads a url, searches a keyword in a search bar,
    and uses assertEqual to ensure the page has the same number of products
    listed as the number given. The unittest library is used here to separate
    setUp, test, and tearDown classes."""

import unittest
from selenium import webdriver

class SearchTest(unittest.TestCase):
    def setUp(self):

        # create a new Chrome session
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        self.driver.get("http://demo-store.seleniumacademy.com/")

    def test_search_by_category(self):

        # get the search textbox
        search_field = self.driver.find_element_by_name('q')
        search_field.clear()

        # enter search keyword and submit
        search_field.send_keys('phones')
        search_field.submit()

        # get all the anchor elements which have product names displayed
        # currently on result page using find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        self.assertEqual(3, len(products))


    def tearDown(self):
        # close the browser window
        self.driver.quit()



