# -------------------------------------------------------------------------------------------------------------------------- #
#                     .g8888bgd 
#                   .dP       M 
# ,pP"Ybd  ,pW8Wq.  dM        ; 
# 8I      6W     Wb MM          
#  YMMMa. 8M     M8 MM.         
# L.   I8 YA.   ,A9  Mb.     , 
# M9mmmP;  .Ybmd9.    ..bmmmd.
# -------------------------------------------------------------------------------------------------------------------------- #

import csv
import os
from splinter import *
import time
from selenium.common.exceptions import NoSuchElementException

LLCS = [line.split(',') for line in open("llclist.txt")]


url = "http://opencorporates.com/companies/us_nc"

fileEmpty = os.stat('output.csv').st_size == 0
    
def llctoname():
	numbers = []
	altnumbers = []
	True_people_numbers = []
	alt_true = []	
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

		for comp in company_address:
			address = comp
		try:
			for owner in owners:
				browser = Browser('chrome')
				browser.visit("http://thatsthem.com/people-search")
				browser.find_by_xpath('//*[@id="fullName"]').fill(owner)
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
				numbers.append(Main_number)
				altnumbers.append(alt_numbers)
				for number in numbers:
					person_number = number
				for alt in altnumbers:
					alternates = alt

					results.append({'Company Name': LLC, 'Address': address, 'Name': owner, 'Number': person_number, 'Alt Numbers': alternates})
					numbers = []
				browser.quit()

		except Exception:
			pass
			browser.quit()
			browser = Browser('chrome')
			browser.visit("http://www.truepeoplesearch.com/")
			browser.find_by_xpath('//*[@id="id-d-n"]').fill(owner)
			time.sleep(5)
			browser.find_by_xpath('//*[@id="id-d-loc-name"]').fill(address)
			time.sleep(5)
			browser.find_by_xpath('//*[@id="btnSubmit"]').click()
			time.sleep(5)

			browser.find_by_xpath('/html/body/div[2]/div/div[2]/div[4]/div[1]/div[2]/a').click()
			time.sleep(5)
			True_People_Search_numbers = []
			True_People_Search_numbers = browser.find_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[6]/div[2]').text
			
			time.sleep(5)
			alt_True_num = []
			try:
				browser.find_by_xpath('/html/body/div[2]/div/div[2]/div[1]/div[6]/div[2]/div[5]/div/button').click()
				alt_True_num = browser.find_by_xpath('//*[@id="morePhones"]').text
				alt_true.append(alt_True_num)
			except Exception:
				pass
			print(True_People_Search_numbers)
			print(alt_True_num)
			True_people_numbers.append(True_People_Search_numbers)

			for people_number in True_people_numbers:
				Their_phone = people_number
			for alt_in in alt_true:
				more_numbers = alt_in

			results.append({'Company Name': LLC, 'Address': address, 'Name': owner, 'Number': Their_phone, 'Alt Numbers': more_numbers})
			True_people_numbers = []
			alt_True_num = []
			browser.quit()



		with open('output.csv', 'a', newline='') as file:
			fieldnames = ['Company Name', 'Address', 'Name', 'Number', 'Alt Numbers']
			writer = csv.DictWriter(file, fieldnames=fieldnames)
			if fileEmpty:
				writer.writeheader()
			for result in results:
				writer.writerow(result)

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