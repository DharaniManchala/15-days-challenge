from collections import defaultdict

def groupAnagrams(strs):
    anagram_map = defaultdict(list)

    for word in strs:
        # Sort the word to use as a key
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)

    # Return grouped anagrams
    return list(anagram_map.values())

# -------------------------
# Input Section
input_str = input("Enter words separated by space: ").strip().split()

# -------------------------
# Function Call and Output
result = groupAnagrams(input_str)
print("✅ Grouped Anagrams:")
for group in result:
    print(group)
