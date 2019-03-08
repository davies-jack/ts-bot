from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import sys
import time

print str(sys.argv)

browser = webdriver.Chrome('C:\Users\Jack\Downloads\chromedriver.exe')

# Open TS
browser.get('http://www.toughsociety.com/')

# Vars
username = browser.find_element_by_id('username')
password = browser.find_element_by_id('password')
loginBtn = browser.find_element_by_id('submit')

print "Entering username " + sys.argv[1]
username.send_keys(sys.argv[1])
print "Entering supplied password"
password.send_keys(sys.argv[2])

print "Clicking login button"
loginBtn.click()

captchaCheck = browser.find_elements_by_id('captcha_txt')
bustSelfCheck = browser.find_elements_by_class_name('js-bust-out')

loopAmount = sys.argv[3]

for i in range(int(sys.argv[3])):
    # Navigate to Crimes
    print "Navigating to crimes page"
    browser.get('https://s4.toughsociety.com/crimes.php')
    if len(bustSelfCheck) > 0:
        print "You are in jail! Waiting longer"
        time.sleep(25)
    else:
        checkAll = browser.find_elements_by_class_name('js-check-toggle')
        crimesCommit = browser.find_element_by_class_name('textarea')

        # Check all crimes
        print "Checking all crimes"
        if len(browser.find_elements_by_class_name('js-check-toggle')) > 0:
            browser.find_element_by_class_name('js-check-toggle').click()


        # Commit crimes

        getTimeLeftOnCrimes = browser.find_elements_by_class_name('crimeTimer')

        if len(browser.find_elements_by_class_name('textarea')) > 0:
            if len(browser.find_elements_by_id('captcha_txt')) < 1:
                print "Clicking commit button"
                crimeBtn = browser.find_element_by_class_name('textarea')
                crimeBtn.click()
            else:
                print "Please type in the captcha code to continue script:"
                browser.find_element_by_id('captcha_txt').send_keys(raw_input())

                print "Clicking commit button"
                crimeBtn = browser.find_element_by_css_selector('.textarea.curve3px')
                crimeBtn.click()

        if ("You got caught" in browser.page_source):
            print "You are now in jail"
            browser.get('https://s4.toughsociety.com/jail.php')
            timeLeft = browser.find_element_by_class_name('crimeTimer')
            print "Waiting for " + str(timeLeft.get_attribute('data-counter'))
            time.sleep(int(timeLeft.get_attribute('data-counter')))
        print "Waiting for 2 seconds."
        time.sleep(2)

        print "Navigating to GTA page"
        browser.get('https://s4.toughsociety.com/gta.php')
        gtaButton = browser.find_element_by_name('gta')
        if len(browser.find_elements_by_id('captcha_txt')) < 1:
            getTimeLeftOnGta = browser.find_element_by_class_name('crimeTimer')
            if getTimeLeftOnGta.text == "Available" or getTimeLeftOnGta.text < 60:
                print "Clicking GTA button"
                if len(browser.find_elements_by_name('gta')) > 0:
                    gtaButton.click()
                    if ("You got caught" in browser.page_source):
                        print "You are now in jail"
                        browser.get('https://s4.toughsociety.com/jail.php')
                        timeLeft = browser.find_element_by_class_name('crimeTimer')
                        print "Waiting for " + str(timeLeft.get_attribute('data-counter'))
                        time.sleep(int(timeLeft.get_attribute('data-counter')))
            else:
                print "GTA is not avaliable, moving on. Timeleft is " + getTimeLeftOnGta.text

            if sys.argv[4] != "melt":
                print "Waiting for 60 seconds"
                time.sleep(60)
        else:
            cap = browser.find_element_by_id('captcha_txt')
            print "GTA Captcha has been found, please enter the captcha:"
            cap.send_keys(raw_input())

            getTimeLeftOnGta = browser.find_element_by_class_name('crimeTimer')
            if getTimeLeftOnGta.text == "Available":
                print "Commiting GTA"

                gtaButton = browser.find_element_by_name('gta')
                if len(browser.find_elements_by_name('gta')):
                    gtaButton.click()
            else:
                print "GTA not avaliable, moving on."
            if ("You got caught" in browser.page_source):
                print "You are now in jail"
                browser.get('https://s4.toughsociety.com/jail.php')
                timeLeft = browser.find_element_by_class_name('crimeTimer')
                print "Waiting for " + str(timeLeft.get_attribute('data-counter'))
                time.sleep(int(timeLeft.get_attribute('data-counter')))
        # Melt Script
        if (sys.argv[4] == "melt"):
            print "Navigating to melt page"
            browser.get('https://s4.toughsociety.com/melt.php')
            getTimeLeftOnMelt = browser.find_element_by_class_name('crimeTimer')
            if getTimeLeftOnMelt.text == "Available":
                # Car radio button
                if len(browser.find_elements_by_name('car_id')) > 0:
                    print "Clicking car to melt"
                    findCarToMelt = browser.find_element_by_name('car_id')
                    findCarToMelt.click()
                else:
                    print "Car ID radio button not found! Skipping"

                # Car melt button
                if len(browser.find_elements_by_name('melt')) > 0:
                    print "Melting car"
                    findCarMeltButton = browser.find_element_by_name('melt')
                    findCarMeltButton.click()
                else:
                    print "Melt car button not found! Skipping"
            else:
                print "Melt is not avaliable! Timeleft is " + getTimeLeftOnMelt.text

            print "Waiting 45 seconds"
            time.sleep(45)