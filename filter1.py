import spacy
import csv
import os

# Load spaCy model
nlp = spacy.load('en_core_web_sm')

# Load word list from file
with open('Magoosh.txt', 'r', encoding='utf-8') as f:
    wordlist = set([line.strip() for line in f])

# Initialize output CSV file
with open('output/output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Word'])  # Header row

    # Loop through all .txt files in directory
    for filename in os.listdir('input'):
        if filename.endswith('.txt'):
            filepath = os.path.join('input', filename)

            # Process text with spaCy
            with open(filepath, 'r', encoding='utf-8') as f:
                text = f.read()
            doc = nlp(text)

            # Check each token against word list and write to CSV
            for token in doc:
                if token.is_alpha and token.text.lower() in wordlist:
                    writer.writerow([token.text])
                else:
                    pass

# Load output CSV file into a set
with open('output/output.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip header row
    output = set([row[0] for row in reader])

# Write output set to file
with open('output/filteredWordlist.txt', 'w', encoding='utf-8') as f:
    for word in output:
        f.write(word + '\n' )
