import os
import pandas as pd

class_data = pd.read_csv(os.pardir+"//statistics.csv", header=None)
length = class_data.shape[0]

def writeToFile(course, name, yearsProvidedIn, termsProvidedIn, instructors, sections, department, college, ASDivision, level, activity, insMode, credits, n_sections, pct_grade, avg_grade, stdev_grade, prop_dropped, avg_workload, stdev_workload, avg_course_rating, stdev_course_rating, avg_instructor_rating, stdev_instructor_rating, easiest_instructor, pctA, pctB, pctC, pctD, pctF, pct_wdrawn, pct_incomp, RAP, honors):
	file = open(course[0:4]+"-"+course[5:9]+".md", 'w')
	file.write("---\nlayout: page\ntitle: \"" + course + " Statistics\"\ncomments: true\ndescription: \"blank\"\nkeywords: \"" + course[0:4] + ", " + course[5:9] + ", CU, Boulder\"\n---")
	file.write(""" 
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
<script src="https://dl.dropboxusercontent.com/s/pc42nxpaw1ea4o9/highcharts.js?dl=0"></script>
<!-- <script src="../assets/js/highcharts.js"></script> -->
<style type="text/css">@font-face {
	font-family: "Bebas Neue";
	src: url(https://www.filehosting.org/file/details/544349/BebasNeue%20Regular.otf) format("opentype");
	}
	h1.Bebas { 
		font-family: "Bebas Neue", Verdana, Tahoma;
	}
</style>
</head>
<body>
	<div id="container" style="float: right; width: 45%; height: 88%; margin-left: 2.5%; margin-right: 2.5%;"></div>
	<script language="JavaScript">
		$(document).ready(function() {
		var chart = {type: 'column'};
		var title = {text: 'Grade Distribution'};
		var xAxis = {categories: ['A','B','C','D','F'],crosshair: true};
		var yAxis = {min: 0,title: {text: 'Percentage'}};
		var tooltip = {headerFormat: '<center><b><span style="font-size:20px">{point.key}</span></b></center>',
		               pointFormat: '<td style="padding:0"><b>{point.y:.1f}%</b></td>',
		               footerFormat: '</table>',shared: true,useHTML: true};
		var plotOptions = {column: {pointPadding: 0.0,borderWidth: 0}};  
		var credits = {enabled: false};var series= [{name: 'Percent',data: ["""+pctA+","+pctB+","+pctC+","+pctD+","+pctF+""",]}];
		var json = {};
		json.chart = chart;
		json.title = title;
		json.tooltip = tooltip;
		json.xAxis = xAxis;
		json.yAxis = yAxis;  
		json.series = series;
		json.plotOptions = plotOptions;  
		json.credits = credits;
		$('#container').highcharts(json);
	});
	</script>
</body>
			   """)
	file.write("\n## " + name)
	file.write("\n\n**Years provided**: " + yearsProvidedIn)
	file.write("\n\n**Terms provided**: " + termsProvidedIn)
	file.write("\n\n**Credits**: " + credits)
	if RAP == "1" and honors == "1":
		file.write("\n\n**RAP/Honors class?** Both")
	elif RAP == "1" and honors == "0":
		file.write("\n\n**RAP/Honors class?** RAP")
	elif RAP == "0" and honors == "1":
		file.write("\n\n**RAP/Honors class?** Honors")
	else:
		file.write("\n\n**RAP/Honors class?** Neither")
	file.write("\n\n**Percent grade**: " + pct_grade + "%")
	file.write("\n\n**Percent withdrawn**: " + pct_wdrawn + "%")
	file.write("\n\n**Percent incomplete**: " + pct_incomp + "%")
	file.write("\n\n**Proportion of students who dropped**: " + prop_dropped)
	file.write("\n\n**Average grade** (4.0 scale): " + avg_grade)
	file.write("\n\n**Standard deviation in grades**: " + stdev_grade)
	file.write("\n\n**Average workload** (raw): " + avg_workload)
	file.write("\n\n**Standard deviation in workload** (raw): " + stdev_workload)
	file.write("\n\n**Average course rating** (6 point scale): " + avg_course_rating)
	file.write("\n\n**Standard deviation in course rating** (6 point scale): " + stdev_course_rating)
	file.write("\n\n**Average instructor rating** (6 point scale): " + avg_instructor_rating)
	file.write("\n\n**Standard deviation in instructor rating** (6 point scale): " + stdev_instructor_rating)
	file.write("\n\n**Instructors**: " + instructors)
	file.write("\n\n**Easiest instructor** (based on class grade): " + easiest_instructor)
	file.write("\n\n**Sections** (and **number of sections**): " + sections + ", " + n_sections)
	file.write("\n\n**Department**: " + department)
	file.write("\n\n**College**: " + college)
	if ASDivision != "nan":
		file.write("\n\n**A&S Division**: " + ASDivision)
	file.write("\n\n**Level**: " + level)
	file.write("\n\n**Activity**: " + activity)
	if insMode != "nan":
		file.write("\n\n**Instructor Mode**: " + insMode)


