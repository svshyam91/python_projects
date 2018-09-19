import requests, os, bs4

import extract_zip

def page1( url, dirName ):

	# Downloading the page
	r = requests.get(url)
	try:
		r.raise_for_status()
	except Exception as ec:
		print("There is a problem downloading the page. \nError:",ec)


	# Parsing the page
	subtitleSoup = bs4.BeautifulSoup(r.text,"html.parser")


	# Finding the movie name element
	movie_names = subtitleSoup.select('.media-heading')
	if movie_names == []:
		print('Coundn\'t find the subtitle for your movie.')

		# This exits the program
		raise SystemExit()
	else:
		i = 1
		print('Total number of results found:',len(movie_names))

		if( len(movie_names) == 1 ):
			ch = 1;
		else: 

			# Printing the number of results
			for movie_name in movie_names:
				print (str(i)+".",movie_name.text)
				i += 1
			ch = int(input('Enter your choice: '))
			print('You have choosen ',ch)


	# Finding the element
	results = subtitleSoup.select('div[class="media-body"] > a')
	if results == []:
		print('Couldn\'t find the subtitle for your movie.')

		# This exits the program
		raise SystemExit()
	else:
		page2(results, ch, dirName)


def page2( results, ch, dirName ):
	# This funtion chooses the language of the subtitle. 
	# By Default: We are choosing English

	resultHref = results[ch-1].get('href')
	link = "https://www.yifysubtitles.com"+resultHref


	# Downloading the page
	load_option_page = requests.get(link)
	try:
		load_option_page.raise_for_status()
	except Exception as ec:
		print("There was a problem opening the page having download option.\nError:",ec)


	# Parsing the page
	load_option_pageSoup = bs4.BeautifulSoup(load_option_page.text,"html.parser")


	# Finding the language(english) element
	sub_langs = load_option_pageSoup.select('.sub-lang')
	# print("Length of sub_langs:",len(sub_langs))
	i = 0
	sub_avail = 0
	for sub_lang in sub_langs:
		i += 1
		if sub_lang.text == 'English':
			sub_avail = 1
			break
	if not sub_avail:
		print("Couldn't find the subtitle in English.")

		# This exits the program
		raise SystemExit()


	# Finding the download link of subtitle(english)
	down_sub = load_option_pageSoup.select('.subtitle-download')[i-1]
	down_sub_href = down_sub.get('href')
	temp = down_sub_href.split('/')
	fileName = temp[2]
	down_sub_link = "https://www.yifysubtitles.com"+down_sub_href
	page3( down_sub_link, fileName, dirName )


def page3( down_sub_link, fileName, dirName ):

	# This funtion downloads the subtitle and puts it in a folder


	# Downloading the page3
	down_sub_req = requests.get(down_sub_link)
	try:
		down_sub_req.raise_for_status()
	except Exception as ec:
		print("There was a problem download page3(Download Page). \n\
			Error:",ec)


	# Parsing the page3
	down_sub_parse = bs4.BeautifulSoup(down_sub_req.text,"html.parser")


	# Finding the element
	download_element = down_sub_parse.select('a[class="btn-icon download-subtitle"]')
	download_link = download_element[0].get('href')
	# print("Download Href:",download_link)


	# Downloading the subtitle
	print("Downloading subtitle %s..."%fileName)
	download_request = requests.get(download_link)
	try:
		download_request.raise_for_status()
	except Exception as ec:
		print('There was a problem downloading the subtitle.\nError:',ec)
	print("Done.")


	# Moving the content into the folder
	fileObj = open(os.path.join(dirName+"/Subtitles", fileName), "wb")
	for chunk in download_request.iter_content(100000):
		fileObj.write(chunk)
	fileObj.close()


	extract_file(fileName, dirName)

def extract_file( fileName, dirName ):

	# Extracting the file
	print("Extracting file "+ fileName +"...")

	dirName = dirName+"/Subtitles"

	# Using extract_zip module
	try:
		extract_zip.e_zip( dirName, fileName )
	except:
		print("There is a problem in extract_zip module.")
	print("Done.")

def main():
	dirName = input("Enter the path of the directory:")

	try: 
		os.makedirs( dirName+"/Subtitles", exist_ok = True )
	except: 
		print("There is a problem in making directory.")

	movie = input('Enter the name of the movie:')
	
	url = "https://www.yifysubtitles.com/search?q=%s"%movie
	page1(url, dirName)


