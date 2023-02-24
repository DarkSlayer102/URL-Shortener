


import pyshorteners
import webbrowser



def url_shortener(link:str):
    
    s = pyshorteners.Shortener()
    shortlink =  s.tinyurl.short(link)


    webbrowser.open_new(shortlink)
    return shortlink


if __name__ == '__main__':
        
   short_url =  url_shortener(input("Enter the url here:"))
   print(short_url)