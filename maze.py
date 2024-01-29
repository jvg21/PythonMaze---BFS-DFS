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
    pass
