import requests
from bs4 import BeautifulSoup

html_text = requests.get("https://sksdb.hacettepe.edu.tr/bidbnew/grid.php?parameters=qbapuL6kmaScnHaup8DEm1B8maqturW8haidnI%2Bsq8F%2FgY1fiZWdnKShq8bTlaOZXq%2BmwWjLzJyPlpmcpbm1kNORopmYXI22tLzHXKmVnZykwafFhImVnZWipbq0f8qRnJ%2BioF6go7%2FOoplWqKSltLa805yVj5agnsGmkNORopmYXam2qbi%2Bo5mqlXRrinJdf1BQUFBXWXVMc39QUA%3D%3D")
html_text = str(html_text.content, "utf-8")
soup = BeautifulSoup(html_text, "lxml")
menus = soup.find_all("tr")

print("-------------------------")
for i in range(5):
    menu = menus[i]

    date = menu.find("div", class_ = "popular")
    allergens = date.find("p")
    allergens.extract()
    print(date.text[3:].strip())

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
        print(food)
    print("-------------------------")
input("PRESS ENTER TO EXIT")
