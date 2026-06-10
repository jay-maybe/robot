### Title:
Part Number Scheme

### Status:
Approved

### Author:
Jay Maybe

### Date:
5/21/26

### Context:
- decide what part number scheme to use

### Considered Options:
- part number length (5 to 8)
- revision number length (1 to 3)
- sequential non-significant (0001,0002,...) vs significant (ADX0101, RDX0202, ...)
    - non-significant carries no additional information besides being a unique identified for the part
    - significant carries additional information about the part (material, part type, etc)

### Decision:
- 5 digit sequential non-significant part number, 3 digit sequential revision number
- format: [5 digit part number]-[3 digit revision number]
- reserved 0xxxx part numbers.
- [(codified here)](../partnumbers.md)

### Rationale:
- 5 digit part number length allows for 100,000 unique parts, way more than enough for this project
- 3 digit part number length allows for 1,000 revisions, plenty of headroom
- non-significant part numbers are simpler.
- I don't like the part numbers starting with 0 (10001 looks cooler than 00001).