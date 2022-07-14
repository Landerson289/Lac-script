###This is the interpreter###



f=open("code.txt","r")#The code
lines=f.read().splitlines()#Split it line by line
keywords=["print","if","else","is","isnum","add","num","str","mult","equals","sub","div"]#All the keywords
variables={}#Dictionary of variables
numbers={}
conditions=[]#List of conditions
skip=False#Whether of not to skip at line (because it is in an if statement)



class line:
  def __init__(self,words,skip):
    self.words=words#The list of the line's words
    self.skip=skip#Whether of not the line should be skipped
    self.value="Null"#The returned value of the line
  #interpret print
  def iprint(self):
    for i in range(1,len(self.words)):#print everything on the line except the print statment
      if self.words[i][0]=="@":#if it is a variable
        index=self.words[i].replace("@","")
        print(variables[index],end=" ")#Print its value
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
    #print(self.words[pos],keywords[9])
    if self.words[pos]==keywords[9]:#If there is a condition
      if str(self.words[pos-1])[0]=="@":#If it is a variable/numuber
        #print(self.words)
        index=self.words[pos-1].replace("@","")#Get the variable's/number's name
        if index in varnames:#If it is a variable
          cond1=variables[index]#Get its value
        elif index in numnames:#If it is a number
          cond1=numbers[index]#Get its value
        else:#If it is neither
          print("VARIABLE:",index,"not found")#Error message
          exit()
      else:#If it is not a variable
        cond1=self.words[pos-1]#Use it
      if words[pos+1][0]=="@":#Same again
        index=words[pos+1].replace("@","")
        if index in varnames:
          cond2=variables[index]
        elif index in numnames:
          cond2=numbers[index]
        else:
          print("VARIABLE:",index,"not found")
      else:
        cond2=self.words[pos+1]
      #print(cond1,cond2)
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

    ###CHECKING FOR COMMENTS
    comment=False#Whether or not it is a comment
    newline=[]#The new line with out the comment
    for i in self.words:#Check all the words
      word=""#The new word
      for j in str(i):#Check all the letters
        if j=="#" and comment==False:#If there is a hashtag and it was not a comment
          comment=True#Make it a comment
        elif j=="#" and comment==True:#Otherwise
          comment=False#Turn off the comment
        elif comment==False:#If it is not a comment
          if j!="#":#Bug fix
            word+=j#Add it to the new word
      newline.append(word)#Add the word to the line
    i=0
    while i<len(newline):
      if newline[i]=="":#If there is nothing there
        newline.pop(i)#Get rid of it
        i=-1#Go back to the start in case anything has been missed by reindexing
      i+=1#Check the next one
    self.words=newline

    ###CHECKING FOR BRACKETS###
    skip=True#Should it be skipped (not the if skip)
    section=[]#The new mimi-line that will have its values returned
    indexes=[]#The part of the line in the section.
    i=0
    while i< len(self.words):#Check all the words
      #print(self.words,section)
      #print(self.words,section,indexes)
      if len(str(self.words[i]))>0:#If the word is something
        if str(self.words[i])[0]=="(":#If there is an opening bracket
          skip=False#Do not skip it
          indexes.append(i)#Add the position to this list
          self.words[i]=self.words[i].replace("(","")#Get rid of the bracket
          section.append(self.words[i])#Add the word to the 
        elif str(self.words[i])[-1]==")":#If it is the end of the section
          skip=True#Start skipping again
          indexes.append(i)#Add the end value
          
          self.words[i]=self.words[i].replace(")","")#Get rid of the bracket
          section.append(self.words[i])#Add the word to the list
          
          if len(section)>0:#Error check
            brackets=line(section,False)#Create a line class
            brackets.interpret()#interpret the line
            returned=brackets.value#The value is the value returned
            for j in range(indexes[0],indexes[1]):
              self.words.pop(j)#Remove the section
            self.words[indexes[0]]=returned#Put the value in its place

            i=0#Go back and check
        elif skip==False:
          section.append(self.words[i])
      i+=1

  
      
  def ivar(self):
    variables[self.words[0]]=""
    for i in range(2,len(self.words)):
      variables[self.words[0]]+=self.words[i]+" "#Create a variable with the name and value
  

  def inum(self):
    numbers[self.words[0]]=int(self.words[2])#Create a variable with type num
  def iadd(self,pos):
    sum=0#The sum
    for i in range(pos+1,len(self.words)):#Loop through all the values
      if str(self.words[i])[0]!="@":#If it is a not variable
        sum+=int(self.words[i])#Add it to the sum
      else:#IF it is a variable
        index=self.words[i].replace("@","")#Get the name
        sum+=numbers[index]#Get the value and add it to the sum
    return sum
  def isub(self,pos):#Change
    sub=0#The running value
    if self.words[pos+1][0]!="@":#If it is not a varialbe
      sub=int(self.words[pos+1])#Add it to the total
    else:
      index=self.words[pos+1].replace("@","")#Get the name
      sub=numbers[index]#Get the value
    for i in range(pos+2,len(self.words)):#Loop through the rest of the values
      if self.words[i][0]!="@":#Same with subtraction
        sub-=int(self.words[i])
      else:
        index=self.words[i].replace("@","")
        sub-=numbers[index]
    return sub
  def imult(self,pos):
    #Same as addition and subtraction but with multiplicion
    prod=1
    for i in range(pos+1,len(self.words)):
      if words[i][0]!="@":
        prod= prod*int(self.words[i])
      else:
        index=self.words[i].replace("@","")
        prod=prod*numbers[index]
    return prod
  def idiv(self,pos):
    #Same as addition and subtraction but with division
    div=0
    if self.words[pos+1][0]!="@":
      div=int(self.words[pos+1])
    else:
      index=self.words[pos+1].replace("@","")
      div=numbers[index]
    for i in range(pos+2,len(self.words)):
      #print(self.words)
      if self.words[i][0]!="@":
        div=div/int(self.words[i])
      else:
        index=self.words[i].replace("@","")
        div=div/numbers[index]
    return div
  def strTOnum(self):
    index=self.words[1].replace("@","")#Get the name
    variables[index]=numbers[index]#Add it to the other list
    numbers.pop(index)#Delete it from the old list
  def interpret(self):
    self.check()#Check for comments
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
          elif self.words[2].lower()==keywords[10]:#minus numbers
            index=self.words[0].replace("@","")
            numbers[index]=self.isub(2)  
          elif self.words[2].lower()==keywords[11]:#divide numbers
            index=self.words[0].replace("@","")
            numbers[index]=self.idiv(2)  
          else:
            self.inum()
        elif self.words[0].lower()==keywords[6] and self.words[2]==keywords[7]:
          self.strTOnum()
    #print(words,self.skip)
        elif self.words[0].lower()==keywords[5]:
          self.value=self.iadd(0)
        elif self.words[0].lower()==keywords[8]:
          self.value=self.imult(0)
        elif self.words[0].lower()==keywords[10]:
          self.value=self.isub(0)
        elif self.words[0].lower()==keywords[11]:
          self.value=self.idiv(0)
    #print(self.value)     
    return self.skip

i=0#Line number Off by one error from the line number if the code file
while i<len(lines):#Line by line interpreted
  words=lines[i].split(" ")#Split the line into words
  lineI=line(words,skip)
  skip=lineI.interpret()
  i+=1
