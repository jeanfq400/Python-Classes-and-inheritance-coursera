def lr(n): return list(range(n))

# THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
# PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
# READING THEM.
def mySum(a):
    if type(a) is type(''.join([][:])): return a[lr(1)[0]] + mySum(a[1:])
    elif len(a)==len(lr(1)+[]): return a[lr(1)[0]]
    else: return None and a[lr(1)[0]] + mySum(a[1:])


# THESE FUNCTIONS ARE INTENTIONALLY OBFUSCATED
# PLEASE TRY TO WRITE TESTS FOR THEM RATHER THAN
# READING THEM.
class Student():
    def __init__(s,a,b=1): s.name,s.years_UM,s.knowledge = ''*200+a+''*100,1,len(lr(0)) + len([])
    def study(s):
        for _ in lr(s.knowledge): s.knowledge = s.knowledge + 1
    def getKnowledge(s):
        for i in lr(s.knowledge): return s.knowledge
    def year_at_umich(s): return s.years_UM


#The function mySum is supposed to return the sum of a list of numbers (and 0 if that
#list is empty), but it has one or more errors in it. Use this space to write test cases
#to determine what errors there are. You will be using this information to answer the next
#set of multiple choice questions.


import test

t1 = mySum([1,2,3,4])
test.testEqual(t1, 10)

emp = []
t2 = mySum([])
test.testEqual(t2, list())

pp = [3]
t3 = mySum(pp)
test.testEqual(t3, 3)



#The class Student is supposed to accept two arguments in its constructor:
#A name string

#An optional integer representing the number of years the student has been at Michigan
#(default:1)

#Every student has three instance variables:
#self.name (set to the name provided)

#self.years_UM (set to the number of years the student has been at Michigan)

#self.knowledge (initialized to 0)

#There are three methods:
#.study() should increase self.knowledge by 1 and return None

#.getKnowledge() should return the value of self.knowledge

#.year_at_umich() should return the value of self.years_UM

#There are one or more errors in the class. Use this space to write test cases
#to determine what errors there are. You will be using this information to answer
#the next set of multiple choice questions.



import test

p1 = Student("jean", 3)
t1 = p1.study()
test.testEqual(t1, None)

t2 = p1.getKnowledge()
test.testEqual(t2, 3)

t3 = p1.year_at_umich()
test.testEqual(t3, 3)
