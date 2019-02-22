#### Imports ####

import argparse
import webbrowser
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import textwrap




#### Argument Parser ####

parser=argparse.ArgumentParser(
    description='Password Audit Reporting and Graphing by GameOfPWNZ (https://gameofpwnz.com). This Python3 tool takes an input file with passwords and counts characters, searches for strings, and creates statistics and graphs.')
parser.add_argument('-c', dest="COMPANY_NAME", help="Company name or initials (String)")
parser.add_argument('-i', dest="INPUT_FILE", help="Input file (eg. input.txt)")
parser.add_argument('-o', dest="OUTPUT_FILE", help="Output file (HTML)")
parser.add_argument('-s', dest="style", help="MatPlotLib Style: Default (seaborn-darkgrid) https://tonysyu.github.io/raw_content/matplotlib-style-gallery/gallery.html")
args=parser.parse_args()


#### Setting Style ####
style = str(args.style)

if style != "None":
	plt.style.use(style)
else:
	plt.style.use('seaborn-darkgrid')

#### Variables ####

compName = args.COMPANY_NAME
inputFile = args.INPUT_FILE
totalPasswords = 0
fileName = args.OUTPUT_FILE
oneThruSeven = 0
str_oneThruSeven = "<7"
eight = 0
str_eight = "8"
nineThruTwelve = 0
str_nineThruTwelve = "9-12"
thirteenPlus = 0
str_ThirteenPlus = "13+"
pwWithCompany = 0
str_company = str(compName).upper()
pwWithPassword = 0
str_password = "PASSWORD"
pwWithSeason = 0
str_season = "SEASONS"


#### Open File ####

f=open(str(inputFile), 'r')
lines = f.readlines()

#### Counting Characters in Passwords ####

for line in lines:
    totalPasswords+=1
    if len(line) - 1 < 8:
   	 oneThruSeven+=1

    elif len(line) - 1  == 8:
   	 eight+=1

    elif len(line) -1 > 8 and len(line) - 1 < 13:
   	 nineThruTwelve+=1

    elif len(line)-1  >= 13:
   	 thirteenPlus+=1

print_Total = str(totalPasswords)
print_oneThruSeven = str(oneThruSeven)
print_eight = str(eight)
print_nineThruTwelve = str(nineThruTwelve)
print_thirteenPlus = str(thirteenPlus)

#### Counting Passwords with Seasons ####

for line in lines:
    if "WINTER" in str(line).upper():
   	 pwWithSeason+=1
    elif "FALL" in str(line).upper():
   	 pwWithSeason+=1
    elif "SPRING" in str(line).upper():
   	 pwWithSeason+=1
    elif "SUMMER" in str(line).upper():
   	 pwWithSeason+=1
    elif "AUTUMN" in str(line).upper():
   	 pwWithSeason+=1
print_season = str(pwWithSeason)

#### Counting Passwords with Password ####

for line in lines:
    if "PASSWORD" in str(line).upper():
   	 pwWithPassword+=1
print_password = str(pwWithPassword)

#### Counting Passwords with Company Name or Initials (User Input) ####

for line in lines:
    if str(compName).upper() in str(line).upper():
   	 pwWithCompany+=1
print_custom = str(pwWithCompany)




#### Creating Bar Chart For Character Count ####

charcount_x = [str_oneThruSeven, str_eight, str_nineThruTwelve, str_ThirteenPlus]
charcount = [oneThruSeven, eight, nineThruTwelve, thirteenPlus]

char_x_pos = [i for i, _ in enumerate(charcount_x)]

plt.bar(char_x_pos, charcount, align='center')
plt.xlabel("Character Count")
plt.ylabel("Password Count")
plt.title("Passwords by Character Count")

plt.xticks(char_x_pos, charcount_x)

plt.savefig('character_count.png')
plt.close()

#### Creating Bar Chart For Containing String ####

strcount_x = [str_company, str_password, str_season]
strcount = [pwWithCompany, pwWithPassword, pwWithSeason]

str_x_pos = [i for i, _ in enumerate(strcount_x)]

plt.bar(str_x_pos, strcount)
plt.xlabel("Strings (Case Insensitive)")
plt.ylabel("Password Count")
plt.title("Passwords by String Count")

plt.xticks(str_x_pos, strcount_x)

plt.savefig('string_count.png')
plt.close()
    	
#### Creating HTML ####

f = open(fileName,'w')

html = """<html>
<head><b><h1 style="color:blue; font: 15px;">Password Audit Reporting and Graphing</h1></head>
<title>Password Audit Reporting and Graphing</title>
<body>
<p>"""
html += """<b>Total Passwords: </b>"""
html += print_Total
html += """</br> </br> <b>Passwords With Less Than 8 Characters: </b>"""
html += print_oneThruSeven
html += """</br> <b>Passwords With 8 Characters: </b>"""
html += print_eight
html += """</br> <b>Passwords With 9-12 Characters: </b>"""
html += print_nineThruTwelve
html += """</br> <b>Passwords With 13+ Characters: </b>"""
html += print_thirteenPlus
html += """</br> <b>Passwords With The Seasons: </b>"""
html += print_season
html += """</br> <b>Passwords With The Word Password: </b>"""
html += print_password
html += """</br> <b>Passwords With The Company Name or Initials (User Input): </b>"""
html += print_custom
html += """</p><p>"""
html += """<img src='character_count.png')>"""
html += """<img src='string_count.png')>"""
html +="""
</p>
</body>
</html>"""

f.write(html)
f.close()

webbrowser.open(fileName)

