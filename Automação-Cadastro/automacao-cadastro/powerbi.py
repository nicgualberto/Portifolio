# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# Passo 2: Logar no sistema da empresa
# Passo 3: Importar base de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir o processo para todos os produtos

import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("Chrome")
pyautogui.press("enter")

time.sleep(1)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(3)

# Logar no sistema
# cordenadas1 : Point(x=444, y=373)
# cordenadas2 : Point(x=452, y=476)
# cordenadas3 : Point(x=672, y=528)

pyautogui.click(x=444, y=373)
pyautogui.write("testepython@gmail.com")
pyautogui.click(x=452, y=476)
pyautogui.write("senhateste1")
pyautogui.click(x=672, y=528)

# Importar base de dados
# Cadastrar produtos
time.sleep(3)

import pandas

tabela = pandas.read_csv("produtos.csv")
# cordenadas4 : Point(x=575, y=258)

# referência
# Cadastrar o primeiro produto
for linha in tabela.index:
    time.sleep(1)
    pyautogui.click(x=575, y=258)
    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = str(tabela.loc[linha, "marca"])
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = str(tabela.loc[linha, "tipo"])
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
        
    # registrar o produto
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(10000)
