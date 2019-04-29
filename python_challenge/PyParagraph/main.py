
import os

# Module for reading CSV files
import csv

import re


# In[16]:


def readfile(myfile):
    totlettercount = 0
    totwordcount = 0
    totsentcount = 0
    paragraphnum = 0
    
    with open("raw_data/" + myfile) as file_object: 
        #totlettercount = 0
        #totwordcount = 0
        #totsentcount = 0
        lines = file_object.readlines()
        print("The file you chose:" + myfile)
        for paragraph in lines: 
            totlettercount = 0
            totwordcount = 0
            totsentcount = 0
            
            wordcount = 0
            #print(paragraph)
            #ericinput = input("pause here")
            
            #re.split("(?<=[.!?]) +", paragraph)
            wordlist = re.split(" ", paragraph)    #split on spaces

            wordcount = len(wordlist)  #word count (REQUIRED)
            totwordcount = totwordcount + wordcount  # to account for possible multiple paragraphs in file
            #print(wordcount)
            sentencelist = re.split("(?<=[.!?]) +", paragraph)   
            sentcount = len(sentencelist)
            totsentcount = totsentcount + sentcount

            for word in wordlist:
                lettercount = len(word)
                totlettercount = totlettercount + lettercount
            avglettercount = totlettercount / wordcount     # REQUIRED

            avgsentencelength = wordcount / sentcount     # REQUIRED


            if wordcount > 1:     
                paragraphnum = paragraphnum + 1
                print("\n#Paragraph Analysis")
                print("#-----------------")
                print(f"#Paragraph # {paragraphnum}")
                print(paragraph + "\n")
                print(f"#Approximate Word Count:  {totwordcount}")
                print(f"#Approximate Sentence Count:   {totsentcount}")
                print(f"#Average Letter Count:  {avglettercount}")
                print(f"#Average Sentence Length:   {avgsentencelength}")


userinput = input("Select (1) for file paragraph_1.txt or (2) for file paragraph_2.txt or (3) for Adam Wayne snippet for processing..")
if userinput == "1":
    chosenfile = "paragraph_1.txt"
    readfile(chosenfile)
elif userinput == "2":
    chosenfile = "paragraph_2.txt"
    print("Showing stats for each paragraph in the file!")
    readfile(chosenfile)
elif userinput == "3":
    chosenfile = "AdamWayne.txt"
    print("2 words off in my count. README.md says 122 words and so does Notepad++, I get 120!")
    readfile(chosenfile)
else:
    print("Please pick number for your file selection.  Please re-run the program")
    chosenfile = ""
    
print("\nFinished!")
