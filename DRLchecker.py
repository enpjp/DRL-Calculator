import cgi

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from corestats import Stats


from HTML_Snippets import HTML_snip
from data_samples import data_samples

from analysis_plus import HT
from national_DRL import NDRL_tables

# Define a global data variable for the data
My_Global_DRL = [None]
My_Global_NDRL = [None]
My_local_DRL = [None]
My_Units_Conversion = [None]



class MainPage(webapp.RequestHandler):
    def get(self):
	HTML = HTML_snip()

       # self.response.headers['Content-Type'] = 'text/plain'
       # Displays in text if you leave this in!!

        self.response.out.write(HTML.header("DRL Calculator","Home"," "))

        self.response.out.write(HTML.body_header())
	self.response.out.write(HTML.welcome())
        self.response.out.write(HTML.footer)

class enterPage(webapp.RequestHandler):
    def get(self):
        global My_Global_DRL
	DRL_num = My_Global_DRL
	global My_Global_NDRL
	NDRL_num = My_Global_NDRL
	global My_local_DRL
	local_DRL = My_local_DRL
	global My_Units_Conversion
	Units_Conversion = My_Units_Conversion
	HTML = HTML_snip()
	DRL_stats = Stats(DRL_num)
	DRL_Histo = HT(DRL_num, NDRL_num,Units_Conversion, local_DRL)
	#Anlysis_stats = Dispatch
	number_of_points = len(DRL_num)

	#self.response.headers['Content-Type'] = 'text/plain'

        self.response.out.write(HTML.header("Data Entry","DataEntry", "enterdata"))

        self.response.out.write(HTML.body_header())
# This has now output the menu up to the point at which we insert the actual content

 	self.response.out.write(HTML.calc_header())

#  Need to put the input output result header here

	self.response.out.write(HTML.data_entry_form_1(NDRL_num))	
	if number_of_points > 1:
	 for item in DRL_num:
		self.response.out.write('%s\n' % item)
	self.response.out.write(HTML.data_entry_form_2())

        self.response.out.write(HTML.footer)


class ResultsPage(webapp.RequestHandler):
    def get(self):
        global My_Global_DRL
	DRL_num = My_Global_DRL
	global My_Global_NDRL
	NDRL_num = My_Global_NDRL
	global My_local_DRL
	local_DRL = My_local_DRL
	global My_Units_Conversion
	Units_Conversion = My_Units_Conversion

	HTML = HTML_snip()
	DRL_stats = Stats(DRL_num)
	DRL_Histo = HT(DRL_num, NDRL_num,Units_Conversion,local_DRL)
	#Anlysis_stats = Dispatch
	number_of_points = len(DRL_num)

	#self.response.headers['Content-Type'] = 'text/plain'

        self.response.out.write(HTML.header("Results","DataEntry","results"))


        self.response.out.write(HTML.body_header())
# This has now output the menu up to the point at which we insert the actual content

 	self.response.out.write(HTML.calc_header())
#  Need to put the input output result header here

#	self.response.out.write(HTML.data_entry_form_1(NDRL_num))	
#	if number_of_points > 1:
#	 for item in DRL_num:
#		self.response.out.write('%s\n' % item)
#	self.response.out.write(HTML.data_entry_form_2())

        self.response.out.write(HTML.openResultContainer)
	if number_of_points > 1:
 	 HTML_bits = DRL_Histo.quick_results()

# This bit is the results and can be included in a separate page
	 HTML_bits_count = len(HTML_bits)
	 for item in range(HTML_bits_count):
          self.response.out.write(HTML_bits[item])         

	else:
         self.response.out.write("""<div class="Result">""")
	 self.response.out.write('No data has been entered yet! <br>  Copy and paste data or enter directly in the box to the left using a new line for each data point.<br> When you are done click the calculate button.<br>  This page will give you a summary of your data.  <br>Go to the analysis tab for a detailed breakdown of your data. <br> You may edit data points directly and use calculate to update the results. <br>  Go to the sample tab to use pre-set data. ')
         self.response.out.write("""</div>""")
	# This is the data entry form. Its position is determined by stylesheet parameters
	self.response.out.write(HTML.closeResultContainer)

        self.response.out.write(HTML.footer)



