#  This is set of classes to analyse DRL data
#  Paul J Palmer 21st October 2010
#  license: GNU LGPL
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.

import sys
import math
import stats
import corestats


# This global variable is used to pass the selected data for the NDR's
My_Global_NDRL = [None]
My_Units_Conversion = [None]
My_local_DRL = [None]

class HT:

	def __init__(self, sequence, NDRL_values,my_unit_conversion,local_DRL):
	# Set the global NDRL
		global My_Global_NDRL
		global My_local_DRL
	        My_local_DRL = local_DRL
		global My_Units_Conversion
		Unit_Conversion = my_unit_conversion
		try:
			conversion_factor = float(Unit_Conversion)
			My_Units_Conversion = conversion_factor			
		except:
			conversion_factor = 1
			My_Units_Conversion = conversion_factor
		try:
		 float(local_DRL)
		except:
		 My_local_DRL = 0


		if len(NDRL_values) > 1:
		 My_Global_NDRL =  NDRL_values
		else:
		 My_Global_NDRL =  [0,0,0,"Not set"]
        # sequence of numbers we will process
        # convert all items to floats for numerical processing 
	# and take the logs
	# Does not work with logs
	# Apply a conversion factor to the data if needed		 


		try:
		  self.sequence = [(float(item))*conversion_factor for item in sequence]
		  self.sequence.sort()
	# Now catches all errors	
		except:
		 return None
		return None

	def count_over_local_DRL(self,):
		# Set the value
		global My_local_DRL
		count_points = 0
		number_of_points = len(self.sequence)
		local_DRL_value = float(My_local_DRL)
		for i in range(number_of_points):
		 if self.sequence[i] > local_DRL_value:
		  count_points = count_points + 1
		return count_points

	def count_over_NDRL(self,):
		# Set the value
		global My_Global_NDRL
		count_points = 0
		number_of_points = len(self.sequence)
		NDRL_value = float(My_Global_NDRL[2])
		for i in range(number_of_points):
		 if self.sequence[i] > NDRL_value:
		  count_points = count_points + 1
		return count_points



	def  min_bin(self):
		if len(self.sequence) < 1: 
            		return None
        	else:
		    	return min(self.sequence)


	def  max_bin(self):
		if len(self.sequence) < 1: 
            		return None
        	else:
            		return max(self.sequence)

    	def avg(self):
        	if len(self.sequence) < 1: 
        	    return None
        	else: 
            	    return sum(self.sequence) / len(self.sequence) 

    	def stdev(self):
        	if len(self.sequence) < 1: 
            	   return None
        	else:
            	 avg = self.avg()
                 sdsq = sum([(i - avg) ** 2 for i in self.sequence])
                 stdev = (sdsq / (len(self.sequence) - 1)) ** .5
                return stdev   

    	def percentile(self, percentile):
	 try:
	  if len(self.sequence) < 4: 
	    value = None
	  elif (percentile >= 100):
	    #sys.stderr.write('ERROR: percentile must be < 100.  you supplied: %s\n'% percentile)
	    value = None
	  else:
	    # This has been modified to use the same method recommended by NIST
	    # This is slightly different from the Excel method.
	    # First sort the sequence
	    self.sequence.sort()
	    # Now find the value of the element at the rank equal to the integer value of percentile
	    element_dec, element_int = math.modf((len(self.sequence)+1) * (percentile / 100.0))
	    element_idx = int(element_int)
	    value = self.sequence[element_idx] + element_dec*(self.sequence[element_idx+1] - self.sequence[element_idx])
	  return value
	 except (TypeError, ValueError, AttributeError):
	  return None
	 return None	

    	def excel_percentile(self, percentile):
	 try:
          if len(self.sequence) < 4: 
            value = None
          elif (percentile >= 100):
            sys.stderr.write('ERROR: percentile must be < 100.  you supplied: %s\n'% percentile)
            value = None
          else:
	    #
            # This is the  Excel method.
	    # First sort the sequence
            self.sequence.sort()
            # Now find the value of the element at the rank equal to the integer value of percentile
	    element_dec, element_int = math.modf((len(self.sequence)-1) * (percentile / 100.0)+1)
            element_idx = int(element_int)
            value = self.sequence[element_idx] + element_dec*(self.sequence[element_idx+1] - self.sequence[element_idx])
          return value
	 except (TypeError, ValueError, AttributeError):
	  return None
	 return None	

    	def DRL_percentile(self, percentile):
    	# Created specially to calculate DRLs which are based on a log-normal distribution
         try:
		if len(self.sequence) < 4: 
            	  value = None
        	elif (percentile >= 100):
            	  sys.stderr.write('ERROR: percentile must be < 100.  you supplied: %s\n'% percentile)
            	  value = None
        	else:
	    	# This has created to make DRLs
           	# This is slightly different from the Excel method.
	    	# First sort the sequence
            	  self.sequence.sort()
	    	# Take the log of each item for processing        
            	  log_sequence = [math.log(item) for item in self.sequence]	
            	# Now find the value of the element at the rank equal to the integer value of percentile
	    	  element_dec, element_int = math.modf((len(self.sequence)+1) * (percentile / 100.0))
            	  element_idx = int(element_int)
                  log_value = log_sequence[element_idx] + element_dec*(log_sequence[element_idx+1] - log_sequence[element_idx])
            	  value = math.exp(log_value)
        	return value   
	 except (TypeError, ValueError, AttributeError):
	 	return None        





	def  number_of_bins(self):
		if len(self.sequence) < 1: 
            		return None
        	else:
		 #number_of_bins = int(len(self.sequence)/5)
		 number_of_bins = 10
		if number_of_bins < 2:
			return 2
		else:
			return number_of_bins

	def  interval(self):
		if len(self.sequence) < 1: 
            		return None
        	else:
		 interval = (self.max_bin() - self.min_bin() )/self.number_of_bins()
		return interval

	def  bin_limits(self):
		number_of_bins = self.number_of_bins()
		if len(self.sequence) < 1: 
            		return None
        	else:
		 bin_limits = [None]*(number_of_bins)
	 

			# Prime the histogram bins
			# Need to implement some bin rounding to ensure no double counting or missing points
		for i in range(number_of_bins):		 	
		 bin_limits[i] = self.min_bin() + self.interval()*i
		bin_limits.append(self.max_bin())
            	return bin_limits

	def  string_bin_limits(self):
		number_of_bins = self.number_of_bins()
		if len(self.sequence) < 1: 
            		return None
        	else:
		 string_bin_limits = [None]*(number_of_bins)
		 bin_limits = self.bin_limits()
		 for i in range(number_of_bins):
		  string_bin_limits[i] = """%.2f """ % bin_limits[i]
		return string_bin_limits
 
	def  freq_bin(self):
		number_of_points = len(self.sequence)
		if number_of_points < 1: 
            		return None
        	else:
		 number_of_bins = self.number_of_bins()


		 bin_count = [None]*(number_of_bins)
		# Now count the frequencies
		# Prime the histogram bin
		 for k in range(number_of_bins):
		   bin_count[k] = 0

		 bin_limits = self.bin_limits()
		# Now count the frequencies
		 for item in self.sequence:
			for j in range(number_of_bins):
			 if item >= bin_limits[j] and item <= bin_limits[j+1]:
				bin_count[j] = (bin_count[j] + 1)
		# Normalise the count as a % frequency
		 for each_bin in range(len(bin_count)):
		  bin_count[each_bin] = round(100*bin_count[each_bin]/number_of_points)
		 freq_bin = bin_count
            	return freq_bin

	def normal(self):
	  # set the values of x
	  number_of_bins = self.number_of_bins()
	  number_of_points = len(self.sequence)
	  bin_limits = self.bin_limits()
	  Expected_count = [None]*(number_of_bins)

	  for i in range(number_of_bins):

    	    z = 1.0*(bin_limits[i]-self.avg())/self.stdev()
            e = math.e**(-0.5*z**2)
            C = math.sqrt(2*math.pi)*self.stdev()
	    A = 1.0*e/C

    	    z = 1.0*(bin_limits[i+1]-self.avg())/self.stdev()
            e = math.e**(-0.5*z**2)
            C = math.sqrt(2*math.pi)*self.stdev()
	    B = 1.0*e/C

	    Expected_count[i] = (A + B)*number_of_points/2

	  normalisation = sum(Expected_count)
	  for each_value in range(len(Expected_count)):
	    Expected_count[each_value] = round(100*Expected_count[each_value]/normalisation)
	  normal = Expected_count
          return normal

	def standard_z(self):
	  # set the values of x
	  #number_of_bins = self.number_of_bins()
	  number_of_bins = 10
	  #number_of_points = len(self.sequence)
	  std_normal_bins = self.standard_normal_freq_bin()
	  bin_limits = std_normal_bins[2]
	  Expected_count = [None]*(number_of_bins)
	  std_dev= 1
	  std_avg = 0
	  for i in range(number_of_bins):
    	    z = 1.0*(bin_limits[i])
            e = math.e**(-0.5*z**2)
            C = math.sqrt(2*math.pi)
	    A = 100.0*e/C

    	    z = 1.0*(bin_limits[i+1])
            e = math.e**(-0.5*z**2)
            C = math.sqrt(2*math.pi)
	    B = 100.0*e/C

	    Expected_count[i] = round((A + B)/2)

	  normalisation = sum(Expected_count)
	  for each_value in range(number_of_bins):
	    Expected_count[each_value] = round(100*Expected_count[each_value]/normalisation)
	  normal = Expected_count
          return normal



	def normal_fit(self):
	  # set the values of x
	  number_of_bins = self.number_of_bins()
	  bin_limits = self.bin_limits()
	  actual_frequency_data = self.freq_bin()
	  normal_frequency_data = self.normal()
	  length_of_data = len(actual_frequency_data)
 	  normal_fit = [None]*length_of_data
	  for item in range(length_of_data):
	    normal_fit[item] = actual_frequency_data[item] - normal_frequency_data[item]
	    if normal_fit[item] >= 0 :
	     normal_fit[item] = normal_fit[item]
	    else:
	     normal_fit[item] = 0 
          return normal_fit

	def normal_fit_negative(self):
	  # set the values of x
	  number_of_bins = self.number_of_bins()
	  bin_limits = self.bin_limits()
	  actual_frequency_data = self.freq_bin()
	  normal_frequency_data = self.normal()
	  length_of_data = len(actual_frequency_data)
 	  normal_fit_negative = [None]*length_of_data
	  for item in range(length_of_data):
	    normal_fit_negative[item] = actual_frequency_data[item] - normal_frequency_data[item]
	    if normal_fit_negative[item] <= 0 :
	     normal_fit_negative[item] = -normal_fit_negative[item]
	    else:
	     normal_fit_negative[item] = 0 
          return normal_fit_negative
    	

	def normal_fit_diff(self):
	  number_of_bins = self.number_of_bins()
	  freq_bins = self.freq_bin()
	  normal_bins = self.normal_fit()
	  normal_fit_diff = [None]*number_of_bins
	  for each_bin in range(number_of_bins):
	   normal_fit_diff[each_bin] = freq_bins[each_bin] - normal_bins[each_bin]
          return normal_fit_diff

	def standard_normal_distribution(self):
	 mean=self.avg()
	 stdev = self.stdev()
	 number_of_points = len(self.sequence)
	 distribution = self.sequence
	 for each_value in range(number_of_points):
	  distribution[each_value]=(distribution[each_value] - mean)/stdev	 
         return distribution

	def log_normal_distribution(self):
	# take logs of sequence
	 log_sequence = []
	 for number in self.sequence:
		log_sequence.append(math.log(number,math.e))
	 mean= stats.lmean(log_sequence)
	 stdev = stats.stdev(log_sequence)
	 number_of_points = len(self.sequence)
	 distribution = log_sequence
	 for each_value in range(number_of_points):
	  distribution[each_value]=(distribution[each_value] - mean)/stdev	 
         return distribution






	# Now modified to use log normal distribution
	def  standard_normal_freq_bin(self):
		number_of_points = len(self.sequence)
		if number_of_points < 1: 
            		return None
        	
		number_of_bins = self.number_of_bins()
		bin_count = [None]*(number_of_bins)
		z_data_distribution = self.log_normal_distribution()
	        # Now set the bin limits
	  	upper_limit = 3.0
		lower_limit = -3.0
		interval = 0.6
		bin_limits = [None]*(number_of_bins)
		#bin_limits_s = [None]*(11)
		for i in range(number_of_bins):		 	
		 bin_limits[i] = lower_limit + interval*i

		bin_limits.append(upper_limit)
		# Now count the frequencies
		# Prime the histogram bin
		for k in range(number_of_bins):
		   bin_count[k] = 0
		#Now count the frequencies
		for item in z_data_distribution:
			for j in range(number_of_bins):
			 if item > bin_limits[j] and item <= bin_limits[j+1]:
				bin_count[j] = (bin_count[j] + 1)
		# Normalise the count as a % frequency
		# This commented out for the moment
		for each_bin in range(len(bin_count)):
		  bin_count[each_bin] = round(100*bin_count[each_bin]/number_of_points)
		freq_bin = bin_count
            	return freq_bin , interval, bin_limits





	def skewness(self):
	#95 % of points should lie with two standard deviations of the mean
	 distribution = self.standard_normal_distribution()	 
	 mean=self.avg()
	 stdev = self.stdev()
	 number_of_points = len(self.sequence)
	 plus_2_stdev = mean + 2*stdev
	 minus_2_stdev = mean - 2*stdev
	 count_low = 0
	 count_high = 0
	 for each_value in range(number_of_points):
	   if distribution[each_value] <= minus_2_stdev:
	    count_low =	 count_low + 1
	   if distribution[each_value] >= plus_2_stdev:
	    count_high = count_high + 1
 
         return count_low, count_high

	def chi_squared(self):
