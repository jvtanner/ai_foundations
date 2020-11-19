import collections
import math

############################################################
# Problem 3a

def findAlphabeticallyLastWord(text):
    """
    Given a string |text|, return the word in |text| that comes last
    alphabetically (that is, the word that would appear last in a dictionary).
    A word is defined by a maximal sequence of characters without whitespaces.
    You might find max() and list comprehensions handy here.
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return max(text.split(' '))
    # END_YOUR_CODE

############################################################
# Problem 3b

def euclideanDistance(loc1, loc2):
    """
    Return the Euclidean distance between two locations, where the locations
    are pairs of numbers (e.g., (3, 5)).
    """
    # BEGIN_YOUR_CODE (our solution is 1 line of code, but don't worry if you deviate from this)
    return math.sqrt((loc2[0] - loc1[0])**2 + (loc2[1] - loc1[1])**2)
    # END_YOUR_CODE

############################################################
# Problem 3c

def mutateSentences(sentence):
    """
    Given a sentence (sequence of words), return a list of all "similar"
    sentences.
    We define a sentence to be similar to the original sentence if
      - it as the same number of words, and
      - each pair of adjacent words in the new sentence also occurs in the original sentence
        (the words within each pair should appear in the same order in the output sentence
         as they did in the original sentence.)
    Notes:
      - The order of the sentences you output doesn't matter.
      - You must not output duplicates.
      - Your generated sentence can use a word in the original sentence more than
        once.
    Example:
      - Input: 'the cat and the mouse'
      - Output: ['and the cat and the', 'the cat and the mouse', 'the cat and the cat', 'cat and the cat and']
                (reordered versions of this list are allowed)
    """
    # BEGIN_YOUR_CODE (our solution is 17 lines of code, but don't worry if you deviate from this)
    words = sentence.split()
    mutated = []
    wordPair = {}

    if len(words) < 3:
        # only one possible sentence combination exists
        mutated.append(sentence)
        return mutated
    else:
        # create set of each pair of adjacent words
        for i in range(0, len(words) - 1):
            w = words[i]

            if w not in wordPair:
                wordPair[w] = set()

            wordPair[w].add(words[i + 1])

            if words[-1] not in wordPair:
                wordPair[words[-1]] = set()

    # generate similar sentences
    mutated = [[word] for word in wordPair]
    for i in range(1, len(words)):
        newSentences = []

        for w in mutated:
            lastSet = w[-1]

            if lastSet in wordPair:
                wordPairCombination = []

                for nextSet in wordPair[lastSet]:
                    wordPairCombination = w + [nextSet]
                    newSentences.append(wordPairCombination)

        mutated = newSentences

    mutated = [' '.join(w) for w in mutated]
    return mutated

    # END_YOUR_CODE

############################################################
# Problem 3d

def sparseVectorDotProduct(v1, v2):
    """
    Given two sparse vectors |v1| and |v2|, each represented as collections.defaultdict(float), return
    their dot product.
    You might find it useful to use sum() and a list comprehension.
    This function will be useful later for linear classifiers.
    Note: A sparse vector has most of its entries as 0
    The keys of the sparse vector can be any type. For example, an input could be {'a': 1.0, 'b': 2.0}
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)

    return sum(v2[x]*y for x, y in v1.items() if x in v2)
    # END_YOUR_CODE

############################################################
# Problem 3e

def incrementSparseVector(v1, scale, v2):
    """
    Given two sparse vectors |v1| and |v2|, perform v1 += scale * v2.
    Do not modify v2 in your implementation.
    This function will be useful later for linear classifiers.
    """
    # BEGIN_YOUR_CODE (our solution is 2 lines of code, but don't worry if you deviate from this)
    v3 = v2*scale
    v1 = v1+v3
    return v1
    # END_YOUR_CODE

############################################################
# Problem 3f

def findSingletonWords(text):
    """
    Splits the string |text| by whitespace and returns the set of words that
    occur exactly once.
    You might find it useful to use collections.defaultdict(int).
    """
    # BEGIN_YOUR_CODE (our solution is 4 lines of code, but don't worry if you deviate from this)

    words = {}
    for word in text.split(' '):
        if word not in words:
            words[word] = 1
        else:
            words[word] += 1
    return set(k for k, v in words.items() if v == 1)

    # END_YOUR_CODE

############################################################
# Problem 3g

def computeLongestPalindromeLength(text):
    """
    A palindrome is a string that is equal to its reverse (e.g., 'ana').
    Compute the length of the longest palindrome that can be obtained by deleting
    letters from |text|.
    For example: the longest palindrome in 'animal' is 'ama' and it's length is 3.
    Your algorithm should run in O(len(text)^2) time.
    You should first define a recurrence before you start coding.
    """
    # BEGIN_YOUR_CODE (our solution is 14 lines of code, but don't worry if you deviate from this)
    store = {}
    letterCount = collections.Counter(text)
    length = 0

    def getLength(text):
        if text in store:
            return store[text]

        textLength = len(text)

        if textLength < 2:  # 0 or 1
            length = textLength
        elif textLength == 2:
            for word in text:
                if letterCount[word] == 2:
                    length = 2
                else:
                    length = 1
        elif text[0] == text[-1]:
            length = 2 + getLength(text[1:-1])
        else:
            removeLast = getLength(text[0:-1])
            removeFirst = getLength(text[1:textLength])
            length = max(removeLast, removeFirst)

        store[text] = length

        return length

    return getLength(text)
    # END_YOUR_CODE
