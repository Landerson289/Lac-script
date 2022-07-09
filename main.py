###This is the interpreter###



f=open("code.txt","r")#The code
lines=f.read().splitlines()#Split it line by line
keywords=["print","if","else","is","isnum","add","num","str","mult"]#All the keywords
variables={}#Dictionary of variables
numbers={}
conditions=[]#List of conditions
skip=False#Whether of not to skip at line (because it is in an if statement)



class line:
  def __init__(self,words,skip):
    self.words=words
    self.skip=skip
  #interpret print
  def iprint(self):
    for i in range(1,len(self.words)):#print everything on the line except the print statment
      if self.words[i][0]=="@":
        index=self.words[i].replace("@","")
        print(variables[index],end=" ")
      else:
        if self.words[i]=="" or self.words[i]==" ": #Bug fix
          print(self.words[i], end="")
        else:
          print(self.words[i], end=" ")#Print it with a space at the end
    print("")#New line
  
  #interpret if
  def iif(self):
    conditions.append(self.icondit(2))#Add the condition to the list
    if conditions[-1]==False:#If the conditioin is false
      self.skip=True#Skip the upcoming lines
  
  def ielse(self):
    if conditions[-1]==False:#If the condition is false
      self.skip=False#Unskip
    else:#Otherwise
      self.skip=True#Skip
  #See if a condition is true or false
  def icondit(self,pos):
    varnames=variables.keys()#list of variable names
    numnames=numbers.keys()#list of numbers
    if words[pos]=="=":#If there is an equals sign
      if words[pos-1][0]=="@":#If it is a variable/numuber
        index=words[pos-1].replace("@","")#Get the variable's/number's name
        if index in varnames:#If it is a variable
          cond1=variables[index]#Get its value
        elif index in numnames:#If it is a number
          cond1=numbers[index]#Get its value
        else:#If it is neither
          print("VARIABLE:",index,"not found")#Error message
      else:#If it is not a variable
        cond1=words[pos-1]#Use it
      if words[pos+1][0]=="@":#Same againn
        index=words[pos+1].replace("@","")
        if index in varnames:
          cond2=variables[index]
        elif index in numnames:
          cond2=numbers[index]
        else:
          print("VARIABLE:",index,"not found")
      else:
        cond2=words[pos+1]
      if cond1==cond2:#If they are the same
        return True#Condition is true
      else:
        return False
    else:#if true { #or similar
      #Dummy code
      condition=self.words[1]
      if condition=="True":
        condition=True
      else:
        condition=False
      return condition

  #Check for comments and other stuff later on/
  def check(self):
    comment=False#Whether or not it is a comment
    line=[]#The new line with out the comment
    for i in self.words:#Check all the words
      word=""#The new word
      for j in i:#Check all the letters
        if j=="#" and comment==False:#If there is a hashtag and it was not a comment
          comment=True#Make it a comment
        elif j=="#" and comment==True:#Otherwise
          comment=False#Turn off the comment
        if comment==False:#If it is not a comment
          if j!="#":#Bug fix
            word+=j#Add it to the new word
      line.append(word)#Add the word to the line
    #print(line)
    #print("line",line)
    #print(line)
    i=0
    while i<len(line):
      #print(line[i]=="",line[i])
      if line[i]=="":#If there is nothing there
        line.pop(i)#Get rid of it
        i=-1#Go back to the start in case anything has been missed by reindexing
      i+=1#Check the next one
    return line#Return the commentless line
  
  def ivar(self):
    variables[self.words[0]]=self.words[2]
    #print(variables)
  

  def inum(self):
    #print(self.words[2])
    numbers[self.words[0]]=int(self.words[2])
  def iadd(self,pos):
    sum=0
    for i in range(pos+1,len(self.words)):
      if words[i][0]!="@":
        sum+=int(self.words[i])
      else:
        index=self.words[i].replace("@","")
        sum+=numbers[index]
    return sum
  def imult(self,pos):
    prod=1
    for i in range(pos+1,len(self.words)):
      if words[i][0]!="@":
        prod= prod*int(self.words[i])
      else:
        index=self.words[i].replace("@","")
        prod=prod*numbers[index]
    return prod
  def strTOnum(self):
    index=self.words[1].replace("@","")
    variables[index]=numbers[index]
    numbers.pop(index)
  def interpret(self):
    self.words=self.check()#Check for comments
    #print(conditions,words,skip)
    #print(skip)
    if self.skip==True:#If you are skipping this line
      if self.words[0]=="}":#If this is the end of an 'indent'
        if len(conditions)>0:#Error checking
          if conditions[-1]==False:#If the latest condition is false
            if len(self.words)>1:#Error checking
              if self.words[1]==keywords[2]:#If it is an else statement
                self.skip=False#Do not skip it
                conditions.pop()#Delete the condition
        else:
          pass#Error statement
      if self.words[0].lower()==keywords[1]:#if it is an if statement
        conditions.append("Filler")#The code will not be run
      elif self.words[0].lower()=="}" and len(self.words)==1:#If it is the end of the if/else statement
        if len(conditions)>0:#Error checking
          conditions.pop()#Delete the condition
    elif self.skip==False:#If you are not going to skip the line
      if len(self.words)>1:#Error checking
        if self.words[0].lower()==keywords[0]:#See if its a print statement
          self.iprint()#print
        elif self.words[0].lower()==keywords[1]:#See if its an if statement
          self.iif()
        elif self.words[1].lower()==keywords[2]:#If it is an else statement
          self.ielse()
        elif self.words[0]=="}" and len(self.words)==1:#If it is the end
          conditions.pop()#delete the condition
        elif self.words[1].lower()==keywords[3]:#If they are assigning a variable
          self.ivar()#Assign the variable
        elif self.words[1].lower()==keywords[4]:#If they are assigning a number
          if self.words[2].lower()==keywords[5]:#add numbers 
            index=self.words[0].replace("@","")
            numbers[index]=self.iadd(2)
          elif self.words[2].lower()==keywords[8]:#times numbers 
            index=self.words[0].replace("@","")
            numbers[index]=self.imult(2)
            
          else:
            self.inum()
        elif self.words[0].lower()==keywords[6] and self.words[2]==keywords[7]:
          self.strTOnum()
    #print(words,self.skip)
    return self.skip

i=0#Line number Off by one error from the line number if the code file
while i<len(lines):#Line by line interpreted
  words=lines[i].split(" ")#Split the line into words
  lineI=line(words,skip)
  skip=lineI.interpret()
  i+=1
