#In this section we are going to start Object Oriented Programing in Python

#lets Just Make Hello world with Class


class HelloWorld:
      value = 'hello world this is my first program in Python OOP'
      
myWorld = HelloWorld();

print myWorld.value;      #Prints Value in class


myList = [3,4,7,5,6];

class assendingOrder:
      
      def makeAssending(self):
      
          return sorted(myList);

assendingOrderClass= assendingOrder();

ac = assendingOrderClass.makeAssending();

print ac;  #prints it in assendingOrder;

#Now makes in Decending order

reverseList = [4,5,234,6,67,345,4,8,9,2,4];

class dessendingOrderClass:
       def makeDessending(self):
            reverseList.sort(reverse=True);
            return reverseList;
dessendingOrder = dessendingOrderClass();

decend = dessendingOrder.makeDessending();

print decend;           