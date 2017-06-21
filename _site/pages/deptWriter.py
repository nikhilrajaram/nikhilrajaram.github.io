import os
from pathlib import Path
import pandas as pd

class_data = pd.read_csv(os.pardir+"//statistics.csv", header=None)
length = class_data.shape[0]

# def writeToFile(course, name, yearsProvidedIn, termsProvidedIn, instructors, sections, department, college, ASDivision, level, activity, insMode, credits, n_sections, pct_grade, avg_grade, stdev_grade, prop_dropped, avg_workload, stdev_workload, avg_course_rating, stdev_course_rating, avg_instructor_rating, stdev_instructor_rating, easiest_instructor, pctA, pctB, pctC, pctD, pctF, pct_wdrawn, pct_incomp, RAP, honors):
# 	file = open(course[0:4]+"-"+course[5:9]+".md", 'w')
# 	file.write("---\nlayout: page\ntitle: \"" + course + " Statistics\"\ncomments: true\ndescription: \"blank\"\nkeywords: \"" + course[0:4] + ", " + course[5:9] + ", CU, Boulder\"\n---")
# 	file.write(""" 
# <head>
# <script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
# <script src="https://dl.dropboxusercontent.com/s/pc42nxpaw1ea4o9/highcharts.js?dl=0"></script>
# <!-- <script src="../assets/js/highcharts.js"></script> -->
# <style type="text/css">@font-face {
# 	font-family: "Bebas Neue";
# 	src: url(https://www.filehosting.org/file/details/544349/BebasNeue%20Regular.otf) format("opentype");
# 	}
# 	h1.Bebas { 
# 		font-family: "Bebas Neue", Verdana, Tahoma;
# 	}
# </style>
# </head>
# <body>
# 	<div id="container" style="float: right; width: 45%; height: 88%; margin-left: 2.5%; margin-right: 2.5%;"></div>
# 	<script language="JavaScript">
# 		$(document).ready(function() {
# 		var chart = {type: 'column'};
# 		var title = {text: 'Grade Distribution'};
# 		var xAxis = {categories: ['A','B','C','D','F'],crosshair: true};
# 		var yAxis = {min: 0,title: {text: 'Percentage'}};
# 		var tooltip = {headerFormat: '<center><b><span style="font-size:20px">{point.key}</span></b></center>',
# 		               pointFormat: '<td style="padding:0"><b>{point.y:.1f}%</b></td>',
# 		               footerFormat: '</table>',shared: true,useHTML: true};
# 		var plotOptions = {column: {pointPadding: 0.0,borderWidth: 0}};  
# 		var credits = {enabled: false};var series= [{name: 'Percent',data: ["""+pctA+","+pctB+","+pctC+","+pctD+","+pctF+""",]}];
# 		var json = {};
# 		json.chart = chart;
# 		json.title = title;
# 		json.tooltip = tooltip;
# 		json.xAxis = xAxis;
# 		json.yAxis = yAxis;  
# 		json.series = series;
# 		json.plotOptions = plotOptions;  
# 		json.credits = credits;
# 		$('#container').highcharts(json);
# 	});
# 	</script>
# </body>
# 			   """)
# 	file.write("\n## " + name)

prefix = "2017-06-13-"
deptName = "AAST"
for i in range(1, length):
	course = str(class_data[i:i+1].iloc[0][0])
	file = Path(prefix + deptName + ".md")
	if file.is_file():
		print "works"
		if (course == str(class_data[(i-1):i].iloc[0][0])):
			print "works again"
	else:
		file = open(prefix + deptName + ".md", 'w')