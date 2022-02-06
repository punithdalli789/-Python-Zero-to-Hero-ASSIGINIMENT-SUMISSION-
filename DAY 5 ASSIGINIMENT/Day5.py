my_list = list(range(1,100))
  
result3 = list(filter(lambda x: (x % 3 == 0), my_list)) 
result5 = list(filter(lambda x: (x % 5 == 0), my_list)) 
  
print(result3,"This number only divisible by 3 in 1-100 number \n") 
print(result5,"This number only divisible by 5 in 1-100 number ") 