from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# драйвер
driver = webdriver.Firefox()

# На закупки
driver.get('https://zakupki.gov.ru/epz/order/extendedsearch/results.html')

# Загрузка страницы
wait = WebDriverWait(driver, 10)

# Ищем
search_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-primary')))

# Взаимодействие с кнопкой
search_button.click()

# Закрываем
#driver.quit()

