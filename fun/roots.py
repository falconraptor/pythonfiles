def findHalf(a,b):
    return (a+b)/2.0
def findRoot(g,a,b,n,num):
    while True:
        if abs((g**n)-num)<.0001:
            break
        elif g**n>num:
            b=g
        elif g**n<num:
            a=g
        g=findHalf(a,b)
        #print "a="+str(a)+" b="+str(b)+" g="+str(g)+" g^"+str(n)+"="+str(g**n)+" abs(g^n-num)="+str(abs(g**n-num))
    return g
while True:
    n=int(raw_input("To find the nth root, n=? "))
    num=float(raw_input("What number would you like the find the "+str(n)+"th root of? "))
    a=b=g=0
    g=findHalf(a,num)
    b=num
    result=findRoot(g,a,b,n,num)
    print "The "+str(n)+"th root of "+str(num)+" is "+str(result)+"\n"
    answer=str(raw_input("Would you like to do another? "))
    if answer=='no' or answer=='No' or answer=='NO' or answer=='n' or answer=='N':
        break
    else:
        print ''