class enter_data(webapp.RequestHandler):
      def post(self):
	global My_Global_DRL
	global My_Global_NDRL
	NDRL_num = My_Global_NDRL
	DRL_num = My_Global_DRL
	global My_local_DRL
	local_DRL = My_local_DRL
	global My_Units_Conversion
	#Units_Conversion = My_Units_Conversion


        # Note the format self.request.get('name') used to collect data from the form.
	# Collect the raw string from the text area field
	local_DRL = self.request.get('localDRL')
	My_local_DRL = local_DRL.decode( 'unicode-escape' ).encode( 'ascii' )
	Units_Conversion = self.request.get('units')
	My_Units_Conversion = Units_Conversion.decode( 'unicode-escape' ).encode( 'ascii' )

	DRL_num_string = self.request.get('DRL_data')
	My_NDRL = self.request.get('2005_NDRL')
	My_NDRL = My_NDRL.decode( 'unicode-escape' ).encode( 'ascii' )
	My_Global_NDRL =My_NDRL.split(',')
	DRL_num_string = DRL_num_string.strip()
	My_Global_DRL = DRL_num_string.splitlines()
	# Test for numbers we do not want anyone pasting scripts here!


	# Need to re-write this to ignore blank lines!!
	# This fails if a single line is not a number
	my_test_list = []
	my_test_drl = My_Global_DRL
	for item in my_test_drl:
		try:
  			i = float(item)
			my_test_list.append(item)
		except ValueError, TypeError:
    			# not numeric
			item = item



	My_Global_DRL = my_test_list




	try:
	 My_test = My_Global_DRL
	 [float(item) for item in My_test]
	except (TypeError, ValueError):
#	 total = sum(My_test)
	 My_Global_DRL = [0]
	try:
	 My_Test_Local=local_DRL
	 float(My_Test_Local)
	except:
	 My_local_DRL = 0
        self.redirect('/results')




class analysis_plus_page(webapp.RequestHandler):
      def get(self):
	global My_Global_DRL
	DRL_num = My_Global_DRL
	global My_Global_NDRL
	NDRL_num = My_Global_NDRL
	global My_Units_Conversion
	my_unit_conversion = My_Units_Conversion
	global My_local_DRL
	local_DRL = My_local_DRL

	HTML = HTML_snip()
	DRL_stats = Stats(DRL_num)
	DRL_Histo = HT(DRL_num, NDRL_num,my_unit_conversion,local_DRL)
	#self.response.headers['Content-Type'] = 'text/plain'

        self.response.out.write(HTML.header("Analysis","DataEntry", "analysis"))


        self.response.out.write(HTML.body_header())
#	data = "true"

 	self.response.out.write(HTML.calc_header())

	HTML_bits = DRL_Histo.data_table()

#	if data == "true":
	 #HTML_bits = DRL_Histo.data_table()
	HTML_bits_count = len(HTML_bits)
	for item in range(HTML_bits_count):
         self.response.out.write(HTML_bits[item])
        self.response.out.write(HTML.footer)

class SampleData(webapp.RequestHandler):
    def get(self):
	HTML = HTML_snip()
	sample = data_samples()
	global My_Units_Conversion
	#My_Units_Conversion = "1"
        # self.response.headers['Content-Type'] = 'text/plain'
       # Displays in text if you leave this in!!

        self.response.out.write(HTML.header("Sample Data","sample"," "))


        self.response.out.write(HTML.body_header())

	self.response.out.write(sample.sample_data())
	#self.response.out.write(sample.sample_data_2())
	#self.response.out.write(sample.sample_data_3())
	#self.response.out.write(sample.sample_data_4())
	#self.response.out.write(sample.sample_data_5())
	#self.response.out.write(sample.sample_data_6())
        self.response.out.write(HTML.footer)


class nationalDRL(webapp.RequestHandler):
    def get(self):
	HTML = HTML_snip()
	NDRL = NDRL_tables()
	#NDRL_v2 = NDRL_tables_v2()
        #self.response.headers['Content-Type'] = 'text/plain'
       # Displays in text if you leave this in!!

        self.response.out.write(HTML.header("National DRLs","National_DRLs", " "))


        self.response.out.write(HTML.body_header())

	#self.response.out.write(NDRL.DRL_2005())
	#self.response.out.write(NDRL.NDRL_table_2005())
	for item in NDRL.NDRL_table_2005():
	 self.response.out.write(item)

        self.response.out.write(HTML.footer)




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

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
