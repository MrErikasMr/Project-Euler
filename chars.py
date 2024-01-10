import re

def solution(first, second):
    accepted_characters = re.compile(r"[^a-z\s]")

    words1 = set(re.sub(accepted_characters, "", first.lower()).split())
    words2 = set(re.sub(accepted_characters, "", second.lower()).split())

    return len(words1.intersection(words2))  # Count common words using set intersection

print(solution("There were four people at dinner..", "There were seven peot dinner."))