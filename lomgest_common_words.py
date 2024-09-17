def longest_common_prefix(words):
    for i in zip(*words):
        if len(set(i)) > 1: return words[0][:words[0].index(i[0])]
    return min(words)

words = ["flower", "flow", "flight"]
print(longest_common_prefix(words))