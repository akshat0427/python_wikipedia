# importing all the required modules
import os 
import requests
from bs4 import BeautifulSoup
import time 
 
# store starting time 
begin = time.time() 
 
# asking for folder name and the range 
folder_name = input("name?- ")
limit = int(input('range- '))

os.mkdir(folder_name) # making the specified folder


lnk = input("link- ")  # the link to be scraped

o= requests.get(lnk).text # scraping the link 

soup = BeautifulSoup(o, 'html.parser')

l = []

for i in soup.find_all("a"):
    try:
        

        if "https" not in (i['href']):
            s= f"https://en.wikipedia.org{i['href']}"
        
            l.append(s)
    except:
        
        pass
    
file_name = []

for i in range(0, len(l)):
    
    file_name.append(l[i].split('/')[-1])
    
file_names = []

for i in file_name:
    test_str = ''.join(letter for letter in i if letter.isalnum())
    file_names.append(test_str)
print("done")

data = []

for i in range(0, limit):
    o2 = requests.get(l[i]).text
    data.append(o2)



os.chdir(folder_name)
for i in range(0, limit):
    with open(f"{file_names[i]}.html",'w', encoding='utf-8') as f:
        f.write(data[i])



end = time.time() 


        
print("done !!!")

print(f"Total runtime of the program is {end - begin}")  # total time taken by the script to run 


        
    







