import requests
from bs4 import BeautifulSoup
import pandas as pd

class Flipkart:
    result=[]
    def __init__(self):
        for i in range(1,11):
            self.loadURL(i) #pages will be load
        self.save()    

    def loadURL(self,i):
        url=f"https://www.flipkart.com/search?q=t+shirts&as=on&as-show=on&otracker=AS_Query_HistoryAutoSuggest_0_0&otracker1=AS_Query_HistoryAutoSuggest_0_0&as-pos=0&as-type=HISTORY&page%7Bi%7D{i}"
        try:
            self.page=requests.get(url) #url pass karege vo load karrege self.page me
            if self.page.status_code==200: #page if success aagaye tho success else error 200 code 
                print("Success")
            else:
                print("error",self.page.status_code)
        except Exception as e:
            print(e)

        self.makeobject()    

    def makeobject(self):
        soup=BeautifulSoup(self.page.text,'lxml') #parsing jo page text file  page aagya on which we have to work
        section=soup.find_all('div',attrs={"class":"_1HmYoV _35HD7C"}) #div ka sirf attrs liya hai
        self.newsection=section[1] # above class 2 hai ek index 0 and indexing 1 so index 1 is for usefull thus we use this
        self.scraping()


    def scraping(self):    
        self.area=self.newsection.find_all('div',attrs={"class":"bhgxx2 col-12-12"})
        self.storeresult()

    def storeresult(self):
        for eachrow in self.area:
            for pieces in eachrow.find_all('div',attrs={"class":"_2LFGJH"}):
                name=pieces.a.text
                discountprice=pieces.find('div',attrs={"class":"_1vC4OE"}).text
                originalprice=pieces.find('div',attrs={"class":"_3auQ3N"}).text
                discount=pieces.find('div',attrs={"class":"VGWI6T"}).text
                Flipkart.result.append({"name   ":name,"dis_price   ":discountprice,"ori_price   ":originalprice,"discount   ":discount})# result list me append kar deiya hai


    def save(self):
        dataset=pd.DataFrame(Flipkart.result) #result ka data frames 
        dataset=dataset[['name   ','ori_price   ','discount   ','dis_price   ']] #us file me jo columns ka name hoyega
        dataset.to_csv("Flipkartdata.csv") #creating csv file
        #for 2nd pages there is no change 

if __name__ == "__main__":#inbuild variables python ???????
    user=Flipkart() 