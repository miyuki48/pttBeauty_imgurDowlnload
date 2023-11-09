import requests
from bs4 import BeautifulSoup

import os

def pttBeauty_imgurDowlnload(keyword,picsNum):   
    picNameList = []
    my_headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"}
    payload = {"from":"/bbs/Beauty/index.html",
                "yes":"yes"}
    
    sess = requests.Session()
    sess.post("https://www.ptt.cc/ask/over18" , data = payload, headers=my_headers)
    
    my_params = {"q":keyword}
    
    url = "https://www.ptt.cc/bbs/Beauty/search"
    
    while True:
        r = sess.post(url, params=my_params, headers=my_headers)
        if r.status_code == 200:
    
            soup = BeautifulSoup(r.text.split("[公告] 不願上表特")[0],"lxml")
            # print(soup)
    
            titles = soup.select("div.title a")
    
            for title in titles:
                # print(title.get("href"))           
                if "Re" not in title.text and keyword in title.text :
                    os.makedirs(keyword,exist_ok=True)
                    insideUrl = "https://www.ptt.cc"+title.get("href")
                    r2 = sess.get(insideUrl)
                    # print(insideUrl)
                    
                    soup2 = BeautifulSoup(r2.text.split("※ 發信站: 批踢踢實業坊")[0],"lxml")                
                    
                    picUrls = soup2.select("a")
                    
                    #存成Vqdx3Ta.png、rdXnSSF.png
                    no = 1
                    for picUrl in picUrls:
                        # print(picUrl.get("href"))
                
                        if "imgur" in picUrl.get("href"):
                            pic = picUrl.get("href").split("/")[-1]
                            if "." in pic:
                                savePic = "https://i.imgur.com/"+pic
                                picNameList.append(pic)
                            else:
                                savePic = "https://i.imgur.com/"+pic+".png"
                                picNameList.append(pic)
                            print(savePic)
                                
                            url = requests.get(savePic)
                            with open("./"+keyword+"/"+savePic.split("/")[-1],"wb") as save:
                                for data in url:
                                    save.write(data)
                            no += 1
                            picsNum -= 1
                            if picsNum == 0:
                                return picNameList
            if soup.select("div.action-bar a")[3].get("href") == None:
                print("沒有imgur圖片可以挖了QQ")
                return picNameList                                
            url = "https://www.ptt.cc"+soup.select("div.action-bar a")[3].get("href")      
      
        
name = input("請輸入想搜尋的人名:")
count = eval(input("請輸入想搜尋的張數:"))

picNameList = pttBeauty_imgurDowlnload(name,count)
