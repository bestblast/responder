# -*- coding: utf-8 -*-
import shutil
from bs4 import BeautifulSoup
from random import choice
import requests
import re
import urllib2
import os
import cookielib
import json,random


def get_soup(url,header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

def get_url_from_query(query):
    # query = raw_input("query image")# you can change the query for the image  here
    # query = "house"
    image_type="ActiOn"
    query= query.split()
    query='+'.join(query)
    url="https://www.google.co.in/search?q="+query+"&source=lnms&tbm=isch&tbs=isz:m"
    print url
    #add the directory for your image here
    DIR="Pictures_g_search"
    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"
            }
    soup = get_soup(url,header)


    ActualImages=[]# contains the link for Large original images, type of  image
    for a in soup.find_all("div",{"class":"rg_meta"}):
        link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
        ActualImages.append((link,Type))

    print  "there are total" , len(ActualImages),"images"

    #if not os.path.exists(DIR):
    #    os.mkdir(DIR)
    #DIR = os.path.join(DIR, query.split()[0])

    #if not os.path.exists(DIR):
    #    os.mkdir(DIR)
##############
    img_links=[]
###print images
    for i , (img , Type) in enumerate( ActualImages):
        img_links.append(img)
        i=i+1

    return random.choice(img_links)

##############
'''

    ###print images
    list_img = []
    for i , (img , Type) in enumerate( ActualImages):
        try:
            req = urllib2.Request(img, headers={'User-Agent' : header})
            raw_img = urllib2.urlopen(req).read()
     #       print img
            list_img.append(str(img))
            #	print req
            #	print list_img
            #print raw_img
            cntr = len([i for i in os.listdir(DIR) if image_type in i]) + 1
            print cntr
            if cntr == 10:
                break
            if len(Type)==0:
                f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+".jpg"), 'wb')
            else :
                f = open(os.path.join(DIR , image_type + "_"+ str(cntr)+"."+Type), 'wb')


            f.write(raw_img)
            f.close()
        except Exception as e:
            print "could not load : "+img
            print e
            list_img.pop()
    shutil.rmtree(DIR)
    #print list_img
    return choice(list_img)

'''



