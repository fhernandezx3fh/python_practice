import os

print os.name
print os.getcwd()
print 
for file in os.listdir(os.getcwd()):
#file_name, file_ext = os.path.splitext(file)
  if file.find('exercise') != -1:
    print file.replace(file.split('_')[1], file.split('_')[1].zfill(2))
    os.rename(file, file.replace(file.split('_')[1], file.split('_')[1].zfill(2)))
  #print file.replace(" ", "_").lower()
  #os.rename(file, file.replace(" ", "_").lower())  
