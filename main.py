import requests
from bs4 import BeautifulSoup
from tkinter import *
from PIL import Image,ImageTk

window = Tk()
window.title("Routine Automat")

window.resizable(False, False)
S_WIDTH = window.winfo_screenwidth()
S_HEIGHT = window.winfo_screenheight()
W_WIDTH = int(S_WIDTH / 2)
W_HEIGHT = int(S_HEIGHT * 0.84)
W_X = int((S_WIDTH / 2) - (W_WIDTH / 2))
W_Y = int(0.8*((S_HEIGHT / 2) - (W_HEIGHT / 2)))
window.geometry("{}x{}+{}+{}".format(W_WIDTH, W_HEIGHT, W_X, W_Y))

windowicon = PhotoImage(file = "windowlogo.png")
window.iconphoto(True, windowicon)
window.config(background = "black")

MENULABEL_WIDTH = int(W_WIDTH / 4)
MENULABEL_HEIGHT = W_HEIGHT
menuimage = ImageTk.PhotoImage(Image.open("menu.png").resize((MENULABEL_WIDTH, MENULABEL_HEIGHT)))
menulabel = Label(window,
                  text = '\n',
                  font = ("Monaco", 8, "bold italic"),
                  bg = "white",
                  fg = "black",
                  image = menuimage,
                  compound = "center",
                  width = MENULABEL_WIDTH,
                  height = MENULABEL_HEIGHT,
                  bd = 0,
                  highlightthickness = 0)

html_text = requests.get("https://sksdb.hacettepe.edu.tr/bidbnew/grid.php?parameters=qbapuL6kmaScnHaup8DEm1B8maqturW8haidnI%2Bsq8F%2FgY1fiZWdnKShq8bTlaOZXq%2BmwWjLzJyPlpmcpbm1kNORopmYXI22tLzHXKmVnZykwafFhImVnZWipbq0f8qRnJ%2BioF6go7%2FOoplWqKSltLa805yVj5agnsGmkNORopmYXam2qbi%2Bo5mqlXRrinJdf1BQUFBXWXVMc39QUA%3D%3D")
html_text = str(html_text.content, "utf-8")
soup = BeautifulSoup(html_text, "lxml")
menus = soup.find_all("tr")

for indexMenu in range(5):
    menu = menus[indexMenu]

    date = menu.find("div", class_ = "popular")
    allergens = date.find("p")
    allergens.extract()
    menulabel.config(text=menulabel.cget("text") + date.text[3:].strip() + '\n')

    menu = menu.p
    unwantedtext = menu.find("strong")
    unwantedtext.extract()

    for br in soup.find_all("br"):
        br.replace_with("\n")
    menu.text.strip()
    foods = menu.text.split("\n")
    for i in range(len(foods)):
        if("(" in foods[i]):
            index = foods[i].find("(")
            foods[i] = foods[i][:index]
        foods[i] = foods[i].strip()
    for i in range(len(foods)-1, -1, -1):
        if(foods[i] == "" or foods[i].startswith("Sıhhiye") or foods[i].startswith("*")):
            del foods[i]
    for food in foods:
        menulabel.config(text=menulabel.cget("text") + food + '\n')
    if(indexMenu != 4):
        menulabel.config(text = menulabel.cget("text") + "---------------------------\n")

menulabel.place(x = 0, y = 0)
window.mainloop()
