
from bs4 import BeautifulSoup
import urllib, urllib3
import time
import sys
import os
import json

conn = urllib3.connection_from_url('https://en.wikipedia.org/wiki/')

def taw(term):
    term = term.replace(' ', '_')
    # fetch the data page of the term from wikipedia
    #http = urllib3.PoolManager()
    r = conn.request('GET', 'https://en.wikipedia.org/wiki/'+term)
    if r.status == 200:
        soup = BeautifulSoup(r.data, 'html.parser')
        # url to the arabic page
        try:
            url = soup.find_all('a', lang='ar')[0]
            ar_term = urllib.unquote(str(url['href'].replace('//ar.wikipedia.org/wiki/', ''))).decode('utf-8')
            ar_term = ar_term.replace('_', ' ')
        except IndexError:
            ar_term = "arabic translation not found"
        return ar_term
    return False


def taw_json(file_name):
    with open(os.getcwd() + '/' +file_name) as to_taw:
        to_taw = json.load(to_taw)
    to_taw[:] = [taw(term) for term in to_taw.itervalues()]
    with open('ar_'+file_name, 'w') as outfile:
        json.dump(to_taw, outfile)
    # for term in to_taw.itervalues():
    #     print("started in %s " %time.time())
    #     print(taw(term))


if __name__ == '__main__':
    taw_json(sys.argv[1])
    # s_time = time.time()
    # print(taw("Kenya"))
    # print("found in %s" %(time.time()-s_time))
    # s_time = time.time()
    # print(taw("British Indian Ocean Territory"))
    # print("found in %s" %(time.time()-s_time))
