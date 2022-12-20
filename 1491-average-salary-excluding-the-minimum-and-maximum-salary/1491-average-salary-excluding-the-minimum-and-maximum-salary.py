class Solution:
    def average(self, salary: List[int]) -> float:
        mini = min(salary)
        maxi = max(salary)
        summ = sum(salary)
        summ -= (mini + maxi)
        return summ/(len(salary)-2)