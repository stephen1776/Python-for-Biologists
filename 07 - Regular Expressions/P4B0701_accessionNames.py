'''
Here's a list of made up gene accession names:

accessions = ['xkn59438', 'yhdck2', 'eihd39d9', 'chdsye847', 'hedle3455', 'xjhd53e', '45da', 'de37dp']

Write a program that will print only the accession names that satisfy the following criteria – treat each criterion separately:

    contain the number 5
    contain the letter d or e
    contain the letters d and e in that order
    contain the letters d and e in that order with a single letter between them
    contain both the letters d and e in any order
    start with x or y
    start with x or y and end with e
    contain three or more digits in a row
    end with d followed by either a, r or p

'''
import re

accessions = ["xkn59438", "yhdck2", "eihd39d9", "chdsye847", "hedle3455", "xjhd53e", "45da", "de37dp"]

print("Contain the number 5:")
for m in accessions:
    if re.search(r"5", m):
        print("\t" + m)

print("Contain the letter d or e:")
for m in accessions:
    if re.search(r"(d|e)", m):
        print("\t" + m)

print("Contain the letters d and e in that order:")
for m in accessions:
    if re.search(r"d.*e", m):
        print("\t" + m)

print("Contain the letters d and e in that order with a single letter between them:")
for m in accessions:
    if re.search(r"(d.e)", m):
        print("\t" + m)

print("Contain both the letters d and e in any order:")
for m in accessions:
    if re.search(r"d.*e", m) or re.search(r"e.*d", m):
        print("\t" + m)

print("Start with x or y:")
for m in accessions:
    if re.search(r"^(x|y)", m):
        print("\t" + m)

print("Start with x or y and end with e:")
for m in accessions:
    if re.search(r"^(x|y).*e$", m):
        print("\t" + m)

print("Contain three or more digits in a row:")
for m in accessions:
    if re.search(r"\d{3,}", m):
        print("\t" + m)

print("End with d followed by either a, r or p:")
for m in accessions:
    if re.search(r"d[arp]$", m):
        print("\t" + m)
