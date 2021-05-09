from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

from time import sleep
from datetime import datetime

from pynotifier import Notification

#### Configuration BEGIN

phone = 8073955450      ### 10 Digits, no zeros and no +91
age_grp = '18'          ### Type either '18' or '45' or 'Both'
vaccine = 'Covaxin'        ### 'Covishield' or 'Covaxin' or 'Both'
state = 'Karnataka'     ### Make sure the spelling is right
district = 'BBMP'       ### Make sure the spelling & casing is right
dose = 1                ### 1 or 2
pos = 2                 ### Position: 1, 2, 3 or 4 according to the benefitiaries registered in your account
refresh_delay = 840     ### in seconds

OTP = None # Input this in the terminal when prompted

#### Configuration END




############################## Main code

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])

class CowinBot():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path= "chromedriver.exe", options=options)
        self.driver.set_window_size(1500, 1500)

    def login(self):
        self.driver.get('https://selfregistration.cowin.gov.in')

        sleep(2)

        phone_in = self.driver.find_element_by_xpath('//*[@id="mat-input-0"]')
        phone_in.send_keys(phone)

        get_otp = self.driver.find_element_by_xpath('//ion-button[contains(text(), "{}")]'.format("Get OTP"))
        get_otp.click()


        ########### Taking OTP Input
        OTP = input("Enter the OTP: ")

        pw_in = self.driver.find_element_by_xpath('//*[@id="mat-input-1"]')
        pw_in.send_keys(OTP)

        verify_proceed = self.driver.find_element_by_xpath('//ion-button[contains(text(), "{}")]'.format("Verify"))
        verify_proceed.click()

    def schedule(self):
        schedule_btn = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-beneficiary-dashboard/ion-content/div/div/ion-grid/ion-row/ion-col/ion-grid[1]/ion-row[{}]/ion-col/ion-grid/ion-row[{}]/ion-col[2]/ul/li/a'.format(pos+1, 4+dose-1))
        schedule_btn.click()
        sleep(0.5)
        schedule_btn_2 = self.driver.find_element_by_xpath('//ion-button[contains(text(), "{}")]'.format("Schedule Now"))
        schedule_btn_2.click()

    def district_select(self):
        search_by_district_btn = self.driver.find_element_by_xpath('//*[@id="main-content"]/app-appointment-table/ion-content/div/div/ion-grid/ion-row/ion-grid/ion-row/ion-col/ion-grid/ion-row/ion-col[2]/form/ion-grid/ion-row/ion-col[1]/div/label/div')
        search_by_district_btn.click()
        sleep(0.25)

        select_state_dropdown = self.driver.find_element_by_xpath('//*[@id="mat-select-value-1"]/span')
        select_state_dropdown.click()
        sleep(0.25)

        select_state_btn = self.driver.find_element_by_xpath('//span[contains(text(), "{}")]'.format(state))
        select_state_btn.click()
        sleep(0.25)

        select_district_dropdown = self.driver.find_element_by_xpath('//*[@id="mat-select-value-3"]/span')
        select_district_dropdown.click()
        sleep(0.25)

        select_district_btn = self.driver.find_element_by_xpath('//span[contains(text(), "{}")]'.format(district))
        select_district_btn.click()
        sleep(0.25)

        search_btn = self.driver.find_element_by_xpath('//ion-button[contains(text(), "{}")]'.format('Search'))
        search_btn.click()  

    def age(self):
        if age_grp == 'Both':
            print('Selecting both age groups')
        else:
            age_btn = self.driver.find_element_by_xpath('//label[contains(text(), "{}")]'.format(age_grp))
            age_btn.click()
        
        
    def vaccine_type(self):
        if vaccine == 'Both':
            print('Selecting both vaccines')
        else:
            vaccine_btn = self.driver.find_element_by_xpath('//label[contains(text(), "{}")]'.format(vaccine))
            vaccine_btn.click() 

    def refresh(self):
        self.driver.get('https://selfregistration.cowin.gov.in/appointment')
    def home(self):
        self.driver.get('https://selfregistration.cowin.gov.in/')


bot = CowinBot()

def initialize():
    bot.login()

    Notification(
	title='OTP Alert!',
	description='Please Enter your Cowin OTP in the terminal!',
	#icon_path='path/to/image/file/icon.png', # On Windows .ico is required, on Linux - .png
	duration=5,                              # Duration in seconds
	urgency='Urgent'
    ).send()

    sleep(4)
    bot.schedule()
    sleep(1)
    bot.district_select()
    sleep(0.25)
    bot.age()
    sleep(0.25)
    bot.vaccine_type()

def keep_alive():
    while True:

        sleep(refresh_delay)
        print("Refreshed at {}".format(datetime.now().time()))
        bot.refresh()
        
        try:
            initialize()
        except:
            print("Incorrect OTP, try again")
            

initialize()
keep_alive()
