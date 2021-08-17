from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time

# webdriver.Chrome() will be used
driver = webdriver.Chrome(executable_path='/home/shivam/Downloads/pycharm/chromedriver')


# URL of the website
url = "https://testing.d3eymc78cqte40.amplifyapp.com/login"

driver.get(url)

time.sleep(2)

#login_with_username_password

driver.find_element_by_xpath('//*[@id="username"]').send_keys("TestUser123")
driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
driver.find_element_by_xpath('//*[@id="root"]/div/form/div[3]/button').click()
#print(driver.page_source)
time.sleep(6)

#place_order

buttons = driver.find_element_by_class_name('css-11hsy1o') 
buttons.click()

time.sleep(5)

#Order Details:

driver.find_element_by_class_name('css-n9lnwn').send_keys("12677")


#Customer Details:


driver.find_element_by_xpath('//input[@id="name"]').send_keys("Ankur1")
driver.find_element_by_xpath('//input[@id="mobile"]').send_keys("9898989898")
driver.find_element_by_xpath('//input[@id="alternative_mobile"]').send_keys("9999999999")
driver.find_element_by_xpath('//input[@id="email"]').send_keys("abcdfg@asd.com")
driver.find_element_by_xpath('//input[@id="address"]').send_keys("asfdsagdsfrdhtgfhg")
driver.find_element_by_xpath('//input[@id="landmark"]').send_keys("asdasdsfdf")
driver.find_element_by_xpath('//input[@id="pin_code"]').send_keys("898989")
driver.find_element_by_xpath('//input[@id="city"]').send_keys("Bangalore")
driver.find_element_by_xpath('//input[@id="state"]').send_keys("karnataka")

time.sleep(5)

#Addess_details
driver.find_element_by_xpath('//input[@id="doctor"]').send_keys("Dr.ankur")

#Medicines
driver.find_element_by_xpath('//input[@id="medicineName"]').send_keys("Crestor")
time.sleep(4)
driver.find_element_by_xpath('//p[normalize-space()="Crestor 10mg Strip Of 30 Tablets"]').click()
driver.find_element_by_xpath('//button[normalize-space()="Submit"]').click()
time.sleep(12)


driver.close()
