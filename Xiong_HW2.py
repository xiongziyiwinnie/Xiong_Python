#HW2 for Course MATH 510
#Instructor:Professor G

## Excellent documentation.

#Problem 1: Prints out the Fibonacci numbers
def fib(n):
    """
    This is a function that prints out all the Fibonacci numbers less than a taken value n

     Parameters:
     n - any non-negative real number
    """
    a=0                   #assigns the first two Fibonacci numbers to variables a,b
    b=1                   #set a=0,b=1
    while a<n:            #set the condition for the loop to run on, that is a<n
       print(a)           #each time store the next Fibonacci number in variable a and ptints out
       a=b
       b=a+b
    return


#Problem 2:Provide the larger one of two numbers
def mymax(m,n):
    """
    This is a function that compares two numbers input by outsiders and then returns the larger one;
  
    Parameters:
    m - any comparable number,integer,float,and so on
    n - any comparable number,integer,float,and so on
    """
    if m<n:              #uses if-then-else to consider on 3 senarios,>,==,<
       return n          #on each judgement,return the larger one
    elif m==n:                         #when they are the same, instead of returning a number
       return('they are the same')     #gives out a word to indicate they are the same
    else:
       return m
       
       
#Problem 3:Provide the largest one of three numbers
def max_of_three(n1,n2,n3):
    """
     This is a function that compares three numbers input by outsiders and then returns the larger one
  
     Parameters:
     n1 - any comparable number,integer,float,and so on
     n2 - any comparable number,integer,float,and so on
     n3 - any comparable number,integer,float,and so on
    """
    if (n1>n2) and (n1>n3):            #compare n1, n2 and n3, if n1 is larger than the rest two, output n1
        max=n1
    elif (n2>n1) and (n2>n3):          #compare n1, n2 and n3, if n2 is larger than the rest two, output n2
        max=n2
    else:                              #the first two senarios are both false and then n3 is the largest and output
        max=n3
    return max
    
  
#Problem 4:Computes the length of a given list or string.
def mylen(x):
    """
     This is a function that counts the characters in a given list or string and then return the number
 
     Parameters:
     x - any list of numbers or strings,e.g [1,2,3,4,5],['a','b','c',d'],'abcde','12345'
    """
    num=0               #stores the counting number in variable num and assigns an initial value of 0 to num
    for item in x:      #iterates the items in given x
     num=num+1          #on each iteration the counting number will increase by 1
    return num          #when loop ends the value stored in num is the number of characters,that is lenth of input list or string


#Problem 5:Judges letter as vowel or not
def vowel(m):
    """
     This function decides whether a given letter is vowel or not
 
     Parameters:
     m - any letter in lower or capital case
    """
    vowel=False                                          #create a flag with default value False
    list=['a','e','i','o','u','A','E','I','O','U']       #create a list that consists of all vowels in both lower and capital cases  
    if m in list:                                        #check if the given letter m is in the vowel list
        vowel=True                                       #if it is, set the flag to True
    return vowel                                         #return the flag
    
    
#Problem 6:Translate a text into "rövarspråket"

## Nice implementation!
def translate(s):
    """
    This function doubles every consonant in a text and place an occurrence of "o" in between
 
    Parameter:
    s - any string consisting of letters,best all in lower cases
    """
    new=list(s)                                          #change the given string into a list and store it in a variable new
    consonant=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','z']
                                                         #create a list that consists all the consonants in lower cases(but the list 
                                                         #can be extended into one with both lower and capital cases in
                                                         
    for i,c in enumerate(new):                           #get the index and element of each item in the list new
      if c in consonant:                                 #decide whether the current element is consonant or not
        new[i]=c+'o'+c                                   #if it is, change the element into a string of element+'o'+element
    return ''.join(new)                                  #join the modified list new
    

#Problem 7:Sum and multiply all numbers in a list
def sum(n): 
    """
     This function sums up all the numbers in a list
 
     Parameter:
     n - any list consisting of numbers
    """
    sum=0                                                #create a variable sum to store the summation result with initial value 0 
    for x in n:                                          #get each number's value in the given list
      sum=sum+x                                          #update sum by adding the current number
    return sum                                           #return the final summation result



