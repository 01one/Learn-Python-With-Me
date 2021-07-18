x="Hello"

x=x.lower()
print(x)    #hello

x=x.upper()
print(x)    #HELLO

a = x.count('L')
print(a)    #2

b=x.index('O')
print(b)    #4

x=x.replace('L','l')
print(x)    #HEllO

#string is immutable.
x=x[:]+" world"
print(x)    #HEllO world

a=len(x)
print(a)  #4
