import re

# Note: \b matches an empty string at the beginning or end of a word
dateRegex = re.compile(r'''(\n|\s|\b)(?<!-)([0-3][0-9]) # day
    /
    ([01][0-9]) # month
    /
    ([0-9]{2})
    (\n|\s|\b)
    ''', re.VERBOSE)



# Detects dates in the DD/MM/YY format
def contains_date(str): 
    result = dateRegex.search(str) 
    if result == None:
        return False
    day, month, year = (int(result.group(2)), int(result.group(3)), int(result.group(4)))
    return day > 0 and day <= 31 and month > 0 and month <= 12 and year >= 0

print(contains_date("Today is: 11/11/11")) # True
print(contains_date("Today is: -11/11/11")) # False
print(contains_date("Tommorow is: ab/dd/dd")) # False
print(contains_date("Tommorow is: 00/00/00")) # False
print(contains_date("Tommorow is: 50/12/00")) # False
print(contains_date("Tommorow is: 01/50/00")) # False