#	 try:
#	  number_of_points = len(self.sequence)
#	 except:
#	  number_of_points = 0
	  
#	 if number_of_points > 2:

	  observed1 = self.standard_normal_freq_bin()
	  observed = observed1[0]
	  expected = self.standard_z()
	  number_of_points = len(expected)
	  chi_squared=[None]*number_of_points	 
	  #chi_squared = (observed - expected)/expected
	  for item in range(number_of_points):
	    if expected[item] >=5:
	     chi_squared[item] = ((observed[item]-expected[item])**2)/expected[item]
	    else:
	     chi_squared[item] = 0
          return chi_squared

	def sum_chi_squared(self):
	 sum_chi_squared = sum(self.chi_squared())
	 return sum_chi_squared

	def chi_squared_p_value(self):
	 df = self.number_of_bins()-1
	 chisq = float(self.sum_chi_squared())
	 chi_squared_p_value = stats.lchisqprob(chisq,df)
	 return chi_squared_p_value*100

# Re writing the histo_chart function to directly construct the chart
	def  histo_chart(self):
#	 try:
	 number_of_points = len(self.sequence)
#	 except:
#	  number_of_points = 3
	  
	 if number_of_points > 2:
	  # Create an ampersand value
	  amp="&amp;"
	  #URL List
	  chart_url = [None]	  
	  #Base URl
	  base_url = "http://chart.apis.google.com/chart?"	  
	  chart_url[0] = base_url
	  # Chart type
 	  chart = "cht=bvs"
	  chart_url.append(chart)
	  # Chart size
	  chart_size = "chs=900x300"
	  chart_url.append(amp)
	  chart_url.append(chart_size)
	  # Chart Title
	  chart_title = "chtt=Simple Plot of Data"
	  chart_url.append(amp)
	  chart_url.append(chart_title)
	  chart_title_colour = "chts=0000FF,20"
	  chart_url.append(amp)
	  chart_url.append(chart_title_colour)
	  # Chart MarginMy_Global_NDRL =  NDRL_values
	  chart_margin = "chma=198"
	  chart_url.append(amp)
	  chart_url.append(chart_margin)

	  
	  # data for chart bars....
	  data_val = "chd=t1:"
	  data1 = self.freq_bin() 
	  # must convert to well behaved string
          data1_str_list = [str(item/.4) for item in data1]
	  data_string1 = ",".join(data1_str_list)
	  #Dataset colour
	  data_colour="chco=0000FF"
	  chart_url.append(amp)
	  chart_url.append(data_colour)

	  # Now the data for the normal distribution line...
	  data2 = self.normal()
          data2_str_list = [str(item/.4) for item in data2]
	  data_string2 = ",".join(data2_str_list)
	  # Now build the string   
	  chart_url.append(amp)
	  chart_url.append(data_val)
	  chart_url.append(data_string1)
	  chart_url.append("|")
	  chart_url.append(data_string2)
	  # plot the line using the 2nd data set count the sets from 0
	  markers = "chm=D,FF0000,1,0,5,1"
	  chart_url.append(amp)
	  chart_url.append(markers)
	  # Set the axis markers	  
	  #my_bin_limits = self.bin_limits()
          #xlabel_str_list = [str(item) for item in my_bin_limits]
	  #my_axis_label = "|".join(xlabel_str_list)
	  # Now set the y range
	  axis_lbl = "chxt=y"
	  chart_url.append(amp)
	  chart_url.append(axis_lbl)
	  axis_range="chxr=0,0,40"
	  chart_url.append(amp)
	  chart_url.append(axis_range)

	  # Set bar widths
	  bar_width = "chbh=50,21"
	  chart_url.append(amp)	
	  chart_url.append(bar_width)
	
	  histo_chart = "".join(chart_url)
	 else:
	  histo_chart = "".join(chart_url)
