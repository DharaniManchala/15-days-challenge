# Function to check if t is an anagram of s
def isAnagram(s: str, t: str) -> bool:
    # Sort both strings and compare
    return sorted(s) == sorted(t)

# -------------------------
# Input Section
s = input("Enter first string (s): ").strip()
t = input("Enter second string (t): ").strip()

# -------------------------
# Function Call and Output
if isAnagram(s, t):
    print("✅ Yes, it's a valid anagram.")
else:
    print("❌ No, it's not a valid anagram.")
