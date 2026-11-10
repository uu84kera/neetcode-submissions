class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    
        # sort position in non-increasing order
        cars = sorted(zip(position, speed), reverse=True)

        stack = []
        for pos, spd in cars:
            # calculate time to reach the target of each car
            time = (target-pos)/spd


            if not stack or time>stack[-1]:
                stack.append(time)
        return len(stack)
