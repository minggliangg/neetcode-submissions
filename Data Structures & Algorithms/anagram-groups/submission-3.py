class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_map = {}

        for word in strs:
            count = [0] * 26

            for char in word:
                count[ord(char) - ord('a')] += 1

            key = tuple(count)

            if key in result_map:
                result_map[key].append(word)
            else:
                result_map[key] = [word]

        return list(result_map.values())