class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        # power = [1, 2, 4, 8 , 16 , 32, 64,128, 256, 512 , 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288,1048576]
        power = [2**a for a in range(22)]
        ct = Counter(deliciousness)
        total = 0
        for item in deliciousness:
            ct[item]-=1
            for j in power:
                case = j - item
                if case in ct:
                    total += ct[case]
        
        return total % (10**9 + 7)
        