with open("india.txt",'r',encoding = 'utf-8') as file:
    text=file.readline()
    count=0
    for i in file:
       if "India" in text:
         count=count+1
       else:
         continue
print(count)
 
