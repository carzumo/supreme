from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# tell location of the webdriver and call it 'driver'
driver = webdriver.Chrome()
driver.implicitly_wait(10) # seconds

#go to website
driver.get('http://www.supremenewyork.com/shop/all/t-shirts')

#look for keywords '___', then click on item
driver.find_element_by_partial_link_text('Fuck The Rest L/S Tee').click()

#click/color
driver.find_element_by_partial_link_text('White').click()

#select size
Select(driver.find_element_by_id('s')).select_by_visible_text('XLarge')

#add to cart
driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()

#check out
wait=WebDriverWait(driver, 10)
something=wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'button edit')))
driver.find_element_by_xpath('//*[@id="cart"]/a[1]').click()

