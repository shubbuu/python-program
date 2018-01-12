from selenium import webdriver
import  pyperclip
browser  = webdriver.Firefox()
browser.get('https://www.jecjabalpur.ac.in/index.aspx')
searchElement = browser.find_element_by_css_selector('#UserLogin1_txtUserName')
searchElement.send_keys('0201IT151074')
search = browser.find_element_by_css_selector('#UserLogin1_txtPassword')
search.send_keys('sk894521')
elem = browser.find_element_by_css_selector('#UserLogin1_btnLogin')
elem.click()


