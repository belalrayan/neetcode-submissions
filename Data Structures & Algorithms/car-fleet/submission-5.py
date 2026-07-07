class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs=sorted(zip(position,speed),reverse=True)

        fleets=0
        last_time_to_target=0

        for pos,spd in pairs:
            time_to_target=(target-pos)/spd

            if time_to_target >last_time_to_target:
                fleets+=1
                last_time_to_target=time_to_target

        return fleets


        