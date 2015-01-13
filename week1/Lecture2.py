print type(3)
print type(3.0)
print type(True)
print 3**2
print float(3)
print int(3.9)
print 2.1**2.0
pi=3.14159
radius=11.2
area=pi*radius**2
print area
print type("hello")
print type('hello')
print "hello"*3
print "hello"+"world"
print "hello"+str(radius)
print len('hello')
print 'abc'[0]
print 'abc'[-1]
print 'abc'[1:3]
y=float(raw_input("Enter a number: "))
print (y*y)
#comment
x=int(raw_input("Enter an integer: "))
if x%2==0:
    print 'Even'
else:
    print 'Odd'
if y==x:
    print str(x)+" is equal to "+str(y)
elif y%2==0 and x%2==0:
    print 'both '+str(x)+' and '+str(y)+' are even'