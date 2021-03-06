#HW3 for Course MATH 510
#Instructor:Professor G

#Problem 1:Print a histogram to screen
def histogram(h):
    """
     This function takes a list of intergers and then outputs a histogram according to the numbers in list
     
     Parameters:
     h - any list of non-negative integers
    """
    for num in h:             #use 'for' loop to get each number in the list
        print('*'*num)        #each time output the current number times '*'
    return
    
    
#Problem 2:Select the largest number in a list
def max_in_list(n):
    """
     This function takes a list of numbers and then return the largest
     
     Parameters:
     n - any list of numbers
    """
    max=0                                 #initial a variable max with 0 to store the max value in the list
    for num in n:                         #use 'for' loop to get each number in the list
        if max<num:                       #if current value of num in the list is larger than max
            max=num                       #update max with the current value of num
    return max                            #finally return the largest number
    
    
    
#Problem 3:Maps a list of words into a list of integers representing the lengths of the corresponding words
def list_len(li):
    """
     This function takes a list of words and output the length of each word in order as a list
     
     Parameters:
     li - any list of strings
    """
    w_list=[]                               #create an empty list to store the lengths of each item in the given list
    for i,word in enumerate(li):            #use for loop to go through the list li and get the index of current item
        w_list.append(len(li[i]))           #use len() to get the length of current item and add this value to w_list
    return w_list
    
    
#Problem 4:Select the longest word in a given list
## Sould return the length of the longest word instead of the word
def find_longest_word(wl):
    """
     This function takes a list of words,get the length of each word and return the longest word
     
     Parameters:
     wl - any list of words with no space in the word since space will be counted in the length calculation
    """
    lgst=[]              #create an empty list lgst to store the longest words with a initail value of the first word
                         #it is probable that there are several largest words,sharing the same length,so here we need a list variable
    lgstlen=0                                  #create a variable to store current largest words' length
    for word in wl:                            #use 'for' loop to get each word in the list 
        if lgstlen<len(word):                  #compare the current word's length with the current largest length
            lgst=[]                            #if the current word is longer, empty the lgst list
            lgst.append(word)                  #adding the current word in wl to lgst and update largest length
            lgstlen=len(word)
        elif len(word)==lgstlen:               #if the current one is as large as the largest,add it to list lgst   
            lgst.append(word)
    return lgst
    
    
#Problem 5:Filter out a list of words whose length is larger than given
def filter_long_words(wl,n):
    """
     This function takes a list of words wl and an integer n,selects all the words longer than n and then returns
     them as a list
     
     Parameters:
     wl - any list of words with no space in the word since space will be counted in the length calculation
     n - any positive integer since a negative n will just output the original entire list
    """
    flw=[]                               #create an empty list to store words whose length is larger than n
    for word in wl:                      #use 'for' loop to get each word in the list wl
        if len(word)>n:                  #if the word's length is larger than n, add this word into list flw
            flw.append(word)
    return flw
    
    
#Problem 6: Recognize phrase palindromes
from string import punctuation                        
def phrase_palindrome(prs):
    """
     This function is to recognize phrase palindromes regardless of punctuation,capitalization and space.
     
     Parameters:
     prs - a string that allows consisting of numbers,letters,space,punctuation
    """
    
    map=prs.maketrans('','',punctuation)                #create a transformation pattern of deleting punctuations in the string
                                                        #the transformation will be passed to translate() as argument
    prs=prs.translate(map)                              #use the method translate() to execute the transformation created
                                                        #by maketrans() and then delete puntuations in the string prs
    prs=prs.replace(' ','')                             #delete all the space in the string prs
    prs=prs.lower()                                     #change all the characters to lower cases
    str=prs[::-1]                                       #generate an new string that is the reversal of prs
    if str==prs:                                        #check whether transformed prs and its reversal are the same 
        return True                                     #if they are the same, return True,False otherwise
    else:
        return False
        
        
        
