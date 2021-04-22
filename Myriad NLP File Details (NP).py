#Assignment 12.1 Extract File Details
#Course: DATA 620 9040 Data Management Visualization (2195)
#Professor: Carrie Beam
#Created by: Laura Ellis
#Date: August 8, 2019

#This file pulls article details from Newspaper articles

#Enter number of case files titled "Myriad(#)"
#numfileend = int(input('Enter number of files: '))     Put this back for user specified # of files
numfileend = 190
numfile = 1


#Specifiy output file
#Open output file
output_file = open('Detail.txt', 'a')
#output_file.write ("Source\t FileNo\t Title\t Newspaper\t Date\n")

#Define data pull loop for each file
def extractloop():
    #Make file number a string
    snumfile = str(numfile)
    
    #File is specified
    #Open and read specified file
    try:
        file = open('Myriad News ('+snumfile+').txt')
        a = file.read()
    #Incompatible files are noted
    except:
        print('Error file number ', snumfile)
        pass

# Split and export case name, court, date, case number
    b = a.strip().splitlines()
    source = 'Newspaper'
    title = (b[0])
    newspaper = (b[1])
    c = (b[2])
    for word in c:
        word = word.replace(",", "")
        d = (c.rsplit(',', 0))
        date = (d[0])
    #print(numfile, title, newspaper, date)
    print(source, '\t', numfile,'\t', title, '\t', newspaper, '\t', date, file=output_file)       
    
    # Close the file
    file.close()
    #print(snumfile)
    
while numfile <= numfileend:
    extractloop()
    numfile = numfile + 1
output_file.close()

# I USED EXCEL TO SEPARATE DATE AND DAY OF WEEK (some have it some don't)
