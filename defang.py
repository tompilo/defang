from asyncio import DatagramTransport
from asyncio.windows_events import NULL
from unittest import result

def defang(ip:str) -> str:
    result_ip = ''
    for a in ip:
        if a == ".":
            result_ip += "[.]"
        else:
            result_ip += a

    return result_ip

def url(url_user:str) -> str:
    result_url = ''

    x = url_user.replace("tt", "xx", 1)
    
    y = x.replace("://", "[://]")  
    
    for char in y:
        if char == ".":
            result_url += "[.]"
        else:
            result_url += char
    
    return result_url

begin = "yes"

while begin.lower() == "yes":
    choose = input("What do u want to defang ? [IP/URL]\n") 
    if choose.lower() == "ip":
        defang_ip = input("Input your IP:\n")
        print("Defanged IP:\n",defang(defang_ip))
        
    elif choose.lower() == "url":
        url_input = input("Input your URL:\n")
        print("Defanged URL:\n",url(url_input))
        
    else:
        print("U r not choose yet...")
    
    begin = input("Do u want to defang again? [yes/no]\n")

# again = input("Do u want to defang again ? [yes/no]")