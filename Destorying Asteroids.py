class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: list[int]) -> bool:
        can_destory = mass
        asteroids.sort()
        for i in asteroids:
            if can_destory >= i:
                can_destory += i
            else:
                return False
        return True
    
def main():
    mass = 10
    asteroids = [3,9,19,5,21]
    print(Solution().asteroidsDestroyed(mass, asteroids))

if __name__ == "__main__":
    main()