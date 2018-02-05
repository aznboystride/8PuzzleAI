#! /usr/bin/env python3
import sys, time, resource
from Data_Structures import queues, stacks
from Max_Heap import heaps

heap = heaps
stack = stacks
queue = queues
visited = set()
node_expanded = 0
max_search_depth = 0

start_ram = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss

class Node:
    def __init__(self,state,goal=[0,1,2,3,4,5,6,7,8],parent=None,operator=[],cost=0):
        self.state = state
        self.parent = parent
        self.operator = operator
        self.cost = cost
        self.goal = goal
        self.heuristic = self.Manhattan_Distance() + cost

    def get_man(self):
        return self.Manhattan_Distance()

    def check(self,state):
        return self.state == state

    def try_Left(self):
        for x in range(0, len(self.state)):
            if self.state[x] == 0:
                if x == 0 or\
                    x == 1 or\
                    x == 6 or\
                    x == 7 or\
                    x == 3 or\
                    x == 4:
                    return True
        return False
    def try_Right(self):
        for x in range(0, len(self.state)):
            if self.state[x] == 0:
                if (x == 1) or\
                    (x == 7) or\
    				(x == 4) or\
    				(x == 2) or\
    				(x == 5) or\
    				(x == 8):
                    return True
        return False
    def try_Down(self):
    	for x in range(0, len(self.state)):
    		if self.state[x] == 0:
    			if (x == 6) or\
    				(x == 7) or\
    				(x == 3) or\
    				(x == 4) or\
    				(x == 5) or\
    				(x == 8):
    				return True
    	return False
    def try_Up(self):
    	for x in range(0, len(self.state)):
    		if self.state[x] == 0:
    			if (x == 0) or\
    				(x == 1) or\
    				(x == 2) or\
    				(x == 3) or\
    				(x == 4) or\
    				(x == 5):
    				return True
    	return False

    def move_Left(self):
    	new = list(self.state)
    	for x in range(0, len(new)):
    		if new[x] == 0:
    			temp = new[x]
    			new[x] = new[x + 1]
    			new[x + 1] = temp
    			return new
    def move_Right(self):
    	new = list(self.state)
    	for x in range(0, len(new)):
    		if new[x] == 0:
    			temp = new[x]
    			new[x] = new[x - 1]
    			new[x - 1] = temp
    			return new
    def move_Down(self):
    	new = list(self.state)
    	for x in range(0, len(new)):
    		if new[x] == 0:
    			temp = new[x]
    			new[x] = new[x - 3]
    			new[x - 3] = temp
    			return new
    def move_Up(self):
    	new = list(self.state)
    	for x in range(0, len(new)):
    		if new[x] == 0:
    			temp = new[x]
    			new[x] = new[x + 3]
    			new[x + 3] = temp
    			return new

    def get_Parent(self):
        return self.parent
    def get_State(self):
        return self.state
    def get_Operator(self):
        return self.operator
    def get_Cost(self):
        return self.cost
    def get_Heuristic(self):
        return self.heuristic

    def Manhattan_Distance(self):
        lst = self.get_State()
        summ = 0
        for x in range(0, 9):
            summ += abs(self.distance(self.get_coord(x,self.goal),self.get_coord(lst[x],self.goal)))
        return summ

    def distance(self,tup1,tup2):
        tup = self.sub_coord(tup1,tup2)
        return self.add_x_y(tup)

    def get_coord(self,i,state):
        if i is 0: return (0,0)
        elif i is 1: return (1,0)
        elif i is 2: return (2,0)
        elif i is 3: return (0,1)
        elif i is 4: return (1,1)
        elif i is 5: return (2,1)
        elif i is 6: return (0,2)
        elif i is 7: return (1,2)
        else: return (2,2)

    def sub_coord(self,tup1, tup2):
        x = abs(tup1[0]-tup2[0])
        y = abs(tup1[1]-tup2[1])
        return (x,y)

    def add_x_y(self,tup):
        return tup[0]+tup[1]

