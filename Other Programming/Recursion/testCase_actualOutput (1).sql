Traceback (most recent call last):
  File "script.py", line 12, in <module>
    ansIs= power(num, powerNum)
  File "script.py", line 9, in power
    val = num*power(num, powerNum-1)
  File "script.py", line 9, in power
    val = num*power(num, powerNum-1)
  File "script.py", line 9, in power
    val = num*power(num, powerNum-1)
  [Previous line repeated 995 more times]
  File "script.py", line 7, in power
    if(powerNum == 1):
RecursionError: maximum recursion depth exceeded in comparison
