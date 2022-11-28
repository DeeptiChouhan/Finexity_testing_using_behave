import time
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
class Helper():
    def __init__(self, context):
        self.context = context
        
    def explicit_wait(self,locator_time):
        wait = WebDriverWait(self.context.browser,30).until(
            EC.visibility_of_all_elements_located(locator_time))
        for locator in wait:
            return locator
            
    def click_on_multiple_element(self,locator):
        elements = [element for element in WebDriverWait(self.context.browser, 25).until(
            EC.visibility_of_all_elements_located(locator))]
        print(elements)
        for element in elements:
            print(element)
            element.click()
            print("clicked on " , element.text)
        
    def hoverover(self,hoverover_on_locator):
        wait = WebDriverWait(self.context.browser,25)
        hover_bttn = wait.until(EC.element_to_be_clickable(hoverover_on_locator))
        actionchains=ActionChains(self.context.browser)
        actionchains.move_to_element(hover_bttn).perform()
        time.sleep(1)    
                   
                   
    