def ast(node,goalState):
    global heap
    global visited
    global node_expanded
    global max_search_depth

    while not heap.front().check(goalState):
        visited.add(tuple(heap.front().get_State()))
        front = heap.pop()
        node_expanded += 1
        if front.try_Down() and tuple(front.move_Down()) not in visited:
            moves = list(front.get_Operator())
            moves.append('Up')
            heap.push(Node(state=front.move_Down(),goal=goalState,parent=front,operator=moves,cost=front.get_Cost()+1))
            visited.add(tuple(front.move_Down()))
        if front.try_Up() and tuple(front.move_Up()) not in visited:
            moves = list(front.get_Operator())
            moves.append('Down')
            visited.add(tuple(front.move_Up()))
            heap.push(Node(state=front.move_Up(),goal=goalState,parent=front,operator=moves,cost=front.get_Cost()+1))
        if front.try_Right() and tuple(front.move_Right()) not in visited:
            moves = list(front.get_Operator())
            moves.append('Left')
            visited.add(tuple(front.move_Right()))
            heap.push(Node(state=front.move_Right(),goal=goalState,parent=front,operator=moves,cost=front.get_Cost()+1))
        if front.try_Left() and tuple(front.move_Left()) not in visited:
            moves = list(front.get_Operator())
            moves.append('Right')
            visited.add(tuple(front.move_Left()))
            heap.push(Node(state=front.move_Left(),goal=goalState,parent=front,operator=moves,cost=front.get_Cost()+1))


    else:
        solution = heap.front()
        heap.pop()
        while not heap.empty():
            if heap.front().get_Cost() <= solution.get_Cost():
                heap.pop()
            else:
                max_search_depth = heap.front().get_Cost()
                break
        else:
            max_search_depth = solution.get_Cost()
        return solution

def BFS(node,goalState):
    global queue
    global visited
    global node_expanded
    global max_search_depth

    while not queue.top().check(goalState):
        node_expanded += 1
        if queue.top().try_Down() and tuple(queue.top().move_Down()) not in visited:
            moves = list(queue.top().get_Operator())
            moves.append('Up')
            queue.push(Node(parent=queue.top(),state=queue.top().move_Down(),operator=moves,cost=queue.top().get_Cost()+1))
        if queue.top().try_Up() and tuple(queue.top().move_Up()) not in visited:
            moves = list(queue.top().get_Operator())
            moves.append('Down')
            queue.push(Node(parent=queue.top(),state=queue.top().move_Up(),operator=moves,cost=queue.top().get_Cost()+1))
        if queue.top().try_Right() and tuple(queue.top().move_Right()) not in visited:
            moves = list(queue.top().get_Operator())
            moves.append('Left')
            queue.push(Node(parent=queue.top(),state=queue.top().move_Right(),operator=moves,cost=queue.top().get_Cost()+1))
        if queue.top().try_Left() and tuple(queue.top().move_Left()) not in visited:
            moves = list(queue.top().get_Operator())
            moves.append('Right')
            queue.push(Node(parent=queue.top(),state=queue.top().move_Left(),operator=moves,cost=queue.top().get_Cost()+1))

        visited.add(tuple(queue.top().get_State()))
        while tuple(queue.top().get_State()) in visited:
            queue.pop()

    else:
        solution = queue.top()
        queue.pop()
        while not queue.isEmpty():
            if queue.top().get_Cost() <= solution.get_Cost():
                queue.pop()
            else:
                max_search_depth = queue.top().get_Cost()
                break
        else:
            max_search_depth = solution.get_Cost()
        return solution

