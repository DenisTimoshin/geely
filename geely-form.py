from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import Keys


# Опции браузера
options = webdriver.ChromeOptions()
#options.add_argument("--headless")
options.add_argument(" --window-size=1920,1080")

# Инициализация драйвера
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 30, poll_frequency=1)

#Футер новостная рассылка

driver.get("https://www.geely-motors.com/")


input__name = driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("Test")

input__email = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("test@test.test")

check__phone = driver.find_element(By.XPATH, '//*[@id="newsletter"]/div[3]/label[1]/i').click()

check__phone = driver.find_element(By.XPATH, '//*[@id="newsletter"]/div[3]/label[2]/i').click()

btn = driver.find_element(By.XPATH, '//*[@id="newsletter"]/div[2]/div/div/button').click()

DELETE_BUTTON = (By.XPATH, '/html/body/div/div[4]/div[1]/div[2]/button')
wait.until(EC.visibility_of_element_located(DELETE_BUTTON)).click()



#Тест драйв
driver.get("https://www.geely-motors.com/forbuyers/test-drive")
input__name = driver.find_element(By.XPATH, '//*[@id="test-drive-form"]/div[1]/label[1]/div').click()
input__name = driver.find_element(By.XPATH, '//*[@id="test-drive-form"]/div[1]/label[1]/div/div/ul/li[3]').click()


input__name = driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("Test")

input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').click()
input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)

check__phone = driver.find_element(By.XPATH, '//*[@id="model-group"]/div[1]/div/div[1]/label/i').click()

check__phone = driver.find_element(By.XPATH, '//*[@id="test-drive-form"]/div[8]/div[3]/label/i').click()

btn = driver.find_element(By.XPATH, '//*[@id="test-drive-form"]/div[8]/button').click()

DELETE_BUTTON = (By.XPATH, '/html/body/div/div[2]/div[3]/div/div[2]/span/p/span/span')
wait.until(EC.visibility_of_element_located(DELETE_BUTTON))



#Записаться на сервис
driver.get("https://www.geely-motors.com/for-owners/maintain-and-repair/servicebooking")
input__name = driver.find_element(By.XPATH, '//*[@id="offer-form"]/div[1]/label[1]/div').click()
input__name = driver.find_element(By.XPATH, '//*[@id="offer-form"]/div[1]/label[1]/div/div/ul/li[2]').click()


input__name = driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("Test")
input__name = driver.find_element(By.XPATH, '//*[@id="lastName"]').send_keys("Test")
input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').click()
input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)
input__email = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("test@test.test")

check__phone = driver.find_element(By.XPATH, '//*[@id="model-group"]/div[1]/div/div[1]/label/i').click()

check__phone = driver.find_element(By.XPATH, '//*[@id="offer-form"]/div[8]/div[3]/label/i').click()

btn = driver.find_element(By.XPATH, '//*[@id="offer-form"]/div[8]/button').click()

DELETE_BUTTON = (By.XPATH, '/html/body/div/div[2]/div[3]/div/div[2]/span/p/span/span')
wait.until(EC.visibility_of_element_located(DELETE_BUTTON))

#ФОС
driver.get("https://www.geely-motors.com/forbuyers/getaquote")

input__name = driver.find_element(By.XPATH, '//*[@id="offer-form"]/div[1]/label[1]/div').click()
input__name = driver.find_element(By.XPATH, '//*[@id="offer-form"]/div[1]/label[1]/div/div/ul/li[2]').click()

input__name = driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("Test")
input__name = driver.find_element(By.XPATH, '//*[@id="lastName"]').send_keys("Test")
input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').click()
input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)
input__email = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("test@test.test")

check__phone = driver.find_element(By.XPATH, '//*[@id="model-group"]/div[1]/div/div[1]/label/i').click()

check__phone = driver.find_element(By.XPATH, '//*[@id="offer-form"]/div[8]/div[3]/label/i').click()

btn = driver.find_element(By.XPATH, '//*[@id="offer-form"]/div[8]/button').click()

DELETE_BUTTON = (By.XPATH, '/html/body/div/div[2]/div[3]/div/div[2]/span/p/span/span')
wait.until(EC.visibility_of_element_located(DELETE_BUTTON))

#ФОС VIN

driver.get("https://www.geely-motors.com/for-owners/customer-support")


input__name = driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("Test")
input__name = driver.find_element(By.XPATH, '//*[@id="lastName"]').send_keys("Test")
input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').click()
input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)
input__email = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("test@test.test")
input__vin = driver.find_element(By.XPATH, '//*[@id="vin"]').send_keys("LB37844S18X044933")

input__name = driver.find_element(By.XPATH, '//*[@id="support-form"]/div/div[1]/label[7]/div').click()
input__name = driver.find_element(By.XPATH, '//*[@id="support-form"]/div/div[1]/label[7]/div/div/ul/li[2]').click()

check__phone = driver.find_element(By.XPATH, '//*[@id="support-form"]/div/div[4]/label/i').click()

btn = driver.find_element(By.XPATH, '//*[@id="support-form"]/div/button').click()

DELETE_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div[2]/span/p/span/span')
wait.until(EC.visibility_of_element_located(DELETE_BUTTON))

driver.get("https://www.geely-motors.com/forbuyers/tradeinpolicy")

input__name = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[5]/div[1]/div[2]/div[3]/div[2]/div/div[1]/label[1]/i').click()
input__name = driver.find_element(By.XPATH, '/html/body/div/div[2]/div[5]/div[2]/div/button').click()

input__name = driver.find_element(By.XPATH, '//*[@id="firstName"]').send_keys("Test")
input__name = driver.find_element(By.XPATH, '//*[@id="lastName"]').send_keys("Test")
input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').click()
input__phone = driver.find_element(By.XPATH, '//*[@id="phone"]').send_keys(1111111111)
input__email = driver.find_element(By.XPATH, '//*[@id="email"]').send_keys("test@test.test")


check__phone = driver.find_element(By.XPATH, '//*[@id="model-group"]/div[1]/div/div[1]/label/i').click()

check__phone = driver.find_element(By.XPATH, '//*[@id="leading-form"]/div[8]/div[3]/label/i').click()

btn = driver.find_element(By.XPATH, '//*[@id="leading-form"]/div[8]/button').click()

DELETE_BUTTON = (By.XPATH, '/html/body/div[1]/div[2]/div[3]/div/div[2]/span/p/span/span')
wait.until(EC.visibility_of_element_located(DELETE_BUTTON))
print("Победа")