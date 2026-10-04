"""
RECORD CHECK  -  my version
===========================

Name  : Matthias Munyao
Lane  :  IT      
Date  : 05/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""



label = input("Please Enter the Hostname: ")
value = float(input("Please enter the value: "))    
limit = float(input("Please enter the limit: "))  

    

difference = limit - value   
percent = (value/limit) * 100      
   
status = "OK"
if percent >= 100:
        status = "OVER LIMIT"
elif percent >= 90:
        status = "WARNING"
else:
        status = "OK"

  
print ()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  value         :         {value:.2f}")
print(f"  Limit         :         {limit:.2f}")
print(f"  Difference    :         {difference:.2f}")
print(f"  Percent       :         {percent:.2f}%")
print(f"  Status        :         {status}")

print("=" * 34)


