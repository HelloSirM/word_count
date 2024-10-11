from collections import Counter
import re

# import pandas as pd

file_path = 'sample.txt'

def count_word_frequencies(file_path):
    with open(file_path, 'r') as file:
            contents = file.read().lower()
            words = re.findall(r'\b\w+\b', contents)
            words_counted = Counter(words)
            return words_counted

            # Save as .CSV using pandas
            # word_counts_df = pd.DataFrame(words_counted.items(),columns=['Word','Frequency'])
            # word_counts_df.to_csv('word_frequencies.csv', index=False)
            # return words_counted


