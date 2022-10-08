import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyautogui
def list():
    arq = open('l.txt', 'rt')
    lista = arq.readlines()
    Nlista = []
    for x in range(0, len(lista)):
        str = lista[x]
        Nlista.append(str[:-1])
    return Nlista


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    list_image = list()
    # print(list_image)
    navegador = webdriver.Chrome(executable_path=r" local do .... ->chromedriver.exe")
    '''exemplo: C:\User\PycharmProjects\auto-DownImage\venv\Lib\site-packages\selenium\webdriver\chromium\chromedriver.exe'''
    time.sleep(3)
    for x in range(0, len(list_image)):
        print(list_image[x])
        url = "Link"+f"{list_image[x]}"
        navegador.get(url)
        time.sleep(5)
        pyautogui.keyDown('Ctrl')
        pyautogui.press(['s'])
        pyautogui.keyUp('Ctrl')
        time.sleep(10)
        pyautogui.click(575, 439)
        time.sleep(5)
