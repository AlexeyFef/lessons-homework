from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://ya.ru")
sleep(3)
driver.fullscreen_window()
driver.save_screenshot('./ya.png')

# driver.get("https://vk.ru")
# driver.back()
# driver.forward()
# driver.refresh()

sleep(10)