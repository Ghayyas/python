# In this section we are going to learn if statement
#Remember Indentation is very important other wise you will get error



checkThis = 'hello';

if checkThis == 'hello':
   print 'This is true';  #Prints this is true

#if with else

myVar = 'python is snake';

if myVar == 'python is snakes':
   print 'python is snakes'
   
elif myVar == 'python':
     print 'python';
elif myVar == myVar:

    print 'elif works python'+ " "+ myVar;  #Else if works
else:
    print 'nothing works';       
    
#lets play with this

userPrompt = raw_input('What is your Name: '); 

if(userPrompt== 'ghayyas'):
  print 'Hello Ghayyas Wellcome';
elif userPrompt == '':
  print 'empty value';
elif userPrompt == 'not defined':
  print 'Undefined value';
else:
     print 'sorry you are not ghayyas';   
     
#Nested if else statement

promptme = input('Enter any value: ');

if promptme == 1:
   secPrompt = input('Enter Second Value: ');
   incrementBoth = promptme + secPrompt;
   print 'Incremanting value is '+ str(incrementBoth);
else: 
   print 'value is not 1';        