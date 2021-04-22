Jupyter Notebook
Laura_Ellis Assignment 12.1 Word Count with Lemmatize
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

​
#Assignment 12.1 Word Count with Lemmatize
#Course: DATA 620 9040 Data Management Visualization (2195)
#Professor: Carrie Beam
#Created by: Laura Ellis
#Date: August 8, 2019

#Run through a list of text files pulled from Nexis Uni.
#Text is split, NLTK lemmatize is used, NLTK stopwords are
#not included. A list of most common words (length deterimined
#by user is created as a text file including file name, word, count.
#Character, word, and line counts are also given for each file.

#Collections for word counting
import collections

#Import packages
#NLTK for Lemmatization
import nltk
from nltk.stem import WordNetLemmatizer
lmtzr = WordNetLemmatizer() 

#NLTK for stopwords, then add custom 
from nltk.corpus import stopwords
stop = stopwords.words('english')
stop.append("•")
stop.append("")
stop.append("myriad")
stop.append("Genetics")
stop.append("genetics")
stop.append("Myriad")
#I'm not in the articles but Nexis Uni adds it in some places
stop.append("Laura")
stop.append("Ellis")

                                        #OPTION 1: NEWS
#Enter numbers for files
#numfile = int(input('Enter number of files: '))        Put this back for user specified # of files
#numfileend = int(input('Enter number of files: '))     Put this back for user specified # of files
#numfile = 1
#numfileend = 190
#source = 'Newspaper'


                                        #OPTION 2: ANNUAL REPORTS
numfile = 2004
numfileend = 2017
source = 'Annual_Report'

#Convert numfile to string for use in file name. (Python cannot concatenate a string and integer.)
strnumfile = str(numfile)

#Enter number of words to return
listlength = int(input('Enter number of words: '))

#Specifiy output file
#Open output file
                                        #CHANGE OUTPUT FILE NUMBER HERE
output_file = open('Word Counts.txt', 'a')
output_file.write ("Source CountType FileNo CountOf Count\n")      #TURN OFF IF RUN 2ND

#Define counting loop for each file
def countingloop():
    #Assign year values based on file being used      #ANNUAL REPORTS ONLY
    nextyear = str((numfile)+1)
    lastyear = str((numfile)-1)
    yearname = str(numfile)
    twoyearsago = str(int(numfile)-2)    
    
    snumfile = str(numfile)
    #File is specified
    #Open and read specified file
    try:
                                        #OPTION 1: NEWS
        #file = open('Myriad News ('+snumfile+').txt')
                                        #OPTION 2: ANNUAL REPORTS
        file = open(snumfile+'.txt')
        a = file.read()
    #Incompatible files are noted
    except:
        print('Error file number ', snumfile)
        pass

# count characters 
    num_chars = len(a)

# count lines 
    num_lines = a.count('\n')
       
# Initiate dictionary
    wordcount = {}

# Add to the dictionary if it doesn't exist. If it does, increase the count. (Only for words not in common word list.)
    for word in a.lower().split():
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace(":","")
        word = word.replace("\"","")
        word = word.replace("!","")
        word = word.replace("-","")
        word = word.replace("—","")
        word = word.replace("•","")
        word = word.replace("$","")
        word = word.replace(")","")
        word = word.replace("(","")
        word = word.replace("?","")
        word = word.replace("+","")
        word = word.replace("[","")
        word = word.replace("]","")
        word = word.replace(";","")
        word = word.replace("*","")
        word = word.replace("~","")
        word = word.replace(">","")
        word = word.replace("}","")
        word = word.replace("{","")
        word = word.replace("¶","")
        word = word.replace("**","")
#Convert mentions of year in annual report to text for easier comparison    ANNUAL REPORTS ONLY
        word = word.replace(yearname,"report_year")
        word = word.replace(nextyear,"following_year")
        word = word.replace(lastyear,"prior_year")
        word = word.replace(twoyearsago,"two_years_ago")        

#Do not include words in stop list 
        if word not in stop:
#Lemmatize first
            word = lmtzr.lemmatize(word)
#IF YOU WANT SPECIFIC WORDS ADD THIS "if word == 'your-word':" (REMEMBER INDENT)
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
                
# Count number of words
    num_words = sum(wordcount[word] for word in wordcount)

#This gives counts for the entire article/report
#Print number of characters, lines, and words to file
    print(source, "list_count", numfile, "chars", num_chars, file=output_file)
    print(source, "list_count", numfile, "lines", num_lines, file=output_file)
    print(source, "list_count", numfile, "words", num_words, file=output_file)
#This gives word counts
#Print word counts to file    
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common(listlength):
        print(source, "word", numfile, word, count, file=output_file)

    # Close the file
    file.close()
    #Show file numbers print for verification
    print(numfile)


#Tell counting loop to perform from first to last file   
while numfile <= numfileend:
    countingloop()
    #Add number for next file
    numfile = numfile + 1
