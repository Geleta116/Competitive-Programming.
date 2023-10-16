class Solution:
    def countVowels(self, word: str) -> int:
        
        vowels = ['a', 'e', 'i', 'o', 'u']
        total_vowel_substring = 0
        
        for idx in range(len(word)):
            if word[idx] in vowels:
                total_vowel_substring += (idx + 1) * (len(word) - idx)
                
        return total_vowel_substring