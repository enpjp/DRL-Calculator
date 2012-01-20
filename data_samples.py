#  This is a set of sample data for DRLs tests
#  Paul J palmer 21st October 2010
#  license: GNU LGPL
#
#  This library is free software; you can redistribute it and/or
#  modify it under the terms of the GNU Lesser General Public
#  License as published by the Free Software Foundation; either
#  version 2.1 of the License, or (at your option) any later version.


class data_samples:

	def sample_data(self):
		string_data = """
<h1>Sample Data Sets</h1>
<p>You may cut and paste these data sets into your own spreadsheet or other software for comparison of results.  Note that your answer may differ from those calculated here due to underlying differences in the software used.
</p>
<div id="Sample 1" class="sample_data">
<div id="Sample 1" class="sample_data_heading">
<h3>PTCA single with stent</h3>
</div>
<form method="post" action="/submit_data" name="DRL Data Entry"> <input
name="Sumit Data" value="Calculate" type="submit"><br>
<input type="hidden" value=" 39, 2, 50.00,  DAP per exam <br>Gy cm<sup>2</sup>" name="2005_NDRL" />
<textarea cols="10" rows="10" name="DRL_data">
17.5
30
29
100.2
83.3
144.1
28.9
121.2
77.3
152
83.7
123.5
56.3
74.7
72.7
103.3
219.4
107.6
58.4
76.2
75
31.7
81.3
41.2
82.9
32.2
36.7
69.2
68.6
80.9
57.5
69.8
67.9
90.2
21
19.6
12.1
30.9
14.9
21.9
45.1
50.8
28.8
21.3

</textarea></form>
</div>
""" 
		self.sample_data = string_data
		return self.sample_data

	def sample_data_2(self):
		string_data = """

<div id="Sample 2" class="sample_data">
<div id="Sample 1" class="sample_data_heading">
<h3>PTCA multi with stents</h3>
</div>
<form method="post" action="/submit_data" name="DRL Data Entry"> <input
name="Sumit Data" value="Calculate" type="submit"><br>
<textarea cols="10" rows="10" name="DRL_data">
57.8
41.5
46.2
79.9
41.4
179.9
36.2
36.2
40.5
39.3
59.7
45.3
109.7
26.3
38.8
97.3
65.3
55
77
54.8
21.4
34.9
29.9
51.9

</textarea></form>
</div>
""" 
		self.sample_data_2 = string_data
		return self.sample_data_2

	def sample_data_3(self):
		string_data = """

<div id="Sample 3" class="sample_data">
<div id="Sample 1" class="sample_data_heading">
<h3>PTCA single and multiwith stentcombined</h3>
</div>
<form method="post" action="/submit_data" name="DRL Data Entry"> <input
name="Sumit Data" value="Calculate" type="submit"><br>
<textarea cols="10" rows="10" name="DRL_data">
57.8
41.5
46.2
79.9
41.4
179.9
36.2
36.2
40.5
39.3
59.7
45.3
109.7
26.3
38.8
97.3
65.3
55
77
54.8
21.4
34.9
29.9
51.9
25.6
37.6
39.8
34.5
21.9
54.3
34.5
44.4
46.5
34.2
12.4
21
13.7
13.6
35.1
16.1
30
9.8
36
17.8
33.6
34.5
17.6
3.4
43.3
80.8
39.9
34.5
45.3
15.1
16.1
27.7
46.5
94
9.9
9.8
16.9
10.2
8.7
69.4
18.7
49.3
33.2
36.7
</textarea></form>
</div>
""" 
		self.sample_data_3 = string_data
		return self.sample_data_3

	def sample_data_4(self):
		string_data = """

<div id="Sample 4" class="sample_data">
<div id="Sample 1" class="sample_data_heading">
<h3>Coronary Arteries Only
</h3>
</div>
<form method="post" action="/submit_data" name="DRL Data Entry"> <input
name="Sumit Data" value="Calculate" type="submit"><br>
<input type="hidden" value=" 19, 2, 29.00,  DAP per exam <br>Gy cm<sup>2</sup>" name="2005_NDRL" />
<textarea cols="10" rows="10" name="DRL_data">
16.4
15.1
11.2
10.6
23.4
11
17.2
7.5
15.2
27
15.2
23.6
11.3
15.3
27
18.7
21.9
23.2
22.9
14
14.8
37.4
33.8
16.6
45
24
11.8
14.2
15
24
32.1

</textarea></form>
</div>
""" 
		self.sample_data = string_data
		return self.sample_data

	def sample_data_4(self):
		string_data = """

<div id="Sample 4" class="sample_data">
<div id="Sample 1" class="sample_data_heading">
<h2>LV & Cors </h2>
</div>
<form method="post" action="/submit_data" name="DRL Data Entry"> <input
name="Sumit Data" value="Calculate" type="submit"><br>
<textarea cols="10" rows="10" name="DRL_data">
19
20.5
24.6
23.6
16.6
27.6
37.8
25.5
33.7
34.5
24
31.6
31.9
21.7
14.3
34.1
55.4
20.3
39.3
19.5
20
15.7
42.5
22.5
23.3
12.1
42.3
27.1
31.2
13.6
128.4
74
34.7
44.4
34.7
17.5
49.5
55.5
26.2
39.1
65.8
37.9
20.8
26.1
28.2
65.4
22
30.8
44
46.8
30.3
63.2
28.3
44
26.4
12.3
5.4
15.3
44.4
24.3
11.7
36.2
25.6
31.9
34.6
38.8
46.5
15.6
30.3
14.2
23.2
20.4
33.9
42.5
52.9
119.1
19.4
24.6
32.3
19.1
52.7
16.4
51.7
26.8
23.2
60.9
50.5
18.1
36.8
20.7
35.8
11.8
32.5
71.8
34.1
58.4
14.1
40.3
22.5
41.1
89.4
14.1
27.6
28.1
36.1
33.7
41
39.1
36.5
32.3
40.4
43.4
8.4
34.4
38.8
48.1
18.2
35.2
34.3
33.9
14.4
52.9
33.3
18.9
38.1
34
29
34.7
31.7
22.3
21.4
17.3
17
21.8
9.8
30
47.2
25.7
30.7
28
30.9
39.7
53
125.6
38.9
32.3
40.6
40.6
39.5
46.2
23
45.1
29.7
24.5
24.1
35.5
40.1
24.7
28.6
27.5
15.7
56.5
11.6
27.3
22.4
35.1
51
28.7
43.8
28.7
15
187.2
23.2
51.6
24.8
34.9
23.1
23.3
47.9
8.9
8.9
16
16.7
16.2
22.7
18
28.2
44
45.7
31.7
21.5
38.3
50
33.6
23.7
34.9
14.8
23.6
30.7
23.9
25.8
29.2
17.2
26
35.7
39.4
31.7
26.3
30.4
29
43.8
54
31.9
17.3
12.4
24.1
16.3
24.7
24.6
60.8
13.7
23
22.9
20
16.1
29.5
32.6
26.3
27.2
26.5
50.8
18.3
21.8
22.8
18
10.9
64.5
22
47.6
13.1
20.8
19.3
28.3
19
13.2
10.8
33.4
42.6
32.6
25.2
37.2
37.8
15.8
9.7
20.7
21.1
20.2
23.3
29.7
32.2
16.4
20.9
22.4
45
32.6
12
19.1
22.5
15.9
27.4
12.6
10.7
20.1
34.2
28.1
25.7
18.1
22.2
19.9
9.4
26.6
35.4
25.4
45.2
14.8
23.9
43.1
12
22.2
21.9
</textarea></form>
</div>
""" 
		self.sample_data = string_data
		return self.sample_data

	def sample_data_5(self):
		string_data = """

<div id="Sample 5" class="sample_data">
<div id="Sample 5" class="sample_data_heading">
<h2>Pacemaker </h2>
</div>
<form method="post" action="/submit_data" name="DRL Data Entry"> <input
name="Sumit Data" value="Calculate" type="submit"><br>
<textarea cols="10" rows="10" name="DRL_data">
911
4626
1498
3378
5604
1806
5865
5229
1255
7381
12659
1537
1076
1778
1865
5499
7006
4518
4571
817
5212
5601
6851
8911
4759
7501
6376
5736
4025
5829
3592
7842
8216
8329
5821
12890
5086
3318
8319
9178
2059
5015
2321
3858
7280
2663
4479
5826
897
11052
6638
12768
974
811
8088
10876
8521
5017
5115
4311
892
3461
1460
783
667
933
1047
8164
2870
5676
5102
1929
7556
1465
10665
23615
7444
1751
30160
2508
5109
8752
4097
1946
4591
7213
10026
3926
826
1774
927
3786
8290
9188
6842
3364
3635
4120
8586
1371
4309
1452
991
3867
1061
1931
1110
13614
1523
746
2524
552
1159
3693
960
3231
3489
3048
6012
788
7421
3818
5807
3376
1004
1142
4503
2659
4290
6538
807
1377
907
6004
3181
5063
2748
6799
3173
6222
3920
516
2300
9125
6294
5482
864
1702
2317
3307
5180
900
4762
4452
3112
4563
927
852
3547
834
5255
5943
4840
16072
4093
1027
4623
5370
1008
1342
8282
7072
5151
3730
3720
3825
1291
4260
4940
7920
4417
5433
</textarea></form>
</div>
""" 
		self.sample_data = string_data
		return self.sample_data

	def sample_data_6(self):
		string_data = """

<div id="Sample 6" class="sample_data">
<div id="Sample 6" class="sample_data_heading">
<h2>Test Data </h2>
</div>
<form method="post" action="/submit_data" name="DRL Data Entry"> <input
name="Sumit Data" value="Calculate" type="submit"><br>
<textarea cols="10" rows="10" name="DRL_data">
550
536
605
1668
1831
874
1256
544
708
538
408
271
441
550
974
424
355
234
1000
598
238
796
217
296
1497
769
1221
253
539
286
455
698
483
328
660
1844
1190
558
344
528
893
194
659
318
937
809
330
2284
551
538
421
620
532
233
230
347
420
289
689
928
680
486
693
438
160
349
1032
5935
548
710
1011
283
420
159
667
508
1131
2085
427
1280
411
125
1056
1662
99
</textarea></form>
</div>
""" 
		self.sample_data = string_data
		return self.sample_data