def multiply(m):
    """
     This function multiplies all the numbers in a given list
 
     Parameter:
     m - any list consisting of numbers
     """

    mul=1                                                #create a variable mul to store the production with initial value 1
    for y in m:                                          #get each number's value in the given list
       mul=mul*y                                         #update mul by multiplying the current number
    return mul                                           #return the final production
    
    
#Problem 8:Get the reversal of a string
def reverse(s):
    """
     This function is to return the reversal of a given string
 
     Parameter:
     s - any kind of string
    """
    new=s[::-1]                                          #generate a string new that copies the given string from the ending to the 
                                                         #beginning,setting step=-1
    return new                                           #return the reversal
    

#Problem 9:Recognize palindromes
def is_palindrome(w):
    """
     This function recognizes a string,i.e, a word that looks the same if written backwards
 
     Parameter:
     w - any kind of string
    """
    r=w[::-1]                                            #generate a string r that is the reversal of the given one
    if r==w:                                             #if the reversal and the original are the same,return True
       return True
    else:                                                #otherwise return False
       return False


#Problem 10:Recognize membership
def is_member(x,a):
    """
     This function decides whether a value x is in the list of values a and returns True if x is a member of a, False otherwise.
 
     Parameters:
     x - a input number,string,etc
     a - a input list of numbers,strings,etc
    """
    flag=False                                          #create a flag with default False
    if x in a:                                          #check whether x is in the list a or not
     flag=True                                          #if it is, set the variable flag to True
    return flag                                         
    
    
    
#Problem 11:Check overlapping of two lists
## This logic does not work properly
def overlapping(m,n):
    """
     This function checks whether the two input lists have at least one element in common. If yes,return True,False otherwise.
 
     Parameters:
     m - any list consists of numbers,strings,etc
     n - any list consists of numbers,strings,etc
    """
    flag=False                                           #create a flag with default False
    for c in m:                                          #get each element in m
        if c in n:                                       #check the element in m is in the other list n or not
          flag=True                                      #if yes, set flag to True and end the loop,otherwise move on
        break
    return flag                                          #return True or False
    
    
#Problem 12:Generate n characters
def generate_n_chars(n,c):
    """
    This function generates a string consisting of the same chars with the number of length n and char c set by input
 
    Parameters:
    n - any positive integer
    c - any kind of character
    """
    str=c                                               #generate a variable str with the initial value of c taken by function                                           
    i=1                                                 #create a counter with initial value of 1
    while i<n:                                          #as long as i is less than n,add character c to str 
      str=str+c                                                                     
      i=i+1                                             #then i increases by 1,in that way i acts as a counter for the number of char
                                                        #in the current str
    return str                                          #once i==n,loop ends and return updated str
    
##TEST CASES

print('#1\n')
fib(500)
print('\n')

print('#2\n')
print(mymax(45,987), '\n')

print('#3\n')
print(max_of_three(3,4,5),'\n')

print('#4\n')
print(mylen('Gerhard'))
print(mylen([1,2,3,4,5,6,7]))
print('\n')

print('#5\n')
print(vowel('e'))
print(vowel('H'))
print('\n')

print('#6\n')
print(translate("this is fun"))
print(translate('aeiou'))
print(translate('YYYYYYY'))
print(translate("mmmmmm"))
print('\n')

print('#7\n')
print(sum([1,2,3,4,5]))
print('\n')

print('#8\n')
print(multiply([0,1,2,3]))
print(multiply([1,2,3,4]))
print('\n')

print('#9\n')
print(reverse("gnitset ma I"))
print('\n')

print('#10\n')
print(is_palindrome('radar'))
print(is_palindrome('Gerhard'))
print('\n')

print('#11\n')
print(is_member('dog', ['cat', 'dog', 'zebra']))
print(is_member(3, [1,2,3,4]))
print(is_member(3, [5,6,7]))
print('\n')

print('#12\n')
print(overlapping([1,2,3], [3,4,5]))
print(overlapping([1,2,3], [6,4,5]))
print('\n')

print('#13\n')
print(generate_n_chars(7, 'g'))