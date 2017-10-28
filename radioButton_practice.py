from selenium import webdriver
driver = webdriver.Chrome()
url = 'http://www.echoecho.com/htmlforms10.htm'
driver.get(url)

# function that asserts that an element is a radio button
def assert_element_is_radio(element):

    my_elem_type = element.get_attribute('type')

    if my_elem_type != "radio":
        raise BaseException('The element passed is NOT a radio button')
    else:
        return True

    return

# function that asserts whether radio button is selected or not
def assert_radio_is_selected(element):

    assert_element_is_radio(element)

    if element.is_selected():
        print("the element is selected")
    else:
        raise AssertionError("the element is NOT selected")

# function that selects a radio button if a valid value is passed as attribute
def select_radio_by_value(elements, value):

    for element in elements:
        assert_element_is_radio(element)

        elem_value = element.get_attribute('value')
        found = False
        if elem_value == value:
            element.click()
            found = True
            break

    if not found:
        raise Exception('None of the radio buttons have the requested value.')

    return


radio_buttons_group = driver.find_elements_by_name("group1")
single_radio_button = driver.find_element_by_xpath("/html/body/div[2]/table[9]/tbody/tr/td[4]/table/tbody/tr/"
                                                   "td/div/span/form/table[3]/tbody/tr/td/table/tbody/tr/td/input[2]")

assert_element_is_radio(single_radio_button)

assert_radio_is_selected(single_radio_button)

select_radio_by_value(radio_buttons_group, 'Cheese')

driver.quit()
