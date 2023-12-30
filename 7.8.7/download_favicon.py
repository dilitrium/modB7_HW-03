from sys import argv
import wget

script, site = argv

def favicon_download(script, site):
    URL = 'https://'+site+'/favicon.ico' 
    site_ico = site.split('.')[0]+".ico"
    response = wget.download(URL, site_ico)
    
print(favicon_download(script, site))
