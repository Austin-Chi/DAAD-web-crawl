
import requests
from bs4 import BeautifulSoup

ref = "https://www.mohw.gov.tw/lp-6565-1.html"
response0 = requests.get(ref)
soup0 = BeautifulSoup(response0.text, "html.parser")
print(soup0.prettify())
# <div class="job_info_content">
#                   <span>
#                    需管理人數 10 人以下
#                   </span>
#                  </div>
# //static.104.com.tw/b_profile/cust_picture/3000/23470593000/logo.gif?v=20210909171908