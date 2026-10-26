"""
RECORD CHECK  -  my version
===========================

Name  : Matthias Munyao
Lane  :  IT      
Date  : 26/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""

class Record:
    def __init__(self, label, value, limit):
        """Store the label, value and limit for one record."""
        self.label = label
        self.value = value
        self.limit = limit

    def status(self):
        """Return OVER LIMIT , WARNING or OK depending on the percentage."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        else:
            return "OK"



def load_records(path):
    """Read label,value,limit lines from a file and return a list of Records."""
    records = []
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append(Record(label, float(value), float(limit)))
    return records



with open("my_records.txt", "w") as f:
    f.write("R-001,87.0,100.0\n")
    f.write("R-002,95.0,100.0\n")
    f.write("R-003,120.0,100.0\n")
    f.write("R-004,140.0,100.0\n")

records = load_records("my_records.txt")



over_limit_count = 0

for record in records:
    print()
    print("=" * 34)
    print(f"  RECORD CHECK  -  {record.label}")
    print("=" * 34)
    print(f"  Value  : {record.value}")
    print(f"  Limit  : {record.limit}")
    print(f"  Status : {record.status()}")
    print("=" * 34)

    if record.status() == "OVER LIMIT":
        over_limit_count += 1

print()
print(f"{over_limit_count} of {len(records)} records were OVER LIMIT")