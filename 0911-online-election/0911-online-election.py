class TopVotedCandidate:
    def __init__(self, persons, times):
        self.leads, self.times, count = [], times, {}
        lead = -1
        for p in persons:
            count[p] = count.get(p, 0) + 1
            if count[p] >= count.get(lead, 0): lead = p
            self.leads.append(lead)

    def q(self, t):
        return self.leads[bisect.bisect(self.times, t) - 1]

#     def __init__(self, persons: List[int], times: List[int]):
#         self.persons = persons
#         self.times = times
        
#         self.leader = self.persons[0]
#         self.values = defaultdict(int)
#         self.values[self.leader] += 1
#         for item in range(1,len(self.persons)):
#             self.values[self.persons[item]] += 1
#             if self.leader > self.values[self.persons[item]]:
#                 self.persons[item] = self.leader
        
            
   

#     def q(self, t: int) -> int:
#         def validate(mid,t):
#             if self.times[mid] >= t:
#                 return True
#             return False
            
        

#         start = -1
#         end = len(self.persons)
#         while end > start + 1:
#             mid = start + (end - start ) // 2
#             if validate(mid,t):
#                 end = mid
#             else:
#                 start = mid
#         if end >= len(self.times):
#             return self.persons[-1]
#         else:
#             if self.times[end] == t:
#                 return self.persons[end]
#             else:
#                 if end == 0:
#                     return self.persons[0]
#                 else:
#                     return self.persons[end - 1]
        
       
# #         if end >= len(self.times):
# #             if self.winners[-1][1] == self.winners[-1][2]:
# #                 return self.winners[-1][0]
# #             else:
# #                 if self.winners[-1][1] > self.winners[-1][2]:
# #                     return 0
# #                 else:
# #                     return 1
        
# #         if self.times[end] == t:
# #             if self.winners[end][1] == self.winners[end][2]:
# #                 return self.winners[end][0]
# #             else:
# #                 if self.winners[end][1] > self.winners[end][2]:
# #                     return 0
# #                 else:
# #                     return 1
# #         else:
# #             if end == 0:
# #                 return self.winners[0][0]
            
# #             else:
                
# #                 if self.winners[end-1][1] == self.winners[end-1][2]:
                    
# #                     return self.winners[end - 1][0]
# #                 else:
# #                     if self.winners[end-1][1] > self.winners[end-1][2]:
# #                         return 0
# #                     else:
# #                         return 1

                

        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)