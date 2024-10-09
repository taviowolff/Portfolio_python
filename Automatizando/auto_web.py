# # Passo 1: entrar no sistema da empresa

import pyautogui
from time import sleep

# pyatogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.5 # Definição de tempo entre códigos

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
sleep(2)

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

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    #clicar no campo de código
    pyautogui.click(x=1100,y=300)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha,"codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # Selecionar proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha,"obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # clicando no botão enviar
    #dar scroll de tudo para cima
    pyautogui.scroll(5000)
    # Passo 5 processo se repete até o fim