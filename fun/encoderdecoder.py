def encode(string):
    return (string[::-1][0::2]+string[::-1][1::2])[::-1]
def decode(string):
    result=""
    string=string[::-1]
    lasthalf=string[len(string)/2:]
    firsthalf=string[:len(string)/2]
    for x in range(0,len(firsthalf)):
        result+=firsthalf[x]
        result+=lasthalf[x]
    return result[::-1]
print 'Type e to exit'
print 'If there is an odd amount of letters type (space) before your encoded phrase'
while True:
    string=str(raw_input('What phrase do you want to encode/decode? '))
    if string=='e':
        break
    length=len(string)
    if length%2==1:
        string+=' '
    print '\nEncoded: '+encode(string)
    print 'Decoded: '+decode(string)
    print 'The amount of letters are '+str(length)+"\n"
print 'Thank you for using this program'