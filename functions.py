from urllib.parse import urlparse
import random
import string

def is_url(url):
  try:
    result = urlparse(url)
    return url
  except ValueError:
    if is_url("http://"+url) == False :
        if is_url("https://"+url) == False :
            return False
        else :
            return "http://"+url
    else : 
        return "http://"+url

def idMaker () :
            id = ""
            for i in range(4) : 
                rando = random.randint(0,2)
                if rando == 0 : 
                    id +=  random.choice(string.ascii_letters)
                elif (rando == 1) :
                    id += str(random.randint(0,9))
                else :
                    id +=  random.choice(string.ascii_uppercase) 
                    
            return id