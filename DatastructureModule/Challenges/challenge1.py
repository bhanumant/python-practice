
from collections import Counter
import re


#Find the Most repeated words


text = """
    Python is great, and Python is easy to learn. 
    Many people love Python because Python is powerful and readable!
"""

# desiredText= text.split()
# print(desiredText)

# count = Counter(desiredText)
# print(count)


desiredText=re.findall('\w+', text)

count = Counter(desiredText)
print(count.most_common(3))