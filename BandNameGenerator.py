import random

# Expanded lists
adjectives = ['Flying', 'Red', 'Silent', 'Broken', 'Dark', 'Mysterious', 'Wild', 'Happy', 'Electric', 'Golden', 'Ancient', 'Loud']
nouns = ['Dragons', 'Wolves', 'Pirates', 'Stars', 'Echoes', 'Storms', 'Mirrors', 'Voices', 'Giants', 'Rangers', 'Warriors', 'Knights']
verbs = ['Whispering', 'Singing', 'Roaring', 'Dancing', 'Raging', 'Dreaming']
places = ['Mountain', 'Forest', 'Ocean', 'Sky', 'Desert', 'River', 'Canyon', 'Beach', 'Lake']

# Function to generate band names with different patterns
def generate_band_name():
    pattern = random.choice(['Adjective Noun', 'Noun and Noun', 'Verb Noun', 'Noun of Place', 'Adjective Verb Noun'])
    if pattern == 'Adjective Noun':
        return f"{random.choice(adjectives)} {random.choice(nouns)}"
    elif pattern == 'Noun and Noun':
        return f"{random.choice(nouns)} and {random.choice(nouns)}"
    elif pattern == 'Verb Noun':
        return f"{random.choice(verbs)} {random.choice(nouns)}"
    elif pattern == 'Noun of Place':
        return f"{random.choice(nouns)} of the {random.choice(places)}"
    elif pattern == 'Adjective Verb Noun':
        return f"{random.choice(adjectives)} {random.choice(verbs)} {random.choice(nouns)}"

# Function to allow user to add custom words
def add_custom_words():
    global adjectives, nouns, verbs, places
    print("You can add your own words to the lists.")
    
    # Adding custom adjectives
    custom_adjectives = input("Enter adjectives (comma-separated): ").split(',')
    adjectives.extend([word.strip() for word in custom_adjectives if word.strip()])
    
    # Adding custom nouns
    custom_nouns = input("Enter nouns (comma-separated): ").split(',')
    nouns.extend([word.strip() for word in custom_nouns if word.strip()])
    
    # Adding custom verbs
    custom_verbs = input("Enter verbs (comma-separated): ").split(',')
    verbs.extend([word.strip() for word in custom_verbs if word.strip()])
    
    # Adding custom places
    custom_places = input("Enter places (comma-separated): ").split(',')
    places.extend([word.strip() for word in custom_places if word.strip()])

# Function to generate multiple band names
def generate_multiple_band_names(count):
    generated_names = set()
    while len(generated_names) < count:
        band_name = generate_band_name()
        generated_names.add(band_name)
    return generated_names

# Main program
if __name__ == "__main__":
    add_custom_words()  # Allow the user to add custom words
    number_of_names = int(input("How many band names would you like to generate? "))
    band_names = generate_multiple_band_names(number_of_names)

    # Print the generated band names
    for name in band_names:
        print(name)
