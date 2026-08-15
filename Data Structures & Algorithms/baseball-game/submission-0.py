class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []

        for i in range(len(operations)):
            if operations[i] == "+":
                score += [score[-1] + score[-2]]

            elif operations[i] == "C":
                score.pop()

            elif operations[i] == "D":
                score += [score[-1] * 2]

            else:
                score += [int(operations[i])]
        return sum(score)
