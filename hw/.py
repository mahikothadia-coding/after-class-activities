rows  =  int(input("enter amount of rows:  "))

for i in range(rows):
     print("  " * (rows - i - 1) ," *" * (i +1))