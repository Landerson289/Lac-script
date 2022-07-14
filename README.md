# Lac-script
A high level programming language that lacks severly in several departments.

Syntax:
  print statments are shown below:
  
    print This is what I want printed

  comments are shown below:
  
    print This is what I want printed #comment
    
    print This is what I #comment# want printed
    
    print This i#comment#s what I want printed

  if/else statements are shown below:
  
    if condition {
    
    print this is what is shown if it is true
    
    } else {
    
    print this is what is shown if it is false
    
    }

  variables are defined as shown below:
  
    name is value
  variables are referred to as shown below:
  
    print @name
    
  numbers are defined as shown below:
  
    name isnum value
   
   numbers are referred to as shown below:
   
    func @name
  
   To do a mathmatical operation, use one of the keywords, "add","sub","mult","div" as shown below.
   
    sum isnum keyword @name1 @name1
    sum isnum keyword number number
    
   Addition and multiplication are the same regardless of the order
   With subtraction the order is as below:
   
    sub @var1 @var2 @var3
    
   corresponds to:
   
    @var1-@var2-@var3
    
   and with division:
   
    div @Var1 @var2 @var3
   
   corresponds to:
   
    (@var1/@var2)/@var3
   
   numbers can be converted to strings as shown below:
   
    num name str
   
   numbers can not be printed and must be converted to strings first
   
   comparisions can be made as shown below:
   
    @name1 equals @name2
   
   brackets can be used to get a value from a section of the code that can be used in the code.
   
    @var1 equals (add @var1 @var2)
    
   
