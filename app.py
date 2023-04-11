import streamlit as st
from selenium import webdriver
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
from selenium.webdriver.common.by import By
import time
import datetime as dt


option = st.radio('Você concorda com a classificão dada pelo modelo:',
                  ['Sim',
                   'Não'])

st.write('You selected:', option)

st.write("""
    # Classificação de ruídos

    **Este App é destinado a demonstração do modelo de classificação de ruido**""")




if st.button('enviar resposta'):
    f = faker.Faker()
    colors = ["Sim","Não"]
    nome = "Julia"

    url = "https://docs.google.com/forms/d/e/1FAIpQLSdo7cVObaa9W5K0Dpe_ndeO6BDlvojeYsIKC0JKQ2MczPGJCg/viewform?usp=sf_link"
    import streamlit as st
    import os, sys

    @st.experimental_singleton
    def installff():
      os.system('sbase install geckodriver')
      os.system('ln -s /home/appuser/venv/lib/python3.7/site-packages/seleniumbase/drivers/geckodriver /home/appuser/venv/bin/geckodriver')

    _ = installff()
    from selenium import webdriver
    from selenium.webdriver import FirefoxOptions
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    driver = webdriver.Firefox(options=opts)

    driver.get(url)
    time.sleep(2)

    textboxes = driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[2]/div/div/div/div[2]/div/div[1]/div/div[1]/input')
    textboxes.send_keys("AppLocal")
    data = driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input' )
    data.send_keys(str(dt.datetime.now()))

    resp = driver.find_element('xpath','//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input' )
    resp.send_keys(option)

    submit = driver.find_element('xpath', '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()

    st.write("""
        # Enviado com sucesso""")
