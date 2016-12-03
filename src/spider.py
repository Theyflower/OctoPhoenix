'''
	OctoPhoenix: A webspider that reforms dead links from their cremated remains.
	Copyright (C) 2016  Aaron Thomas

	This program is free software: you can redistribute it and/or modify
	it under the terms of the GNU General Public License as published by
	the Free Software Foundation, either version 3 of the License, or
	(at your option) any later version.

	This program is distributed in the hope that it will be useful,
	but WITHOUT ANY WARRANTY; without even the implied warranty of
	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
	GNU General Public License for more details.

	You should have received a copy of the GNU General Public License
	along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

"""
Crawler.
Go to a website.
Get all the links on a page
	Put them into two groups
		1. internal (same website)
		2. external (different website)
	go to all the internal links (dont go to any twice)
check all external links
send dead links to phoenix
"""
import requests
import phoenix

def twitching(page):
	'''
	Checks if something caught in the web is still twitching
	(Checks if a link is dead, dead links don't twitch)
	'''
	status = page.status_code
	if status != 200: #yah this could beone line of code, but chances are I'll need to handle more than just 200s
		return True
	else:
		return False


def crawl(domain, url, br, indexed=None, deadlinks=[]):
	'''
	@preconditions
		@params:
			domain is the website being cralwed
			url is a link inside of the domain (might be dead)
			br is a mechanicalsoup browser object
			indexed is a list of pages already visited on the domain
				defaults to None for when main calls this function
				can't be an empty list because it needs to be a single 
			deadlinks is a list of the dead links
				defaults to an empty list
	@postconditions
		@todo(aaron) write this
	
	note to self: returns [indexed, deadlinks]
	'''
	if indexed == None:
		indexed = [url]
	page = br.get(url)#todo(aaron) if this fails log it as a deadlink and then return
	if twitching(page):

	links = page.find_all('a')#d@todo(aaron) get all the <a elements
	crawlme = []
	for link in links:
		if link.has_attr('href'):
			url = link.get('href')
		else
			#todo(aaron) make it LOGTHIS
			continue
		if url.startswith(domain): #todo(aaron) make it detect internal urls that dont have the domain name "/dir/page.ext"
			if url not in indexed:
				indexed.append(url)
				new = crawl(domain, url, br, indexed, deadlinks)
				indexed = new[0]
				deadlinks = new[1] #@todo(you) make this good cool stuff with 
		else:
			page = requests.get(url)
			if twitching(page):
				deadlinks.append[phoenix.Ashes(page)]
	return [indexed, deadlinks]