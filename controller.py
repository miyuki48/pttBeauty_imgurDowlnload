'''
讓使用者輸入找某人照片+張數，秀出該張數之照片(用到動態元件之產生)
'''
import requests
from bs4 import BeautifulSoup
import os

from PyQt5 import QtWidgets, QtGui, QtCore
from UI import Ui_MainWindow

from PyQt5.QtGui import QImage, QPixmap
import cv2
import numpy as np

from time import sleep

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
		# in python3, super(Class, self).xxx = super().xxx
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_control()

    def setup_control(self):
        self.count = 0
        self.ui.pushButton.clicked.connect(self.buttonClicked)
        self.ui.nextButton.clicked.connect(self.nextButtonClicked)
        self.ui.lastButton.clicked.connect(self.lastButtonClicked)
        
        self.picNameList = []
        self.picDownloadNums = 0
        self.totalPage=0
        self.currentPage=0
        self.keyword = ""
        
    def buttonClicked(self):
        self.ui.downloadMsg.setText("下載中請稍等...")
        self.ui.downloadMsg.repaint()  #https://stackoverflow.com/questions/4510712/qlabel-settext-not-displaying-text-immediately-before-running-other-method
        self.ui.pushButton.setEnabled(False)
        self.ui.downloadMsg.repaint()

        self.ui.page.setText("")
        self.ui.result_1.setPixmap(QPixmap())
        self.ui.result_2.setPixmap(QPixmap())
        self.ui.result_3.setPixmap(QPixmap())
        self.ui.result_4.setPixmap(QPixmap())
        self.ui.result_5.setPixmap(QPixmap())
        self.ui.result_6.setPixmap(QPixmap())
        
        global picNameList,picDownloadNums,keyword
        keyword = self.ui.keyword.text()
        picsNum = eval(self.ui.picsNum.text())
        
        self.picNameList = self.pttBeauty_imgurDowlnload(keyword,picsNum) 
        self.picDownloadNums = len(self.picNameList)
        print(self.picNameList)
        
        if self.picDownloadNums > 0:
            global totalPage,currentPage
            self.totalPage = (self.picDownloadNums-1) // 6 +1
            self.currentPage = 1
            self.ui.downloadMsg.setText("下載完畢!")
            
            if self.picDownloadNums < 6:
                for i in range(self.picDownloadNums):
                    self.img_path = fr".\{keyword}\{self.picNameList[i]}"
                    self.display_img(i+1)
                    self.ui.page.setText(f"第1頁/共{self.totalPage}頁,總共{self.picDownloadNums}張")
            else:
                for i in range(6):
                    self.img_path = fr".\{keyword}\{self.picNameList[i]}"
                    self.display_img(i+1)
                    self.ui.page.setText(f"第1頁/共{self.totalPage}頁,總共{self.picDownloadNums}張")
            
            if self.totalPage > self.currentPage:
                self.ui.nextButton.setEnabled(True)

            self.ui.pushButton.setEnabled(True)
            
        else:
            self.display_noImg()
            
    def nextButtonClicked(self):
        self.ui.page.setText("")
        self.ui.result_1.setPixmap(QPixmap())
        self.ui.result_2.setPixmap(QPixmap())
        self.ui.result_3.setPixmap(QPixmap())
        self.ui.result_4.setPixmap(QPixmap())
        self.ui.result_5.setPixmap(QPixmap())
        self.ui.result_6.setPixmap(QPixmap())
        
        self.currentPage += 1 
        
        try:
            for i in range(6*(self.currentPage-1),6*self.currentPage):
                self.img_path = fr".\{keyword}\{self.picNameList[i]}"
                self.display_img(i+1)
                self.ui.page.setText(f"第{self.currentPage}頁/共{self.totalPage}頁,總共{len(self.picNameList)}張")
        except:
            pass
        
        if self.totalPage > self.currentPage and self.currentPage > 1:
            self.ui.nextButton.setEnabled(True)        
            self.ui.lastButton.setEnabled(True)  
        elif self.totalPage > self.currentPage:
            self.ui.nextButton.setEnabled(True)
            self.ui.lastButton.setEnabled(False) 
        elif self.currentPage > 1:    
            self.ui.nextButton.setEnabled(False) 
            self.ui.lastButton.setEnabled(True) 
        else:
            self.ui.nextButton.setEnabled(False)
            self.ui.lastButton.setEnabled(False)
            
    def lastButtonClicked(self):
        self.ui.page.setText("")
        self.ui.result_1.setPixmap(QPixmap())
        self.ui.result_2.setPixmap(QPixmap())
        self.ui.result_3.setPixmap(QPixmap())
        self.ui.result_4.setPixmap(QPixmap())
        self.ui.result_5.setPixmap(QPixmap())
        self.ui.result_6.setPixmap(QPixmap())
        
        self.currentPage -= 1 
        try:
            for i in range(6*(self.currentPage-1),6*self.currentPage):
                self.img_path = fr".\{keyword}\{self.picNameList[i]}"
                self.display_img(i+1)
                self.ui.page.setText(f"第{self.currentPage}頁/共{self.totalPage}頁,總共{len(self.picNameList)}張")
        except:
            pass
        if self.totalPage > self.currentPage and self.currentPage > 1:
            self.ui.nextButton.setEnabled(True)        
            self.ui.lastButton.setEnabled(True)  
        elif self.totalPage > self.currentPage:
            self.ui.nextButton.setEnabled(True)
            self.ui.lastButton.setEnabled(False) 
        elif self.currentPage > 1:    
            self.ui.nextButton.setEnabled(False) 
            self.ui.lastButton.setEnabled(True) 
        else:
            self.ui.nextButton.setEnabled(False)
            self.ui.lastButton.setEnabled(False)
        
        
    def display_img(self,position):
        # self.img = cv2.imread(self.img_path) #https://blog.csdn.net/weixin_44941350/article/details/125217307
        self.img = cv2.imdecode(np.fromfile(self.img_path,dtype=np.uint8),-1)
        height, width, channel = self.img.shape
        bytesPerline = 3 * width
        
        #https://blog.csdn.net/qq_40089560/article/details/131942477?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-0-131942477-blog-53925720.235^v38^pc_relevant_anti_vip&spm=1001.2101.3001.4242.1&utm_relevant_index=3
        #https://forum.qt.io/topic/127392/qimage-to-qpixmap-where-should-i-add-scale-if-i-want-to-set-to-qlable
        self.qimg = QImage(self.img, width, height, bytesPerline, QImage.Format_RGB888).rgbSwapped().scaled(300, 300, QtCore.Qt.KeepAspectRatio)
        
        if position % 6 == 1:
            self.ui.result_1.setPixmap(QPixmap.fromImage(self.qimg))
            self.ui.result_1.adjustSize()
        elif position % 6 == 2:
            self.ui.result_2.setPixmap(QPixmap.fromImage(self.qimg))
            self.ui.result_2.adjustSize()
        elif position % 6 == 3:
            self.ui.result_3.setPixmap(QPixmap.fromImage(self.qimg))
            self.ui.result_3.adjustSize()
        elif position % 6 == 4:
            self.ui.result_4.setPixmap(QPixmap.fromImage(self.qimg))
            self.ui.result_4.adjustSize()
        elif position % 6 == 5:
            self.ui.result_5.setPixmap(QPixmap.fromImage(self.qimg))
            self.ui.result_5.adjustSize()
        elif position % 6 == 0:
            self.ui.result_6.setPixmap(QPixmap.fromImage(self.qimg))
            self.ui.result_6.adjustSize()
         
    def display_noImg(self):
        self.ui.downloadMsg.setText("沒有imgur圖片可以挖了QQ")
        
    def pttBeauty_imgurDowlnload(self,keyword,picsNum):   
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
                                    picNameList.append(pic+".png")
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
        
    # name = input("請輸入想搜尋的人名:")
    # count = eval(input("請輸入想搜尋的張數:"))
        
 

# if __name__ == '__main__':
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     sys.exit(app.exec_())