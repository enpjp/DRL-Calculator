#  This is a set of HTML Snippets to make the core code look neat
#  Paul J palmer 21st October 2010
#  license: GNU LGPL
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.

from national_DRL import NDRL_tables

class HTML_snip:

	def __init__(self):
        # The static HTML code here:
       		self.footer = """
<!--Content ends here and the footer begins-->
</div>
</div>
</body>
</html>
"""
		self.openResultContainer = """
<div class="ResultsContainer"> <h2>Quick Results</h2>"""

		self.closeResultContainer = """
</div> """

	def insertResult(self, result_desc, result_data):
		insertResultString = """
<div class="Result"> %s %s
</div>
""" %(result_desc, result_data)
		self.insertResult = insertResultString
		return self.insertResult

	def welcome(self):
		self.welcome = """
<h1>DRL Calculator</h1>
<div class="warning">
<p>This software is still under development so may change without notice.  During updates, which may happen at any time,  the server may not be accessible for several minutes. As this tool is made available to you free of charge during this development phase we ask you to be patient.</p>


</div>

<div class="information">
<h2>About this Tool</h2>
<p>This calculator has been designed to analyse data associated with X-ray diagnostic imaging and to assist in the setting of local DRLs (Diagnostic Reference Levels).  Unlike more general purpose tools such as spreadsheets and statistical analysis software, this tool has been optimised for a single task.  This allows appropriate statistical analysis to be pre-programmed and some interpretation of the results provided.
</p>
<p>
The use of this tool is simple: copy and paste your data from whatever document you have to hand.  The data entry box expects each data item on a new line, but will automatically strip out commas, if they are present.  Hit calculate and go to the results tab for a graph and analysis of your data.
</p>


<h2>Accuracy of Calculation</h2>
<p>There are some interesting issues around the use of statistical functions within spreadsheets, that can result in unexpected errors in results.  Most of the time these errors are small and can be ignored, but the nature of the DRL calculation makes it sensitive to the method used, so discrepancies can occur when the same data is used in different software.  In spreadsheets the actual method used to make the calculation is hidden, making auditing of results difficult. This DRL calculator addresses these issues by:
<ul>
<li>
 By using open source libraries we allow you to audit the calculation methods and check for systematic errors; </li>
<li>Several sample data sets have been provided to let you compare the result using the DRL calculator and any other method.  You will notice that with "well behaved" data sets that meet the log normal distribution all methods agree on the answer.  With more typical data discrepancies can be large!</li></ul> 

The most likely cause of unexpected results are:
<ul>
<li>data from more than one procedure or mode combined into a single data set. <strong>The graphical view of the data will show two or more humps if this is the case</strong>;</li>  
<li>insufficient number of points;  <strong>Experience has shown that a minimum of twenty points are required, and more typically at least twice this number for consistent results.</strong> </li></ul>
</p> 
<p>We would welcome more data sets for demonstration purposes.
</p>
<h2>Legal</h2>
<p>This tool uses Open Source libraries for statistical calculations released under LGPL and Webnebulus Ltd gratefully acknowledges their use and associated licence conditions. As this is an on-line tool we refer you to www.gnu.org for full licence details.</p>
<p>Under the terms of the licence we make the source code available for your inspection and use under LGPL. </p>

<h2>Privacy</h2>
<p>This tool does not collect, save or otherwise store any information relating to the data used.  Some annonymous usage data  is automatically collated: the number of times the tool is used; error states; and similar technical data. This information will be used to guage the potential interest for a commercial product. </p>
<h2>Comments</h2>
<p> We encourage comments and enquiries about this product and welcome suggestion for application ideas. You may send  emails to drlchecker@webnebulus.co.uk or use the comment forms on the webnebulus.co.uk website</p>
</div>

"""
			
		return self.welcome


	def data_entry_form_1(self,ndrl_select):
		NDRL = NDRL_tables()
		selection_1 = NDRL.select_exam_2005(ndrl_select)
		string_data_1 = """
<div class="FormContainer">
<h2>Data Entry</h2>
<form method="post" action="/submit_data" name="DRL Data Entry">
<p>Select the appropriate entry from the drop down list if you wish to compare your data against a National (2005) DRL:   </p>
%s 
<p>

Enter your local DRL value using the same units as in the National (2005) DRL table (or leave blank if none set).</p>
<p><input type="text" name="localDRL" /></p>
<div class="PasteText">
<p>The box below will take data entered by hand or pasted from another document. Only numbers are accepted.  If you are comparing your data against a national DRL then be sure to use the same units. The radio buttons can be used to apply a conversion factor to your data if needed.</p>

<div class="PasteTextArea"> <input name="Sumit Data"
value="Calculate" type="submit"><br>
<textarea cols="10" rows="20" name="DRL_data">""" % selection_1
			
		self.data_entry_form_1 = string_data_1
		return self.data_entry_form_1


	def data_entry_form_2(self):
		string_data_2 = """</textarea> 
</div>
<div class="PasteTextArea2">
 Your units are in:<br>
<input type="radio" name="units" value="1" checked > mGy; Gycm<sup>2</sup>; or minutes. (No conversion needed).<br>
<input type="radio" name="units" value="0.1" > cGy; x 0.1 <br>
<input type="radio" name="units" value="0.001"> mGycm<sup>2</sup>; x 0.001<br>
<input type="radio" name="units" value="0.01"> cGycm<sup>2</sup>; x 0.01<br>
<input type="radio" name="units" value="0.0001"> Gym<sup>2</sup>; x 0.0001<br>
<input type="radio" name="units" value="0.01666667"> seconds; x 0.0167<br>
</div>

</div>


</form>
</div>
""" 
		self.data_entry_form_2 = string_data_2
		return self.data_entry_form_2

	def header(self,page_title, id_tab, breadcrumbs):
		self.header = """
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
<meta name="google-site-verification" content="hzsqNDGY2aX-zRMSik8gkLvIOFDc5r86ji-63TqyPeY" />
<meta content="text/html; charset=ISO-8859-1"
http-equiv="content-type">
<title>%s</title>
<link rel="stylesheet" href="stylesheets/app.css" type="text/css">
<style title="Internal" type="text/css">
#%s {
background-color: black;
}
#%s{
  background-color: black;

}

</style>
</head>
<body> """ % (page_title, id_tab, breadcrumbs)

		return self.header

	def body_header(self):
		self.header = """


<div class="menu_container"><!-- Menu container -->
<div class="content_image_top"><!-- Imagefile here --><br>
</div>
<div class="Menu_item_container"><!-- menu Item container -->
<div id="Home" class="menu_item"><a href="/" >Home</a><br>
</div>
</div>

<div class="Menu_item_container"><!-- menu Item container -->
<div id="DataEntry" class="menu_item"><a href="/enter">Calculation</a><br>
</div>
</div>

<div class="Menu_item_container"><!-- menu Item container -->
<div id="National_DRLs" class="menu_item"><a href="/National_DRLs" >National DRLs</a></div>
</div>

<div class="Menu_item_container"><!-- menu Item container -->
<div id="sample" class="menu_item"><a href="/sample" >Sample</a></div>
</div>


</div>
<div class="content_container"><!-- Content Container -->
<div class="content_image_top"><!-- Imagefile here --><br>
</div>
<div class="content"><!--Actual content starts here-->

""" 

		return self.header

	def calc_header(self):
		self.header = """
<div class="menubar_container">
<div class="menubar_container_item" id="enterdata"><a
 href="/enter">Enter Data</a>
</div>
<div class="menubar_container_item" id="results"><a
 href="/results">Results</a>
</div>
<!--
<div class="menubar_container_item" id="analysis"><a
 href="/analysis_plus">Analysis</a> 
</div>
-->
</div>


""" 
#
		return self.header



