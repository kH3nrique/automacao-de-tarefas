import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")

pyautogui.hotkey()
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#tempo para carregar o site
time.sleep(3)

#realização do login
pyautogui.click(x=573, y=398)
pyautogui.write("kh3nriqueafs18@gmail.com")

pyautogui.press("tab")
pyautogui.write("asdfghjkl")

pyautogui.press("tab")
pyautogui.click(x=669, y=560)
time.sleep(5)

#cadastro de produtos
import pandas
tabela = pandas.read_csv("produtos.csv")

print(tabela)
for i in tabela.index:
    
    #código
    pyautogui.click(x=686, y=285)
    pyautogui.write(tabela.loc[i, "codigo"])

    #marca
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[i, "marca"])

    #tipo
    pyautogui.press("tab")
    pyautogui.write(tabela.loc[i, "tipo"])

    #categoria
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[i, "categoria"]))

    #preço
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[i, "preco_unitario"]))

    #custo
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[i, "custo"]))

    #observação
    pyautogui.press("tab")
    #verifica se a obs está vazia
    obs = tabela.loc[i, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(obs)

    #enviar produtos
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll("5000")