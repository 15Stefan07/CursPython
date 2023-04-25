from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pandas as pd

browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-1-martie-ora-13-00-2/")

header = browser.find_element(by=By.XPATH, value="//*[@id=\"post-29587\"]/div/div/table[1]/tbody/tr[1]")
header_list = header.text.split(" ")
# print(header_list)
# print(header_list[0] + " " + header_list[1])
# print(header_list[2])
# print(type(header_list))
# //*[@id="post-29587"]/div/div/table[1]/tbody/tr[1]/td[1]
cap_tabel = []
cap_tabel.append(header_list[0]+ " "+ header_list[1])
cap_tabel.append(header_list[2])
cap_tabel.append("01.03")
cap_tabel.append("02.03")
cap_tabel.append("03.03")
cap_tabel.append("04.03")
cap_tabel.append("05.03")
# print(cap_tabel)

lista_orase = []
for i in range(2,46):
    text_tabel = browser.find_element(by=By.XPATH, value="//*[@id=\"post-29587\"]/div/div/table[1]/tbody/tr[{0}]/td[2]".format(i))
    lista_orase.append(text_tabel.text)
# print(lista_orase)
# print("\n")

nr_crt = []
for i in range(2,46):
    text_tabel = browser.find_element(by=By.XPATH, value="//*[@id=\"post-29587\"]/div/div/table[1]/tbody/tr[{0}]/td[1]".format(i))
    nr_crt.append(text_tabel.text)

# print(nr_crt)
# print("\n")
# //*[@id="post-29587"]/div/div/table[1]/tbody/tr[2]/td[1]

# //*[@id="post-29587"]/div/div/table[1]/tbody/tr[45]/td[3]

# //*[@id="post-29627"]/div/div/table[1]/tbody/tr[45]/td[3]

# //*[@id="post-29664"]/div/div/table[1]/tbody/tr[45]/td[3]

# //*[@id="post-29690"]/div/div/table[1]/tbody/tr[2]/td[3]

# //*[@id="post-29726"]/div/div/table[1]/tbody/tr[45]/td[3]

date_ziua_unu = []
for i in range(2,47):
    text_tabel = browser.find_element(by=By.XPATH, value="//*[@id=\"post-29587\"]/div/div/table[1]/tbody/tr[{0}]/td[3]".format(i))
    date_ziua_unu.append(text_tabel.text)
# print(date_ziua_unu)
# print("\n")


browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-2-martie-ora-13-00-2/")

date_ziua_doi = []
for i in range(2,46):
    text_tabel = browser.find_element(by=By.XPATH, value="//*[@id=\"post-29627\"]/div/div/table[1]/tbody/tr[{0}]/td[3]".format(i))
    date_ziua_doi.append(text_tabel.text)
# print(date_ziua_doi)
# print("\n")


browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-3-martie-ora-13-00-2/")

date_ziua_trei = []
for i in range(2,46):
    text_tabel = browser.find_element(by=By.XPATH, value="//*[@id=\"post-29664\"]/div/div/table[1]/tbody/tr[{0}]/td[3]".format(i))
    date_ziua_trei.append(text_tabel.text)
# print(date_ziua_trei)
# print("\n")

browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-4-martie-ora-13-00-3/")

date_ziua_patru = []
for i in range(2,46):
    text_tabel = browser.find_element(by=By.XPATH, value="//*[@id=\"post-29690\"]/div/div/table[1]/tbody/tr[{0}]/td[3]".format(i))
    date_ziua_patru.append(text_tabel.text)
# print(date_ziua_patru)
# print("\n")

browser.get("https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-5-martie-ora-13-00/")

date_ziua_cinci = []
for i in range(2,46):
    text_tabel = browser.find_element(by=By.XPATH, value="//*[@id=\"post-29726\"]/div/div/table[1]/tbody/tr[{0}]/td[3]".format(i))
    date_ziua_cinci.append(text_tabel.text)
# print(date_ziua_cinci)
# print("\n")


dictionar = {i: [] for i in cap_tabel}
for j in range(0,len(cap_tabel)):
    for i in range(44):
        if j == 0:
            dictionar[cap_tabel[int(j)]].append(nr_crt[i])
        elif j == 1:
            dictionar[cap_tabel[int(j)]].append(lista_orase[i])
        elif j == 2:
            dictionar[cap_tabel[int(j)]].append(date_ziua_unu[i])
        elif j == 3:
            dictionar[cap_tabel[int(j)]].append(date_ziua_doi[i])
        elif j == 4:
            dictionar[cap_tabel[int(j)]].append(date_ziua_trei[i])
        elif j == 5:
            dictionar[cap_tabel[int(j)]].append(date_ziua_patru[i])
        else:
            dictionar[cap_tabel[int(j)]].append(date_ziua_cinci[i])

print(dictionar)
df = pd.DataFrame(dictionar)
df.to_excel("INFO_COVID19.xlsx")