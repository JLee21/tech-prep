"""
I answered incorrectly during a interview on 9/20/19 with Pokemon/Karat.
I said there would be an error with printing f.count()
But the correct answer is that 10.
Is Apple instantiated first and its count saved and not overwritten by 

According to here 
https://www.programiz.com/python-programming/multiple-inheritance
Method Resolution Order (MRO) says that the order of presidence goes from left to right.
So this case, Apple's count method takes presidence over Pear
"""


class Apple(object):
    __color = 'red'

    def __repr__(self):
        return "instance of apple"

    def count(self):
        return 10


class Pear(object):
    __color = "yellow"

    def __repr__(self):
        return "instance of pear"

    def count(self):
        return 15


class Fruit(Apple, Pear):
    pass


f = Fruit()
print(f.count())