def dfs(node, goalState):
    global stack
    global visited
    global max_search_depth
    global node_expanded

    while not stack.top().check(goalState):
        node_expanded += 1
        pop = stack.pop()
        visited.add(tuple(pop.get_State()))

        if pop.try_Left() and tuple(pop.move_Left()) not in visited:
            moves = list(pop.get_Operator())
            moves.append('Right')
            stack.push(Node(state=pop.move_Left(),parent=pop,operator=moves,cost=pop.get_Cost()+1))
            visited.add(tuple(pop.move_Left()))
        if pop.try_Right() and tuple(pop.move_Right()) not in visited:
            moves = list(pop.get_Operator())
            moves.append('Left')
            stack.push(Node(state=pop.move_Right(),parent=pop,operator=moves,cost=pop.get_Cost()+1))
            visited.add(tuple(pop.move_Right()))
        if pop.try_Up() and tuple(pop.move_Up()) not in visited:
            moves = list(pop.get_Operator())
            moves.append('Down')
            stack.push(Node(state=pop.move_Up(),parent=pop,operator=moves,cost=pop.get_Cost()+1))
            visited.add(tuple(pop.move_Up()))
        if pop.try_Down() and tuple(pop.move_Down()) not in visited:
            moves = list(pop.get_Operator())
            moves.append('Up')
            stack.push(Node(state=pop.move_Down(),parent=pop,operator=moves,cost=pop.get_Cost()+1))
            visited.add(tuple(pop.move_Down()))

    else:
        solution = stack.pop()
        while not stack.isEmpty():
            if stack.top().get_Cost() <= solution.get_Cost():
                stack.pop()
            else:
                max_search_depth = stack.top().get_Cost()
                break
        else:
            max_search_depth = solution.get_Cost()
        return solution




def getState(x):
	x = x.split(',')
	y = []
	for i in x:
		y.append(int(i))
	return y

def main():
    goalState = [
                    [0,1,2,3,4,5,6,7,8], [1,0,2,3,4,5,6,7,8],  [1,2,3,0,4,5,6,7,8],
                    [1,2,3,4,0,5,6,7,8], [1,2,3,4,5,0,6,7,8],  [1,2,3,4,5,6,0,7,8],
                    [1,2,3,4,5,6,7,8,0], [1,2,0,3,4,5,6,7,8],  [1,2,3,4,5,6,7,0,8]
                ]
    stateGoal = goalState[6]

    try:
        initial_state = getState(sys.argv[2])
    except:
        print('You must enter \'bfs, ast, or dfs\' followed by current configuration of the puzzle')
        sys.exit(0)

    initial = Node(state=initial_state)

    if sys.argv[1] == 'bfs':
        start_time = time.time()

        queue.push(initial)

        solution = BFS(initial, stateGoal)

        path_to_goal = solution.get_Operator()
        search_depth = cost_of_path = solution.get_Cost()

        f = open('solution.txt', 'w')
        f.write('path_to_goal: %s\ncost_of_path: %d\nnodes_expanded: %d\nsearch_depth: %d\nmax_search_depth: %d\nrunning_time: %.8f\nmax_ram_usage: %.8f' %(str(path_to_goal),cost_of_path,node_expanded,search_depth,max_search_depth,(time.time()-start_time),resource.getrusage(resource.RUSAGE_SELF).ru_maxrss-start_ram))
    elif sys.argv[1] == 'ast':
        start_time = time.time()

        heap.push(initial)

        solution = ast(initial, stateGoal)

        path_to_goal = solution.get_Operator()
        search_depth = cost_of_path = solution.get_Cost()

        f = open('output.txt', 'w')
        f.write('path_to_goal: %s\ncost_of_path: %d\nnodes_expanded: %d\nsearch_depth: %d\nmax_search_depth: %d\nrunning_time: %.8f\nmax_ram_usage: %.8f' %(str(path_to_goal),cost_of_path,node_expanded,search_depth,max_search_depth,(time.time()-start_time),resource.getrusage(resource.RUSAGE_SELF).ru_maxrss-start_ram))

    elif sys.argv[1] == 'dfs':
        start_time = time.time()

        stack.push(initial)

        solution = dfs(initial, stateGoal)

        path_to_goal = solution.get_Operator()
        search_depth = cost_of_path = solution.get_Cost()

        f = open('output.txt', 'w')
        f.write('path_to_goal: %s\ncost_of_path: %d\nnodes_expanded: %d\nsearch_depth: %d\nmax_search_depth: %d\nrunning_time: %.8f\nmax_ram_usage: %.8f' %(str(path_to_goal),cost_of_path,node_expanded,search_depth,max_search_depth,(time.time()-start_time),resource.getrusage(resource.RUSAGE_SELF).ru_maxrss-start_ram))

    else:
        print("Please enter ast, bfs, or dfs")
        sys.exit(0)

if __name__ == '__main__':
    main()
