import csv

from splinter import *
import time
from selenium.common.exceptions import NoSuchElementException

LLCS = [line.split(',') for line in open("llclist.txt")]


n = input("what State?")
if n == "nc":
    url = "http://opencorporates.com/companies/us_nc"
elif n == "":
    url ="https://opencorporates.com/companies/"


    
def llctoname():
	numbers = []
	altnumbers = []
	results = []
	owners = []
	ownername = []
	company_address = []
	try:
		browser = Browser('chrome')
		browser.visit(url)
		browser.find_by_xpath('//*[@id="q"]').fill(LLC)
		time.sleep(5) 
		browser.find_by_xpath('/html/body/div[2]/div[2]/div[1]/div[1]/form/div[2]/input[2]').click()
		time.sleep(5)
		browser.find_by_xpath('//*[@id="results"]').click()
		browser.find_by_xpath('//*[@id="companies"]').click()
		browser.find_by_xpath('/html/body/div[2]/div[2]/div[1]/div[2]/ul/li/a[2]').click()
		time.sleep(5)
		ownername = browser.find_by_xpath("/html/body/div[2]/div[2]/div[1]/div[1]/div/dl/dd[9]/ul/li[1]/a").text
		substring = ","
		if substring in ownername:
			newname = ownername.split(",")[1]
			newlast = ownername.split(',')[0]
			fixed_owner_name = (newname+" "+newlast)
			print(fixed_owner_name)
			owners.append(fixed_owner_name)
		else:
			owners.append(ownername)
		company_address_get = browser.find_by_xpath("/html/body/div[2]/div[2]/div[1]/div[4]/div[2]/div/div[1]/p").text
		zip_code_string = "-"
		if zip_code_string in company_address_get:
			newaddress = company_address_get.split('-')[0]
			print(newaddress)
			company_address.append(newaddress)
		else:
			company_address.append(company_address_get)
			print(company_address)
		browser.quit()

		for owner in owners:
			name = owner
		for comp in company_address:
			address = comp
		try:
			browser = Browser('chrome')
			browser.visit("http://thatsthem.com/people-search")
			browser.find_by_xpath('//*[@id="fullName"]').fill(name)
			time.sleep(5)
			browser.find_by_xpath('//*[@id="address"]').fill(address)
			time.sleep(5) 
			browser.find_by_xpath('/html/body/div/main/section[1]/div/form/div/button').click()
			time.sleep(5)
			Main_number = []
			Main_number = browser.find_by_xpath("/html/body/div[1]/main/section[3]/div[2]/div[1]/div/div[3]/div[2]/dl/dd[1]").text
			time.sleep(5)
			print(Main_number)
			alt_numbers = []
			alt_numbers = browser.find_by_xpath("/html/body/div[1]/main/section[3]/div[2]/div[1]/div/div[3]/div[2]/dl/dd[2]").text
			time.sleep(5)
			print(alt_numbers)
			browser.quit()
		except Exception:
			pass
			browser.quit()
	except Exception:
		pass
		browser.quit()


if __name__ == '__main__':
	while True:
		for LLC in LLCS:
			try:
				llctoname()
			except Exception:
				pass