#	  histo_chart = "images/no_data.png"
         return histo_chart
# End def histo_chart

	def  standard_normal_histo_chart(self):
#	 try:
	 number_of_points = len(self.sequence)
#	 except:
#	  number_of_points = number_of_points
	  
	 if number_of_points > 2:
	  # Create an ampersand value
	  scale_factor = .3
	  amp="&amp;"
	  #URL List
	  chart_url = [None]	  
	  #Base URl
	  base_url = "http://chart.apis.google.com/chart?"	  
	  chart_url[0] = base_url
	  # Chart type
 	  chart = "cht=bvs"
	  chart_url.append(chart)
	  # Chart size
	  chart_size = "chs=900x300"
	  chart_url.append(amp)
	  chart_url.append(chart_size)
	  # Chart Title
	  chart_title = "chtt=Standard Log Normal Plot of Data"
	  chart_url.append(amp)
	  chart_url.append(chart_title)
	  chart_title_colour = "chts=0000FF,20"
	  chart_url.append(amp)
	  chart_url.append(chart_title_colour)
	  # Chart Margin
	  chart_margin = "chma=198"
	  chart_url.append(amp)
	  chart_url.append(chart_margin)
	  # data for chart bars....
	  data_val = "chd=t1:"
	  data1 = self.standard_normal_freq_bin() 
	  # must convert to well behaved string
          data1_str_list = [str(item/scale_factor) for item in data1[0]]
	  data_string1 = ",".join(data1_str_list)
	  #Dataset colour
	  data_colour="chco=0000FF"
	  chart_url.append(amp)
	  chart_url.append(data_colour)
	  # Now the data for the normal distribution line...
	  data2 = self.standard_z()
          data2_str_list = [str(item/scale_factor) for item in data2]
	  data_string2 = ",".join(data2_str_list)
	  # Now build the string   
	  chart_url.append(amp)
	  chart_url.append(data_val)
	  chart_url.append(data_string1)
	  chart_url.append("|")
	  chart_url.append(data_string2)
	  # plot the line using the 2nd data set count the sets from 0
	  markers = "chm=D,FF0000,1,0,5,1"
	  chart_url.append(amp)
	  chart_url.append(markers)
	  # Set the axis markers	  
	  axis_lbl = "chxt=y"
	  chart_url.append(amp)
	  chart_url.append(axis_lbl)
	  upper_scale = round(100*scale_factor)
	  axis_range=("chxr=0,0,%s" % upper_scale)
	  chart_url.append(amp)
	  chart_url.append(axis_range)

	  # Set bar widths
	  bar_width = "chbh=50,21"
	  chart_url.append(amp)	
	  chart_url.append(bar_width)
	  histo_chart = "".join(chart_url)
	 else:
	  histo_chart =  "".join(chart_url)
         return histo_chart
