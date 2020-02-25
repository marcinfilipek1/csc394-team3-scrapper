import requests
import bs4
from bs4 import BeautifulSoup
import time
jobs = []

def jobTitle():
    cnt = 0
    jobLinks = open("jobs.txt","r")

    while True:
        try:
            link = jobLinks.readline()
            if link == '' or cnt == 5:
                break
            else:
                URL = link
                page = requests.get(URL)
                soup = BeautifulSoup(page.text,"html.parser")
                result = soup.find_all("h3",{"class":"icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title"})
                for res in result:
                    jobs.append(res.text)
                    cnt += 1
                    print("Job Added")
        except:
            print("Failed to add")
            pass
jobTitle()

jobTitles = open("jobTitles.txt","w")
for names in jobs:
    jobTitles.write(str(names)+"\n")
jobTitles.close()

print(jobs)
