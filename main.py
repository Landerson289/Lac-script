###This is the interpreter###



f=open("code.txt","r")#The code
lines=f.read().splitlines()#Split it line by line
keywords=["print","if","else","is"]#All the keywords
variables={}


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
  cond=icondit(words[1])
  #print(cond)
  if cond==True:
    skip=False
  else:
    skip=True
  return skip,cond

def ielse(words):
  if cond==False:
    skip=False
  else:
    skip=True
  return skip
      
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

skip=False
i=0
while i<len(lines):#Line by line interpreted
  words=lines[i].split(" ")#Split the line into words
  words=check(words)#Check for comments
  #print(words)
  if skip==True and words[0]=="}":
    skip=False
  if skip==False:
    if len(words)>1:
      if words[0].lower()==keywords[0]:#See if its a print statement
        iprint(words)#print
      elif words[0].lower()==keywords[1]:#See if its an if statement
        skip,cond=iif(words)
      elif words[1].lower()==keywords[2]:
        skip=ielse(words)
      elif words[1].lower()==keywords[3]:
        ivar(words)
  i+=1

#Conditions
#Repeat until, for, while.
#Fix multiple if statements.
#Write code into a python file.
#Functions
#Classes
#Built in functions