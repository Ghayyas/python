#In this Section we are going to learn about Sub class and SuperClass

#So what is mean by SuperClass??

#As you can see its Super Class which represent a class which is super. 
#super means any class which is big.

#So it means A big class or in others OtherWords Parent Class.

#Sub Class.

#sub means any thing which under an other. Means Class which is the of other class.

#lets Make Super and Sub class

class mySuperClass:
      var1 = 'this is my super class';
      var2 = 'Print from my Super class var2';
  
class mySubClass(mySuperClass):
    pass           #Remember The pass statement in Python is used when a statement is required syntactically but you do not want any command or code to execute.
                   #The pass statement is a null operation; 
                   # nothing happens when it executes  
                   
printClass = mySubClass();

print printClass.var1;  #Printing from super class








#Change Variable in subClass



class parentClass:
    var1 = 'Abeera';
    var2 = 'farheen';
    
class childClass:
    var2 = 'saba';   #Replace Farheen with saba

printClass = childClass();

print printClass.var2;    #Prints Saba.