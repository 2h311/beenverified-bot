#! python3
'''beenverifed bot written in python'''

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *

import os, random, time 

ignored_exceptions = (
	ElementClickInterceptedException, 
	ElementNotInteractableException, 
	NoSuchElementException,
	TimeoutException,
)

count = 0; total_count = 0; acc = '';

def wait_time(secs = random.randint(3, 5)):
	print(f"\t[-] Sleeping for {secs}\n")
	time.sleep(secs)

def sanity(list_):
	new = list()
	for term in list_:
		if bool(term):
			pass
		else:
			term = '-'
		new.append(term)
	return ','.join(new)

def login():
	## ############################## ##
	try:
		# fetch login page
		print("[+] Fetching Login Page")
		browser.get("https://www.beenverified.com/app/login")

		# get the submit button
		bt_submit = WebDriverWait(browser, 480, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[type=submit]")))

		# wait for the user to solve the captcha challenge and click the submit button
		print("[*] Waiting for User to Sign in...")
		WebDriverWait(browser, timeout=86400, poll_frequency=1).until(EC.staleness_of(bt_submit))
		print("[*] Log in Successfull...")
	except UnexpectedAlertPresentException:
		# incase there is a login failure due to captcha failure, 
		login()

def prop_info_a():
	## ############################## ##
	county = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="property-location"]/div/div/div[2]/div[1]/div/div/ul/li[2]/span'))).text.replace(',', ' ').replace('\n', ' ')
	city = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="property-location"]/div/div/div[2]/div[1]/div/div/ul/li[4]/span'))).text.replace(',', ' ').replace('\n', ' ')
	state = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="property-location"]/div/div/div[2]/div[1]/div/div/ul/li[1]/span'))).text.replace(',', ' ').replace('\n', ' ')
	beds = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="property-building-details"]/div/div/div[6]/div[1]/div/div/ul/li[2]/span'))).text.replace(',', ' ').replace('\n', ' ')
	baths = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="property-building-details"]/div/div/div[6]/div[2]/div/div/ul/li[1]/span'))).text.replace(',', '').replace('\n', ' ')
	sq_ft = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="property-building-details"]/div/div/div[5]/div[1]/div/div/ul/li[1]/span'))).text.replace(',', '').replace('\n', '')
	lots = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="property-building-details"]/div/div/div[2]/div[2]/div/div/ul/li[1]/span'))).text.replace(',', '').replace('\n', '')
	stories = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="property-building-details"]/div/div/div[4]/div[1]/div/div/ul/li[2]/span'))).text.replace(',', ' ').replace('\n', ' ')
	garage = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="property-building-details"]/div/div/div[5]/div[2]/div/div/ul/li[1]/span'))).text.replace(',', ' ').replace('\n', ' ')
	basement = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="property-building-details"]/div/div/div[5]/div[2]/div/div/ul/li[2]/span'))).text.replace(',', ' ').replace('\n', ' ')
	yr_built = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="property-building-details"]/div/div/div[4]/div[1]/div/div/ul/li[4]/span'))).text.replace(',', ' ').replace('\n', ' ')
	class_ = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="property-building-details"]/div/div/div[4]/div[2]/div/div/ul/li[2]/span'))).text.replace(',', '').replace('\n', '')
	cons_type = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="property-building-details"]/div/div/div[4]/div[2]/div/div/ul/li[3]/span'))).text.replace(',', ' ').replace('\n', ' ')
	codes = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="property-building-details"]/div/div/div[4]/div[2]/div/div/ul/li[4]/span'))).text.replace(',', ' ').replace('\n', ' ')
	prop_type = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="property-building-details"]/div/div/div[2]/div[1]/div/div/ul/li[1]/span'))).text.replace(',', ' ').replace('\n', ' ')
	prop_tax = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="property-value-taxes"]/div/div/div[2]/div/div/div[2]/ul/li/span'))).text.replace(',', '').replace('\n', '')
	est_val = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="property-overview"]/div[2]/div[4]/div/div/strong'))).text.replace(',', '').replace('\n', '')
	#####################################
	ret = sanity([prop_locatn,county,city,state,zip_code,beds,baths,sq_ft,lots,stories,garage,basement,yr_built,class_,cons_type,codes,prop_type,prop_tax,est_val])
	global acc
	acc += f"{ret},"
	## ############################## ##

