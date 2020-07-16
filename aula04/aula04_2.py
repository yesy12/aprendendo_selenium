# Selenium com Python #04 - Navegação e atributos
# Busca aninhada
# Atributos
# Navegação
from selenium.webdriver import Firefox
from time import sleep

driver = Firefox()

url = "http://selenium.dunossauro.live/aula_04_a.html"
driver.get(url)
sleep(2)

def find_by_text(driver, tag, text): 
    """
    Encontrar o elemento com o texto `text`.
    
    Argumentos:
        - driver = Instancia do Navegador [firefox,Opera,Chrome]
        - tag = onde será procurado o coutendo
        - texto = conteudo da tag
    """
    
    elementos = driver.find_elements_by_tag_name(tag)
    for elemento in elementos:
        if(elemento.text == text):
            return elemento
    return 

def find_by_href(driver, link):
    """
    Encontrar o elemento `a` com o link `link`.
    
    Argumentos:
        - driver = Instancia do Navegador [firefox,Opera,Chrome]
        - link = link que será procurado em todos os a    
    """
    
    elementos = driver.find_elements_by_tag_name("a")
    
    for elemento in elementos:
        if( link in elemento.get_attribute("href")):
            return elemento
    return 
        
google = find_by_text(driver,"li","Google")
google_url = find_by_href(driver,"google")


