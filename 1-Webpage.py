# https://www.youtube.com/watch?v=o3tYiyE_OXE
from selenium import webdriver    #to use selenium to open website
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains    # to perform mouse action
from time import sleep

wait = 5

# need to specify where the chromedriver.exe is
driver = webdriver.Chrome(executable_path="C:\\Users\Diyanah\Downloads\chromedriver_win32\chromedriver.exe")

'''
# open the website
driver.get("https://ringgitplus.com/en/credit-card/")

# get the title of the page
print(driver.title)

# return the URL of the page
print(driver.current_url)

# close the cuurent website
# driver.close()

# close all browsers/tab
# driver.quit()

sleep(wait)

# Navigation back on forth of a website (click back)
driver.get("https://ringgitplus.com/en/")     # change website address
print(driver.title)
sleep(wait)

driver.back()             # click page back button
print(driver.title)
sleep(wait)

driver.forward()          # click page forward button
print(driver.title)
sleep(wait)





# to get title, link and text of the xpath
title = driver.find_element_by_xpath("//*[@id='/en/credit-card/']").get_attribute("title")
href = driver.find_element_by_xpath("//*[@id='/en/credit-card/']").get_attribute("href")
text = driver.find_element_by_xpath("//*[@id='/en/credit-card/']").text
print(title)
print(href)
print(text)



#open in new tab
link = driver.find_element_by_link_text()
driver.execute_script("window.open('https://rinplus.com/en/credit-card/', 'new window')")

driver.execute_script("window.open('https://ringgitplus.com/en/credit-card/', 'new window')")

name = "Jirnexu Dev - Banking"
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

# close the tab
# (Keys.CONTROL + 'w') on other OSs.
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')


# CONDITIONAL COMMANDS
driver.get("http://newtours.demoaut.com/")   #open new website

# check if the field is displayed and enabled
user_name = driver.find_element_by_name("userName")
pwd = driver.find_element_by_name("password")

print("User name field displayed:", user_name.is_displayed())
print("User name fields displayed:", user_name.is_enabled())

print("Password field displayed:", pwd.is_displayed())
print("Password field displayed:", pwd.is_enabled())

sleep(wait)

# login
user_name.send_keys("mercury")   # input string into the field
pwd.send_keys("mercury")
driver.find_element_by_name("login").click()    # click sign in button

sleep(wait)

driver.get("https://www.fireflyz.com.my/")   #open new website

sleep(wait)

round_trip = driver.find_element_by_css_selector("input.btn-list.button_web_roundtrip")
one_way = driver.find_element_by_css_selector("input.btn-list.button_web_oneway")

print("Is roundtrip selected:", round_trip.is_selected())          # check if the radio button is selected. Works for checkbox too
print("Is oneway selected:", one_way.is_selected())


# WAITS COMMANDS
# 1. implicit wait
# - wait until the next element is loaded
# - we only need to specify it once in the whole code. then it will do for all the lines

driver.get("https://ringgitplus.com/en/")

driver.implicitly_wait(1)   # wait for 10 sec for the element to show
assert "Compare Malaysia's Top Finance Products and Apply Online" in driver.title  # check if the string in the title. Boolean value


# 2. Explicit wait
# - it will wait for a condition to be fulfilled
driver.get("https://www.expedia.com.my/")

driver.implicitly_wait(5)      # applicable for all element

driver.maximize_window()    # to maximise the window

driver.find_element(By.ID, "tab-flight-tab-hp").click()    # another way to right this. similar like selenium
driver.find_element(By.ID, "flight-origin-hp-flight").send_keys("SFO")
driver.find_element(By.ID, "flight-destination-hp-flight").send_keys("NYC")
sleep(wait)
driver.find_element(By.ID, "flight-departing-hp-flight").send_keys("10/3/2020")
driver.find_element(By.ID, "flight-returning-hp-flight").clear()                   # since it is auto populated. need to clear it first
driver.find_element(By.ID, "flight-returning-hp-flight").send_keys("15/3/2020")
driver.find_element(By.XPATH, "//*[@id='gcw-flights-form-hp-flight']/div[8]/label/button").click()


wait2 = WebDriverWait(driver, 10)    # 10sec is the max timeout

# no need to include drver.find_element etc since it is in the EC
# this condition will omit Implicit wait, it will follow 10 sec Explicit wait
element = wait2.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='stopFilter_stops-0']")))  # memang kene double bracket
element.click()   # click the checkbox

sleep(wait)


# DROPDOWN BOX
# for some case where the options does not have specific name where we cant locate them using it, we need to use Select class
# Count how many text field there is
driver.get("https://www.facebook.com/campaign/landing.php?campaign_id=1742551639&extra_1=s%7Cc%7C339402894398%7Ce%7Cfacebook%20sign%20up%7C&placement=&creative=339402894398&keyword=facebook%20sign%20up&partner_id=googlesem&extra_2=campaignid%3D1742551639%26adgroupid%3D72230629190%26matchtype%3De%26network%3Dg%26source%3Dnotmobile%26search_or_content%3Ds%26device%3Dc%26devicemodel%3D%26adposition%3D1t1%26target%3D%26targetid%3Dkwd-5066597374%26loc_physical_ms%3D9066763%26loc_interest_ms%3D%26feeditemid%3D%26param1%3D%26param2%3D&gclid=EAIaIQobChMItquE0J-Z5wIVBx4rCh37gAe3EAAYASAAEgLz7PD_BwE")

sleep(wait)

# BUG - cant extract val
print(len(driver.find_elements_by_xpath('//input[@data-type = "text"]')))  # to find how many text field there is


day = driver.find_element_by_name("birthday_month")
drp_day = Select(day)      # assigning this object to Select function. So it is selectable. Note this can only be used if the html start with 'Select'

# there are 3 methods of selecting the option
# 1. by text
drp_day.select_by_visible_text("Sep")

# by index
# drp_day.select_by_index(12)

# by values
# drp_day.select_by_value("2")


# Getting how many options there is
print(len(drp_day.options))

all_options = drp_day.options
for option in all_options:
    print(option.text)      # extract text value


# LINKS
# say we wanna know
# 1. how many links present
# 2. capture the links
# 3. click on the links
driver.get("https://ringgitplus.com/en/")

links = driver.find_elements_by_tag_name("a")    # store all links in links variable. all links have tag 'a'
print("Number of links present:", len(links))                                # print how many links

# for link in links:
#    print(link.text)                     # if we want to print the text of the link
#    print(link.get_attribute("href"))    # if we want to print the link

# driver.find_element_by_link_text("FIXED DEPOSITS").click()
driver.find_element_by_partial_link_text("Online Shopping").click()


# ALERT BOX
# 1. OK button
# 2. OK/Cancel button
# 3. text field button
driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
sleep(wait)
driver.find_element_by_xpath('//button[@onclick = "myConfirmFunction()"]').click()
sleep(wait)

# driver.switch_to_alert().accept()            # accept notification
driver.switch_to.alert.dismiss()               # can also use in this form
sleep(wait)

driver.find_element_by_xpath('//button[@onclick = "myPromptFunction()"]').click()
sleep(wait)
driver.switch_to.alert.send_keys("yohoo")
driver.switch_to.alert.accept()


# dismiss notfication alert box
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(options=chrome_options, executable_path="C:\\Users\Diyanah\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("https://ringgitplus.com/en/")


# FRAMES - 2:23:35
# frame is when we have a scrollable section in a page

driver.get("https://selenium.dev/selenium/docs/api/java/index.html")
# driver.find_element_by_link_text("com.thoughtworks.selenium").click()   # just this is not enough. We need to switch to the frame, then only execute them
# there will be <frame element where it specify which frame it is
# we need to switch the frames using these

# 1st frame -  top left
driver.switch_to.frame("packageListFrame")    # input the name of the frame
driver.find_element_by_link_text("org.openqa.selenium").click()
sleep(wait)
# now all the actions will be in this frame
# we need to switch back if we want to use other frame

# 2nd frame - bottom left
driver.switch_to.default_content()   # go back to default frame
driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("WebDriver").click()
sleep(wait)

# 3rd frame - right frame
driver.switch_to.default_content()   # go back to default frame
driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]").click()
sleep(wait)

# can also use index instead of name
# driver.switch_to.frame(0)         # select by index 0


# BROWSER WINDOWS - 2:35:47

driver.get("https://ringgitplus.com/en/")
sleep(wait)
driver.find_element_by_xpath("/html/body/footer/section[5]/ul/li[1]/a").click()
print(driver.current_window_handle)      # handle value of the parent window. The original one

handles = driver.window_handles          # will return handles for all open windows (tab)
print(handles)
sleep(wait)

for handle in handles:
    driver.switch_to.window(handle)      # switch window
    print(driver.title)                  # get the title of the page
    sleep(wait)

    if driver.title == "Compare Malaysia's Top Finance Products and Apply Online":
        driver.close()                   # say we wanna close the parent window

# extra eg
# say we wanna close all other tab than current one

driver.get("https://ringgitplus.com/en/")
sleep(wait)
driver.find_element_by_xpath("/html/body/footer/section[5]/ul/li[1]/a").click()   # click fb (new tab)
parent_win = driver.current_window_handle               # store the value of current window handle
sleep(wait)
driver.switch_to.window(parent_win)                     # switch to parent window

driver.find_element_by_xpath("/html/body/footer/section[5]/ul/li[2]/a").click()   # click yt (new tab)
parent_win = driver.current_window_handle               # store the value of current window handle
sleep(wait)
driver.switch_to.window(parent_win)                     # switch to parent window

driver.find_element_by_xpath("/html/body/footer/section[5]/ul/li[3]/a").click()   # click twt (new tab)
sleep(wait)

handles = driver.window_handles

for handle in handles:
    sleep(wait)
    driver.switch_to.window(handle)
    print(driver.title)
    sleep(wait)
    if driver.current_window_handle != parent_win:
        driver.close()


# WEB TABLES - 2:48:30
driver.get("https://ringgitplus.com/en/car-insurance/Allianz-Comprehensive-Motor-Insurance.html?filter=Allianz")

rows_body = len(driver.find_elements_by_xpath("//*[@id='coverage']/table/tbody[1]/tr"))      # count how many elements inside for body rows
col_body = len(driver.find_elements_by_xpath("//*[@id='coverage']/table/tbody[1]/tr[1]/td"))     # count how many columns in the first row tr[1]

print(rows_body)
print(col_body)

for r in range(1, rows_body + 1):     # loop thru all 5 row
    for c in range(1, col_body + 1):     # loop thru all coloumn in 1 row
        value = driver.find_element_by_xpath("//*[@id='coverage']/table/tbody[1]/tr[" + str(r) + "]/td[" + str(c) + " ]").text
        print(value, end='   ')           # will print 'val1  val2   val3' for all column in 1 row
    print()                               # go next line for each new row
    print()


//*[@id="coverage"]/table                          # all
//*[@id="coverage"]/table/tbody[1]                 # first row all
//*[@id="coverage"]/table/tbody[1]/tr[1]           # first row
//*[@id="coverage"]/table/tbody[1]/tr[1]/td[1]     # first row, first col
//*[@id="coverage"]/table/tbody[1]/tr[1]/td[2]     # first row, 2nd col
//*[@id="coverage"]/table/tbody[1]/tr[2]/td[1]

//*[@id="coverage"]/table/tbody[2]/tr[1]/td[1]


# SCROLLING - 3:07:00
# 1. Scroll by pixel
# 2. Scroll till element found
# 3. Scroll till end of page

# by PIXEL
driver.get("https://ringgitplus.com/en/")
# driver.execute_script("window.scrollBy(0,1000)", "")     # move by 1000 pixel from 0

# by ELEMENT
flag = driver.find_element_by_xpath("/html/body/main/section[7]/h2")
# driver.execute_script("arguments[0].scrollIntoView();", flag)

# till END
sleep(wait)     # this is important cause we might scroll till the end without the page completely loaded. if this the case, it wont be the end
driver.execute_script("window.scrollBy(0, document.body.scrollHeight)")


# MOUSE ACTIONS - will use ActionChains class 
# 1. Mouse Hover
# 2. Double Click
# 3. Right Click
# 4. Drag and Drop


# 1. Mouse Hover
from selenium.webdriver import ActionChains

driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(5)
driver.find_element_by_name("txtUsername").send_keys("Admin")
driver.find_element_by_name("txtPassword").send_keys("admin123")
driver.find_element_by_name("Submit").click()

admin = driver.find_element_by_id("menu_admin_viewAdminModule")
usr_mngmnt = driver.find_element_by_id("menu_admin_UserManagement")
users = driver.find_element_by_id("menu_admin_viewSystemUsers")

actions = ActionChains(driver)     # ActionChains is a class that allow to mouse over. We are assigning and object actions to the class, and driver has the type of class
actions.move_to_element(admin).move_to_element(usr_mngmnt).move_to_element(users).click().perform()    # has to be chain, else it break


# 2. Double Click
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
element = driver.find_element_by_xpath("//button[@ondblclick = 'myFunction1()']")
actions = ActionChains(driver)
actions.double_click(element).perform()    # need to end with perform always


# 3. Right Click
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
button = driver.find_element_by_xpath("/html/body/div/section/div/div/div/p/span")
actions = ActionChains(driver)
actions.context_click(button).perform()        # right click action


# 4. Drag and Drop
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()
driver.implicitly_wait(wait)
rome = driver.find_element_by_id("box6")
italy = driver.find_element_by_id("box106")

actions = ActionChains(driver)
actions.drag_and_drop(rome, italy).perform()     # source, target


# UPLOAD FILE - 3:45:06
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(wait)

driver.switch_to.frame(0)         # select by index
upload_btn = driver.find_element_by_id("RESULT_FileUpload-10")
driver.execute_script("arguments[0].scrollIntoView();", upload_btn)
upload_btn.send_keys("C://Users/Diyanah/Pictures/front.png")    # change to forward slash and ://


# DOWNLOAD FILE - 3:51:31
# changing file download location
from selenium.webdriver.chrome.options import Options     # import Option class


chrome_Options = Options()       # create an object for this class
chrome_Options.add_experimental_option("prefs", {
    "download.default_directory": "C:\\Users\Diyanah\Pictures\PyCharmDownload"}
                                      )    # the preferred setting need to be define in {}

driver = webdriver.Chrome(options=chrome_Options, executable_path="C:\\Users\Diyanah\Downloads\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()

# 1. Text file
driver.find_element_by_id("textbox").send_keys("testing text file")
driver.find_element_by_id("createTxt").click()
driver.find_element_by_id("link-to-download").click()

# 2. PDF file
driver.find_element_by_id("pdfbox").send_keys("testing pdf file")
driver.find_element_by_id("createPdf").click()
driver.find_element_by_id("pdf-link-to-download").click()


# COOKIES -  5:05:00
# use for login credentials etc
# - capture all cookies from browser
# - count number of cookies
# - read cookies pairs
# - adding new cookies
# - deleting specific cookies by using name of cookies
# - deleting all cookies


# 1. Capture all cookies created by the browser
driver.get("https://github.com/")

cookies = driver.get_cookies()
print(len(cookies))
print(cookies)


# 2. Add cookie to the browser
cookie = {"name": "Mycookie",
          "value": "1234567890"
          }

driver.add_cookie(cookie)
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)


# 3. Deleting cookie
driver.delete_cookie("Mycookie")
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)


# 4. Delete all cookies
driver.delete_all_cookies()
cookies = driver.get_cookies()
print(len(cookies))
print(cookies)


# SCREENSHOTS -  5:23:00

driver.get("https://ringgitplus.com/en/")
driver.save_screenshot("C:/Users/Diyanah/Pictures/Saved Pictures/rp.jpg")

# another way, but this only accept PNG
driver.get_screenshot_as_file("C:/Users/Diyanah/Pictures/Saved Pictures/rp2.png")   
'''

