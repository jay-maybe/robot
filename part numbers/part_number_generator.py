import csv

### SCRIPT ###

print("(1): Generate new part number")
print("(2): Query existing part numbers")
selection = input(": ")

# Load part number CSV into memory.
with open("part_numbers.csv",newline='') as csvfile:
    
    # Generate new part number.
    if  selection == 1:

    # Query existing part numbers.
    elif selection == 2:

    else:
        pass

### END SCRIPT ###

### REFERENCES ###

# https://docs.python.org/3/library/csv.html

### END REFERENCES ###