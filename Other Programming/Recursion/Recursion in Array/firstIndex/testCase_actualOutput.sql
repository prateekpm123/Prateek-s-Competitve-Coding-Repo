Traceback (most recent call last):
  File "script.py", line 25, in <module>
    val = searchIndex(arr, x, 0)
  File "script.py", line 18, in searchIndex
    currIndex = searchIndex(arr, x, n+1)
  File "script.py", line 18, in searchIndex
    currIndex = searchIndex(arr, x, n+1)
  File "script.py", line 18, in searchIndex
    currIndex = searchIndex(arr, x, n+1)
  [Previous line repeated 995 more times]
  File "script.py", line 15, in searchIndex
    if(n == len(arr)):
RecursionError: maximum recursion depth exceeded while calling a Python object
