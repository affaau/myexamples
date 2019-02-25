# Python 3

x = '֧'
y = 'abc'
with open('unicode_nonlatin.txt','w') as f:
    f.write(y)

with open('encode_nonlatin.txt', 'wb') as f:
    f.write(x.encode())

#with open('encode_nonlatin.txt', 'rb') as f:
    #print(f.read.decode())   # not working?!

with open('encode_nonlatin.txt', 'r') as f:
    print(f.read())

