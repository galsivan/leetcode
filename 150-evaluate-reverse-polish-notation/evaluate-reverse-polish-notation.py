import operator

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }

        # operators = set("+", "-", "*", "/")
        for token in tokens:
            if token in operators:
                b = s.pop()
                a = s.pop()
                s.append(int(operators[token](a, b)))
            else:
                s.append(int(token))
        return s[0]