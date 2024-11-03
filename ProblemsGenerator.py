import random

class ProblemsGenerator:
    def __init__(self, n, nMoves):
        self.n = n
        self.goal = list(range(1, n * n)) + [0]
        self.nMoves = nMoves

    def generate(self):
        problem = self.goal.copy()
        state = problem.copy()
        for j in range(self.nMoves):
            move = self.randomMove(state)
            state = self.aplly_move(move, state).copy()
        problem = state.copy()
        return problem

    def aplly_move(self, move, state):
        state_ = state.copy()
        x = state_.index(0)
        if move == 'Left':
            state_[x], state_[x - 1] = state_[x - 1], state_[x]
        elif move == 'Right':
            state_[x], state_[x + 1] = state_[x + 1], state_[x]
        elif move == 'Up':
            state_[x], state_[x - self.n] = state_[x - self.n], state_[x]
        elif move == 'Down':
            state_[x], state_[x + self.n] = state_[x + self.n], state_[x]
        
        return state_

    def isLegalMove(self, move, state):
        state_ = state.copy()
        x = state_.index(0)
        if move == 'Left' and x % self.n == 0:
            return False
        if move == 'Right' and x % self.n == self.n - 1:
            return False
        if move == 'Up' and x - self.n < 0:
            return False
        if move == 'Down' and x + self.n > self.n * self.n - 1:
            return False
        return True

    def randomMove(self, state):
        moves = ['Left', 'Right', 'Up', 'Down']
        while True:
            move = random.choice(moves)
            if self.isLegalMove(move, state):
                return move
                
    def get_goal(self):
        return self.goal

if __name__ == "__main__":
    n = 3
    generator = ProblemsGenerator(n, 30)
    print("goal: ", generator.get_goal())

    print("problem: ", generator.generate())
    
    

