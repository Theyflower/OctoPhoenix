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
import mechanicalsoup

def crawl(url, br, deadlinks=[], indexed=None):
    '''
    '''
    if indexed == None:
        indexed = [url]
    page = br.get(url)

    links = #@todo(aaron) get all the <a elements
    for link in links:
        print(link.href)