# LOGGING
# Log levels
# - debug      Sev 3
# - info       Sev 2
# - warning    Sev 2
# - error      Sev 1
# - critical   Sev 1

import logging


# to log these logs in a file
# logging.basicConfig(filename="C:/Users/Diyanah/Documents/Selenium Log/test.log")
# logging.basicConfig(filename="test.log")    # will be store here in this folder
'''
# if we want to log debug and info logs, we need to specify using level
logging.basicConfig(filename="C:/Users/Diyanah/Documents/Selenium Log/test2.log",
                    level=logging.DEBUG)      # now, all is recorded

logging.debug("This is debug message")        # not printed by default
logging.info("This is info message")          # not printed by default
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")


# adding timestamp in the logs
logging.basicConfig(filename="C:/Users/Diyanah/Documents/Selenium Log/test3.log",
                    format="%(asctime)s: %(levelname)s: %(message)s",    # time : level name : message
                    level=logging.DEBUG)

logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")


# say we want to change date format
logging.basicConfig(filename="C:/Users/Diyanah/Documents/Selenium Log/test4.log",
                    format="%(asctime)s: %(levelname)s: %(message)s",    # time : level name : message
                    datefmt="%d/%m/%y %I:%M:%S %p",
                    level=logging.DEBUG)

logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("This is warning message")
logging.error("This is error message")
logging.critical("This is critical message")


# another way of writing this
logging.basicConfig(filename="C:/Users/Diyanah/Documents/Selenium Log/test5.log",
                    format="%(asctime)s: %(levelname)s: %(message)s",    # time : level name : message
                    datefmt="%d/%m/%y %I:%M:%S %p")
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.info("This is debug message")
logger.debug("This is info message")
logger.warning("This is warning message")
logger.error("This is error message")
logger.critical("This is critical message")
'''

# UNITTEST
import unittest


class Test(unittest.TestCase):     # inherit TestCase class

    def test_firstTest(self):
        print("This is my first unit test case")


if __name__ == "__main__":         # command to run the unit test
    unittest.main()