#Problem 7:Recognize a pangram
def is_pangram(sts):
    """
     This function is to recognize a sentense that contains all the English letters in alphabet at least once
     
     Parameters:
     sts - any kind of string
    """
    alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
                                                 #put all the English letters in alphabet in a list
    lts=[s for s in sts.lower() if s.isalpha()]  #unify all the English letters in the sentence in lower cases 
                                                 #and put them together into a new variable lts
    for alp in alphabet:                    #check from 'a' to 'z" in the alphabet to see whether it is in variable lts
        if alp not in lts:                   
            return False                    #if there is one alphabet letter not in sts,end loop and return False
    return True                             #otherwise all alphabet letters are in the sentence and return True
        
        
        
#Problem 8:Generalize all the repetitive verse in the song "99 bottles of coke"
def verse(n):
    """
     This function is to output all the verses repeated in a song and the repeating times is an input.The numbers in
     the verse decreases by 1 each time
     
     Parameters:
     n - any positive integer
    """
    for i in range(n,0,-1):                  #use 'for' loop starting from n backward to 0 with step=-1
        print("%d bottles of beer on the wall, %d bottles of beer.\n"%(i,i)+
               "Take one down, pass it around, %d bottles of beer on the wall."%(i-1))
                                        #print out verse repeatedly with the numbers in verse decreasing by 1 each time
    return
    
    
    
#Problem 9:Represent a samll bilingual lexicon as a Python dictionary
## Function should take a list of strings as input - Prof G
def translate(eng):
    """
     This function is to translate Christmas cards from English into Swedish in the following fashion:
     fashion {"merry":"god", "christmas":"jul", "and":"och", "happy":gott","new":"nytt", "year":"ar"}
     
     Parameters:
     eng - a string that allows containing the following words:"merry","christmas","and","happy","new","year"
           which are not sensative to capitalization
    """
    dic={"merry" : "god",                                 #create a dictionary that provides mappings from English to Swidish                  
       "christmas" : "jul",
       "and":"och",
       "happy":"gott",
       "new":"nytt",
       "year":"ar"}
    tranStr = ""                                           #create an empty string to store translation word
    to_list=eng.split(" ")                                 #change input string into a list with each word as an element in string
                                                           #here use space as seperator
    for i in to_list:                                      #use 'for' loop to get each word in the list to_list
        if str(dic.get(i.lower()))!= "None":               #change the current element into lower case and look for the 
                                                           #corresponding Swidish word from the dictionary dic
            tranStr = tranStr+str(dic.get(i.lower()))+" "  #if can be translated,update tranStr by adding the translation
        else:
            return ('the sentence cannot be translated')   #once there is a word that cannot translated,return the message
    return tranStr                          
    
    
    
#Problem 10:Build frequency listing of the characters for a given string

#Solution 1:
#the idea here is to use dictionary and update it
def char_freq1(string):
    """
     This function is to count the occurrence for each character in the given string and output a frequency listing．
     It can count all the types of characters such as letters,numbers,space,puntuation and so on
     
     Parameters:
     string - any kind of string
    """
    dic={}                          #initiate an empty dictionary to record each character and its occurrence in string
    for c in string:                #use 'for' loop to get each character in string
        if dic.get(c)==None:        #check whether the character has already in the dic,if not,add this character as 
                                    #as key and 1 as initial value to dictionary dic
            dic[c]=1
        else:
            dic[c]=dic[c]+1         #if it has existed, update the dic by adding 1 to this key's value
    return dic    

#Solution 2:
#the idea here is to use collections.Counter() to get problem solved easier
import collections                             #import collections module
def char_freq2(string):
    counter=collections.Counter(string)        #use the method collections.Counter() to get problem solved
    print(counter)
    return
    
    
    
