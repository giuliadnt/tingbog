   '''internship project tinbog
1 - get rid of table of contents and intro
2 - one year per file
3 - transform special char, reduce multiple spaces
4 - strip html tags
5 - find court cases
6 - ensure they are consecutive
7 - write to individual files name by year, case num
8 - use no special char or spaces in the name
'''

import re
import os

#parse htm files, remove spaces, remove tags
def parsefile(path):
   #read file
   file = open(path, "r")
   fileread = file.read()
   #remove &nbsp
   no_space = fileread.replace("&nbsp;", " ")
   #remove html tags with regex
   no_tags = re.sub ('<[^<]+?>', '' ,no_space)
   return no_tags

#get text between indices (two purposes: separate single cases, separate years grouped in the same file)
def divide_file(mytext, first_item, last_item):
    first_index = mytext.find(first_item) + len(first_item)
    last_index = mytext.find(last_item) + len(last_item)
    return mytext[first_index : last_index]
    
#create new file - get title - create file - write file
def create_case_file(path):
    mytext = parsefile(path)
    court_book_path = os.path.basename(path)
    indices = ["[" + i for i in (re.findall(r"\[(\d+)\s", mytext))]
    court_book_title = [os.path.splitext(court_book_path)[0] + " " + i for i in indices]
    cases = [mytext[0:mytext.find("[1")]]
    for i, j in enumerate(indices):
        if i < len(indices)-1:
            cases.append(find_text_between(mytext, indices[i], indices[i+1]))
    for case, filename in zip(cases, court_book_title):
        with open(filename + ".txt", 'w') as output:
            output.write(case + '\n')
    #return zip(court_book_title, cases)
    return None
    

#mydata = parsefile('C:\Users\GiuliaDnt\Desktop\intern\Skast Herreds Tingbog 1636_TXT.htm')

#create_case_file('C:\Users\GiuliaDnt\Desktop\intern\Skast Herreds Tingbog 1636_TXT.htm')




