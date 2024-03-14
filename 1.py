import re
text = """
Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversations?"
"""
pattern = r'\b[Aa]\w+'  
matches = re.findall(pattern, text)
print("Words starting with 'A' or 'a':", matches)
match = re.search(pattern, text)
if match:
    print("First word starting with 'A' or 'a':", match.group())
else:
    print("No match found.")
