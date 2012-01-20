#  corestats.py (COREy STATS) 
#  Copyright (c) 2006-2007, Corey Goldberg (corey@goldb.org)
#    
#    statistical calculation class
#    for processing numeric sequences
#
#  license: GNU LGPL
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.
#  
#  Percentile modified by Paul.J.Palmer 21st October 2010



import sys
import math

class Stats:
        
    def __init__(self, sequence):
        # sequence of numbers we will process
        # convert all items to floats for numerical processing        
		try:
		  self.sequence = [float(item) for item in sequence]
		except :
		 return None
                return None
    
    def sum(self):
        if len(self.sequence) < 1: 
            return None
        else:
            return sum(self.sequence)
    
    
    def count(self):
        return len(self.sequence)

    
    def min(self):
        if len(self.sequence) < 1: 
            return None
        else:
            return min(self.sequence)
    
    
    def max(self):
        if len(self.sequence) < 1: 
            return None
        else:
            return max(self.sequence)
    

    def avg(self):
        if len(self.sequence) < 1: 
            return None
        else: 
            return sum(self.sequence) / len(self.sequence)    
    
    
    def median(self):
        if len(self.sequence) < 1: 
            return None
        else:
            self.sequence.sort()
            return self.sequence[len(self.sequence) // 2]
            
    
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
            sys.stderr.write('ERROR: percentile must be < 100.  you supplied: %s\n'% percentile)
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

# Sample script using this class:
# -------------------------------------------    
#    #!/usr/bin/env python
#    import corestats
#    
#    sequence = [1, 2.5, 7, 13.4, 8.0]
#    stats = corestats.Stats(sequence)
#    print stats.avg()
#    print stats.percentile(90)
# -------------------------------------------  
