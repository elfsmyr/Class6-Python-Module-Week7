import string
def letters_file_line(number): 
      with open("alphabet.txt", "w") as f:
        text= string.ascii_uppercase
        
        modifiedletters = [text[i:i + number] +
               "\n" for i in range(0, len(text), number)]
        for j in modifiedletters:
              f.write(j)
        # count=0
        # for j in text:
        #         print(j,end="")
        #         count=count+1
        #         if count==number:
        #                 print("\n",end="")
        #                 count=0
                
number=int(input("enter number:"))
letters_file_line(number)
   