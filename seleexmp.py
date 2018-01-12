from selenium import webdriver
browser = webdriver.Firefox()
browser.get('https://www.jecjabalpur.ac.in/index.aspx')
searchEle = browser.find_element_by_css_selector('#UserLogin1_txtUserName')
searchEle.send_keys('0201IT151074')
searchEle = browser.find_element_by_css_selector('#UserLogin1_txtPassword')
searchEle.send_keys('sk894521')
searchEle = browser.find_element_by_css_selector('#UserLogin1_btnLogin')
searchEle.click()
