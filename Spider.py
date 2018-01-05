import requests
from Scrapper import Scrap
from Urls import Url
from Textprocessing import process
class spider:
    
    def __init__(self,urls=None,url=None):
            self.urls=urls
            self.url=url
            if self.urls!=None:
                for URL in self.urls:
                        Url().SetUrlToVisit(URL)
            elif self.url!=None:
                    Url().SetUrlToVisit(self.url)
            self.crawl()
    def crawl(self):               
                    #while True:
                    URL=Url().UrlToVisit()
                    #print(URL)
                
                    #try:
                        #response=requests.get(URL).text
                        #print(response)
                        #Url().setUrlVisited(URL)

                    Scrap(process().html,URL)
                    #except:
                    #    pass

