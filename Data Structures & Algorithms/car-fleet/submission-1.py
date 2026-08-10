class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            time = (target-position[i])/speed[i]
            cars.append((position[i], time))

        fleetTime = 0
        fleets = 0

        cars.sort(reverse=True)
        for pos, time in cars:
            if time> fleetTime:
                fleets+=1
                fleetTime = time
        
        return fleets
        