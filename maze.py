class node():
    def __init__(self,state,parent,action):
        self.state = state
        self.parent = parent
        self.action = action

    
class StackFrontier():
    def __init__(self):
        self.frontier = []
    
    def add(self,node):
        self.frontier.append(node)

    def contains_State(self,state):
        return any(node.state == state for node in self.frontier)
    
    def isEmpty(self):
        return len(self.frontier) == 0 #boolean
    
    def remove(self):
        if self.isEmpty():
            raise Exception('Empty Frontier')
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[0 :-1] ### actual frontier without the last element
            return node
        
class QueueFrontier(StackFrontier):
    def remove(self):
        if self.isEmpty():
            raise Exception('Empty Frontier')
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:] ### actual frontier without the first element
            return node


class Maze():
    def __init__(self,filename) :
        with open(filename) as f:
            file_content = f.read()

        if file_content.count("A")!=1:
            raise Exception("Maze must have one starting point") 
        if file_content.count("B")!=1:
            raise Exception("Maze must have one exit point")
        
        file_content = file_content.splitlines()
        self.heigth = len(file_content)
        self.width = max(len(line) for line in file_content)

        self.walls = []
        for i in range(self.heigth):
            row = []
            for j in range(self.width):
                try:
                    if file_content[i][j] == 'A':
                        self.start = (i,j)
                        row.append(False)

                    elif file_content[i][j] == 'B':
                        self.goal = (i,j)
                        row.append(False)
                    
                    elif file_content[i][j] == ' ':
                        row.append(False)
                    
                    else:
                        row.append(True)

                except IndexError:
                    row.append(False)

            self.walls.append(row)

        self.solution = None
    
    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i, row in enumerate(self.walls):
            for j, col in enumerate(row):
                if col:
                    print("█",end="") 
                elif (i,j) == self.start:
                    print("A",end="")
                elif (i,j) == self.goal:
                    print("B",end="")
                elif solution is not None and(i,j) in solution:
                    print("*",end="")
                else:
                    print(" ",end="")
            
            print()
        print()

    def neighbors(self,state):
        row, col = state
        candidates = [
            ("up",(row - 1, col)),
            ("down",(row + 1, col)),
            ("right",(row, col + 1)),
            ("left",(row, col - 1))
        ]

        result = []

        for action,(r,c) in candidates:
            try:
                if not self.walls[r][c]:
                    result.append((action,(r,c)))
            except IndexError:
                continue

        return result

    


