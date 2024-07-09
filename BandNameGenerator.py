import random

# List of adjectives
adjectives = ['Cosmic', 'Ethereal', 'Sonic', 'Chromatic', 'Euphonic', 'Resonant', 'Harmonic', 'Melodic']

# List of nouns
nouns = ['Stardust', 'Horizon', 'Vortex', 'Spectrum', 'Amplitude', 'Resonance', 'Cadence', 'Crescendo']

def generate_band_name():
    # Randomly select an adjective and a noun
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    
    # Combine the adjective and noun to form the band name
    band_name = f"{adjective} {noun}"
    
    return band_name

# Generate and print a band name
print("Your new band name is:", generate_band_name())
