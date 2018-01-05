

class Url:
    #self.visitedUrls=set()
    #self.UrlsVisit=[]
    def __init__(self):
        self.visitedUrls=set()
        self.UrlsVisit=[]
        self.readUrlVisited()
        self.readToVisited()
    def readUrlVisited(self):
        try:
            with open("VisitedUrls.txt","r") as f:
                self.visitedUrls=set(f.read().split("!::!"))
            f.close()
        except:
            pass
        return
    def readToVisited(self):
        try:
            with open("UrlsToVisit.txt","r") as f:
                self.UrlsVisit=f.read().split("!::!")
            f.close()
        except:
            pass
        return
    def isUrlVisited(self,url):
        return url in self.visitedUrls
    def setUrlVisited(self,url):
        if not self.isUrlVisited(url):
            with open("VisitedUrls.txt","a") as f:
                f.write("{}!::!".format(url))
            f.close()
            self.readUrlVisited()
        return
    def UrlToVisit(self):
        url=""
        url=self.UrlsVisit[0]
        self.UrlsVisit.remove(url)
        self.UpdateToUrlsToVisitFile()       
        return url
    def UpdateToUrlsToVisitFile(self):
        string=""
        for url in self.UrlsVisit:
            substr=url+"!::!"
            string=string+substr
        with open("UrlsToVisit.txt","w") as f:
            f.write(string)
        f.close()
        return
    def SetUrlToVisit(self,url):
        if not self.isUrlVisited(url):
            self.UrlsVisit.append(url)
            with open("UrlsToVisit.txt","a") as f:
                f.write("{}!::!".format(url))
            f.close()
        return




