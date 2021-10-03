3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
Score Grade
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
< 0.6 F
If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.

python
s=input("Enter the Score: ")
try:
    sr=int(s)
except:
    sr=-1
if sr>10:
  print('Not in Range')
elif sr<0:
  print('Not In Range')
elif sr>=0.9:
  print('Your Grade is: A')
elif sr>=0.8:
  print('Your Grade is: B')
elif sr>=0.7:
  print('Your Grade is: C')
elif sr>=0.6:
  print('Your Grade is: D')
elif sr<0.6:
  print('Your Grade is: F')
print('All Done')
