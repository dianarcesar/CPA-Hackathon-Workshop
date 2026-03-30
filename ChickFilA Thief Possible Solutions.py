# --- THE HODO DORM CHICK-FIL-A HEIST: SOLUTIONS ---

# THE EVIDENCE: 
# Time: 12:15 PM
# Destination: Atwood II

# ---------------------------------------------------------
# SOLUTION 1: THE PARALLEL LISTS METHOD (Beginner)
# ---------------------------------------------------------
# This method uses separate lists. We use an index (i) to 
# "link" the same person across different lists.

print("--- Solution 1: Parallel Lists ---")

names = ["Alice", "Bob", "Charlie", "Lilly"]
times = ["12:00 PM", "12:15 PM", "12:15 PM", "12:45 PM"]
destinations = ["Library", "Atwood II", "Atwood 1", "Cullen Science Center"]

# Extraneous Data (Noise)
majors = ["Nursing", "Biology", "Psychology", "Business"]
balances = [15.00, 2.50, 50.00, 10.00]

for i in range(len(names)):
    if times[i] == "12:15 PM" and destinations[i] == "Atwood II":
        print(f"The thief is {names[i]}!")

print("\n")

# ---------------------------------------------------------
# SOLUTION 2: LIST OF DICTIONARIES (Intermediate)
# ---------------------------------------------------------
# This organizes each suspect into their own object. 
# It makes the code much more readable and "real-world."

print("--- Solution 2: List of Dictionaries ---")

suspects = [
    {"name": "Alice", "time": "12:00 PM", "dest": "Library", "major": "Nursing", "balance": 15.00},
    {"name": "Bob", "time": "12:15 PM", "dest": "Atwood II", "major": "Biology", "balance": 2.50},
    {"name": "Charlie", "time": "12:15 PM", "dest": "Atwood 1", "major": "Psychology", "balance": 50.00},
    {"name": "Lilly", "time": "12:45 PM", "dest": "Cullen Science Center", "major": "Business", "balance": 10.00}
]

for person in suspects:
    # Notice how we ignore 'major' and 'balance' entirely
    if person["time"] == "12:15 PM" and person["dest"] == "Atwood II":
        print(f"The thief is {person['name']}!")

print("\n")

# ---------------------------------------------------------
# SOLUTION 3: FILTERING WITH LIST COMPREHENSION
# ---------------------------------------------------------
# This is a one-line way to filter a list. It creates a new list 
# containing only the people who meet the criteria.

print("--- Solution 3: Filtering ---")

# Using the 'suspects' list from the previous solution
thief = [s["name"] for s in suspects if s["time"] == "12:15 PM" and s["dest"] == "Atwood II"]

if thief:
    print(f"The thief is {thief[0]}!")