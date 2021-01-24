import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(executable_path="C:\chromedriver.exe")
driver.get("https://www.korayspor.com")
driver.maximize_window()

def wait(by, time):
    return WebDriverWait(driver, 10).until(EC.element_to_be_clickable((by, time)))

driver.find_element_by_class_name("btn-signin-span").click() 
driver.find_element_by_id("ctl00_u11_ascUyeGiris_txtKUTU_UYEEMAIL").send_keys("v_durmus8@outlook.com")
driver.find_element_by_id("ctl00_u11_ascUyeGiris_txtKUTU_UYESIFRE").send_keys("adgjmptw18")
driver.find_element_by_xpath("//*[@id=\"ctl00_u11_ascUyeGiris_lbfbtnKutuLogin\"]").click()



def search(arama):
    assert search_term, arama


search_term = driver.find_element_by_id("lbfSearchLabel").click()
driver.find_element_by_name("txtARM_KEYWORD").send_keys("futbol topu")
driver.find_element_by_name("txtARM_KEYWORD").send_keys(Keys.ENTER)