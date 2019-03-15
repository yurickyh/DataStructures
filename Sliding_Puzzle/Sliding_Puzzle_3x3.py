import sys
import heapq
import copy

# 0 1 2
# 3 4 5
# 6 7 8
class Sliding_Puzzle:
    def __init__(self, config, parent = None, cost = 1):
        self.config = config
        self.parent = parent
        for i in range(0, 9):
            if(self.config[i/3][(i%3)] == 0):
                self.zero_index = i
        self.cost = cost

    def is_goal_state(self):
        goal_state = [[1,2,3], [4,5,6], [7,8,0]]
        return (self.config == goal_state)

    def get_next_states(self):
        next_states_nodes = []

        # try to move the zero to the left
        if(self.zero_index%3 > 0):
            config_left = copy.deepcopy(self.config)
            # print(config_left)
            # print(self.zero_index)
            config_left[self.zero_index/3][(self.zero_index%3)] = config_left[self.zero_index/3][(self.zero_index%3)-1]
            config_left[self.zero_index/3][(self.zero_index%3)-1] = 0
            next_state_left = Sliding_Puzzle(config_left, self, self.cost+1)
            next_states_nodes.append(next_state_left)

        # try to move the zero to the right
        if(self.zero_index%3 < 2):
            config_right = copy.deepcopy(self.config)
            config_right[self.zero_index/3][(self.zero_index%3)] = config_right[self.zero_index/3][(self.zero_index%3)+1]
            config_right[self.zero_index/3][(self.zero_index%3)+1] = 0
            next_state_right = Sliding_Puzzle(config_right, self, self.cost+1)
            next_states_nodes.append(next_state_right)

        # try to move the zero up
        if(self.zero_index/3 > 0):
            config_up = copy.deepcopy(self.config)
            config_up[self.zero_index/3][(self.zero_index%3)] = config_up[self.zero_index/3-1][(self.zero_index%3)]
            config_up[self.zero_index/3-1][(self.zero_index%3)] = 0
            next_state_up = Sliding_Puzzle(config_up, self, self.cost+1)
            next_states_nodes.append(next_state_up)
        
        # try to move the zero down
        if(self.zero_index/3 < 2):
            config_down = copy.deepcopy(self.config)
            config_down[self.zero_index/3][(self.zero_index%3)] = config_down[self.zero_index/3+1][(self.zero_index%3)]
            config_down[self.zero_index/3+1][(self.zero_index%3)] = 0
            next_state_down = Sliding_Puzzle(config_down, self, self.cost+1)
            next_states_nodes.append(next_state_down) 
        
        return next_states_nodes       

    def solve_puzzle(self):
        pq = []
        count = 0
        heapq.heappush(pq, (self.cost, count, self))
        current_node = heapq.heappop(pq)[2]
        memory = []
        memory.append(current_node.config)
        while(not current_node.is_goal_state()):
            for child_node in current_node.get_next_states():
                if(child_node.config not in memory):
                    count += 1
                    heapq.heappush(pq, (child_node.cost, count, child_node))
                    memory.append(child_node)
            if(len(pq) <= 0):
                return None
            current_node = heapq.heappop(pq)[2]
        return current_node           

def main(*args):
    file = open(sys.argv[1], "r")
    puzzle = [[],[],[]]
    for i in range(0, 3):
        line = file.readline().replace(".", "0").split(" ")
        puzzle[i].append(int(line[0]))
        puzzle[i].append(int(line[1]))
        puzzle[i].append(int(line[2]))
    initial = Sliding_Puzzle(puzzle)
    current_node = initial.solve_puzzle()
    stack = []
    while(current_node.config != initial.config):
        stack.append(current_node.config)
        current_node = current_node.parent
    stack.append(initial.config)
    while(len(stack) > 0):
        last = stack.pop()
        print(last[0])
        print(last[1])
        print(last[2])
        print("")
main()