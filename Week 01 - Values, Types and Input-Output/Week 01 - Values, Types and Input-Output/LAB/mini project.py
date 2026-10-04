"""
RECORD CHECK  -  my version
===========================

Name  : Matthias Munyao
Lane  :   IT      
Date  : 02/10/2026

Run it:   python template.py





label = ""      
first = 0.0     
second = 0.0    





difference = 0.0   
percent = 0.0      




print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)



print("=" * 34)





label = input("Enter hostname: ")
first = float(input("Enter GB used: "))
second = float(input("Enter GB total: "))


difference = second - first
percent = (first / second) * 100


print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"  GB used:      {first:10.2f}")
print(f"  GB total:     {second:10.2f}")
print(f"  Difference:   {difference:10.2f}")
print(f"  Percent:      {percent:10.2f}%")
print(f"  Free GB:      {difference:10.2f}")

print("=" * 34)