#Problem 11: Implement an encoder/decoder of ROT-13
def encoder_decoder(string):
    """
     This funcrion is to transform a string into a new one following rule ROT-13.And the key for ROT-13 is represented
     in a dictionary defined in function
     
     Parameters:
     string - any kind of string.But note that here only encode or decode English letters with other characters 
              unchanged
    """
    key={'a':'n', 'b':'o', 'c':'p', 'd':'q', 'e':'r', 'f':'s', 'g':'t', 'h':'u', 
       'i':'v', 'j':'w', 'k':'x', 'l':'y', 'm':'z', 'n':'a', 'o':'b', 'p':'c', 
       'q':'d', 'r':'e', 's':'f', 't':'g', 'u':'h', 'v':'i', 'w':'j', 'x':'k',
       'y':'l', 'z':'m', 'A':'N', 'B':'O', 'C':'P', 'D':'Q', 'E':'R', 'F':'S', 
       'G':'T', 'H':'U', 'I':'V', 'J':'W', 'K':'X', 'L':'Y', 'M':'Z', 'N':'A', 
       'O':'B', 'P':'C', 'Q':'D', 'R':'E', 'S':'F', 'T':'G', 'U':'H', 'V':'I', 
       'W':'J', 'X':'K', 'Y':'L', 'Z':'M'}                                         #create key for translation matching
    
    newString=""                            #create an empty string to store the encoding or decoding result

    for c in string:                        #use 'for' loop to get each character in string
        if key.get(c)== None:               #check whether the current character has a corresponding one in dictionary,if not,
            newString=newString+c           #update the newString by adding it with no change
        else:                               #if it has been matched,update the newString by adding the corresponding letter
            newString=newString+key.get(c)
    return newString                        #return the final newString encoding or decoding result
    
    
    
#Problem 12:Spelling correction
import re                                            #re module, regular expression,used for matching pattern
def correct(string):
    """
     This function is to correct the input string in following way:
     1) two or more occurrences of the space of the space character is compressed into one, and 
     2)inserts an extra space after a period if the period is directly followed by a letter.
     
     Parameters:
     string - any kind of string
    """
    string=re.sub(r'( )+',' ',string)                  #substitute two or more space in the string with one space in the string
    string=re.sub(r'[.]([a-zA-Z])',r'. \1',string)     #search for pattern of "."+letter  
                                                       #and substitute the first group "." with ". "
    return string
    
    
    
#Problem 13:Transform a verb in infinitive form into its third person singular form
def make_3sg_form(verb):
    """
     This function is to transform a verb in infinitive form into its third person singular form following the rules:
      1) If the verb ends in y, remove it and add ies
      2) If the verb ends in o, ch, s, sh, x or z, add es
      3) By default just add s
     
     Parameters:
     verb - a string type that is a verb since this function cannot check verb or not itself but only do transformation 
            following a simple set of rules
    """
    if verb.endswith('y'):             #if the verb ends in y, remove it and add ies
        verb=verb[:-1]+'ies'
    elif verb.endswith('o'):           #if the verb ends in o, ch, s, sh, x or z, add es
        verb=verb+'es'
    elif verb.endswith('ch'):
        verb=verb+'es'
    elif verb.endswith('s'):
        verb=verb+'es'
    elif verb.endswith('sh'):
        verb=verb+'es'
    elif verb.endswith('x'):
        verb=verb+'es'
    elif verb.endswith('z'):
        verb=verb+'es'
    else:                              #by default just add s
        verb=verb+'s'
    return verb
    
    
    
#Problem 14:Transform a verb in infinitive form into the present participle
def is_vowel(l):
    """
     This function is to check a letter is a vowel or not, if it is,return True,False otherwise
     It will be called by function make_ing_form()
    """
    if l in ['a','e','i','o','u']:
        return True
    else:
        return False

