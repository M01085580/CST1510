"""
RECORD CHECK  -  my version
===========================

Name  : Matthias Munyao
Lane  :  IT      (delete two)
Date  : 20/11/2026

Run it:   python template.py

Work through the numbered sections in order. Each one tells you what it must do.
Delete these instructions as you replace them with your code.
"""


"""
RECORD CHECK - IT
"""



def parse_line(raw_line):
    line = raw_line.strip()

    hostname_part, rest = line.split(",", 1)
    hostname = hostname_part.strip().lower()

    fields = {}

    for piece in rest.split(","):
        key, value = piece.split("=")
        fields[key.strip().lower()] = float(value.strip())

    return {
        "hostname": hostname,
        "used": fields["used"],
        "total": fields["total"]
    }


def status_of(record):
    percentage = record["used"] / record["total"] * 100

    if percentage >= 100:
        return "OVER LIMIT"
    elif percentage >= 90:
        return "WARNING"
    else:
        return "OK"



raw_records = []

with open("messiest_lines.txt") as file:
    for line in file:
        raw_records.append(line)


# The process and the output

total_records = 0
flagged_records = 0

for raw_record in raw_records:
    record = parse_line(raw_record)
    status = status_of(record)

    print(record)
    print(status)

    total_records += 1

    if status != "OK":
        flagged_records += 1


print("Total records:", total_records)
print("Flagged records:", flagged_records)
