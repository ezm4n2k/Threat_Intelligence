import time;
import random
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

#Stop and wait
def wait(timeFrom, timeTo = 0):
    if(timeTo > 0 and timeTo > timeFrom):
        time.sleep(random.randint(timeFrom, timeTo));
    time.sleep(timeFrom);

#Wait ultil element loaded
def waitElement(driver, elm, selectorBy = By.CSS_SELECTOR):
    while(True):
        elems = driver.find_elements(by=selectorBy, value=elm);
        if(len(elems) > 0): 
            break
        time.sleep(1);

#find an element
def findElement(driver, elem, selectorBy = By.CSS_SELECTOR):
    return driver.find_element(selectorBy, elem);
def getElement(driver, elem, selectorBy = By.CSS_SELECTOR):
    return findElement(driver, elem, selectorBy)

#find a list of elements    
def findElements(driver, elem, selectorBy = By.CSS_SELECTOR):
    return driver.find_elements(selectorBy, elem);
def getElements(driver, elem, selectorBy = By.CSS_SELECTOR):
    return findElements(driver, elem, selectorBy)

def elementExist(driver, selector, selectorBy = By.CSS_SELECTOR):
    elements = findElements(driver, selector, selectorBy);
    return len(elements)>0;
    
def clickToElm(driver, element):
    action = ActionChains(driver)
    action.move_to_element(element)
    action.click_and_hold()
    action.release()
    action.perform()
    
def clickToElement(driver, element):
    clickToElm(driver, element);
    
#get elemenet attribute by attribute code
def getElmAttr(elm, attribute):
    return elm.get_attribute(attribute)

#get element text    
def getElmText(elm):
    return getElmAttr(elm, 'innerText')

#get element html
def getElmHtml(elm):
    return getElmAttr(elm, 'innerHTML')

#get element value    
def getElmValue(elm):
    return getElmAttr(elm, 'value')

#execute a javascript
def exeScript(driver, script):
    driver.execute_script(script)

#scroll the page down
def scrollPageDown(driver, scroll_amount = 0):
    if(scroll_amount == 0):
        scroll_amount = random.randint(500, 800)
    i = 0;
    j = 0;
    while (i < scroll_amount):
        scrollStep = random.randint(3, 5) + j
        driver.execute_script(f"window.scrollBy(0, {scrollStep});")
        j += 1;
        i +=scrollStep;

def waitForElement(driver, selector, seconds = False):
    waitTime = 0
    while (True):
        if waitTime > seconds:
            break;
            
        if elementExist(driver, selector):
            return True;
        wait(1);

    return False;