class MinStack:

    def __init__(self):
        self.l = []
        self.mins = []
    
    def push(self, val: int) -> None:
        self.l.append(val)
        self.mins.append(val if not self.mins else min(val, self.mins[-1]))
        return None

    def pop(self) -> None:
        self.l.pop()
        self.mins.pop()
        return None

    def top(self) -> int:
        return self.l[-1]
        

    def getMin(self) -> int:
        return self.mins[-1]
        