def lender_a():
	## ############################## ##
	# lender one
	lender1 = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deed_list"]/li[1]/div[2]/div[1]/div[1]/div/div/ul/li[1]/span'))).text.replace(',', ' ').replace('\n', ' ')
	loan_amt1 = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deed_list"]/li[1]/div[2]/div[1]/div[1]/div/div/ul/li[2]/span'))).text.replace(',', '').replace('\n', '')
	lender_type1 = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deed_list"]/li[1]/div[2]/div[1]/div[1]/div/div/ul/li[3]/span'))).text.replace(',', ' ').replace('\n', ' ')
	loan_type1 = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deed_list"]/li[1]/div[2]/div[1]/div[1]/div/div/ul/li[4]/span'))).text.replace(',', '').replace('\n', '')
	lyn_f_credt_loan1 = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deed_list"]/li[1]/div[2]/div[1]/div[1]/div/div/ul/li[5]/span'))).text.replace(',', ' ').replace('\n', ' ')
	###################################
	ret = sanity([lender1,loan_amt1,lender_type1,loan_type1,lyn_f_credt_loan1])
	global acc
	acc += f"{ret},"

def lender_b():
	## ######################### ##
	# lender two
	lender2 = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deed_list"]/li[1]/div[2]/div[1]/div[2]/div/div/ul/li[1]/span'))).text.replace(',', ' ').replace('\n', ' ')
	loan_amt2 = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deed_list"]/li[1]/div[2]/div[1]/div[2]/div/div/ul/li[2]/span'))).text.replace(',', '').replace('\n', '')
	lender_type2 = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deed_list"]/li[1]/div[2]/div[1]/div[2]/div/div/ul/li[3]/span'))).text.replace(',', ' ').replace('\n', ' ')
	loan_type2 = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deed_list"]/li[1]/div[2]/div[1]/div[2]/div/div/ul/li[4]/span'))).text.replace(',', ' ').replace('\n', ' ')
	lyn_f_credt_loan2 = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deed_list"]/li[1]/div[2]/div[1]/div[2]/div/div/ul/li[5]/span'))).text.replace(',', ' ').replace('\n', ' ')
	#############################
	ret = sanity([lender2,loan_amt2,lender_type2,loan_type2,lyn_f_credt_loan2])
	global acc
	acc += f"{ret},"
	## ######################### ##

def prop_info_b():
	## ####################### ##
	trans_date = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deed_list"]/li[1]/div[2]/div[2]/div[1]/div/div/ul/li[3]/span'))).text.replace(',', ' ').replace('\n', ' ')
	trans_val = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deed_list"]/li[1]/div[2]/div[2]/div[1]/div/div/ul/li[4]/span'))).text.replace(',', '').replace('\n', '')
	trans_tax = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deed_list"]/li[1]/div[2]/div[2]/div[1]/div/div/ul/li[5]/span'))).text.replace(',', '').replace('\n', '')
	trans_type = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deed_list"]/li[1]/div[2]/div[2]/div[1]/div/div/ul/li[6]/span'))).text.replace(',', ' ').replace('\n', ' ')
	deed_type = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deed_list"]/li[1]/div[2]/div[2]/div[1]/div/div/ul/li[7]/span'))).text.replace(',', ' ').replace('\n', ' ')
	doc_no = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deed_list"]/li[1]/div[2]/div[2]/div[2]/div/div/ul/li[1]/span'))).text.replace(',', ' ').replace('\n', ' ')
	doc_type = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deed_list"]/li[1]/div[2]/div[2]/div[2]/div/div/ul/li[2]/span'))).text.replace(',', ' ').replace('\n', ' ')
	book_no = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deed_list"]/li[1]/div[2]/div[2]/div[2]/div/div/ul/li[3]/span'))).text.replace(',', ' ').replace('\n', ' ')
	page_no = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deed_list"]/li[1]/div[2]/div[2]/div[2]/div/div/ul/li[4]/span'))).text.replace(',', ' ').replace('\n', ' ')
	rec_date = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deed_list"]/li[1]/div[2]/div[2]/div[2]/div/div/ul/li[5]/span'))).text.replace(',', ' ').replace('\n', ' ')
	rec_type = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deed_list"]/li[1]/div[2]/div[2]/div[2]/div/div/ul/li[6]/span'))).text.replace(',', ' ').replace('\n', ' ')
	quitclaim_dd = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="deed_list"]/li[1]/div[2]/div[2]/div[2]/div/div/ul/li[7]/span'))).text.replace(',', ' ').replace('\n', ' ')
	###########################
	ret = sanity([trans_date,trans_val,trans_tax,trans_type,deed_type,doc_no,doc_type,book_no,page_no,rec_date,rec_type,quitclaim_dd])
	global acc
	acc += f"{ret}"
	## ####################### ##

