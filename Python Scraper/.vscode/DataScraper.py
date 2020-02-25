import requests
import bs4
import time
import csv
import re
from bs4 import BeautifulSoup
from datetime import datetime
from multiprocessing import Process

def getStackoverflowJobs():
    jobLinks = open("StackoverflowJobLinks.txt","r")
    cnt = 0
    data = []
    data.append(["Title", "Company", "Location", "Pay", "Posted", "Link", "Timestamp"])
    Title = ""
    Company = ""
    Location = ""
    Pay = ""
    Posted = ""
    Link = ""
    Timestamp = ""

    while True:
        try:
            link = jobLinks.readline()
            link = link.strip('\n')
            if link == '':
                break
            else:
                time.sleep(1.25)
                URL = link
                page = requests.get(URL)
                soup = BeautifulSoup(page.text,"lxml")

                for title in soup.find_all("h1",{"class":"fs-headline1 mb4"}):
                    Title = title.text.strip()
                    
                    
                for company in soup.find_all("div", {"class":"fc-black-700 fs-body3"}):
                    try:
                        a_tag = company.find("a", {"class": "fc-black-700"})
                        Company = a_tag.text
                    except:
                        a_tag = company.find("a", {"class": "fc-black-800 employer _up-and-out"})
                        Company = a_tag.text
                        pass
                    
                
                for location in soup.find_all("div", {"class":"fc-black-700 fs-body3"}):
                    span_tag = location.find("span", {"class": "fc-black-500"})
                    Location = span_tag.text[27:].strip()
                   
                for salary in soup.find_all("div", {"class": "main-columns"}):
                    try:
                        div_tag = salary.find("div", {"class": "mt12"})
                        span_tag = div_tag.find("span", {"class": "-salary pr16"})
                        Pay = span_tag.text.strip()
                        
                    except:
                        Pay = ("")
                        continue

                for posted in soup.find_all("div", {"class": "grid mb24 fs-body1 fc-black-500 gs8 ai-baseline"}):
                    div_tag = posted.find("div", {"class": "grid--cell"})
                    Posted = div_tag.text
                      
                
                date = datetime.now()
                Timestamp = date.strftime("%m %d %Y  %H:%M:%S")
                Link = URL
                data.append([Title,Company,Location,Pay,Posted,Link,Timestamp])
                cnt += 1
        except:
            print(link)
            pass
    jobLinks.close()
    with open('StackoverflowData.csv', 'w', newline='') as file:
        for row in data:
            try:
                writer = csv.writer(file)
                writer.writerow(row)
            except:
                print(link)
                pass
    file.close()
    exit()
    


def getGlassdoorJobs():
    jobLinks = open("GlassdoorJobLinks.txt","r")
    cnt = 0
    data = []
    data.append(["Title", "Company", "Location", "Pay", "Posted", "Link", "Timestamp"])
    Title = ""
    Company = ""
    Location = ""
    Pay = ""
    Posted = ""
    Link = ""
    Timestamp = ""

    while True:
        try:
            link = jobLinks.readline()
            link = link.strip('\n')
            if link == '':
                break
            else:
                URL = link
                page = requests.get(URL, headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"})
                soup = BeautifulSoup(page.text,"lxml")

                for title in soup.find_all("h2",{"class":"mt-0 margBotXs strong"}):
                    Title = title.text.strip()
                    
                    
                for company in soup.find_all("div", {"css-khulwh e11nt52q0"}):
                    span_tag = company.find("span", {"class": "strong ib"})
                    Company = span_tag.text.strip()
                    
                
                for location in soup.find_all("div", {"class":"css-khulwh e11nt52q0"}):
                    span_tag = location.find("span", {"class": "subtle ib"})
                    Location = span_tag.text[3:].strip()
                   
                for salary in soup.find_all("div", {"class": "css-khulwh e11nt52q0"}):
                    try:
                        div_tag = salary.find("div", {"class": "css-b7ysi2 e11nt52q1"})
                        span_tag = div_tag.find("span", {"class": "small css-16r13ie e1v3ed7e1"})
                        Pay = span_tag.text.split(' ')[0].strip()
                        if "Hour" in Pay or ".css" in Pay:
                            Pay = ""
                        
                        
                    except:
                        Pay = ("")
                        continue

                    Posted = ""
                      
                
                date = datetime.now()
                Timestamp = date.strftime("%m %d %Y  %H:%M:%S")
                Link = URL
                data.append([Title,Company,Location,Pay,Posted,Link,Timestamp])
                cnt += 1
        except:
            print(link)
            pass
    jobLinks.close()
    with open('GlassdoorData.csv', 'w', newline='') as file:
        for row in data:
            try:
                writer = csv.writer(file)
                writer.writerow(row)
            except:
                print(link)
                pass
    file.close()
    exit()

def getIndeedJobs():
    jobLinks = open("IndeedJobLinks.txt","r")
    cnt = 0
    data = []
    data.append(["Title", "Company", "Location", "Pay", "Posted", "Link", "Timestamp"])
    Title = ""
    Company = ""
    Location = ""
    Pay = ""
    Posted = ""
    Link = ""
    Timestamp = ""

    while True:
        try:
            link = jobLinks.readline()
            link = link.strip('\n')
            if link == '':
                break
            else:
                URL = link
                page = requests.get(URL)
                soup = BeautifulSoup(page.text,"lxml")

                for title in soup.find_all("h3",{"class":"icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title"}):
                    Title = title.text.strip()
                    
                    
                for company in soup.find_all("div",{"class":"icl-u-lg-mr--sm icl-u-xs-mr--xs"}):
                    company.text
                    if company.text != "-":
                        Company = company.text
                   
                loc = soup.find_all("div",{"icl-u-xs-mt--xs icl-u-textColor--secondary jobsearch-JobInfoHeader-subtitle jobsearch-DesktopStickyContainer-subtitle"})
                for location in loc:
                    x = re.sub('^.*?-', '', location.text)
                    Location = x
                   
                for stamp in soup.find_all("div",{"class":"jobsearch-JobMetadataFooter"}):
                    try:
                        x = stamp.text
                        res = [int(i) for i in x.split() if i.isdigit()]
                        Pop = res.pop(0)
                        Posted = str(Pop)+" days ago"
                    except:
                        Posted = "30+ days ago"
                        continue

                Pay = ""
                date = datetime.now()
                Timestamp = date.strftime("%m %d %Y  %H:%M:%S")
                Link = URL
                data.append([Title,Company,Location,Pay,Posted,Link,Timestamp])
                cnt += 1
        except:
            print(link)
            pass
    jobLinks.close()
    with open('IndeedData.csv', 'w', newline='') as file:
        for row in data:
            try:
                writer = csv.writer(file)
                writer.writerow(row)
            except:
                print(link)
                pass
    file.close()
    exit()

if __name__ == '__main__':
     #p1 = Process(target = getStackoverflowJobs)
     #p1.start()
     #p2 = Process(target = getGlassdoorJobs)
     #p2.start()
     #p3 = Process(target = getIndeedJobs)
     #p3.start()
     #p1.join()
     #p2.join()
     #p3.join()
     getGlassdoorJobs()
     exit()