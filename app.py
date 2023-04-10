import streamlit as st
import pandas as pd
import time
import json
from datetime import datetime
import pathlib
import glob
import sys
sys.path.append(".")
import faker
import numpy as np
import pandas as pd
import time
import datetime as dt
from selenium import webdriver


st.write("""
    # Classificação de ruídos

    **Este App é destinado a demonstração do modelo de classificação de ruido**""")

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path="./chromedriver", options = options)

f = faker.Faker()
colors = ["Sim","Não"]
nome = "Julia"

url = "https://docs.google.com/forms/d/e/1FAIpQLSdo7cVObaa9W5K0Dpe_ndeO6BDlvojeYsIKC0JKQ2MczPGJCg/viewform?usp=sf_link"

#s=Service(ChromeDriverManager().install()) ##
#driver = webdriver.Chrome(executable_path=s,chrome_options=options )


driver.get(url)
time.sleep(2)

textboxes = driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/input')
textboxes.send_keys("App")
data = driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input' )
data.send_keys(str(dt.datetime.now()))

resp = driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input' )
resp.send_keys("Sim")

submit = driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
submit.click()

st.write("""
    # Enviado com sucesso""")
