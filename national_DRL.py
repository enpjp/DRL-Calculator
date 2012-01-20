#  This is set of classes to analysise DRL data
#  Paul J Palmer 21st October 2010
#  license: GNU LGPL
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.

class NDRL_tables:
	def DRL_2005(self):
# Note 0 means no value set or not applicable
# Text method used as it makes for easy data entry
	 DRL_list = [None]
	 DRL_list[0] = ["N", "None","No selection", 0, 0,0]
	 DRL_list.append(["H", "Individual Radiograph","Individual Radiograph", "ESD per radiograph <br> mGy", "DAP per radiograph <br>Gy cm<sup>2</sup>"," N/A" ])
	 DRL_list.append(["D", " Individual Radiograph", " Abdomen AP",  4,2.6, 0])
	 DRL_list.append(["D", " Individual Radiograph", " Chest LAT",  0.6, 0.3, 0])
	 DRL_list.append(["D", " Individual Radiograph", " Chest PA",  0.15, 0.11, 0])
	 DRL_list.append(["D", " Individual Radiograph", " Lumbar spine AP",  5, 1.6, 0])
	 DRL_list.append(["D", " Individual Radiograph", " Lumbar spine LAT",  11, 2.5, 0])
	 DRL_list.append(["D", " Individual Radiograph", " Lumbar spine LSJ",  26, 2.6, 0])
	 DRL_list.append(["D", " Individual Radiograph", " Pelvis AP ",  4, 2.1, 0])
	 DRL_list.append(["D", " Individual Radiograph", " Skull AP/PA",  2, 0.8, 0])
 	 DRL_list.append(["D", " Individual Radiograph", " Skull LAT",  1.3, 0.5, 0])
 	 DRL_list.append(["D", " Individual Radiograph", " Thoracic spine AP",  4, 0.9, 0])
 	 DRL_list.append(["D", " Individual Radiograph", " Thoracic spine LAT", 7, 1.4, 0])
 	 DRL_list.append(["H", " Diagnostic Examination", " Diagnostic Examination", " N/A", " DAP per exam <br>Gy cm<sup>2</sup>", " Flouroscopy time per exam <br>minutes"])
 	 DRL_list.append(["D", " Diagnostic Examination", " Barium (or water soluble) enema",  0, 24, 28])
 	 DRL_list.append(["D", " Diagnostic Examination", " Barium follow through",  0, 12, 2.2])
  	 DRL_list.append(["D", " Diagnostic Examination", " Barium meal",  0, 14, 2.7])
 	 DRL_list.append(["D", " Diagnostic Examination", " Barium meal &amp; swallow",  0, 11, 2.2]) 
 	 DRL_list.append(["D", " Diagnostic Examination", " Barium (or water soluble) swallow",  0, 9, 2.3])
 	 DRL_list.append(["D", " Diagnostic Examination", " Coronary angiography",  0, 29, 4.5])
 	 DRL_list.append(["D", " Diagnostic Examination", " Femoral angiography", 0,  36, 5.5])
 	 DRL_list.append(["D", " Diagnostic Examination", " Fistulography",  0, 13, 3.8])
 	 DRL_list.append(["D", " Diagnostic Examination", " Hysterosalpingography",  0, 3, 1])
 	 DRL_list.append(["D", " Diagnostic Examination", " IVU",  0, 14, 0])
 	 DRL_list.append(["D", " Diagnostic Examination", " MCU", 0, 12, 1.9])
 	 DRL_list.append(["D", " Diagnostic Examination", " Nephrostography", 0, 12, 4.8])
 	 DRL_list.append(["D", " Diagnostic Examination", " Sialography", 0, 2, 1.7])
 	 DRL_list.append(["D", " Diagnostic Examination", " Sinography",  0, 9, 2.1])
 	 DRL_list.append(["D", " Diagnostic Examination", " Small bowel enema", 0, 40, 4.2]) 
 	 DRL_list.append(["D", " Diagnostic Examination", " T-tube cholangiography",  0, 8, 1.9])
 	 DRL_list.append(["D", " Diagnostic Examination", " Venography",  0, 7, 2.2])
 	 DRL_list.append(["H", " Interventional Procedure", " Interventional Procedure", " N/A", " DAP per exam <br>Gy cm<sup>2</sup>", " Flouroscopy time per exam <br>minutes"])
 	 DRL_list.append(["D", " Interventional Procedure", " Biliary drainage/intervention",  0, 50, 15])
 	 DRL_list.append(["D", " Interventional Procedure", " Facet joint injection",  0, 5, 1.8])
 	 DRL_list.append(["D", " Interventional Procedure", " Hickman line",  0, 3, 1.4])
 	 DRL_list.append(["D", " Interventional Procedure", " Nephrostomy",  0, 14, 5.1])
	 DRL_list.append(["D", " Interventional Procedure", " Oesophageal dilation",  0, 11, 2.8])
 	 DRL_list.append(["D", " Interventional Procedure", " Oesophageal stent",  0, 25, 5.9])
 	 DRL_list.append(["D", " Interventional Procedure", " Pacemaker",  0, 11, 8.2])
 	 DRL_list.append(["D", " Interventional Procedure", " PTCA (single stent)",  0, 50, 13])
 	 DRL_list.append(["H", " Dental Radiography", " Dental Radiography Radiograph", " N/A", " DAP per exam <br>Gy cm<sup>2</sup>", " N/A"])
 	 DRL_list.append(["D", " Dental Radiography", " Panoramic (adult & child)",  0, 82, 0])

	 return DRL_list

	def NDRL_table_2005(self):
