class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = [[position[pos],speed[pos]] for pos in range(len(position))]
        cars.sort(reverse = True)
        
        accumulator = []

        for car in cars:
            if not accumulator:
                accumulator.append((target-car[0])/car[1])
            else:
                if accumulator[-1] < (target - car[0]) / car[1]:
                    accumulator.append((target-car[0])/car[1])
        return len(accumulator)
                    
                    