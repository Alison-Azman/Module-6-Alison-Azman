


def load_words(filename: str) -> list[str]:
    words=[]
    with open("words.txt", "r") as openfile:
        for line in openfile:
            word=line.strip()
            if word !="":
                words.append(word)
    return words

def normalize(text: str) -> str:
    cleanword=""
    text=text.lower()
    for char in text:
        if char.isalpha():
            cleanword+=char
    return cleanword


def set_signature(text: str) -> frozenset:
    cleantext=normalize(text)
    frozentext=frozenset(cleantext)
    return frozentext    


def freq_signature(text: str) -> tuple:
    cleantext=normalize(text)
    counts=[]
    for letter in "abcdefghijklmnopqrstuvwxyz":
        found=cleantext.count(letter)
        counts.append(found)
    counts=tuple(counts)
    return counts
 


def is_anagram_using_sets(a: str, b: str) -> bool:
    return set_signature(a) == set_signature(b)


def is_anagram(a: str, b: str) -> bool:
    return freq_signature(a) == freq_signature(b)




def group_anagrams(words: list[str]) -> dict[tuple, list[str]]:
    groups={}
    for word in words:
        key=freq_signature(word)
        if key in groups:
            groups[key].append(word)
        else:
            groups[key]=[word]
    return groups


def main(): 
    words = load_words("words.txt")

    # Part 3 counterexamples
    print("SET COUNTEREXAMPLES (When sets says it's True, but it is not an anagrams):")
    pairs = [("aab", "ab"), ("mississippi", "misp"), ("aabbcc", "abc")]
    for a, b in pairs:
        if is_anagram_using_sets(a, b) and not is_anagram(a, b):
            print(f"  {a} vs {b}")



    groups= group_anagrams(words)
    sorted_groups=sorted(groups.values(), key=len, reverse=True)
    largest_group_len= len(sorted_groups[0])


    total_words= len(words)

    total_groups=len(groups)

    singletons=0
    for single in groups.values():
        if len(single)==1:
            singletons+=1



    print("Anagram Group Report")
    print(f"Total words loaded: {total_words}")
    print(f"Total anagram groups: {total_groups}")
    print(f"Singleton groups (size 1) {singletons}")

    print(f"Largest group size: {largest_group_len}\nWords: {sorted_groups[0]}")

    print()
    print(f"The top 5 groups were:")
    for group in sorted_groups[:5]:
        print()
        print(f"Size: {len(group)}\nWords: {group}")
    print()
    print("Short Big-O Reflection")
    print("Question 1:\n Because sets jump directly to the value instead of searching through every item- sets use a hash table internally.")
    print("Question 2:\n Because time increases as the elements in the list grow, becuase Python will check all x amount of elements worst that comes to worse")
    print("Question 3:\n It is of O(k) because you will need to loop through each charachter of the word. the longer the word the more charachetrs to loop through.")
    print("Question 4:\nSets alone fails for anagrams because it removes any duplicates and will match aabc with cab because a set will take aabc and turn it into abc")



main()
