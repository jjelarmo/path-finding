import pygame, sys, random
from pygame.math import Vector2

class NODE(object):
    def __init__(self,x,y):
        self.coordinates=(x,y)
        self.predecessor=None
        self.status="unvisited"
        self.step=0
        
class BOX(object):
    def __init__(self,x,y):
        self.pos = Vector2(x,y)
        self.node = NODE(x,y)
        self.neighbors=[]
        
    def draw_box(self):
        outer_box = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size ,cell_size,cell_size)
        inner_box = pygame.Rect((self.pos.x * cell_size)+2.75, (self.pos.y * cell_size)+2.75,cell_size-5,cell_size-5)
        pygame.draw.rect(screen, (255,255,255), outer_box)
        pygame.draw.rect(screen, (120,140,150), inner_box)
        
    def marked_wall(self):
        inner_box = pygame.Rect((self.pos.x * cell_size)+2.75, (self.pos.y * cell_size)+2.75,cell_size-5,cell_size-5)
        pygame.draw.rect(screen, (150,255,150), inner_box)
        self.node.status = "marked"

    def visit_node(self):
        inner_box = pygame.Rect((self.pos.x * cell_size)+2.75, (self.pos.y * cell_size)+2.75,cell_size-5,cell_size-5)
        pygame.draw.rect(screen, (255,255,47), inner_box)
        self.node.status = "visited"

    def set_source(self):
        inner_box = pygame.Rect((self.pos.x * cell_size)+2.75, (self.pos.y * cell_size)+2.75,cell_size-5,cell_size-5)
        pygame.draw.rect(screen, (255,0,0), inner_box)
        self.node.status = "source"

    def set_destination(self):
        inner_box = pygame.Rect((self.pos.x * cell_size)+2.75, (self.pos.y * cell_size)+2.75,cell_size-5,cell_size-5)
        pygame.draw.rect(screen, (150,0,220), inner_box)
        self.node.status = "destination"

    def trace_path(self):
        inner_box = pygame.Rect((self.pos.x * cell_size)+2.75, (self.pos.y * cell_size)+2.75,cell_size-5,cell_size-5)
        pygame.draw.rect(screen, (150,0,220), inner_box)

    def find_neighbors(self,grid):
        x,y = int(self.pos.x), int(self.pos.y)
        potential_neighbors=[(x-1,y), (x+1,y), (x,y-1), (x,y+1), (x+1,y+1), (x+1,y-1), (x-1,y-1), (x-1,y+1)]
        for (new_x, new_y) in potential_neighbors:
            if new_x<cell_number-1 and new_x>0 and new_y<cell_number-1 and new_y>0:
                self.neighbors.append(grid[new_x][new_y])
                #grid[new_x][new_y].visit_node()
        return self.neighbors

class Queue(object):

    def __init__(self):
        self.array=[]

    def __len__(self):
        return len(self.array)

    def is_empty(self):
        return len(self)==0

    def enqueue(self,i):
        self.array.append(i)

    def dequeue(self):
        return self.array.pop(0)

def bfs(grid,source,destination):
    q=Queue()
    q.enqueue(source)
    source.node.status = "found"
    
    while(not q.is_empty()):
        current_node = q.dequeue()
        for next_node in current_node.find_neighbors(grid):
            if next_node.node.status == "destination":
                next_node.node.predecessor = current_node
                return True
            elif next_node.node.status == "unvisited":
                next_node.node.status = "found"
                next_node.node.predecessor = current_node
                next_node.visit_node()
                pygame.time.wait(10)
                pygame.display.update()
                q.enqueue(next_node)
        current_node.node.status = "visited"
    if q.is_empty():
        return False

def source_to_destination(grid, source, destination):
    current_node = destination
    current_node.trace_path()
    while(current_node != source):
       current_node = current_node.node.predecessor
       current_node.trace_path()
        
pygame.init()
cell_size = 20
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size)) #origin top left corner
#clock = pygame.time.Clock()
start_search = False
SCREEN_UPDATE = pygame.USEREVENT
#pygame.time.set_timer(SCREEN_UPDATE,2)
screen.fill((175,215,70))

grid = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]

for x in range(cell_number):
    for y in range(cell_number):
        grid[x][y] = BOX(x,y)
        grid[x][y].draw_box()

source=grid[1][1]
source.set_source()
destination=grid[15][15]
destination.set_destination()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            (click_x, click_y) = pygame.mouse.get_pos()
            pos_x, pos_y = click_x // cell_size, click_y // cell_size
            grid[pos_x][pos_y].marked_wall()
        if event.type == pygame.KEYDOWN:
            if event.key== pygame.K_SPACE:
                if(bfs(grid,source,destination)):
                    source_to_destination(grid, source, destination)
                else:
                    print("Not found")
                    
    pygame.display.update()
    #clock.tick(100000)