# End def standard_normal_histo_chart

	def  quick_results(self):
	 global My_Global_NDRL
	 global My_Units_Conversion
	 global My_local_DRL
	 local_DRL = My_local_DRL
	 Units_Conversion = My_Units_Conversion
	 #Units_Conversion = "1"
	 #DRL_stats = Stats(self.sequence)
	 NDRL_num = My_Global_NDRL
	 try:
	  number_of_points = len(self.sequence)
	  
	 except:
	  number_of_points = 1
	 if number_of_points > 2:
	  number_of_points = number_of_points


	  table_start1 = """ <div = "information"><p>This is a quick summary of your data. </p>
<p>You may cut and paste data from this page into a spreadsheet or other document. (Formatting is usually preserved better when pasting into a spreadsheet).</p>
</div>"""

#	  table_start2 ="""<table style="text-align: left; width: 100%;" border="0" cellpadding="1" cellspacing="2"> <tbody> """
	  table_start2 ="""<table > <tbody> """
	  table_end= """</tbody>
	</table>"""
	  table_start_row = "<TR>"
	  table_end_row = ""
	  table_start_cell = """<TD align="right">"""
	  table_end_cell = ""
# 	  Now create a table of all the data
# 	  This method is "clunky" but easy to read
#	  Start the table:
	  data_table = [None]
	  data_table.append(table_start1)

	  data_table.append("""<BR> """)

