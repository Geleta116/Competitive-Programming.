class Solution:
    def unhappyFriends(self, n: int, preference: List[List[int]], pairs: List[List[int]]) -> int:
        
        matrix = [[ 0 for _ in range(n) ] for __ in range(n)]
        
        for row in range(n):
            for idx in range(len(preference[row])):
                if row == preference[row][idx]:
                    continue
                matrix[row][preference[row][idx]] = idx + 1
                
        
        
        pair_dict = defaultdict(int)
        for pair in pairs:
            pair_dict[pair[0]] = pair[1]
            pair_dict[pair[1]] = pair[0]
        
        count = 0
        
        
        for pair in pairs:
            friendA, friendB = pair[0], pair[1]
            prefA, prefB = preference[friendA], preference[friendB]

            curr_pair_preference_A = matrix[friendA][friendB]
            curr_pair_preference_B = matrix[friendB][friendA]

            for i in range(curr_pair_preference_A):
                otherFriend = prefA[i]
                if matrix[otherFriend][friendA] < matrix[otherFriend][pair_dict[otherFriend]]:
                    count += 1
                    break

            for i in range(curr_pair_preference_B):
                otherFriend = prefB[i]
                if matrix[otherFriend][friendB] < matrix[otherFriend][pair_dict[otherFriend]]:
                    count += 1
                    break

        return count
