"""
RECORD CHECK  -  my version
===========================

Name  : Matthias Munyao
Lane  : IT      
Date  : 18/10/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


def check_record(value, limit):
    """Gives us the difference, percent of limit used, and status needed."""
    difference = limit - value
    percent = value / limit * 100
    if value > limit:
        status = "OVER LIMIT"
    else:
        status = "OK"


    return difference, percent, status





def print_for_me(label,value, limit, difference, percent, status):
    """Prints one record's label, numbers, and status on a single line. One line at a time"""
    print(f"{label}: {value} out of {limit} ({percent:.2f}%) difference {difference:.2f} status : {status}")




def load_records(path):
    """Reads label,value,limit lines from a file and return a list of dictionaries."""
    records = []
    try:    
        with open(path) as f:
            for line in f:
                line = line.strip()
                label,value,limit = line.split(",")
                records.append({
                "label" : label,
                "value" : float(value),
                "limit" : float(limit),
                })
    except FileNotFoundError:
        print(f"File not found. Empty list returned")
        return []
    return records


records = load_records("records_sample.txt")



over_count = 0

with open("results.txt", "w") as f:
    for record in records:
        difference, percent, status = check_record(record["value"], record["limit"])
        print_for_me(record["label"], record["value"], record["limit"], difference, percent, status)
        f.write(f"{record['label']},{status}\n")
        if status == "OVER LIMIT":
            over_count += 1

print(f"Records over limit: {over_count}")


# missing file test: used "nope.txt", no crash.
# it printed "File not found. Empty list returned" and 0 over limit.