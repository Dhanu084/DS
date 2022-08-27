from collections import defaultdict
inputDict = set(["i","a","at","starling","staring","storing","attire","star"])

def lcs(word, w, index, wordMap):
    currentWord = ''.join(w)
    if index >= len(word):
        if currentWord in inputDict and currentWord!=word:
            wordMap[word].add(currentWord)
        return

    if ''.join(w) in inputDict and currentWord!=word:
        wordMap[word].add((''.join(w)))

    w.append(word[index])
    lcs(word,w,index+1, wordMap)
    if w:
        w.pop()
    lcs(word,w,index+1,wordMap)


if __name__ == "__main__":
    
    wordMap = defaultdict(set)
    for word in inputDict:
        lcs(word,[],0,wordMap)
    # expected output should be 4
    # from starling I can reach - staring, star, i , a
    print(len(max(wordMap.values())))