from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.support.select import select
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

#wait for sizedropdown
#wait=WebDriverWait(driver, 10)
#something=wait.until(EC.presence_of_element_located((By.ID, 's')))

#select size
#wait=WebDriverWait(driver, 10)
Select(driver.find_element_by_id('s')).select_by_visible_text('XLarge')

#add to cart
#wait=WebDriverWait(driver, 10)
driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click()

# nav to home
#wait=WebDriverWait(driver, 10)
driver.find_element_by_xpath('//*[@id="cctrl"]/form/fieldset[1]/a').click()
#driver.get('http://www.supremenewyork.com/shop/')

#check out
#wait=WebDriverWait(driver, 30)
driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()

