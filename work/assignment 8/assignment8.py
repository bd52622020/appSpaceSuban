#assignment8

# Python program to display all the prime numbers within an interval

lower = 0
upper = 100

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
    all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)
           
           
      #  question 2
      
# Python program to check if year is a leap year or not

year = 2005

 To get year (integer input) from the user
 year = int(input("Enter a year: "))

if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{0} is a leap year".format(year))
       else:
           print("{0} is not a leap year".format(year))
   else:
       print("{0} is a leap year".format(year))
else:
 #  print("{0} is not a leap year".format(year))
   
   
   #qustion 3
   
   # Python code to check if a  
# given ISBN is valid or not. 
  
def isValidISBN(isbn): 
  
    # check for length 
    if len(isbn) != 10: 
        return False
      
    # Computing weighted sum  
    # of first 9 digits 
    _sum = 0
    for i in range(9): 
        if 0 <= int(isbn[i]) <= 9: 
            _sum += int(isbn[i]) * (10 - i) 
        else: 
            return False
          
    # Checking last digit 
    if(isbn[9] != 'X' and 
       0 <= int(isbn[9]) <= 9): 
        return False
      
    # If last digit is 'X', add  
    # 10 to sum, else add its value. 
    _sum += 10 if isbn[9] == 'X' else int(isbn[9]) 
      
    # Return true if weighted sum of  
    # digits is divisible by 11 
    return (_sum % 11 == 0) 
  
# Driver Code 
isbn = "007462542X"
if isValidISBN(isbn): 
    print('Valid') 
else: 
    print("Invalid") 
   
   
   
   
   
   
   
   #question 4
   
   # Python program to check if all  
 ments in a List are same  
  
def ckeckList(lst): 
  
    ele = lst[0] 
    chk = True
      
     Comparing each element with first item  
    for item in lst: 
    if ele != item: 
            chk = False
           break; 
              
    if (chk == True): print("True") 
   else: print("False")             
  
 Driver Code 
lst = ['suban', 'suban', 'suban', 'suban', ] 
ckeckList(lst) 
   