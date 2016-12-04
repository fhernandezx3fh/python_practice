import os

print os.name
print os.getcwd()
print 
for file in os.listdir(os.getcwd()):
  print file
  #print file.replace(" ", "_").lower()
  os.rename(file, file.replace(" ", "_").lower())  
