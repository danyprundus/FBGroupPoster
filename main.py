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

driver = webdriver.Chrome()
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
#text = 'Angajam animator/supraveghetor evenimente/loc de joaca copii !\nLocatie: TheMagic House: str. C-tin Brancusi nr 1 -la etaj- Cluj-Napoca\nDetalii la telefon: 0756 977 516\nCerinte:\n- persoana sociabila, comunicativa, dornica sa fie in preajma copiilor si sa se joace cu ei;\n- indemanatica si creativa;\n- spirit de echipa si vesela;\n- disponibilitate in weekend.\nResponsabilitati:\n- supravegherea si entertainment-ul/animarea copiilor in spatiul de joaca in timpul activitatilor/evenimentului;\n- organizarea si amenajarea si spatiului de joaca atat pentru evenimente cat si pentru joaca si ateliere;\n- pastrarea si depozitarea jucariilor pentru o desfasurare a activitatilor in conditii cat mai bune in spatiul de joaca;\n- pregatirea si servirea mesei pentru evenimente;\n- pastrarea ordinii si curateniei;\n- buna dispozitie si veselie.\nVa rugam sa trimiteti CV-urile la adresa de mail:\nThemagichousecj@gmail.com\n Fa un copil sa zambeasca cu zambetul tau si te luam in echipa de la TheMagic House Cluj Napoca!\n'
#print text
groupData=""
print "Opened facebook..."
driver.find_element_by_id('m_login_email').send_keys(username)
print "Email Id entered..."
driver.find_element_by_name('pass').send_keys(password)
print "Password entered..."
driver.find_element_by_name('login').click() #login button
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
        #driver.find_element_by_name("xc_message").send_keys(text)
        #driver.save_screenshot('text.png')
        #print "Add Text"
        #driver.find_element_by_xpath('//*[@id="root"]/div[1]/div[3]/form/div/span/div[1]/table/tbody/tr/td[2]/input').click() #click on post picture
        driver.find_element_by_name("view_photo").click()
        driver.save_screenshot('group.png')
        print "click on post picture"
        sleep(2)
        driver.find_element_by_name("file1").send_keys(groupPicture)
        driver.save_screenshot('picture.png')
        print "Choose file"

        sleep(2)
        driver.find_element_by_name('add_photo_done').click() #click previzualizare
        print "click on prev"
        driver.save_screenshot('screenshot1.png')
        sleep(2)
        driver.find_element_by_name('view_post').click() #click POsteaza
        sleep(2)
        driver.save_screenshot('screenshot2.png')
        driver.find_element_by_name('done').click() #click POsteaza
driver.close();
#driver.get('https://mbasic.facebook.com/prundus.d.ioan')


#driver.find_element_by_name("view_post").click()
#driver.find_element_by_name("view_photo").click()
