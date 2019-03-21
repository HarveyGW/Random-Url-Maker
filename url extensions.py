#Made by HarveyGW
import random; import string; from colorama import Fore; import urllib.request

def randomString(stringLength=int(input("Enter the length of the string: "))):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(stringLength))
for i in range(1, int(input("Enter the amount of times to loop: "))):
    print(Fore.LIGHTYELLOW_EX + "Random String is"+" {", randomString()+" }")
    webUrl = input("Enter the URL (template says https://[URL NAME]/ ")
    url = ("https://"+webUrl+"/")
    print(url)
    print(urllib.request.urlopen(url))
