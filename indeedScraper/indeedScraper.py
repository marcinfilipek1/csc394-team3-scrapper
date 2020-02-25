import requests
import bs4
from bs4 import BeautifulSoup
import time
from datetime import datetime
import re
from xlwt import Workbook
wb = Workbook()
jobData = wb.add_sheet('jobData')


jobs = []
def jobTitle():
    jobLinks = open("jobs.txt","r")
    cnt = 0

    while True:
        try:
            link = jobLinks.readline()
            link = link.strip('\n')
            if link == '':
                break
            else:
                URL = link
                page = requests.get(URL)
                soup = BeautifulSoup(page.text,"html.parser")
                
                '''Job name'''
                result = soup.find_all("h3",{"class":"icl-u-xs-mb--xs icl-u-xs-mt--none jobsearch-JobInfoHeader-title"})
                for res in result:
                    jobs.append(res.text)
                    jobData.write(cnt, 0,res.text)
                    print("Job Added")

                '''company name'''
                company = soup.find_all("div",{"class":"icl-u-lg-mr--sm icl-u-xs-mr--xs"})
                for comp in company:
                    x = comp.text
                    if x != "-":
                        jobs.append(comp.text)
                        jobData.write(cnt, 1, comp.text)
                        print("Company Added")
        
                '''Location of job'''    
                location = soup.find_all("div",{"class":"icl-u-xs-mt--xs icl-u-textColor--secondary jobsearch-JobInfoHeader-subtitle jobsearch-DesktopStickyContainer-subtitle"})
                for loc in location:
                    x = re.sub('^.*?-', '', loc.text)
                    jobs.append(x)
                    jobData.write(cnt, 2, x)
                    print("Location Added")

                '''Time job has been up'''
                timePosted = soup.find_all("div",{"class":"jobsearch-JobMetadataFooter"})
                for stamp in timePosted:
                    try:
                        x = stamp.text
                        res = [int(i) for i in x.split() if i.isdigit()]
                        Pop = res.pop(0)
                        jobs.append(str(Pop)+" days ago")
                        jobData.write(cnt, 3, str(Pop)+" days ago")
                        print("Posted Time")
                    except:
                        jobs.append("30+ days ago")
                        jobData.write(cnt,3,"30+ days ago")
                        print("Posted Time")
                        continue
                '''Job Posting URL'''
                jobs.append(URL)
                jobData.write(cnt, 4, URL)
                print("URL Added")
                
                '''Time Scraped'''
                date = datetime.now()
                date = date.strftime("%m %d %Y  %H:%M:%S")
                jobs.append(date)
                jobData.write(cnt, 5, date)
                print("Time scraped Added")

                cnt += 1    
        except:
            jobs.clear()
            print("Failed to add")
            pass
            
jobTitle()
wb.save('jobData.xls')