for i in range(1, length):
	course = str(class_data[i:i+1].iloc[0][0])
	name = str(class_data[i:i+1].iloc[0][1])
	yearsProvidedIn = str(class_data[i:i+1].iloc[0][2])
	termsProvidedIn = str(class_data[i:i+1].iloc[0][3])
	instructors = str(class_data[i:i+1].iloc[0][4])
	sections = str(class_data[i:i+1].iloc[0][5])
	department = str(class_data[i:i+1].iloc[0][6])
	college = str(class_data[i:i+1].iloc[0][7])
	ASDivision = str(class_data[i:i+1].iloc[0][8])
	level = str(class_data[i:i+1].iloc[0][9])
	activity = str(class_data[i:i+1].iloc[0][10])
	insMode = str(class_data[i:i+1].iloc[0][11])
	credits = str(class_data[i:i+1].iloc[0][12])
	n_sections = str(class_data[i:i+1].iloc[0][13])
	pct_grade = str(round(float(class_data[i:i+1].iloc[0][17])*100,2))
	avg_grade = str(round(float(class_data[i:i+1].iloc[0][18]),2))
	stdev_grade = str(round(float(class_data[i:i+1].iloc[0][19])*100,2))
	prop_dropped = str(round(float(class_data[i:i+1].iloc[0][20])*100,2))
	avg_workload = str(round(float(class_data[i:i+1].iloc[0][21]),2))
	stdev_workload = str(round(float(class_data[i:i+1].iloc[0][22]),2))
	avg_course_rating = str(round(float(class_data[i:i+1].iloc[0][23]),2))
	stdev_course_rating = str(round(float(class_data[i:i+1].iloc[0][24]),2))
	avg_instructor_rating = str(round(float(class_data[i:i+1].iloc[0][25]),2))
	stdev_instructor_rating = str(round(float(class_data[i:i+1].iloc[0][26]),2))
	easiest_instructor = str(class_data[i:i+1].iloc[0][27])
	pctA = str(round(float(class_data[i:i+1].iloc[0][28])*100,2))
	pctB = str(round(float(class_data[i:i+1].iloc[0][29])*100,2))
	pctC = str(round(float(class_data[i:i+1].iloc[0][30])*100,2))
	pctD = str(round(float(class_data[i:i+1].iloc[0][31])*100,2))
	pctF = str(round(float(class_data[i:i+1].iloc[0][32])*100,2))
	pct_wdrawn = str(round(float(class_data[i:i+1].iloc[0][38])*100,2))
	pct_incomp = str(round(float(class_data[i:i+1].iloc[0][39])*100,2))
	RAP = str(class_data[i:i+1].iloc[0][45])
	honors = str(class_data[i:i+1].iloc[0][46])
	writeToFile(course, name, yearsProvidedIn, termsProvidedIn, instructors, sections, department, college, ASDivision, level, activity, insMode, credits, n_sections, pct_grade, avg_grade, stdev_grade, prop_dropped, avg_workload, stdev_workload, avg_course_rating, stdev_course_rating, avg_instructor_rating, stdev_instructor_rating, easiest_instructor, pctA, pctB, pctC, pctD, pctF, pct_wdrawn, pct_incomp, RAP, honors)

