
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
    return term


def taw_json(file_name):
    with open(os.getcwd() + '/' +file_name) as to_taw:
        to_taw = json.load(to_taw)
    taw_result = {}
    for key, term in to_taw.iteritems():
        ar_term = taw(term)
        taw_result[key] = ar_term.encode('utf-8')
        print(taw_result[key])
    with open('ar_'+file_name, 'w') as outfile:
        json.dump(taw_result, outfile)

if __name__ == '__main__':
    stime = time.time()
    taw_json(sys.argv[1])
    etime = time.time()
    ttime = etime - stime
    print("Started at %s" %stime)
    print("Ended at %s" %etime)
    print("Total is %s" %ttime)
    # s_time = time.time()
    # print(taw("Kenya"))
    # print("found in %s" %(time.time()-s_time))
    # s_time = time.time()
    # print(taw("British Indian Ocean Territory"))
    # print("found in %s" %(time.time()-s_time))
