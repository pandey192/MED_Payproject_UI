from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import xlrd
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
time.sleep(4)

#place_order

buttons = driver.find_element_by_class_name('css-11hsy1o') 
buttons.click()

time.sleep(4)

#Order Details:
print('abcd')
patId = driver.find_element_by_class_name('css-n9lnwn')
print('abcdd',patId)

#Customer Details:

name = driver.find_element_by_xpath('//input[@id="name"]')
mobile = driver.find_element_by_xpath('//input[@id="mobile"]')
Altmobile = driver.find_element_by_xpath('//input[@id="alternative_mobile"]')
Emailid = driver.find_element_by_xpath('//input[@id="email"]')
address = driver.find_element_by_xpath('//input[@id="address"]')
landmark = driver.find_element_by_xpath('//input[@id="landmark"]')
pincode = driver.find_element_by_xpath('//input[@id="pin_code"]')
city = driver.find_element_by_xpath('//input[@id="city"]')
state = driver.find_element_by_xpath('//input[@id="state"]')

time.sleep(5)

#Addess_details
Doctore = driver.find_element_by_xpath('//input[@id="doctor"]')

#Medicines
driver.find_element_by_xpath('//input[@id="medicineName"]').send_keys("Crestor")
time.sleep(4)
driver.find_element_by_xpath('//p[normalize-space()="Crestor 10mg Strip Of 30 Tablets"]').click()
time.sleep(2)

driver.find_element_by_xpath('//button[normalize-space()="Submit"]').click()
time.sleep(6)


workbook = xlrd.open_workbook("Datafile.xlsx")
sheet = workbook.sheet_by_name("input")


#Get_total_no_of_count

rowCount = sheet.nrows
colcount = sheet.ncols
print (rowCount)
print (colcount)

for curr_row in range(1, rowCount):
    PartnerId = int(sheet.cell_value(curr_row,0))
    Name = sheet.cell_value(curr_row,1)
    Mobile = int(sheet.cell_value(curr_row,2))
    Alternate_Mobile = int(sheet.cell_value(curr_row,3))
    Email = sheet.cell_value(curr_row,4)
    Address = sheet.cell_value(curr_row,5)
    Landmark = sheet.cell_value(curr_row,6)
    PinCode = int(sheet.cell_value(curr_row,7))
    City = sheet.cell_value(curr_row,8)
    State = sheet.cell_value(curr_row,9)
    Doctor = sheet.cell_value(curr_row,10)


    patId.clear()
    patId.send_keys(PartnerId)
    name.clear()
    name.send_keys(Name)
    mobile.clear()
    mobile.send_keys(Mobile)
    Altmobile.clear()
    Altmobile.send_keys(Alternate_Mobile)
    Emailid.clear()
    Emailid.send_keys(Email)
    address.clear()
    address.send_keys(Address)
    landmark.clear()
    landmark.send_keys(Landmark)
    pincode.clear()
    pincode.send_keys(PinCode)
    city.clear()
    city.send_keys(City)
    state.clear()
    state.send_keys(State)
    Doctore.clear()
    Doctore.send_keys(Doctor)
    
    time.sleep(4)


    driver.close()
