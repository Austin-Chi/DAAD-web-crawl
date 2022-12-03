import requests
from bs4 import BeautifulSoup
import os
path = '/Users/austin/Desktop/NTUEE_2_1/Coding/morning.txt'
num = 0
for page in range(1,14):
    response0 = requests.get(
        "https://www.daad.org.tw/de/ueber-uns/aktuelles/page/"+str(page)+"/")
    soup0 = BeautifulSoup(response0.text, "html.parser")
    teaser_results = soup0.find_all("div", class_="teaser two-column-teaser")
    for tesear_result in teaser_results:
        num+=1
        img_link = tesear_result.select_one("img").get("src")
        print(img_link)
        if not os.path.exists("images"):
            os.mkdir("images")  # 建立資料夾
            print("directory built!")
        img = requests.get(img_link)  # 下載圖片
        pic_out = open("/Users/austin/Desktop/NTUEE_2_1/Coding/images/"  + str(num) + ".jpg", "wb")  # 開啟資料夾及命名圖片檔
        pic_out.write(img.content)  # 寫入圖片的二進位碼
        st = tesear_result.select_one("a").get("href")
        print(st)
        response = requests.get(
        st)
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find("div", class_="content-area row").find("div").find("div")
        paras = result.select("p")
        f = open(path, 'a')

        for para in paras:
            print(para.getText(), file = f)  #輸出排版後的HTML內容
        print('\n', file = f)
        info = result.select_one("div", class_="infobox infobox-full")#.select_one("p").select_one("a").get("href")
        print(info, file = f)
        print('\n', file = f)
        print('\n', file = f)
        f.close

print(num)
# print(soup.prettify())
