# DOM
# CSSOM
# Eventos
# Ouvinte de Eventos

from selenium.webdriver import Firefox
from selenium.webdriver.support.events import (
    AbstractEventListener,
    EventFiringWebDriver,
)

from time import sleep

driver = Firefox()

url = "https://selenium.dunossauro.live/aula_07_d"
url2 = "https://selenium.dunossauro.live/aula_07_c"

sleep(4)

class Escuta(AbstractEventListener):
    def before_navigate_to(self, url, webdriver):
        print(f"O Link: {url}")
    
    def before_click(self, element, webdriver):
        span = webdriver.find_element_by_tag_name("span")
        print(span.text)
        # print("Antes do Click")
        
    def after_click(self, element, webdriver):
        span = webdriver.find_element_by_tag_name("span")
        print(span.text)
        # print("Depois do click")
        
wraperBroswer = EventFiringWebDriver(driver, Escuta())     
        
wraperBroswer.get(url)      
        

        
input_ = wraperBroswer.find_element_by_tag_name("input")
span = wraperBroswer.find_element_by_tag_name("span")
p = wraperBroswer.find_element_by_tag_name("p")


input_.click()

wraperBroswer.get(url2) 