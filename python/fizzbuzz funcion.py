
def fizzbuzz(x):
   if resultado := x % 3 == 0 and x % 5 == 0:  
      print('fizzbuzz') 
   elif resultado := x % 3 == 0: #fizz 
      print('fizz')
   elif resultado := x % 5 == 0: #buzz 
      print('buzz')
   else: 
      print(x)
   
fizzbuzz(15)