#  We will spilt this into several tables
# Start the first table
	  data_table.append(table_start2)
	  bins = self.bin_limits()
	  cols_span = len(bins)
 


#  Start with the DRL estimates:

# Percentile Calculations DRL

	  data_table.append("""<CAPTION><EM>Key Calculations</EM></CAPTION> """)

	  data_table.append("""<TR class="H"> """)
	  data_table.append(table_start_cell)
	  data_table.append(" ")

	  data_table.append(table_start_cell)
	  data_table.append( 'Results <br>' )
	  data_table.append(table_start_cell)
	  data_table.append("Units %s" %(Units_Conversion) )

	  data_table.append(table_start_row)
	  data_table.append(table_start_cell)
	  data_table.append("Number of points")


	  data_table.append(table_start_cell)
	  data_table.append( ' %.0f <br>' % (len(self.sequence)))
	  data_table.append(table_start_cell)
	  data_table.append( "count ")

	  data_table.append(table_start_row)
	  data_table.append(table_start_cell)
	  data_table.append("NDRL")
	  data_str = My_Global_NDRL[2]
	  data_table.append(table_start_cell)
	  data_table.append( ' %.0f <br>' % (float(data_str)))
	  data_table.append(table_start_cell)
	  data_table.append( " %s <br> " % NDRL_num[3])



	  data_table.append(table_start_row)
	  data_table.append(table_start_cell)
	  data_table.append("Number of points over NDRL")

	  data_table.append(table_start_cell)
	  data_table.append( ' %.0f <br>' % (self.count_over_NDRL()))
	  data_table.append(table_start_cell)
	  data_table.append( "count ")

	  data_table.append(table_start_row)
	  data_table.append(table_start_cell)
	  data_table.append(" Local DRL")
	  data_str = local_DRL
	  data_table.append(table_start_cell)
	  data_table.append( ' %.0f <br>' % (float(data_str)))
	  data_table.append(table_start_cell)
	  data_table.append( " %s <br> " % NDRL_num[3])

	  data_table.append(table_start_row)
	  data_table.append(table_start_cell)
	  data_table.append("Number of points over Local DRL")

	  data_table.append(table_start_cell)
	  data_table.append( ' %.0f <br>' % (self.count_over_local_DRL()))
	  data_table.append(table_start_cell)
	  data_table.append( "count ")





	  data_table.append(table_start_row)
	  data_table.append(table_start_cell)
	  data_table.append("Mean")



	  data_table.append(table_start_cell)
	  data_table.append( ' %.2f <br>' % (self.avg()))
	  data_table.append(table_start_cell)
	  data_table.append( " %s <br> " % NDRL_num[3])


	  data_table.append(table_start_row)
	  data_table.append(table_start_cell)
	  data_table.append("Standard Deviation")


	  data_table.append(table_start_cell)
	  data_table.append( ' %.2f <br>' % (self.stdev()))
	  data_table.append(table_start_cell)
	  data_table.append( " %s <br> " % NDRL_num[3])


	  data_table.append(table_start_row)
	  data_table.append(table_start_cell)
	  data_table.append("90th Percentile")


	  data_table.append(table_start_cell)
	  data_table.append( ' %.2f <br>' % (self.DRL_percentile(90)))
	  data_table.append(table_start_cell)
	  data_table.append( " %s <br> " % NDRL_num[3])

	  data_table.append(table_start_row)
	  data_table.append(table_start_cell)
	  data_table.append("75th Percentile")


	  data_table.append(table_start_cell)
	  data_table.append( ' %.2f <br>' % (self.excel_percentile(75)))
	  data_table.append(table_start_cell)
	  data_table.append( " %s <br> " % NDRL_num[3])






