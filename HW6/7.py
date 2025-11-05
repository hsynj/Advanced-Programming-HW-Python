import re

def build(text):
    words = re.findall(r'\b\w+\b', text)
    the_dict = {}
    for word in words:
        length = len(word)
        if length not in the_dict:
            the_dict[length] = []
        the_dict[length].append(word)
    return the_dict


text2 = "why 111 does someone believe you when you say there are four billion stars but they have to check when you say the paint is wet"
print(build(text2))
