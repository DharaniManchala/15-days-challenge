def strStr(haystack: str, needle: str) -> int:
    return haystack.find(needle)

# -------------------------
# Input Section
haystack = input("Enter the haystack string: ").strip()
needle = input("Enter the needle string: ").strip()

# -------------------------
# Function Call and Output
index = strStr(haystack, needle)
if index != -1:
    print(f"✅ First occurrence at index: {index}")
else:
    print("❌ Needle not found in haystack.")
