Jupyter Notebook
Assignment 12-Copy1.1 Myriad News Article Detail
(autosaved)
Current Kernel Logo
Python 3 
File
Edit
View
Insert
Cell
Kernel
Widgets
Help

Source\t 
#Assignment 12.1 Extract File Details
#Course: DATA 620 9040 Data Management Visualization (2195)
#Professor: Carrie Beam
#Created by: Laura Ellis
#Date: August 8, 2019
​
#This file pulls article details from Newspaper articles
​
#Specify Report Years
numfile = 2004
numfileend = 2017
snumfile = str(numfile)
​
#Specifiy output file
#Open output file
output_file = open('Detail.txt', 'a')
output_file.write ("Source\t FileNo\t Title\t Newspaper\t Date\n")
​
#Define data pull loop for each file
def extractloop():
    #Make file number a string
    snumfile = str(numfile)
    
    #File is specified
    #Open and read specified file
    source = 'Annual_Report'
    title = 'Annual Report'
    newspaper = 'n/a'
    date = '1/1/'+snumfile
    #print(numfile, title, newspaper, date)
    print(source, '\t', numfile,'\t', title, '\t', newspaper, '\t', date, file=output_file)       
​
    
while numfile <= numfileend:
    extractloop()
    numfile = numfile + 1
output_file.close()
​
​
