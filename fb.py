from selenium import webdriver
import sys
browser = webdriver.Firefox()
browser.get('https://www.facebook.com/')
search = browser.find_element_by_css_selector('#email')
search.send_keys('shubhamsk100@gmail.com')
search = browser.find_element_by_css_selector('#pass')
search.send_keys('Shubham@123')
search = browser.find_element_by_css_selector('#u_0_2')
search.click()
search = browser.find_element_by_css_selector('#u_0_1t > div:nth-child(1) > div:nth-child(2) > span:nth-child(1) > label:nth-child(1) > input:nth-child(1)')
receiver = sys.argv[1]
search.send_keys(receiver)
search.click()


