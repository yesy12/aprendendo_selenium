from selenium.webdriver import Firefox
from selenium.webdriver.support.events import (
    AbstractEventListener,
    EventFiringWebDriver
)
from time import sleep

driver = Firefox()

url = "https://selenium.dunossauro.live/exercicio_07"

nome_text = []
email_text = []
senha_text = []


class Escutando(AbstractEventListener):
    
    def before_click(self, element, webdriver):
        nome = webdriver.find_element_by_id("lnome").text
        email = webdriver.find_element_by_id("lemail").text
        senha = webdriver.find_element_by_id("lsenha").text
        
        if not "nome:" in nome_text:
            nome_text.append(nome)

        if not "email:" in email_text:
            email_text.append(email)
            
        if not "senha:" in senha_text:
            senha_text.append(senha)       
        
    def after_click(self, element, webdriver):
        nome = webdriver.find_element_by_id("lnome").text
        email = webdriver.find_element_by_id("lemail").text
        senha = webdriver.find_element_by_id("lsenha").text
        
        if nome != "nome:":
            nome_text.append(nome)
        
        if email != "email:":
            email_text.append(email)
        
        if senha != "senha:":
            senha_text.append(senha)

        

wraperBroswer = EventFiringWebDriver(driver,Escutando())
wraperBroswer.get(url)

sleep(4)
nome = wraperBroswer.find_element_by_id("nome")
nome.send_keys("Alison")
nome.click()

email = wraperBroswer.find_element_by_id("email")
email.send_keys("a@a.com")
email.click()

senha = wraperBroswer.find_element_by_id("senha")
senha.send_keys("123456")
senha.click()

button = wraperBroswer.find_element_by_id("btn")
button.click()


print(nome_text)
# ['nome:', 'Não vale mentir o nome']
print(email_text)
# ['email:', 'Esse email é mesmo válido?']
print(senha_text)
# ['senha:', 'Já falei pra não colocar 1234']