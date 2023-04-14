import os

# Open the keyword list file and read its contents into a set
with open('output/filteredWordlist.txt', 'r', encoding='utf-8') as f:
    keywords = set(line.strip() for line in f)

# Open the input file and read its lines into a list
with open('TEM-8 wordlist.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Iterate through each line and check if it contains any of the keywords
matching_lines = []
for line in lines:
    if any(keyword in line for keyword in keywords):
        matching_lines.append(line)

# Write the matching lines to an output file
with open('TEM-8 Vocabulary in ChatGPT News.txt', 'w',encoding='utf-8') as f:
    f.writelines(matching_lines)