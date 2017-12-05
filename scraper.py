# coding: utf-8
import bs4
from pandas import DataFrame
import urllib.request # get webpage
import csv
import numpy as np
import pandas as pd
for i in range(1, 30): #Number of pages plus
    if(i==1):
        url = "http://police.psu.edu/daily-crime-log"
    else:
        url = "http://police.psu.edu/daily-crime-log?field_reported_value[value]=&page="+str(i)

    # print url
    # print "#####################"
    allCrimes = pd.DataFrame(columns = ['Incident#', 'Occurred', 'reported', 'nature of incident', 'offenses', 'location', 'disposition'])

    source = urllib.request.urlopen(url).read()
    bs_tree = bs4.BeautifulSoup(source, "lxml")

    # print bs_tree
    # print "#####################"

    incident_nums = bs_tree.findAll('div',attrs={"class" : "views-field views-field-title"})

    occurred = bs_tree.findAll('div',attrs={"class" : "views-field views-field-field-occurred"})

    # print occurred
    # print "#####################"
    reported = bs_tree.findAll('div',attrs={"class" : "views-field views-field-field-reported"})

    # print reported
    # print "#####################"

    incidents = bs_tree.findAll('div',attrs={"class" : "views-field views-field-field-nature-of-incident"})

    # print incidents
    # print "#####################"

    offenses = bs_tree.findAll('div',attrs={"class" : "views-field views-field-field-offenses"})

    # print offenses
    # print "#####################"

    locations = bs_tree.findAll('div',attrs={"class" : "views-field views-field-field-location"})

    # print locations
    # print "#####################"

    dispositions = bs_tree.findAll('div',attrs={"class" : "views-field views-field-field-case-disposition"})

    # print dispositions
    # print "#####################"

    total = len(incident_nums)

    # print total
    # print "#####################"

    count = 0

    while (count<total):
        incNum = incident_nums[count].find('span',attrs={"class" : "field-content"}).get_text()
        occr = occurred[count].find('span',attrs={"class" : "field-content"}).get_text()
        repo = reported[count].find('span',attrs={"class" : "field-content"}).get_text()
        incNat = incidents[count].find('span',attrs={"class" : "field-content"}).get_text()
        offe = offenses[count].find('span',attrs={"class" : "field-content"}).get_text()
        loca = locations[count].find('span',attrs={"class" : "field-content"}).get_text()
        disp = dispositions[count].find('span',attrs={"class" : "field-content"}).get_text()
        allCrimes.loc[count] =[incNum, occr, repo, incNat, offe, loca, disp]
        with open('New_Crime_Log', 'a') as f:
            allCrimes.to_csv(f, header=True)
        count +=1
