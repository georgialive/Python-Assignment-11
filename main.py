# Name: Georgia Vrana
# Date Submitted: Tuesday, April 16th, 2024
# Assignment-11: Dictionary
# Description: The Python program defines a dictionary of famous scientists, 
#              calculates their ages at death, and prints their birthplaces and main scientific contributions.

# Define the scientists dictionary as per the assignment
scientists = {
    'Einstein': {'first_name': 'Albert', 'born': 1879, 'died': 1955, 'country': 'Germany', 'contribution': 'theory of relativity'},
    'Curie': {'first_name': 'Marie', 'born': 1867, 'died': 1934, 'country': 'Poland', 'contribution': 'discovery of radium'},
    'Newton': {'first_name': 'Isaac', 'born': 1642, 'died': 1727, 'country': 'England', 'contribution': 'gravitational motion'},
    'Darwin': {'first_name': 'Charles', 'born': 1809, 'died': 1882, 'country': 'England', 'contribution': 'theories of evolution'},
    'Tesla': {'first_name': 'Nikola', 'born': 1856, 'died': 1943, 'country': 'Serbia', 'contribution': 'electrical transmission'},
    'Pasteur': {'first_name': 'Louis', 'born': 1822, 'died': 1895, 'country': 'France', 'contribution': 'pasteurization'},
    'Copernicus': {'first_name': 'Nicolaus', 'born': 1473, 'died': 1543, 'country': 'Poland', 'contribution': 'planetary motion'},
    'Mendel': {'first_name': 'Gregor', 'born': 1822, 'died': 1884, 'country': 'Austria', 'contribution': 'hereditary genes'},
    'Jenner': {'first_name': 'Edward', 'born': 1749, 'died': 1823, 'country': 'England', 'contribution': 'vaccine pioneer'},
}

# Function to calculate age at death for each scientist
def calculate_ages(scientists_dict):
    return {name: info['died'] - info['born'] for name, info in scientists_dict.items()}

# Function to print the country of birth for each scientist
def print_birth_countries(scientists_dict):
    for info in scientists_dict.values():
        print(f"{info['first_name']} was born in {info['country']}")

# Function to print the contributions of each scientist
def print_contributions(scientists_dict):
    for name, info in scientists_dict.items():
        print(f"{info['first_name']} {name}: {info['contribution']}")

# Call the functions and print the output
ages_at_death = calculate_ages(scientists)
print("Ages at death:")
for name, age in ages_at_death.items():
    print(f"{name} {age}")

print("\nBirthplaces:")
print_birth_countries(scientists)

print("\nContributions:")
print_contributions(scientists)


