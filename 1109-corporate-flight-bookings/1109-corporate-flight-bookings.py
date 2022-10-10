class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        lst = [0]*(n)
        for i,j,k in bookings:
                lst[i-1]+=k
                if j < len(lst):
                    lst[j]-=k
        for c in range(1,n):
            lst[c]+=lst[c-1]
            
        return lst
                
            
        