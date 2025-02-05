# Import webDriver
from selenium import webdriver

# accesing selectors in python
Element=driver. find_element(By.ID,"LoginID")  
Element=driver. find_element(By.NAME,"FormName")  
Element=driver. find_element(By.XPATH,"//form[@id='loginForm']")  

https://www.w3schools.com/xml/xpath_syntax.asp
**xpath for visible text :**  //*[text()='visible_text']

#driver inbuild methods
# https://www.geeksforgeeks.org/web-driver-methods-in-selenium-python/

# get location
element.location

# Save instance in element by selector
Element=driver. find_element(By.LINK_TEXT,"Continue")
Element=driver. find_element(By.PARTIAL_LINK_TEXT,"partial link text")
Element=driver. find_element(By.TAG_NAME,"h1")
Element=driver. find_element(By.CLASS_NAME,"content")
Element=driver. find_element(By.CSS_SELECTOR,"p.content")

# Import wait and exception from driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#EC conditions:
title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present

# Explicit Waits
element = WebDriverWait(driver, 10).until(  
    EC.presence_of_element_located((By.ID, "myDynamicElement"))

# implicit wait 
driver.implicitly_wait(10) # seconds

## Action chains
from selenium.webdriver.common.action_chains import ActionChains

# example 
action = ActionChains(driver)
Element = driver.find_element_by_css_selector(".nav")
actions.move_to_element(Element)
actions.click(Element)

# perform the operation
actions.perform()

# click the item 
action.click(on_element = element)

# click and hold  the item  
action.click_and_hold(on_element = element)

# context click the item 
action.context_click(on_element = element)

# double click the item 
action.double_click(on_element = element)

# drag and drop the item 
action.drag_and_drop(Element1, Element2)

# clicks Ctrl+C  (key down is pres key and hold ) 
action.key_down(Keys.CONTROL).send_keys('F').key_up(Keys.CONTROL).perform()
# or 
action.send_keys(Keys.CONTROL + Keys.ALT + Keys.Delete)
action.perform()
# or
action.key_down(Keys.CONTROL + Keys.ALT + Keys.Delete).perform()

# move the cursor 
action.move_by_offset(200, 200)

# perform the operation like collab move to element , click, perform 
action.move_to_element(element).click().perform()

## hold the mouse click 
# click the item
action.click(on_element = element)
action.pause(1000)

# click the item
action.click(on_element = element)
# send keys 
action.send_keys("Arrays")

# reset the action ---------
action.reset_actions()


# iterate in elements
elements = driver.find_elements_by_class_name('content_1')  
    for element in elements:  
        NumePlaje = element.find_element_by_class_name('content_2')  
        print (NumePlaje.text)  

# screen shot
driver.get_screenshot_as_file("file_name.jpg")

# swtich to alert
driver.switch_to_alert()


# get current window handle
p = driver.current_window_handle
#get first child window
chwd = driver.window_handles
for w in chwd:
#switch focus to child window  
    if(w!=p):  
    driver.switch_to.window(w)  

#find if checkbox is checked
# Find checkbox element
mycheckbox = driver.find_element(By.ID, 'banana')

# Check if checkbox is selected
if mycheckbox.is_selected():  
    print(f"{mycheckbox.get_attribute('value')} checkbox is selected.")  
else:  
    print(f"{mycheckbox.get_attribute('value')} checkbox is not selected.")  


url=driver.current_url()  

driver.execute_script("window.scrollBy(0,500)","")   