## This function should return the corrected string instead of printing it - Prof G
def make_ing_form(verb):
    """
     This function is to get a present participle by adding the suffix -ing to the infinite form following a simple set
     of rules:
      1)If the verb ends in 'e', drop the 'e' and add 'ing' (if not exception:be,see, flee, knee, etc.)
      2)If the verb ends in 'ie', change 'ie' to 'y' and add 'ing'
      3)For words consisting of consonant-vowel-consonant, double the final letter before adding 'ing'
      4)By default just add 'ing'
      
      Parameters:
      verb - a string type that is a verb since this function cannot check verb or not itself but only do transformation 
            following a simple set of rules
      
    """
    if verb.endswith('ie'):                   #if the verb ends in 'ie', change 'ie' to 'y' and add 'ing'
        print(verb[:-2]+'ying')
    elif verb.endswith('ee')or len(verb)==2:  #if the verb ends with 'ee' or there are only 2 letters in the word
                                              #this is to exclude some simple exceptions such as be,see, flee, knee, etc.
        print(verb+'ing')                     #add 'ing' directly
    elif verb.endswith('e'):                  #if the verb ends in 'e', drop the 'e' and add 'ing'
        print(verb[:-1]+'ing')
    elif is_vowel(verb[-3])==False and is_vowel(verb[-2])==True and is_vowel(verb[-1])==False:
                #if the verb ends with a form of consonant-vowel-consonant,double the final letter and addi 'ing'
                #here use the function is_vowel() defined before to check whether vowel or not
        print(verb+verb[-1]+'ing')
    else:                                     #by default just add 'ing'
        print(verb+'ing')
    return

##Test Cases
help(histogram)
help(make_ing_form)

print("1 Histogram ", histogram([1,2,3,5,6,7,6,5,4,3,2,1]), '\n')

print("2 Max in List 77 ", max_in_list([1,2,3,77,4,5,6,7]), '\n')

print("3 word to length map 3,5,7,4 ", list_len(['dog', 'snake', 'dolphin', 'cats']), '\n')

print("4 Longest word 7 ", find_longest_word(['dog', 'snake', 'dolphin', 'cats']), '\n')

print("5 filter long words snake, dolphin ", filter_long_words(['dog', 'snake', 'dolphin', 'cats'],4), '\n')

print("6 Palindrome phrase TRUE ", phrase_palindrome("Go hang a salami I'm a lasagna hog."), '\n')

print("7 Pangram TRUE ", is_pangram("The quick brown fox jumps over the lazy dog."), '\n')

print("8 Cokes \n", verse(9))

# print("9 Translating to Swedish ['god', 'jul', 'gott'] ", translate(['merry', 'christmas', 'happy']), '\n')
print("9 Translating to Swedish ['god', 'jul', 'gott'] ", translate('merry christmas happy'), '\n')

print("10 Char Freq1 {'a': 7, 'c': 3, 'b': 14, 'e': 2, 'd': 3, 'g': 7, 'f': 3} ", char_freq1("agbbabgcbdbabdgbdbabageebabcbgcbffgfabg"), '\n')
print("10 Char Freq2 {'a': 7, 'c': 3, 'b': 14, 'e': 2, 'd': 3, 'g': 7, 'f': 3} ", char_freq2("agbbabgcbdbabdgbdbabageebabcbgcbffgfabg"), '\n')


print("11 Decoder Caesar cipher? I much prefer Caesar salad!", encoder_decoder("Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"), '\n')

print("12 correct This is very funny and cool. Indeed!", correct("This is very funny and cool.Indeed!"), '\n')

print("13 3ps brushes ", make_3sg_form("brush"), '\n')
print("13 3ps tries ", make_3sg_form("try"), '\n')
print("13 3ps runs ", make_3sg_form("run"), '\n')
print("13 3ps fixes ", make_3sg_form("fix"), '\n')

print("14 ing lying ", make_ing_form("lie"), '\n')
print("14 ing seeing ", make_ing_form("see"), '\n')
print("14 ing moving ", make_ing_form("move"), '\n')
print("14 ing hugging ", make_ing_form("hug"), '\n')