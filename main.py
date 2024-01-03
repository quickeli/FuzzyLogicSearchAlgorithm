import pandas as pd
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

df = pd.read_csv('random_words.csv')

print("Please enter a word to be searched in our dataset.")
search_term = input()


def find_similar_words(search_term, random_words):

    matches = process.extract(search_term, random_words, scorer=fuzz.token_set_ratio, limit=5)

    print(f"Top 5 matches for '{search_term}':")
    for match, score in matches:
        print(f"{match} (Score: {score})")


random_words = df['yesterday'].tolist()

find_similar_words(search_term, random_words)
