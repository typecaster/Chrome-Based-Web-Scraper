"""# -*- coding: utf-8 -*-

@Info:      Selenium Based Web Crawler capable of capturing Recent Journals in PDF format given the keywords.
            The captured PDF is then ready for processing to scrape Required information from it.

@Dated:     17th Oct, 2019

@Authors:   Asif Nawaz

"""
import csv
from sys import argv
#import parameters
from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#script, keyword = argv
keyword = "Computer Vision"
path = str(r"D:\chromedriver_win32\chromedriver.exe")
driver = webdriver.Chrome(path)

################################################################################
#           ACM Scraping Section
################################################################################
driver.get("https://scholar.google.com/")
sleep(3)

search_query = driver.find_element_by_xpath('//*[@id="gs_hdr_tsi"]')
try:
    search_query.send_keys("site:dl.acm.org AND " + keyword)
    sleep(0.5)
    search_query.send_keys(Keys.RETURN)
    sleep(1)
except:
    print("NO  SUBJECT FOUND!")
    driver.quit()

search_results_page = Selector(text=driver.page_source)
links = search_results_page.xpath('//h3/a/@href').extract()
print(links)
sleep(1)

for link in links:
    if "https://dl.acm.org/" in link:
        driver.get(link)
        sleep(0.5)
        try:
            print("Hello sir, gotcha")
            response_page = Selector(text=driver.page_source)
            pdf_link = response_page.xpath('//*[@id="divmain"]/table/tbody/tr/td[1]/table[1]/tbody/tr/td[2]/a/@href').extract_first()
            pdf_link = 'https://dl.acm.org/'+pdf_link
            driver.get(pdf_link)
            sleep(0.5)
        except:
            print("PDF LINK NOT FOUND, VISITING NEXT PAGE.")
            sleep(0.5)
    else:
        print("No results in the given domain")
#print("Links Browsed: ")
#print(links)
################################################################################
""" One Domain: "https://dl.acm.org/" crawled and TOP 10 results captured."""
################################################################################
#               IEEE SCRAPING SECTION
################################################################################
driver.get("https://scholar.google.com/")
sleep(3)
search_query = driver.find_element_by_xpath('//*[@id="gs_hdr_tsi"]')
try:
    search_query.send_keys("site:ieee.org AND " + keyword)
    sleep(0.5)
    search_query.send_keys(Keys.RETURN)
    sleep(1)
except:
    print("NO  SUBJECT FOUND!")
    driver.quit()

search_results_page = Selector(text=driver.page_source)
links = search_results_page.xpath('//h3/a/@href').extract()
print(links)
sleep(1)
for link in links:
    if "https://ieeexplore.ieee.org/" in link:
        driver.get(link)
        sleep(0.5)
        try:
            print("Hello sir, gotcha")
            response_page = Selector(text=driver.page_source)
            pdf_link = response_page.xpath('//*[@id="LayoutWrapper"]/div/div/div/div[5]/div[2]/xpl-root/xpl-document-details/div/div[1]/div/div[2]/xpl-left-side-bar/div/div/ul/li[1]/a/@href').extract_first()
            pdf_link = 'https://ieeexplore.ieee.org/'+pdf_link
            driver.get(pdf_link)
            sleep(0.5)
        except:
            print("PDF LINK NOT FOUND, VISITING NEXT PAGE.")
            sleep(0.5)
    else:
        print("No results in the given domain")
print("Links Browsed: ")
print(links)
################################################################################
"""One Domain: "https://ieeexplore.ieee.org/" crawled and TOP 10 results captured."""
################################################################################
#           SPRINGER Journals Scraping Section
################################################################################
"""
driver.get("https://scholar.google.com/")
sleep(3)
search_query = driver.find_element_by_xpath('//*[@id="gs_hdr_tsi"]')
try:
    search_query.send_keys("site:springer.com AND " + keyword)
    sleep(0.5)
    search_query.send_keys(Keys.RETURN)
    sleep(1)
except:
    print("NO  SUBJECT FOUND!")
    driver.quit()

search_results_page = Selector(text=driver.page_source)
links = search_results_page.xpath('//h3/a/@href').extract()
print(links)
sleep(1)
for link in links:
    if "https://link.springer.com/" in link:
        driver.get(link)
        sleep(0.5)
        try:
            print("Hello sir, gotcha")
            download_button = driver.find_element_by_xpath('//*[@id="download"]')
            download_button.click()

            sleep(0.5)
        except:
            print("PDF LINK NOT FOUND, VISITING NEXT PAGE.")
            sleep(0.5)
    else:
        print("No results in the given domain")
print("Links Browsed: ")
print(links)
"""
################################################################################
"""One Domain: "https://ieeexplore.ieee.org/" crawled and TOP 10 results captured."""
################################################################################
#       ScienceDirect Scraping Section
################################################################################
driver.get("https://scholar.google.com/")
sleep(3)
search_query = driver.find_element_by_xpath('//*[@id="gs_hdr_tsi"]')
try:
    search_query.send_keys("site:sciencedirect.com AND " + keyword)
    sleep(0.5)
    search_query.send_keys(Keys.RETURN)
    sleep(1)
except:
    print("NO  SUBJECT FOUND!")
    driver.quit()

search_results_page = Selector(text=driver.page_source)
links = search_results_page.xpath('//h3/a/@href').extract()
print(links)
sleep(1)

for link in links:
    if "sciencedirect.com" in link:
        driver.get(link)
        sleep(0.5)
        try:
            print("Hello sir, gotcha")
            response_page = Selector(text=driver.page_source)
            pdf_link = response_page.xpath('').extract_first()
            pdf_link = 'https:///'+pdf_link
            driver.get(pdf_link)
            sleep(0.5)
        except:
            print("PDF LINK NOT FOUND, VISITING NEXT PAGE.")
            sleep(0.5)
    else:
        print("No results in the given domain")
print("Links Browsed: ")
print(links)