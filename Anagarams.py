def printAnagramsTogether(words):
    groupedWords = defaultdict(list)
 
    for word in words:
        groupedWords["".join(sorted(word))].append(word)
 
    for group in groupedWords.values():
        print(" ".join(group))
 
 
if __name__ == "__main__":
    arr = [[""]]
    printAnagramsTogether(arr)