# # Passo 1: entrar no sistema da empresa

import pyautogui
from time import sleep

# pyatogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.1 # Definição de tempo entre códigos

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
sleep(1)
pyautogui.press("tab")
pyautogui.press("enter")

# entrar no link
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
sleep(3)

# Passo 2: Fazer login
# Selecionar o campo de email
pyautogui.click(x=1100,y=408)
# Escrever o seu email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") # selecionar próximo campo
pyautogui.write("sua senha")
pyautogui.press("tab")
pyautogui.press("enter")
sleep(3)
pyautogui.press("enter")

# Passo 3: importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("C:\\Users\\otavi\\OneDrive\\Documentos\\Portfolio_python\\produtos.csv")

print(tabela)