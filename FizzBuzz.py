class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fizzBuz_list = []
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                fizzBuz_list.append("FizzBuzz")
            elif i % 3 == 0:
                fizzBuz_list.append("Fizz")
            elif i % 5 == 0:
                fizzBuz_list.append("Buzz")
            else:
                fizzBuz_list.append(str(i))
        return fizzBuz_list