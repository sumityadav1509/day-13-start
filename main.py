
# Bug generating data type error:
year=input("Type a year that needs to be checked. ") 


if year%4==0:
  if year%100==0:
    if year%400==0:
      print("Leap Year.") 
    else:
      print("Not Leap Year. ")
  else:
    print("Leap Year. ")      
else:
  print("Not Leap Year. ")           








# Debugging Completed:
year=int(input("Type a year that needs to be checked. ")) 


if year%4==0:
  if year%100==0:
    if year%400==0:
      print("Leap Year.") 
    else:
      print("Not Leap Year. ")
  else:
    print("Leap Year. ")      
else:
  print("Not Leap Year. ")           