from selenium.webdriver import Firefox
from time import sleep
# url_drive = executable_path=r"./../driver/chromedriver.exe"
driver = Firefox()

url = "https://curso-python-selenium.netlify.app/aula_03.html"
driver.get(url)

sleep(5)
a = driver.find_element_by_tag_name("a")

for i in range(4):
    a.click()

p = driver.find_elements_by_tag_name("p")
for info in p:
    print(info.text)
    
driver.quit()