# This function returns a full set of tables for the National DRLs in a consistent format
	 full_list = self.DRL_2005()
	 table = [None]
	 table_start = """ 
<table style="text-align: left; width: 100%;" border="1" cellpadding="1" cellspacing="2"> <tbody>  
<tr><th colspan = "4"> Source: HPA-RPD-029 "Doses to patients from radiographic and flouroscopic X-ray imaging procedures in the UK"  2005 review.  Authors:  Hart, M C Hillier and B F Wall.  ISBN: 978-0-85951-600-6 


"""
	 table[0] = table_start
	 table_row_start = """ <tr class = "B">"""
	 table_row_start_heading = """ <tr class = "H">"""
	 table_cell_start = """ <td>"""
	 table_cell_end = """ """
	 table_row_end = """ """
	 table_end = """</tbody></table>"""
# Get each row of NDRL data
	 for each_row in range(len(full_list)):
	  if each_row > 0:
# skip the first row
#	 for item in full_list:
#  	   table.append(table_row_start)
	   data_row = full_list[each_row]
	   if data_row[0] == "H":
  	    table.append(table_row_start_heading)
	   else:
  	    table.append(table_row_start)		
	   for data_item in range(len(data_row)):
	    if data_item >= 2:
	     table.append(table_cell_start)
	     table.append(data_row[data_item])
	    #table.append(table_cell_end)
	  #table.append(table_row_end)
	 table.append(table_end)
	 #table_str_list = [str(item) for item in table]
	 #table_str = " ".join(table_str_list)
	 return table

	def select_exam_2005(self,ndrl_select):
# Creates a selection list to be used inside a form
#<select name="name here">
#<option value="Value here"> selection text here</option>
#</select>
	 NDRL_select= [None]
	 NDRL_select = ndrl_select
	 if len(NDRL_select) < 2:
	  NDRL_select = ["0","0","0","0"]
	 Select_list = [None]
	 Select_list[0] = """<select name="2005_NDRL">"""	
	 full_list = self.DRL_2005()
# set the inital slected option
	 is_selected = """ """
	 has_been_selected = False
	 First_item = full_list[0]
	 option = ("""<option value="1, 0, 0, "Not set""> %s   </option> \n """ % (First_item[2] ))
	 Select_list.append(option)
# option value is set to:
# 0 = index value in full list, 1 = column_index, 2 = DRL_value, 3 = Units	
# need to make an index of the selection
	 for item in range(len(full_list)):
	  item_list = full_list[item]
	  if item_list[0] == "H":
	   esd_units = item_list[3]
	   dap_units = item_list[4]
	   mins_units = item_list[5]
	  elif item_list[0] == "D":
	   procedure_name = item_list[2]
	   if item_list[3] > 0:
	    if item == int(NDRL_select[0]) and int(NDRL_select[1]) == 1:
	     has_been_selected = True
	     is_selected = """selected = "selected" """	     
	    option = ("""<option %s value= " %s, 1, %.2f, %s"> %s (%.2f %s)  </option> \n """ % ( is_selected, item, item_list[3], esd_units, procedure_name, item_list[3], esd_units) )
	    is_selected = """ """
	    Select_list.append(option)
	   if item_list[4] >0:
	    if item == int(NDRL_select[0]) and int(NDRL_select[1]) == 2:
	     has_been_selected = True
	     is_selected = """selected = "selected" """	     
	    option = ("""<option %s value=" %s, 2, %.2f, %s"> %s (%.2f %s)  </option> \n """ % ( is_selected, item, item_list[4], dap_units, procedure_name, item_list[4], dap_units) )
	    is_selected = """ """
	    Select_list.append(option)
	   if item_list[5] >0:
	    if item == int(NDRL_select[0]) and int(NDRL_select[1]) == 3:
	     has_been_selected = True
	     is_selected = """selected = "selected" """	    
	    option = ("""<option %s value="%s, 3, %.2f,%s"> %s (%.2f %s)  </option> \n """ % (is_selected, item, item_list[5], mins_units, procedure_name,item_list[5], mins_units) )
	    is_selected = """ """
	    Select_list.append(option)
# set the inital slected option
	 First_item = full_list[0]
	 if has_been_selected == False:
	  is_selected = """selected = "selected" """	 
	  Select_list[1] = ("""<option %s value="1, 0, 0, "Not set""> %s   </option> \n """ % (is_selected, First_item[2] ))
	 
	 Select_list.append("""</select>""")
	 Select_list_str = "".join(Select_list)
	 return Select_list_str   
	   
	  