if __name__ == '__main__':
	main()
import requests, os, bs4

import extract_zip

def page1( url, dirName ):

	# Downloading the page
	r = requests.get(url)
	try:
		r.raise_for_status()
	except Exception as ec:
		print("There is a problem downloading the page. \nError:",ec)


	# Parsing the page
	subtitleSoup = bs4.BeautifulSoup(r.text,"html.parser")


	# Finding the movie name element
	movie_names = subtitleSoup.select('.media-heading')
	if movie_names == []:
		print('Coundn\'t find the subtitle for your movie.')

		# This exits the program
		raise SystemExit()
	else:
		i = 1
		print('Total number of results found:',len(movie_names))

		if( len(movie_names) == 1 ):
			ch = 1;
		else: 

			# Printing the number of results
			for movie_name in movie_names:
				print (str(i)+".",movie_name.text)
				i += 1
			ch = int(input('Enter your choice: '))
			print('You have choosen ',ch)


	# Finding the element
	results = subtitleSoup.select('div[class="media-body"] > a')
	if results == []:
		print('Couldn\'t find the subtitle for your movie.')

		# This exits the program
		raise SystemExit()
	else:
		page2(results, ch, dirName)


def page2( results, ch, dirName ):
	# This funtion chooses the language of the subtitle. 
	# By Default: We are choosing English

	resultHref = results[ch-1].get('href')
	link = "https://www.yifysubtitles.com"+resultHref


	# Downloading the page
	load_option_page = requests.get(link)
	try:
		load_option_page.raise_for_status()
	except Exception as ec:
		print("There was a problem opening the page having download option.\nError:",ec)


	# Parsing the page
	load_option_pageSoup = bs4.BeautifulSoup(load_option_page.text,"html.parser")


	# Finding the language(english) element
	sub_langs = load_option_pageSoup.select('.sub-lang')
	# print("Length of sub_langs:",len(sub_langs))
	i = 0
	sub_avail = 0
	for sub_lang in sub_langs:
		i += 1
		if sub_lang.text == 'English':
			sub_avail = 1
			break
	if not sub_avail:
		print("Couldn't find the subtitle in English.")

		# This exits the program
		raise SystemExit()


	# Finding the download link of subtitle(english)
	down_sub = load_option_pageSoup.select('.subtitle-download')[i-1]
	down_sub_href = down_sub.get('href')
	temp = down_sub_href.split('/')
	fileName = temp[2]
	down_sub_link = "https://www.yifysubtitles.com"+down_sub_href
	page3( down_sub_link, fileName, dirName )


def page3( down_sub_link, fileName, dirName ):

	# This funtion downloads the subtitle and puts it in a folder


	# Downloading the page3
	down_sub_req = requests.get(down_sub_link)
	try:
		down_sub_req.raise_for_status()
	except Exception as ec:
		print("There was a problem download page3(Download Page). \n\
			Error:",ec)


	# Parsing the page3
	down_sub_parse = bs4.BeautifulSoup(down_sub_req.text,"html.parser")


	# Finding the element
	download_element = down_sub_parse.select('a[class="btn-icon download-subtitle"]')
	download_link = download_element[0].get('href')
	# print("Download Href:",download_link)


	# Downloading the subtitle
	print("Downloading subtitle %s..."%fileName)
	download_request = requests.get(download_link)
	try:
		download_request.raise_for_status()
	except Exception as ec:
		print('There was a problem downloading the subtitle.\nError:',ec)
	print("Done.")


	# Moving the content into the folder
	fileObj = open(os.path.join(dirName+"/Subtitles", fileName), "wb")
	for chunk in download_request.iter_content(100000):
		fileObj.write(chunk)
	fileObj.close()


	extract_file(fileName, dirName)

def extract_file( fileName, dirName ):

	# Extracting the file
	print("Extracting file "+ fileName +"...")

	dirName = dirName+"/Subtitles"

	# Using extract_zip module
	try:
		extract_zip.e_zip( dirName, fileName )
	except:
		print("There is a problem in extract_zip module.")
	print("Done.")

def main():
	dirName = input("Enter the path of the directory:")

	try: 
		os.makedirs( dirName+"/Subtitles", exist_ok = True )
	except: 
		print("There is a problem in making directory.")

	movie = input('Enter the name of the movie:')
	
	url = "https://www.yifysubtitles.com/search?q=%s"%movie
	page1(url, dirName)


if __name__ == '__main__':
	main()