def tab_find():
	try:
		print('[**] Looking for Tab')
		tabs = WebDriverWait(browser, 35, ignored_exceptions=ignored_exceptions).until(EC.presence_of_all_elements_located((By.ID, 'person_info')))
		if tabs:
			# if found, click the top-most tab
			tabs[0].click()  
		else:
			pass
	except TimeoutException:
		pass

def poss_owners():

	elems_a = WebDriverWait(browser, 360, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located((By.XPATH, '//*[@id="property-owners"]/div'))).find_elements_by_class_name('ember-view')

	person_urls = [ elem.get_attribute('href') for elem in elems_a ]
	for page in person_urls:  # people's address
		print(f"*** Fetching {page}")
		browser.get(page)
		tab_find()  # find tab
		### ##################################################################################################### ###
		print("\tScraping Name\n")
		full_name = WebDriverWait(browser, 120, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.ID, 'overview'))).find_element_by_class_name("txt-black").text
		o_fn, o_mdn, o_lsn = full_name.split(' ')[0], full_name.split(' ')[1], ' '.join(full_name.split(' ')[-1:])
		## ############################################# ##
		contact_card = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.ID, 'phone-numbers'))).find_elements_by_class_name("modal-header")
		print("\tScraping Contact\n")
		con = '**'.join([ con.text.replace(',', '').replace('\n', ' ') for con in contact_card ])
		## ############################################# ##
		emails_card = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.ID, 'email-addresses'))).find_elements_by_class_name("modal-header")
		print("\tScraping Email\n")
		email = '**'.join([ email.text.replace(',', '').replace('\n', ' ') for email in emails_card ])
		## ################################################ ##
		socials_card = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.ID, 'social'))).find_elements_by_class_name("info")
		print("\tScraping Social Medias\n")
		soc = '**'.join([ soc.text.replace(',', '').replace('\n', ' ') for soc in socials_card if soc.text ])
		## ####################################################### ##
		addr_card = WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.ID, 'address_history'))).find_elements_by_class_name("modal-header")
		print("\tScraping Address\n")
		add = '**'.join([ addr.text.replace(',', '').replace('\n', ' ') for addr in addr_card ])
		## #################################################### ##
		if len(person_urls) == 1:
			return f"{full_name},{o_fn},{o_mdn},{o_lsn},{email},{con},{soc},{add},—,—,—,—,—,—,—,—,"
		else:
			return f"{full_name},{o_fn},{o_mdn},{o_lsn},{email},{con},{soc},{add},"
		### ##################################################################################################### ###

