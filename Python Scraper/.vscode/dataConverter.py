import csv
import re
from geopy.geocoders import Nominatim



def convertData(dataFiles):
    states = {
		"AL" : "Alabama",
		"AL" : "Alaska",
		"AZ" : "Arizona",
		"AR" : "Arkansas",
		"CA" : "California",
		"CO" : "Colorado",
        "CT" : "Connecticut",
		"DE" : "Delaware",
		"FL" : "Florida",
		"GA" : "Georgia",
		"HI" : "Hawaii",
		"ID" : "Idaho",
        "IL" : "Illinois",
		"IN" : "Indiana",
		"IA" : "Iowa",
		"KS" : "Kansas",
		"KY" : "Kentucky",
		"LA" : "Louisiana",
        "ME" : "Maine",
		"MD" : "Maryland",
		"MA" : "Massachusetts",
		"MI" : "Michigan",
		"MN" : "Minnesota",
		"MS" : "Mississippi",
        "MO" : "Missouri",
		"MT" : "Montana",
		"NE" : "Nebraska",
		"NV" : "Nevada",
		"NH" : "New Hampshire",
		"NJ" : "New Jersey",
        "NM" : "New Mexico",
		"NY" : "New York",
		"NC" : "North Carolina",
		"ND" : "North Dakota",
		"OH" : "Ohio",
		"OK" : "Oklahoma",
        "OR" : "Oregon",
		"PA" : "Pennsylvania",
		"RI" : "Rhode Island",
		"SC" : "South Carolina",
		"SD" : "South Dakota",
		"TN" : "Tennessee",
        "TX" : "Texas",
		"UT" : "Utah",
		"VT" : "Vermont",
		"VA" : "Virginia",
		"WA" : "Washington",
		"WV" : "West Virginia",
        "WI" : "Wisconsin",
        "WY" : "Wyoming"
	}
    with open('jobData.csv', 'w', newline='') as file:
        data = []
        data.append(["Title", "Company", "City","State", "lowPay", "hightPay","Equity" ,"latitude", "longitude" ,"Posted", "Link", "Timestamp"])
        for files in dataFiles:
            with open(files) as csvfile:
                cnt = 0
                readCSV = csv.reader(csvfile, delimiter=',')

                for row in readCSV:
                    if "Title" in row[0] and "Company" in row[1]:
                        continue
                    else:
                        Title = ""
                        Company = ""
                        City = ""
                        State = ""
                        lowPay = -1
                        highPay = -1
                        Equity = False
                        Latitude = -1
                        Longitude = -1
                        Posted = ""
                        Link = ""
                        Timestamp = ""
                        Title = row[0]
                        Company = row[1]
                        Posted = row[4]
                        Link = row[5]
                        Timestamp = row[6]
                        try:
                            temp = row[2]
                            temp = temp.split(',')
                            City = temp[0]
                            temp = temp[1].split(' ')
                            State = temp[1]
                            State = states.get(State)
                        except:
                            City = ""
                            State = ""
                            pass

                        if row[3] == "" or row[3] == " ":
                            pass
                        elif "Equity" in row[3]:
                            Equity = True
                        else:
                            temp = row[3].split('-')
                            temp2 = temp[0]
                            lowPay = temp2[temp2.find("$")+1:temp2.find("K")]
                            
                            try:
                                lowPay = int(lowPay) * 1000
                            except:
                                lowPay = temp2[temp2.find("$")+1:temp2.find("k")]
                                lowPay = int(lowPay) * 1000
                                pass

                            temp2 = temp[1]
                            highPay = temp2[temp2.find(" ")+1:temp2.find("k")]
                            try:
                                highPay = int(highPay) * 1000
                            except:
                                highPay = temp2[temp2.find("$")+1:temp2.find("K")]
                                highPay = int(highPay) * 1000
                                pass
                        try:
                            geolocator = Nominatim(user_agent= "dataConverter")
                            location = geolocator.geocode(City + "," + State)
                            if location:
                                Latitude =location.latitude
                                Longitude =location.longitude
                            else:
                                Latitude = None
                                Longitude = None
                                
                        except:
                            print("ERRORS WITH GEO CODE")
                            pass
                        data.append([Title,Company,City,State,lowPay,highPay,Equity,Latitude,Longitude,Posted,Link,Timestamp])
                        Equity = False
                        cnt += 1
                        if cnt == 50:
                            break
            csvfile.close()
        for row in data:

            try:
                writer = csv.writer(file)
                writer.writerow(row)
            except:
                pass
    file.close()
                

                        
stack = "StackoverflowData.csv"
indeed ="IndeedData.csv"
glass = "GlassdoorData.csv"

files = []
files.append(stack)
files.append(indeed)
files.append(glass)
convertData(files)
