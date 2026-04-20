class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 0.1. Prepare empty dictionary.
        anagram_dict = {}
        # 1. Iterate through each item in the list using a for loop.
        for word in strs:
        #   2. Check the current Item with Counter(item).
            word_signature = Counter(word)
        #   3. Make immutable key out of it.
            anagram_key = tuple(sorted(word_signature.items()))
        #   4. If the Counter is not present within the dictionary as key:
            if anagram_dict.get(anagram_key) is None:
        #       4.1. Add new key-value pair to dictionary, key is list index within prepared list, value is current Item of the for loop.        
                anagram_dict[anagram_key] = [word]
        #   5. If the Counter is present within the library:
            else:
        #       5.1. Add current item to list in the value field of the dictionary.
                anagram_dict[anagram_key].append(word)
        # 6. return Lists within List via Dictionary.
        return list(anagram_dict.values())