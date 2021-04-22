#Assignment 12.1 Sentiment
#Course: DATA 620 9040 Data Management Visualization (2195)
#Professor: Carrie Beam
#Created by: Laura Ellis
#Date: August 8, 2019

#This file assigns sentiment values to sentences based on Vader.
#<-.05 = negative, >.05 = positive

#Enter year numbers for Annual Reports
numfile = 2004
numfileend = 2017
strnumfile = str(numfile)

#Type of file
source = 'Annual_Report'

#Specify where results will be placed
output_file = ('Sentiment.txt', 'w')

#Import VADER
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import nltk.data
import re

analyzer = SentimentIntensityAnalyzer()

#Define counting loop for each file
def countingloop():
    #File is specified
    snumfile = str(numfile)
    #Open and read specified file
    try:
        file = open(snumfile+'.txt')
        a = file.read()
    #Incompatible files are noted
    except:
        print('Error file number', numfile)
        pass
    sentences = re.split(r' *[\.\?!][\'"\)\]]* *', a)
    for line in sentences:
        score = analyzer.polarity_scores(line)
#No write function for tuple so I copied and pasted this time
        print(source, numfile, score)   
    file.close()

#Tell counting loop to perform from first to last file   
while numfile <= numfileend:
    countingloop()
    #Add number for next file
    numfile = numfile + 1
    
#I cleaned this up in Excel to add headers and delete text keeping only numbers.