# end the first table and start the next one

	  data_table.append(table_end)	
	  data_table.append("""<br>""")	 
	  data_table.append(table_start2)


# Standard Normal Histogram
	  data_table.append(table_start_row)
	  #data_table.append(table_start_cell)
	  bins = self.bin_limits()
	  cols_span = len(bins)
	  data_table.append("""<TD colspan="%s" align="left" >""" % cols_span) 
	  data_table.append("""

<p>This is a simple plot of the data. Ideally the blue bars will just touch red line to produce a smooth bell shaped curve.</p><br>

""" )




# Histogram
	  data_table.append(table_start_row)
	  #data_table.append(table_start_cell)
	  #data_table.append("Histogram")
	  #data_table.append(table_end_cell)
	  data = self.standard_normal_histo_chart()

	  data_table.append("""<TD colspan="%s" align="left" >""" % cols_span) 
	  data_table.append("""
<img alt="Plot of input data" src="%s"/> <br>

""" % data)



# Observed data
	  data_table.append(table_start_row)
	  data_table.append(table_start_cell)
	  data_table.append("Observed Frequency")

	  data = self.standard_normal_freq_bin()
	  Observed_data_frequency = data[0]
	  for item in range(len(Observed_data_frequency)):
	   data_table.append(table_start_cell)	   
	   data_table.append("%d" % Observed_data_frequency[item])
	   data_table.append(table_end_cell)

