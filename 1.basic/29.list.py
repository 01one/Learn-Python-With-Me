x=[1,2,3,4,5]  #list
print(x)    #[1,2,3,4,5]
print(x[0]) #1

print(x[:]) #[1,2,3,4,5]

x[0]=2
print(x)    #[2,2,3,4,5]

x.pop(4)
print(x)    #[2,2,3,4] #remove item at index 4

x.append(7)
print(x)    #[2,2,3,4,7] #add item at the end of the list

x.insert(3,20)
print(x)    #[2,2,3,20,4,7] #insert item 20 at index 3

#   index starts from 0  
#   Index 4 means 5th item.
#   [0,1,2,3,4] In this example there is 4 at index 5