#Close output file
output_file.close()
#Assignment 12.1 Word Count with Lemmatize
#Course: DATA 620 9040 Data Management Visualization (2195)
#Professor: Carrie Beam
#Created by: Laura Ellis
#Date: August 8, 2019
​
#Run through a list of text files pulled from Nexis Uni.
#Text is split, NLTK lemmatize is used, NLTK stopwords are
#not included. A list of most common words (length deterimined
#by user is created as a text file including file name, word, count.
#Character, word, and line counts are also given for each file.
​
#Collections for word counting
import collections
​
#Import packages
#NLTK for Lemmatization
import nltk
from nltk.stem import WordNetLemmatizer
lmtzr = WordNetLemmatizer() 
​
#NLTK for stopwords, then add custom 
from nltk.corpus import stopwords
stop = stopwords.words('english')
stop.append("•")
stop.append("")
stop.append("myriad")
stop.append("Genetics")
stop.append("genetics")
stop.append("Myriad")
#I'm not in the articles but Nexis Uni adds it in some places
stop.append("Laura")
stop.append("Ellis")
​
                                        #OPTION 1: NEWS
#Enter numbers for files
#numfile = int(input('Enter number of files: '))        Put this back for user specified # of files
#numfileend = int(input('Enter number of files: '))     Put this back for user specified # of files
#numfile = 1
#numfileend = 190
#source = 'Newspaper'
​
​
                                        #OPTION 2: ANNUAL REPORTS
numfile = 2004
numfileend = 2017
source = 'Annual_Report'
​
#Convert numfile to string for use in file name. (Python cannot concatenate a string and integer.)
strnumfile = str(numfile)
​
#Enter number of words to return
listlength = int(input('Enter number of words: '))
​
#Specifiy output file
#Open output file
                                        #CHANGE OUTPUT FILE NUMBER HERE
output_file = open('Word Counts.txt', 'a')
output_file.write ("Source CountType FileNo CountOf Count\n")
​
#Define counting loop for each file
def countingloop():
    #Assign year values based on file being used      #ANNUAL REPORTS ONLY
    nextyear = str((numfile)+1)
    lastyear = str((numfile)-1)
    yearname = str(numfile)
    twoyearsago = str(int(numfile)-2)    
    
    snumfile = str(numfile)
    #File is specified
    #Open and read specified file
    try:
                                        #OPTION 1: NEWS
        #file = open('Myriad News ('+snumfile+').txt')
                                        #OPTION 2: ANNUAL REPORTS
        file = open(snumfile+'.txt')
        a = file.read()
    #Incompatible files are noted
    except:
        print('Error file number ', snumfile)
        pass
​
# count characters 
    num_chars = len(a)
​
# count lines 
    num_lines = a.count('\n')
       
# Initiate dictionary
    wordcount = {}
​
# Add to the dictionary if it doesn't exist. If it does, increase the count. (Only for words not in common word list.)
    for word in a.lower().split():
        word = word.replace(".","")
        word = word.replace(",","")
        word = word.replace(":","")
        word = word.replace("\"","")
        word = word.replace("!","")
        word = word.replace("-","")
        word = word.replace("—","")
        word = word.replace("•","")
        word = word.replace("$","")
        word = word.replace(")","")
        word = word.replace("(","")
        word = word.replace("?","")
        word = word.replace("+","")
        word = word.replace("[","")
        word = word.replace("]","")
        word = word.replace(";","")
        word = word.replace("*","")
        word = word.replace("~","")
        word = word.replace(">","")
        word = word.replace("}","")
        word = word.replace("{","")
        word = word.replace("¶","")
        word = word.replace("**","")
#Convert mentions of year in annual report to text for easier comparison    ANNUAL REPORTS ONLY
        word = word.replace(yearname,"report_year")
        word = word.replace(nextyear,"following_year")
        word = word.replace(lastyear,"prior_year")
        word = word.replace(twoyearsago,"two_years_ago")        
​
#Do not include words in stop list 
        if word not in stop:
#Lemmatize first
            word = lmtzr.lemmatize(word)
#IF YOU WANT SPECIFIC WORDS ADD THIS "if word == 'your-word':" (REMEMBER INDENT)
            if word not in wordcount:
                wordcount[word] = 1
            else:
                wordcount[word] += 1
                
# Count number of words
    num_words = sum(wordcount[word] for word in wordcount)
​
#This gives counts for the entire article/report
#Print number of characters, lines, and words to file
    print(source, "list_count", numfile, "chars", num_chars, file=output_file)
    print(source, "list_count", numfile, "lines", num_lines, file=output_file)
    print(source, "list_count", numfile, "words", num_words, file=output_file)
#This gives word counts
#Print word counts to file    
    word_counter = collections.Counter(wordcount)
    for word, count in word_counter.most_common(listlength):
        print(source, "word", numfile, word, count, file=output_file)
​
    # Close the file
    file.close()
    #Show file numbers print for verification
    print(numfile)
​
​
#Tell counting loop to perform from first to last file   
while numfile <= numfileend:
    countingloop()
    #Add number for next file
    numfile = numfile + 1
#Close output file
output_file.close()
​

​
