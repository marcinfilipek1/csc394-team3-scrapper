import requests
from bs4 import BeautifulSoup
from multiprocessing import Process

#Indeed Link Scraper
def getIndeedJobs():
    pageCounter = 1
    urls = []
    urls.append("https://www.indeed.com/jobs?q=artificial+intelligence&l=United+States&start=")
    urls.append("https://www.indeed.com/jobs?q=Deep+Learning&l=United+States&start=")
    urls.append("https://www.indeed.com/jobs?q=Machine+Learning&l=United+States&start=")
    urls.append("https://www.indeed.com/jobs?q=cyber+security&l=United+States&start=")
    urls.append("https://www.indeed.com/jobs?q=software+developer&l=United+States&start=")

    myfile = open("IndeedJobLinks.txt", "w")
    for url in urls:
         result = requests.get(url)
         src = result.content
         soup = BeautifulSoup(src, 'lxml')

         for i in range(0,100):
             for div_tag in soup.find_all("div", {"class": "title"}):
                a_tag = div_tag.find('a')
                myfile.write("https://www.indeed.com/" + a_tag.attrs['href'] + "\n")
             pageCounter += 1
             result = requests.get(url + str(pageCounter * 10))
             src = result.content
             soup = BeautifulSoup(src, 'lxml')
    myfile.close()
    exit()


#------------------------------------------------------------------------------------------------------------------------------------------
#GlassDoor Link Scraper
def getGlassdoorJobs():
    pageCounter = 1
    urls = []
    urls.append("https://www.glassdoor.com/Job/us-artificial-intelligence-jobs-SRCH_IL.0,2_IN1_KE3,26_IP")
    urls.append("https://www.glassdoor.com/Job/us-deep-learning-jobs-SRCH_IL.0,2_IN1_KO3,16_IP")
    urls.append("https://www.glassdoor.com/Job/us-machine-learning-jobs-SRCH_IL.0,2_IN1_KO3,19_IP")
    urls.append("https://www.glassdoor.com/Job/us-cyber-security-jobs-SRCH_IL.0,2_IN1_KO3,17_IP")
    urls.append("https://www.glassdoor.com/Job/software-developer-jobs-SRCH_KO0,18_IP")

    myfile = open("GlassdoorJobLinks.txt", "w")
    for url in urls:
         result = requests.get(url + ".htm", headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"})
         src = result.content
         soup = BeautifulSoup(src, 'lxml')

         for i in range(1,30):
             for div_tag in soup.find_all("div", {"class": "jobContainer"}):
                a_tag = div_tag.find('a')
                myfile.write("https://www.glassdoor.com" + a_tag.attrs['href'] + "\n")
             pageCounter += 1
             result = requests.get(url + str(pageCounter) + ".htm", headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.81 Safari/537.36"})
             src = result.content
             soup = BeautifulSoup(src, 'lxml')
    myfile.close()
    exit()



#------------------------------------------------------------------------------------------------------------------------------------------
#Stack Overflow Link Scraper
def getStackoverflowJobs():
    pageCounter = 1
    urls = []
    urls.append("https://stackoverflow.com/jobs?q=artificial+intelligence&l=United+States&d=3000&u=Miles&sort=i&pg=")
    urls.append("https://stackoverflow.com/jobs?q=Deep+learning&l=United+States&d=3000&u=Miles&sort=i&pg=")
    urls.append("https://stackoverflow.com/jobs?q=machine+learning&l=United+States&d=20&u=Miles&sort=i&pg=")
    urls.append("https://stackoverflow.com/jobs?q=cyber+security&l=United+States&d=3000&u=Miles&sort=i&pg=")
    urls.append("https://stackoverflow.com/jobs?q=software+developer&l=United+States&d=3000&u=Miles&sort=i&pg=")

    myfile = open("StackoverflowJobLinks.txt", "w")
    for url in urls:
         result = requests.get(url)
         src = result.content
         soup = BeautifulSoup(src, 'lxml')
         pageNumber = 0
         for pageNumberFinder in soup.find_all("a", {"class": "s-pagination--item"}):
             if(pageNumberFinder.text != "\nnextchevron_right\n" and pageNumber < int(pageNumberFinder.text)):
                pageNumber = int(pageNumberFinder.text)


         for i in range(1, pageNumber):
             for div_tag in soup.find_all("h2", {"class": "mb4 fc-black-800 fs-body3"}):
                a_tag = div_tag.find('a')
                myfile.write("https://www.stackoverflow.com" + a_tag.attrs['href'] + "\n")
             pageCounter += 1
             result = requests.get(url + str(pageCounter))
             src = result.content
             soup = BeautifulSoup(src, 'lxml')
    myfile.close()
    exit()

if __name__ == '__main__':
     p1 = Process(target= getIndeedJobs)
     p1.start()
     p2 = Process(target= getStackoverflowJobs)
     p2.start()
     p3 = Process(target= getGlassdoorJobs)
     p3.start()
     p1.join()
     p2.join()
     p3.join()
     exit()
     