# py -m pip install selenium
# py -m pip install webdriver_manager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
try:
    x = input("Enter your CNIC: ")
    driver.get("https://pkphone.info/search-sim-database-online-2022.php")
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div/div/form/div[1]/input')))
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div/div/form/div[1]/input').send_keys(str(x))
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/div/div/div/form/div[1]/input').send_keys(Keys.ENTER)
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/table[1]/tbody/tr[1]/td[2]/span')))
    print("Phone Number: 0"+driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/table[1]/tbody/tr[1]/td[2]/span').get_attribute("innerText"))
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/table[1]/tbody/tr[2]/td[2]/span')))
    print("Name: "+driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/table[1]/tbody/tr[2]/td[2]/span').get_attribute("innerText"))
    WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/table[1]/tbody/tr[4]/td[2]/span')))
    print("Address: "+driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div[2]/div/div[2]/div/div/table[1]/tbody/tr[4]/td[2]/span').get_attribute("innerText"))
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
except:
    print("Invalid CNIC")