#This is a script checks for Result of 3 sem every 15 Min 
#Author Chittaranjan Kumar
#Just for Fun
import urllib2
import re
import os
import time
 
while 1:
 
	#Type your university result's url instead of http://www.gtu.ac.in/results.asp.
    html_content = urllib2.urlopen('http://www.gtu.ac.in/results.asp').read() 
 
	#Type your semester instead of BE SEM 3.
    matches = re.findall('BE SEM 3', html_content);  
 
 
    if len(matches) == 0: 
       os.system("notify-send 'Yeah' 'Result is not declared yet'")
       time.sleep(900) #You can mention your own time in second.
 
    else:
       os.system("notify-send 'Oops' 'Result Declared'")
       quit()
