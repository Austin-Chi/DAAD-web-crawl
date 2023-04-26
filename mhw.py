
import requests
from bs4 import BeautifulSoup

ref0 = "https://www.mohw.gov.tw/lp-6565-1-"
ref1 = "-20.html"
for i in range(1,5):
	response0 = requests.get(ref0+str(i)+ref1)
	soup0 = BeautifulSoup(response0.text, "html.parser")
	sect = soup0.find("section", class_ = "list01")
	# print(sect)
	listOfA = sect.find_all("a")
	for ais in listOfA:
		# print(ais.get("href"))
		ref = ais.get("href")
		response = requests.get(ref)
		soup = BeautifulSoup(response.text, "html.parser")
		title = soup.find("section", class_ = "cp").select_one("h2").getText()
		print("標題："+title)
		paragraoh = soup.find("article").getText()
		print("內文："+paragraoh)
		print(" ")
