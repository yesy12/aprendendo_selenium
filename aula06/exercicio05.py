from selenium.webdriver import Firefox
from time import sleep

driver = Firefox()
url = "https://selenium.dunossauro.live/exercicio_05.html"

driver.get(url)

for a in range(1,5):
    sleep(2)
    header_span = driver.find_element_by_tag_name("span")
    print(header_span.text)
    form = driver.find_element_by_css_selector(f".form-{header_span.text}")

    form_input_name = form.find_element_by_css_selector("[name='nome']")
    form_input_name.send_keys("Alison")

    sleep(0.2)
    form_password_name = form.find_element_by_css_selector("[name='senha']")
    form_password_name.send_keys("1")
    sleep(0.3)

    button_submit = form.find_element_by_css_selector(f"[name={header_span.text}]")
    button_submit.click()
    
    sleep(4)