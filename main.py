#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#Not needed
#os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
# Note this must be the first line
from google.appengine.dist import use_library
use_library('django', '1.2')
import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import webapp
from google.appengine.ext import db
from corestats import Stats



from views import *

from HTML_Snippets import HTML_snip
from data_samples import data_samples

from analysis_plus import HT
from national_DRL import NDRL_tables

# Define a global data variable for the data
My_Global_DRL = [None]
My_Global_NDRL = [None]
My_local_DRL = [None]
My_Units_Conversion = [None]


def main():
    	application = webapp.WSGIApplication(
                                     [('/', MainPage),
                                      ('/enter', enterPage),
        		       	      ('/submit_data',enter_data),
                                      ('/results', ResultsPage),
                                      ('/analysis_plus', analysis_plus_page),
                                      ('/National_DRLs', nationalDRL),
				      ('/sample', SampleData),
 #                                      ('/debug', TestPage),
 #                                     ('/deleteentry', DeleteEntry),
       					],
                                     debug=True)
    #util.run_wsgi_app(application)
	run_wsgi_app(application)

if __name__ == '__main__':
    main()


