# Passo a Passo do projeto
# Passo 1: Entrar no sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login
# pip install pyautogui
import pyautogui
import time
import pandas

pyautogui.PAUSE = 0.5

# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar 1 tecla do teclado

# abrir  navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no site
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# dar uma pausa um pouco maior (3) segundos
time.sleep(3)

# Passo 2: Fazer 
pyautogui.click(x=3320, y=519)
pyautogui.write("teste@gmail.com")

#ecrever a senha
pyautogui.press("tab")
pyautogui.write("senhateste")

# clicar no botão de logar
pyautogui.click(x=3388, y=708)
time.sleep(3)

# Passo 3: Importar a base de dados
# pip install pandas numpy openxl
tabela = pandas.read_csv("produtos.csv")

# Passo 4: Cadastrar um produto
# para cada linha da minha tabela
for linha in tabela.index:

    # Clica no pop-up do chrome
    pyautogui.click(x=3614, y=454)
    # clicar no primeiro campo
    pyautogui.click(x=3033, y=368)

    # código do produto
    codigo = tabela.loc[linha, "codigo"] # .loc é pra localizar uma informação dentro da tabela
    pyautogui.write(codigo)
    pyautogui.press("tab")

    # marca
    pyautogui.write(tabela.loc[linha, "marca"])
    pyautogui.press("tab")

    # tipo
    pyautogui.write(tabela.loc[linha, "tipo"])
    pyautogui.press("tab")

    # categoria
    # str() string -> texto
    # str(1) -> 1 -> "1"
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    # preco
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    # custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # obs
    obs = str(tabela.loc[linha, "obs"])
    if not pandas.isna(obs):
        pyautogui.write(obs) # .isna verifica se está vazio
    pyautogui.press("tab")

    # enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até acabar

# Programando horário para rodar seu código: https://www.youtube.com/watch?v=SxEjHAlCqmo