def search_one(term):
	# work dey here ooooo
	prop_locatn = ','.join(term.strip('\n').split(',')[1:]).replace(',', ' ')  # also used as the property location
	zip_code = prop_locatn.split(' ')[-1]
	######################
	
	print("[+] Going to the page that has the search form")
	browser.get(r"https://www.beenverified.com/app/report/property?address=1202%20NE%20117th%20St&city=Miami&permalink=3c513bbab81a47c11b78446ce589ad4cba4eafb75c64c033d8e108&state=FL&zipcode=33161")
	wait_time()

	try:
		print(f"[+]\tSearching for {prop_locatn}")
		# click the property tab at the bottom of the page
		WebDriverWait(browser, 360, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.LINK_TEXT, "PROPERTY"))).click()
		WebDriverWait(browser, 360, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.ID, "footerFullAddress"))).send_keys(prop_locatn)
		wait_time(2)
		# click the search_button
		WebDriverWait(browser, 360, ignored_exceptions=ignored_exceptions).until(EC.element_to_be_clickable((By.ID, "search-property-btn"))).click()
		if WebDriverWait(browser, 80, ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located((By.ID, 'loading-overlay'))):
			print("Overlay Found")
			print("Waiting for Disappearance of Overlay")
			WebDriverWait(browser, 60, ignored_exceptions=ignored_exceptions).until(EC.invisibility_of_element_located((By.ID, 'loading-overlay')))
			print("Scraping Data")
			return True
		else:
			print(f"Couldn't fetch for {prop_locatn}")
			return False
			
	except ignored_exceptions as e:
		print(f"[+] {e}")

def collect_file():
	'''
	this function keeps calling asking for a valid filepath until the user enter a valid file path
	file to read from must be a valid csv file
	'''
	rd_frm = input("\t[+] File to Read from -> ")
	if os.path.exists(rd_frm) and os.path.splitext(rd_frm)[-1].lower() == '.csv':
		print(f"\t[++] File Found")
		num = int(input("\t[+] Enter line number to start reading -> "))
		con = open(rd_frm, 'r').readlines()[1:]  # skip the headers
		return con[num - 1:], rd_frm
	else:
		print(f"\t{rd_frm} does not exists. Input a valid file path, make sure File is a CSV file")
		collect_file()

def write_headers():
	'''
	this function writes the headers into the file
	'''
	with open('output.csv', 'w') as fp:
		print("Owner1 - Name,Owner1 - First Name,Owner1 - Middlename,Owner1 - Lastname,Owner1 - Email,Owner1 - Phone,Owner1 - Social,Owner1 - Address,Owner2 - Name,Owner2 - First Name,Owner2 "
			"- Middlename,Owner2 - Lastname,Owner2 - Email,Owner2 - Phone,Owner2 - Social,Owner2 - Address,Address,County,City,State,Zip Code,Beds,Baths,sqFt,Lot Size,Stories,Garage,Basement,"
			"Year Built,Class,Construction Type,Codes,Property Type,Property Tax,Est. Value,Lender1,Loan Amount,Lender Type,Loan Type,Line of Credit Loan,Lender2,Loan Amount,Lender Type,Loan Type,"
			"Line of Credit Loan,Transfer Date,Transfer Value,Transfer Tax,Transfer Type,Deed Type,Document Number,Document Type,Book Number,Page Number,Recorded Date,Recorded Type,Quitclaim Deed", file=fp)

def write_all_info():
	'''
	this function write all accumulated information into the file
	'''
	with open('output.csv', 'a') as fp:
		print(f"{poss_owners()}{acc}", file=fp)	
		count += 1  # for search search only
	total_count += 1  # for all counts - successful and non successful search

def close_op():
	wait_time(3)
	browser.close()
	os._exit(1)

now = time.time()  # this is the time the bot began operation
browser = webdriver.Chrome()
login()

contents, rd = collect_file()

write_headers()  # write the headers into the output file
for term in contents:
	if term:
		try:
			# perform search op
			if search_one(term):
				print("Proceeding to Scrape...")

				# search procedures
				print(f"\n[++] Done Crawling for {prop_locatn}\n")
			else:
				continue
		except KeyboardInterrupt:
			close_op()
		except Exception as e:
			print(f"[+] {e}")
	else:
		print(f"Found An Error: {term}")

print(f"PROCESSING TIME -: {time.time() - now} secs")
print(f"RESULTS Found -: {count}")
print(f"TOTAL Searched -: {total_count}")
print("DONE writing to csv...Check the file -: output.csv")
print(f"LAST file searched -: {rd}")
close_op()
