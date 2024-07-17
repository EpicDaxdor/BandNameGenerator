import random

# Expanded lists
adjectives = ['Flying', 'Red', 'Silent', 'Broken', 'Dark', 'Mysterious', 'Wild', 'Happy', 'Electric', 'Golden', 'Ancient', 'Loud']
nouns = ['Dragons', 'Wolves', 'Pirates', 'Stars', 'Echoes', 'Storms', 'Mirrors', 'Voices', 'Giants', 'Rangers', 'Warriors', 'Knights']
verbs = ['Whispering', 'Singing', 'Roaring', 'Dancing', 'Raging', 'Dreaming']
places = ['Mountain', 'Forest', 'Ocean', 'Sky', 'Desert', 'River']

# Function to generate band names with different patterns
def generate_band_name():
    pattern = random.choice(['Adjective Noun', 'Noun and Noun', 'Verb Noun', 'Noun of Place'])
    if pattern == 'Adjective Noun':
        return f"{random.choice(adjectives)} {random.choice(nouns)}"
    elif pattern == 'Noun and Noun':
        return f"{random.choice(nouns)} and {random.choice(nouns)}"
    elif pattern == 'Verb Noun':
        return f"{random.choice(verbs)} {random.choice(nouns)}"
    elif pattern == 'Noun of Place':
        return f"{random.choice(nouns)} of the {random.choice(places)}"

# Generate a few band names
for _ in range(10):
    print(generate_band_name())