# Expected data
	  data_table.append(table_start_row)
	  data_table.append(table_start_cell)
	  data_table.append("Expected Frequency")

	  Expected_data_frequency = self.standard_z()
	  for item in range(len(Expected_data_frequency)):
	   data_table.append(table_start_cell)	   
	   data_table.append("%d" % Expected_data_frequency[item])
	   data_table.append(table_end_cell)






	  data_table.append(table_end)	  
	 	  

	  
	 return data_table



	def  data_table(self):
	 global My_Global_NDRL
	 NDRL_num = My_Global_NDRL
	 data_table = [None]
	 try:
	  number_of_points = len(self.sequence)
	  
	 except:
	  number_of_points = 1
	  data_table.append("""<br><div class="warning">No data!  """)
	  data_table.append("""Enter data or select from sample tab.</div>""")






	 if number_of_points > 2:
	  number_of_points = number_of_points
	  output_comment = stats.lchisquare(self.freq_bin(),self.normal())
	  comment = """Your data is awful! """

	  if output_comment[1] >= .98:
	    comment = """ Your data is an excellent fit to a "log normal distribution" so you may be confident in the output of this and any other statistical analysis on this data. """
	  elif output_comment[1] < .98 and output_comment[1] >= .80 :
	    comment = """Your data is a reasonable fit to a "log normal distribution" but you should investigate for potential reasons for the discrepancy.  <br>
<strong>Any local DRL or other statistic claculated from this data should be treated with some caution.</strong> """	
	  elif output_comment[1] < .80 and output_comment[1] >= .50 :
	    comment = """<div class="warning">Your data is a very poor fit to a "log normal distribution" so you should investgate why, as any attempt to calculate a local DRL or other statistic will be invalid.</div> """	 
	  elif output_comment[1] < .50 and output_comment[1] >= .20 :
	   comment = """<div class="warning">Your data very random and not behaving like a set of radiation total doses.  You should investgate why, as any attempt to calculate a local DRL or other statistic will be invalid.  The data comprises of mixed procedures or mixed units.</div> """	

	  else:
	    comment = """<div class="warning">Your data is very, very random and not behaving like a set of radiation total doses so you should investgate why, as any attempt to calculate a local DRL or other statistic will be invalid.  Perhaps the data comprises of mixed procedures or mixed units.</div> """



	  table_start1 = """ <div = "information"><p>This is a summary of your data that includes so statistical tests for validity. A good quality set of data will fit a "log normal distribution". When plotted correctly, a log normal distribution looks like a smooth bell shaped curve.  If your data does not fit such a curve, then you should seek a reason for the discrepancy.</p>
<p>You may cut and paste data from this page into a spreadsheet or other document. (Formatting is usually preserved better when pasting into a spreadsheet).</p>
</div>"""

	  table_start2 ="""<table style="text-align: left; width: 100%;" border="0" cellpadding="1" cellspacing="2"> <tbody> """
	  table_end= """</tbody>
	</table>"""
	  table_start_row = "<TR>"
	  table_end_row = "</TR>"
	  table_start_cell = """<TD align="right">"""
	  table_end_cell = "</TD>"
