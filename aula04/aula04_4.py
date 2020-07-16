from selenium.webdriver import Firefox
from urllib.parse import urlparse

driver = Firefox()

url = "https://selenium.dunossauro.live/aula_04.html"

driver.get(url)

url_parse = urlparse(driver.current_url)
driver.refresh()
#ParseResult(
    # scheme='https', 
    # netloc='selenium.dunossauro.live', 
    # path='/aula_04.html', 
    # params='', 
    # query='', 
    # fragment='')