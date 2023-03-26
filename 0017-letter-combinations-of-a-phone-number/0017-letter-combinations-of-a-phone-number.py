class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.letters = {"2":["a","b","c"],"3":["d","e","f"],"4":["g","h","i"],"5":["j","k","l"],"6":["m","n","o"],"7":["p","q","r","s"],"8":["t","u","v"],"9":["w","x","y","z"]}
        self.out = []
        if not digits:
            return []
        def backtrack(arr,index):
            if len(arr) == len(digits):
                self.out.append("".join(arr))
                return
            if len(arr) > len(digits):
                return
            
            for item in self.letters[digits[index]]:
                arr.append(item)
                backtrack(arr, index + 1)
                arr.pop()
        backtrack([],0)
        return self.out
        