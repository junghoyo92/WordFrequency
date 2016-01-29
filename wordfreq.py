import string

def get_words(f_obj,my_dict):
    for line in f_obj:
        line = line.strip()
        word_list = line.split()
        for word in word_list:
            word = word.lower()
            word = word.strip(string.punctuation)
            if word:
                if word in my_dict:
                    my_dict[word]+=1
                else:
                    my_dict[word]=1

def print_words(my_dict):
    print_cols = 0
    for word,cnt in my_dict.items():
        print('{:11s}:{:3d}    '.format(word,cnt),end=' ')
        if print_cols == 3:
            print()
            print_cols = 0
        else:
            print_cols += 1

 
#def main():
file_str = input('What file: ')
file_obj = open(file_str)
my_dict = {}
get_words(file_obj,my_dict)
file_obj.close()
print('There were {:d} words in the file {:s}'.format(len(my_dict),file_str))
print_words(my_dict)
