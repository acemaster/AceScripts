from __future__ import print_function
import sys
import requests
from BeautifulSoup import BeautifulSoup
import urllib2
import re
import os

def download_file(url,basefolder):
	try:
	    local_filename = url.split('/')[-1]
	    # NOTE the stream=True parameter
	    r = requests.get(url, stream=True)
	    count = 0
	    with open(basefolder+"/"+local_filename, 'wb') as f:
	        for chunk in r.iter_content(chunk_size=1024): 
	            if chunk: # filter out keep-alive new chunks
	                f.write(chunk)
	                count = count +1
	                if count%100 == 0:
	                	print('=', end="")
	                #f.flush() commented by recommendation from J.F.Sebastian
	    print("==",end="\n")
	    print("Download of file "+ local_filename+ " complete",end="\n")
	    return local_filename
	except:
		return "Could not download_file"



# download_file(sys.argv[1])
def createdirectory(url):
	if not os.path.exists(url):
		os.makedirs(url)

def getpage(url,directory):
	html_page = urllib2.urlopen(url)
	soup = BeautifulSoup(html_page)
	# print(soup)
	createdirectory(directory)
	for link in soup.findAll('a'):
	    print("Downloading "+url+link.get('href'),end="\n")
	    url_to_download = url+link.get('href')
	    local = download_file(url_to_download,directory)
	    print(local)


getpage(sys.argv[1],sys.argv[2])