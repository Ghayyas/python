#let talk about methods

#for Example

#lets start with count

# we Have items in our list and we want to count how many times items repeated there

#to do this

myList = [1,2,3,4,5];

print myList.count(2);  # prints 1 beacuse only 1 times 2 is repeated in list



#lets find the length of list

print len(myList);  #prints 5 beacuse 5 items in the list


#let say we have two list and we want to concate them 

# how to do this on python

myFirstItem = ['Hello','My','name'];
mySecondItem = ['is','Ghayyas'];

#lets print First and second items
print myFirstItem;
print mySecondItem;  

#it prints the values on the list

#now Concate them.
myFirstItem.extend(mySecondItem);

print myFirstItem;  #successfully Concated


#lets find index of selected items;

indexIs = myFirstItem.index('is');

print indexIs;


#lets insert something in any where in array

myFirstItem.insert(2,'hle');

print myFirstItem;  #replace the 2 index of list is hle

#let pop the 2 index item in this list

myFirstItem.pop(2);

print myFirstItem;  # so its remove hle from array

#lets try remove method 

myFirstItem.remove('is');

print myFirstItem;  # it remove is from list;

#lets Reverse our list

myFirstItem.reverse();  

print myFirstItem;   ### successfully reverse :)