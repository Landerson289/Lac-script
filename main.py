###This is the interpreter###



f=open("code.txt","r")#The code
lines=f.read().splitlines()#Split it line by line
keywords=["print","if","else","is"]#All the keywords
variables={}
conditions=[]

#interpret print
def iprint(words):
  for i in range(1,len(words)):#print everything on the line except the print statment
    if words[i][0]=="@":
      index=words[i].replace("@","")
      print(variables[index],end=" ")
    else:
      if words[i]=="" or words[i]==" ": #Bug fix
        print(words[i], end="")
      else:
        print(words[i], end=" ")#Print it with a space at the end
  print("")#New line

#interpret if
def iif(words):
  conditions.append(icondit(words[1]))#Add the condition to the list
  if conditions[-1]==False:#If the conditioin is false
    skip=True#Skip the upcoming lines

def ielse(words):
  if conditions[-1]==False:#If the condition is false
    skip=False#Unskip
  else:#Otherwise
    skip=True#Skip
#See if a condition is true or false
def icondit(condition):
  if condition=="True":
    condition=True
  else:
    condition=False
  return condition

#Check for comments and other stuff later on/
def check(words):
  comment=False#Whether or not it is a comment
  line=[]#The new line with out the comment
  for i in words:#Check all the words
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

#Gets segment of line inbetween semicolons
def iseg(lines,start):#Fix
  seg=[]
  x=start
  words=lines[x].split(" ")#Split the line into words
  #print(words[0])
  while words[0]!="}":
    #print(words[0])
    x+=1
    seg.append(lines[x])
    words=lines[x].split(" ")#Split the line into words
  seg.pop(-1)
  return seg

def ivar(words):
  variables[words[0]]=words[2]
  #print(variables)


skip=False#Whether of not to skip at line (because it is in an if statement)
i=0#Line number Off by one error from the line number if the code file
while i<len(lines):#Line by line interpreted
  words=lines[i].split(" ")#Split the line into words
  words=check(words)#Check for comments
  #print(conditions,words,skip)
  if skip==True:#If you are skipping this line
    if words[0]=="}":#If this is the end of an 'indent'
      if len(conditions)>0:#Error checking
        if conditions[-1]==False:#If the latest condition is false
          if len(words)>1:#Error checking
            if words[1]==keywords[2]:#If it is an else statement
              skip=False#Do not skip it
              conditions.pop()#Delete the condition
      else:
        pass#Error statement
    if words[0].lower()==keywords[1]:#if it is an if statement
      conditions.append("Filler")#The code will not be run
    elif words[0].lower()=="}" and len(words)==1:#If it is the end of the if/else statement
      if len(conditions)>0:#Error checking
        conditions.pop()#Delete the condition
  elif skip==False:#If you are not going to skip the line
    if len(words)>1:#Error checking
      if words[0].lower()==keywords[0]:#See if its a print statement
        iprint(words)#print
      elif words[0].lower()==keywords[1]:#See if its an if statement
        iif(words)
      elif words[1].lower()==keywords[2]:#If it is an else statement
        ielse(words)
      elif words[0]=="}" and len(words)==1:#If it is the end
        conditions.pop()#delete the condition
      elif words[1].lower()==keywords[3]:#If they are assigning a variable
        ivar(words)#Assign the variable
  i+=1
