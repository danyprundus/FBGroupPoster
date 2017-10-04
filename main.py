from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import NoSuchElementException
import ConfigParser
import sys

driver = webdriver.PhantomJS()
driver.get('https://mbasic.facebook.com')
Config = ConfigParser.ConfigParser()
Config.read("config.ini")
def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1


data = ConfigSectionMap("FBData")
username = data['username']
password = sys.argv[1]
groupData=""
print "Opened facebook..."
driver.find_element_by_id('m_login_email').send_keys(username)
print "Email Id entered..."
driver.find_element_by_name('pass').send_keys(password)
print "Password entered..."
driver.find_element_by_xpath('//*[@id="login_form"]/ul/li[3]/input').click() #login button
sleep(2);
driver.find_element_by_xpath('//*[@id="root"]/table/tbody/tr/td/div/a').click() #ignore one login
sleep(2);
with open('groups.txt') as fp:
    for line in fp:
        groupURL, groupPicture=line.split(",")
        print groupURL
        print groupPicture
        sleep(2)
        driver.get(groupURL);#casuta jucariilor
        print "Go to group"
        driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[3]/form/div/span/div[1]/table/tbody/tr/td[2]/input').click() #click on post picture
        print "click on post picture"
        sleep(2)
        driver.find_element_by_xpath('//*[@id="root"]/table/tbody/tr/td/form/div[1]/div/input').send_keys("/Users/dprundus/PycharmProjects/facebook/om zap.jpeg")
        #driver.find_element_by_name('file1').send_keys(groupPicture)
        driver.save_screenshot('picture.png')
        print "Choose file"

        sleep(2)
        driver.find_element_by_xpath('//*[@id="root"]/table/tbody/tr/td/form/div[3]/input[1]').click() #click previzualizare
        print "click on prev"
        driver.save_screenshot('screenshot1.png')
        sleep(2)
        driver.find_element_by_xpath('//*[@id="composer_form"]/input[17]').click() #click POsteaza
        sleep(2)
        driver.save_screenshot('screenshot2.png')
        driver.find_element_by_xpath('//*[@id="root"]/table/tbody/tr/td/form/div[5]/input').click() #click POsteaza
driver.close();
#driver.get('https://mbasic.facebook.com/prundus.d.ioan')
#driver.find_element_by_name("xc_message").send_keys('test daniel, ignorati')
#driver.find_element_by_name("view_post").click()
