from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.chrome.options import Options 
from selenium.common.exceptions import TimeoutException 
from selenium.webdriver.common.keys import Keys 
import time 
import os
import subprocess
  
chrome_options = webdriver.ChromeOptions() 
  
prefs = {"profile.default_content_setting_values.notifications": 2} 
chrome_options.add_experimental_option("prefs", prefs) 
try:
    browser = webdriver.Chrome(options=chrome_options)
except Exception as e:
    print("Erro ao criar o objeto webdriver.Chrome:", str(e))
    raise e 
browser.get('https://www.facebook.com/') 
username = 'joaorobertodemoraes@outlook.com.br'

with open('pass2.txt', 'r') as myfile: 
    password = myfile.read().replace('\n', '') 
  
print("Iniciando programa...") 
print("Inciando login em conta 1...")
  
element = browser.find_elements(By.XPATH, '//*[@id ="email"]') 
element[0].send_keys(username) 
  
print("Usuario escrito") 
  
element = browser.find_element(By.XPATH, '//*[@id ="pass"]') 
element.send_keys(password)
  
print("Senha escrita") 
log_in = browser.find_element(By.NAME, 'login') 
log_in.click()
  
print("Login realizado com sucesso")
time.sleep(5) 
  
browser.get('https://www.facebook.com/events/birthdays/')
time.sleep(5) 
  
feed = 'A Gramado Coffee & Chocolate (Bebedouro, SP) parabeniza você nesta data tão especial!!'

parent = browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div[2]")

children = parent.find_elements(By.XPATH, "./child::*")

for i in range(len(children)):
    try:
        txt = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div[" + str(i+1) + "]/div/div[2]/div[2]/div/form/input"
        button = browser.find_element(By.XPATH, txt)
        txt = "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div/div/div/div[2]/div[" + str(i+1) + "]/div/div[2]/div[2]/div/form/div/div/div[1]/div[1]"
        message = browser.find_element(By.XPATH, txt)
        message.send_keys(feed)
        message.send_keys(Keys.RETURN)
        print('parabens enviado!')
    except:
        print('Mensagem deve ser enviada por Messenger')   

browser.close()