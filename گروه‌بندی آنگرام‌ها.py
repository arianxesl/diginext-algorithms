def groupAnagrams(strs):
    anagrams = {}
    
    for s in strs:
        sorted_str = ''.join(sorted(s))
        
        if sorted_str not in anagrams:
            anagrams[sorted_str] = []
        
        anagrams[sorted_str].append(s)

    return list(anagrams.values())

# example:
input_strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
output = groupAnagrams(input_strs)

print(output)  # output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
