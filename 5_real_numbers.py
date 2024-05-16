a = input()
num_list = ["1","2","3","4","5","6","7","8","9","0","."]

if a.count(".")<2:
 if a[: ] in num_list:
  print(True)
 if all(char in num_list for char in a):
  print(True)
else:
  print(False);
 
