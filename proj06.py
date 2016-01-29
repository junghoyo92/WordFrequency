## CSE 231 sec 02
## project 06
#####################################################

import string

## This function takes a list, an empty dictionary, and a stop word list as parameters.
## It adds words that are not in the stop word list to create a dictionary.
## The dictionary counts the frequency of each word.
## Returns a dictionary
def get_words(List, my_dict, stop):
        for word in List:
            word = str(word)
            word = word.lower()
            word = word.strip(string.punctuation)
            if word in my_dict and word not in stop:
                my_dict[word] += 1
            elif word not in my_dict and word not in stop:
                my_dict[word] = 1
        return my_dict

## This function prints a dictionary out by formatting it to 3 columns.
def print_words(my_dict):
    print_cols = 0
    for word,cnt in my_dict:
        print('{:15s}:{:3d}    '.format(word,cnt),end=' ')
        if print_cols == 3:
            print()
            print_cols = 0
        else:
            print_cols += 1


## This function takes the file as a parameter and creates lists of the words spoken by each speaker respectively.
## It uses tokens to set which speaker is speaking and adds the words after to a the respective list,
## until the token is changed.
## Returns a list of words for each speaker.
def speaker_list(file_obj):
    romney_list = []   
    obama_list = []
    lehrer_list = []
    obama_stop = ['PRESIDENT OBAMA','OBAMA','PRESIDENT OBAMA:', 'OBAMA','BARRACK']
    romney_stop = ['GOVERNOR ROMNEY', 'MR ROMNEY', 'ROMNEY', 'GOVERNOR ROMNEY:', 'MR ROMNEY:', 'ROMNEY:']
    lehrer_stop = ['MR LEHRER:', 'LEHRER:', 'MR LEHRER', 'LEHRER','JIM']
    current_speaker = 0
    for line in file_obj:
        line = line.strip()
        word_list = line.split()
        for word in word_list:
            word = word.strip(string.punctuation)
            if word:
                
                if word in obama_stop:
                    current_speaker = 2
                elif word in romney_stop:
                    current_speaker = 1
                elif word in lehrer_stop:
                    current_speaker = 0
                    
                if current_speaker == 2:
                    if word in obama_stop:
                        del word
                    elif word not in obama_stop:
                        obama_list = obama_list + [word]
                elif current_speaker == 1:
                    if word in romney_stop:
                        del word
                    elif word not in romney_stop:
                       romney_list = romney_list + [word]
                elif current_speaker ==0:
                    if word in lehrer_stop:
                        del word
                    elif word not in lehrer_stop:
                        lehrer_list = lehrer_list + [word]

    return romney_list, obama_list

## This function opens the stop words file and adds the words in the file to a list.
## Returns a list of words.
def stop_words(file_stop):
    stop = ['mr','jim']
    for line in file_stop:
        stop += [line.strip('\n')]
    return stop

## This function takes a dictionary and creates a list of tuples.
## It then sorts the list of tuples and reverses the order.
## The output is a list of the words with the highest frequency.
def top_counts(my_dict):
    tuple_list = []
    my_tuple = ((count,word) for word,count in my_dict.items())
    tuple_list += my_tuple
    tuple_list.sort()
    tuple_list.reverse()
    return tuple_list
    

def make_HTML_box(body):
    '''Required -- body (string), a string of words
       Return -- a string that specifies an HTML box containing the body
    '''
    box_str = """<div style=\"
    width: 560px;
    background-color: rgb(125,125,125);
    border: 1px grey solid;
    text-align: center\" >{:s}</div>
    """
    return box_str.format(body)

def make_HTML_word(cnt,word,high,low):
    ''' make a word with a font size to be placed in the box. Font size is scaled
    between high and low (to be user set). high and low represent the high 
    and low counts in the document. cnt is the count of the word 
    Required -- word (string) to be formatted
             -- cnt (int) count of occurances of word
             -- high (int) highest word count in the document
             -- low (int) lowest word count in the document
    Return -- a string formatted for HTML that is scaled with respect to cnt'''
    ratio = (cnt-low)/float(high-low)
    font_size = high*ratio + (1-ratio)*low
    font_size = int(font_size)
    word_str = '<span style=\"font-size:{:s}px;\">{:s}</span>'
    return word_str.format(str(font_size), word)

def print_HTML_file(body,title):
    ''' create a standard html page (file) with titles, header etc.
    and add the body (an html box) to that page. File created is title+'.html'
    Required -- body (string), a string that specifies an HTML box
    Return -- nothing'''
    fd = open(title+'.html','w')
    the_str="""
    <html> <head>
    <title>"""+title+"""</title>
    </head>

    <body>
    <h1>"""+title+'</h1>'+'\n'+body+'\n'+"""<hr>
    </body> </html>
    """
    fd.write(the_str)
    fd.close()
               
## This is the main function which uses the other functions to output the 40 most frequently use
## in the debate and also outputs an html box with those words in it.
def main():
    file_str = input('What file: ')
    file_obj = open(file_str)
    file_stop = open('stopWords.txt')
    stop = stop_words(file_stop)
    romney_list, obama_list = speaker_list(file_obj)

    my_dict = {}
    obama_dict = get_words(obama_list, my_dict, stop)
    obama_top = top_counts(obama_dict)
    obama = obama_top[:41]
    print('Obama')
    print('==========================')
    print(obama)
    print('==========================')

    my_dict = {}
    romney_dict = get_words(romney_list, my_dict, stop)
    romney_top = top_counts(romney_dict)
    romney = romney_top[:41]
    print('Romney')
    print('==========================')   
    print(romney)
    print('==========================') 
    
    high_count=73
    low_count=11
    body=''
    for cnt,word in obama:
        body = body + " " + make_HTML_word(cnt,word,high_count,low_count)
    box = make_HTML_box(body)  # creates HTML in a box
    print_HTML_file(box,'Obama')  # writes HTML to file name 'Obama.html'

    high_count=122
    low_count=19
    body=''
    for cnt,word in romney:
        body = body + " " + make_HTML_word(cnt,word,high_count,low_count)
    box = make_HTML_box(body)  # creates HTML in a box
    print_HTML_file(box,'Romney')  # writes HTML to file name 'Romney.html'
    
    file_obj.close()
    file_stop.close()

main()


