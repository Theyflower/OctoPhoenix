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
PLANS FOR THIS FILE:
Put the code here that gets the archive.org snapshots of pages
how am I gonna do this?
"""
class Ashes:
	def __init__(self, body, time):
		'''
		body is the corpse of a dead link
		(the request)
		'''
		self.url = body.url
		self.response = body.status_code
		self.time = time
		self.life = reincarnate(self.url)

	def to_string(self):
		return """
		Dead link found at {}
				URL = {}
				REPONSE = {}
				GOODLINK = {}
		""".format(self.time, self.url, self.response, self.life)

def reincarnate(ashes):#@todo(aaron make this)
	'''
	Take the cremated remains of a dead link and makes it rise from the ashes.

	Gets an archive.org
	'''
	base_url = "https://web.archive.org/web/0/"
	url = "{}{}".format(base_url, ashes)
	return url