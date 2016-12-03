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
import mechanicalsoup
import config
import spider
from time import strftime

"""
the main thing

input a website
crawl it
log the dead links
"""
def main():
	br = mechanicalsoup.Browser()
	domain = config.DOMAIN
	f = open("{}{}".format(strftime('%l:%M%p %z on %b %d, %Y')," OctoPhoenixLog.txt"),"w")
	web = spider.crawl(f, domain, domain, br)
	checkedpages = web[0]
	deadlinks = web[1]
	for ash in deadlinks:
		phoenix.reincarnate(ash)

if __name__ == "__main__":
	main()