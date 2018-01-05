from  bs4 import BeautifulSoup
from Urls import Url
from Keywords import keywords

class Scrap:
    def __init__(self,response,currentHost):
        self.response=response
        if currentHost.endswith("/"):
            self.currentHost=currentHost[:-1]
        else:
            self.currentHost=currentHost
        self.soup=BeautifulSoup(response)
        
        self.CheckForUrl()
        self.CheckData()

    def CheckForUrl(self):
        links=self.soup.find_all("a")
        for link in links:
            try:
                Url_link=str(link.get("href"))
                if Url_link.startswith("http://") or Url_link.startswith("https://"):
                    Url().SetUrlToVisit(Url_link)
                elif Url_link.startswith("www"):
                    Url().SetUrlToVisit("http://"+Url_link)
                elif Url_link.startswith("/"):
                    #Url().SetUrlToVisit(self.currentHost+Url_link)      
                    pass
            except:
                pass
   
    def CheckData(self):
        all_tags=self.soup.body.find_all_next()
        #print(all_tags)
        count=0
        for  tag in all_tags:
                    # print("\n\n\n\n"+str(tag))
                    try:

                        dict_tags=BeautifulSoup("""<p>{}</p>""".format(str(tag))).div.attrs
                        if keywords().isPriceKeyword(dict_tags):                    
                            #print(BeautifulSoup(str(tag)).div.find_all_next())
                                # if len(BeautifulSoup(str(tag)).div.find_all_next())>2:                        
                                c=count
                                while c>0:
                                    soup2=BeautifulSoup("""<p><div>{}</div></p>""".format(str(all_tags[c])))                                    
                                    all_tags2=soup2.div.find_all_next()
                                    print("")
                                    if self.CheckPrice(all_tags2) and self.CheckProduct(all_tags2):
                                        print(all_tags2.string)
                                        break
                                    
                                    c=c-1

                    except:
                        pass
                    try:
                        dict_tags=BeautifulSoup("""<p>{}</p>""".format(str(tag))).span.attrs
                        if keywords().isPriceKeyword(dict_tags):
                                # if len(BeautifulSoup(str(tag)).div.find_all_next())>2:
                                c=count
                                while c>0:
                                    soup2=BeautifulSoup("""<p>{}</p>""".format(str(all_tags[c])))
                                    all_tags2=soup2.p.find_all_next()
                                    print("\n\n\n"+str(all_tags2))
                                    if self.CheckPrice(all_tags2) and self.CheckProduct(all_tags2):
                                        print(all_tags2.string)
                                        break
                                    
                                    c=c-1
                    except:
                        pass
                    try:
                        dict_tags=BeautifulSoup("""<p>{}</p>""".format(str(tag))).dt.attrs
                        if keywords().isPriceKeyword(dict_tags):
                                # if len(BeautifulSoup(str(tag)).div.find_all_next())>2:
                                c=count
                                while c>0:
                                    soup2=BeautifulSoup("""<p><div>{}</div></p>""".format(str(all_tags[c])))
                                    all_tags2=soup2.dt.find_all_next()
                                    if self.CheckPrice(all_tags2) and self.CheckProduct(all_tags2):
                                        print(all_tags2.string)
                                        break
                                   
                                    c=c-1
                    except:
                        pass
                    try:
                        dict_tags=BeautifulSoup("""<p>{}</p>""".format(str(tag))).dd.attrs
                        if keywords().isPriceKeyword(dict_tags):
                                # if len(BeautifulSoup(str(tag)).div.find_all_next())>2:
                                c=count
                                while c>0:
                                    soup2=BeautifulSoup("""<p><div>{}</div></p>""".format(str(all_tags[c])))
                                    all_tags2=soup2.dd.find_all_next()
                                    if self.CheckPrice(all_tags2) and self.CheckProduct(all_tags2):
                                        print(all_tags2.string)
                                        break
                                    
                                    c=c-1
                    except:
                        pass
                    count=count+1

                
        




    def CheckProduct(self,all_tags2):
        for  tag in all_tags2:
            try:
                dict_tags=BeautifulSoup("""<p>{}</p>""".format(str(tag))).div.attrs
                if keywords().isProductKeyword(dict_tags):
                    return True
                    
            except:
                pass
            try:
                dict_tags=BeautifulSoup("""<p>{}</p>""".format(str(tag))).span.attrs
                if keywords().isProductKeyword(dict_tags):
                    return True
            except:
                pass
            try:
                dict_tags=BeautifulSoup("""<p>{}</p>""".format(str(tag))).dt.attrs
                if keywords().isProductKeyword(dict_tags):
                    return True
            except:
                pass
            try:
                dict_tags=BeautifulSoup("""<p>{}</p>""".format(str(tag))).dd.attrs
                if keywords().isProductKeyword(dict_tags):
                    return True
            except:
                pass
        return False
    def CheckPrice(self,all_tags2):
        for  tag in all_tags2:
            try:
                dict_tags=BeautifulSoup("""<p>{}</p>""".format(str(tag))).div.attrs
                if keywords().isPriceKeyword(dict_tags):
                    return True
                    
            except:
                pass
            try:
                dict_tags=BeautifulSoup("""<p>{}</p>""".format(str(tag))).span.attrs
                if keywords().isPriceKeyword(dict_tags):
                    return True
            except:
                pass
            try:
                dict_tags=BeautifulSoup("""<p>{}</p>""".format(str(tag))).dt.attrs
                if keywords().isPriceKeyword(dict_tags):
                    return True
            except:
                pass
            try:
                dict_tags=BeautifulSoup("""<p>{}</p>""".format(str(tag))).dd.attrs
                if keywords().isPriceKeyword(dict_tags):
                    return True
            except:
                pass
        return False
            
            
        