# 	  Now create a table of all the data
# 	  This method is "clunky" but easy to read
#	  Start the table:
#	  data_table = [None]
	  data_table.append(table_start1)
	  data_table.append(comment)
	  data_table.append(table_start2)
# Histogram
	  data_table.append(table_start_row)
	  #data_table.append(table_start_cell)
	  #data_table.append("Histogram")
	  #data_table.append(table_end_cell)
	  data = self.standard_normal_histo_chart()
	  bins = self.bin_limits()
	  cols_span = len(bins)
	  data_table.append("""<TD colspan="%s" align="left" >""" % cols_span) 
	  data_table.append("""
<img alt="Plot of input data" src="%s"/> <br>

""" % data)




# Units
	  data_table.append(table_start_row)
	  data_table.append(table_start_cell)
	  data_table.append("Units")

	  data = self.bin_limits()
	  for item in range(len(data)-1):
	   data_table.append(table_start_cell) 
	   data_table.append("%s" %NDRL_num[3])
	   data_table.append(table_end_cell)



# Observed data
	  data_table.append(table_start_row)
	  data_table.append(table_start_cell)
	  data_table.append("Observed Frequency")

	  data = self.standard_normal_freq_bin()
	  Observed_data_frequency = data[0]
	  for item in range(len(Observed_data_frequency)):
	   data_table.append(table_start_cell)	   
	   data_table.append("%d" % Observed_data_frequency[item])
	   data_table.append(table_end_cell)

# Expected data
	  data_table.append(table_start_row)
	  data_table.append(table_start_cell)
	  data_table.append("Expected Frequency")

	  Expected_data_frequency = self.standard_z()
	  for item in range(len(Expected_data_frequency)):
	   data_table.append(table_start_cell)	   
	   data_table.append("%d" % Expected_data_frequency[item])
	   data_table.append(table_end_cell)


# Standard Normal Histogram
	  data_table.append(table_start_row)
	  #data_table.append(table_start_cell)
	  bins = self.bin_limits()
	  cols_span = len(bins)
	  data_table.append("""<TD colspan="%s" align="left" >""" % cols_span) 
	  data_table.append("""

<p>The standard normal histogram plots the data as bell shaped curve of with a mean of 0 and a standard deviation of 1.  This view allows for easier interpretation of anomalies in the data set. </p><br>

""" )





	  output = stats.lchisquare(self.freq_bin(), self.normal() )
# Single data row
	  data_table.append(table_start_row)
	  data_table.append(table_start_cell)
	  data_table.append("Sum of Chi Squared  ")

	  data_table.append("""<TD colspan="%s" align="left" >""" % cols_span) 
	  data_table.append( """ (The closer this value is to zero the better fit your data is to a normal distribution ) =  %.2f """ % output[0] )



# Single data row
	  data_table.append(table_start_row)
	  data_table.append(table_start_cell)
	  data_table.append("P value ")

	  #data = self.histo_fit_chart()
	  #bins = self.bin_limits()
	  #cols_span = len(bins)-1
	  data_table.append("""<TD colspan="%s" align="left" >""" % cols_span)
	  output_percent = output[1]*100
	  data_table.append( """ (The closer this is to 100%% higher the probability that you have a normal distribution) = %.2f %% """ % output_percent )



# Single data row skewness
	  data_table.append(table_start_row)
	  data_table.append(table_start_cell)
	  data_table.append("Skewness ")
	  skewness = self.skewness()

	  data_table.append("""<TD colspan="%s" align="left" >""" % cols_span)
	  data_table.append( """ left = %s, right = %s """ % (skewness[0], skewness[1]) )



# Single data My_Global_NDRL:
#	  data_table.append(table_start_row)
#	  data_table.append(table_start_cell)
#	  data_table.append("Selected NDRL Data ")

#
#	  data_table.append("""<TD colspan="%s" align="left" >""" % cols_span)
#	  data_table.append( """ left = %s, right =  """ % (My_Global_NDRL[0]) )
#
#



	  data_table.append(table_end)	  
	 	  

	  
	 return data_table

