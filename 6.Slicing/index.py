# So what is slicing? let say you have number of array or sequence or list. and you want to sort it out.
# To do this you need slicing.

# for example


abc = [0,1,2,3];
print abc;   #prints the list.

myList = ['My','Name','is','Ghayyas'];

print myList[:3]; # prints My name is

print myList[1:2]; #only Prints Name

print myList[-2:-1]; #only prints is

print myList[-2:1]; #empty Array

print myList[0:1];  #print My

print myList[-1]; #prints Ghayyas

print myList[-4:-1];  #print My name is;


print myList[0:4:2]; #prints my and is;

print myList[::2] #prints my and is;


#let split the string in array;

name = 'Ghayyas';

print list(name);

#lets find out if there is x in name;

print 'x' in name;  # return false;

#lets delete s in name;

convertStringNameInList = list(name);

del convertStringNameInList[6];

print convertStringNameInList; # S is delete

print 'x' in convertStringNameInList; # returns false

#lets add s in convertStringNameInList

addItem = convertStringNameInList.append('s');

print convertStringNameInList;  #returns ghayyas;


#lets add an item in middle of the list

addNewItem  = convertStringNameInList[3:3] = 'hello';
print convertStringNameInList;  #prints hello in middle of array


