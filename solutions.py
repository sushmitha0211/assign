
'''
# 1 => Define a function that can accept two strings as input and print the string with maximum length in console.
#  If two strings have the same length, then the function should print all strings line by line.
str1 = raw_input("enter the  string :")
str2 = raw_input("enter the second string:")


def func1(str1, str2):
       if len(str1) == len(str2):
            print str1
            print str2
       elif len(str1) > len(str2):
            print str1
       else:
            print str2

func1(str1,str2)

# 2 )Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
#  Then the function needs to print all values except the first 5 elements in the list.


def squares():
    l=list()

    for i in range(1,21):
        l.append(i**2)
    print(l[:5])

squares()

# 3) Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area

class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14


Circle = Circle(2)
print Circle.area()


# 4)  Write a program that accepts a sequence of whitespace separated words as input and
#  prints the words after removing all duplicate words and sorting them alphanumerically.

'''

seq = raw_input("enter the white space seperated by words:")

words = [word for word in seq.split(" ")]
print " ".join(sorted(list(set(words))))

# 5) Write a program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".

s = raw_input()
if s == "yes" or s == "YES" or s == "Yes":
    print "Yes"
else:
    print "No"

#6) Define a function which can generate a dictionary where the keys are numbers between 1 and 20 (both included) and the values are square of keys. The function should just print the keys only.

def newdict():
    d = dict()
    for i in range(1, 21):
        d[i] = i ** 2
    for k in d.keys():
        print k


newdict()

# 7)Use a list comprehension to square each odd number in a list. The list is input by a sequence of comma-separated numbers.

number = raw_input()
numbers = [x for x in number.split(",") if int(x)%2!=0]
print ",".join(numbers)

# 8) Define a class named Circle which can be constructed by a radius. The Circle class has a method which can compute the area.


class Circle(object):
     def __init__(self, r):
         self.radius = r

     def area(self):
         return self.radius**2*3.14

NewCircle = Circle(6)
print NewCircle.area()

# 9 ) Define a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.

def gen(n):
    i = 0
    while i < n:
        j = i
        i = i+1
        if j%7==0:
            yield j
gen(15)

 #10) Write a program which accepts a sequence of words separated by whitespace as input to print the words composed of digits only.

import re
s = raw_input()
print re.findall("\d+",s)













