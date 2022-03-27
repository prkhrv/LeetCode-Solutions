# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys
import re

def camel_case(s,action):
  s = re.sub(r"(_|-)+", " ", s).title().replace(" ", "")
  if action == "C":
    return s
  return ''.join([s[0].lower(), s[1:]])

def process_string(inp):
    arr = inp.split(";")
    if arr[0] == "S":
        text = re.sub( r"([A-Z])", r" \1", arr[2]).split()
        ans = " ".join(x.lower() for x in text)
        if arr[1] == "M":
            return ans[:-2]
        return ans
    elif arr[0] == "C":
        cc = camel_case(arr[2].lower(),arr[1])
        if arr[1] == "M":
            cc = cc+"()"
        return cc
        
        
        
    
for line in sys.stdin:
  inp = line.rstrip()
  ans = process_string(inp)
  print(ans.strip())
  
