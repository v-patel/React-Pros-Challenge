from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
<<<<<<< HEAD
# enable browser logging
d = DesiredCapabilities.CHROME
d['loggingPrefs'] = { 'browser':'ALL' }
=======

d = DesiredCapabilities.CHROME
d['loggingPrefs'] = { 'browser': 'ALL' }



>>>>>>> d131876361e05e8aa85e362fffdb3794d0a9f80a
options = Options()
options.add_argument("--headless")
options.add_argument("--disable-gpu")
browser = webdriver.Chrome("C:\\Users\\vedan\\Desktop\\React-Pros-Challenge\\pros-challenge\\src\\chromedriver.exe", options=options)
<<<<<<< HEAD
site = webdriver.Chrome(desired_capabilities=d)
=======
site = webdriver.Chrome("C:\\Users\\vedan\\Desktop\\React-Pros-Challenge\\pros-challenge\\src\\chromedriver.exe", options=options) 
site = webdriver.Chrome(  desired_capabilities = d)
while not os.path.exists("data.txt"):
	time.sleep(1)
>>>>>>> d131876361e05e8aa85e362fffdb3794d0a9f80a

site.get("localhost:3000")

split = []
while len(split) == 0:
	entry = site.get_log('browser')
	if entry.text.index("IMPORTANT VARIABLE") != -1 and entry.text.index("20") != -1:
		split = entry.text.split(" ")

depart = split[2]
arrive = split[3]
depDateYMD = split[4]

browser.get("https://www.google.com/flights#flt="+depart+"."+arrive+"."+depDateYMD+";c:USD;e:1;sd:1;t:f;tt:o")
<<<<<<< HEAD
=======
site.get("localhost:3000")

for entry in site.get_log('browser'):
    if entry.text.index("IMPORTANT VARIABLE") != -1:
        if entry.text.index(20) != -1:
            print(entry)
>>>>>>> d131876361e05e8aa85e362fffdb3794d0a9f80a

browser.implicitly_wait(2)
nav = browser.find_element_by_class_name("gws-flights-results__best-flights")

#print(nav.text)

lines = nav.text.splitlines()
# with open('flights.csv', 'w', newline='') as csvfile:
# 	csvwriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
# 	csvwriter.writerow(['Time', 'Airline', 'Duration', 'Airports', 'Cost'])
# 	index = 3
# 	while index+7 < len(lines):
# 		csvwriter.writerow([lines[index], lines[index+1], lines[index+3], lines[index+4], lines[index+7]])
# 		index += 8
o=open("flights.txt", "w+")
o.write("Time\tAirline\tDuration\tAirports\tCost\n")


for array in lines:
	if "Operated" in array:
		del lines[lines.index(array)]

index = 3
while index+5 < len(lines):
	o.write(lines[index]+"---" +lines[index+1]+"---" +lines[index+2]+"---"+ lines[index+3]+"---"+ lines[index+5]+"\n")
	#print(lines[index]+"\t" +lines[index+1]+"\t" +lines[index+2]+"\t"+ lines[index+3]+"\t"+ lines[index+5]+"\n")
	index += 6

#print(lines)
o.close()
browser.quit()
