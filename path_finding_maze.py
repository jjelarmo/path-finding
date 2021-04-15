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

def search_next(grid,current_node):
    x,y = int(current_node.pos.x), int(current_node.pos.y)
    if grid[x+1][y+1].node.status == "unvisited" or grid[x+1][y+1].node.status == "destination": 
        next_node=grid[x+1][y+1]
    elif grid[x][y+1].node.status == "unvisited" or grid[x][y+1].node.status == "destination":
        next_node=grid[x][y+1]
    elif grid[x+1][y].node.status == "unvisited" or grid[x+1][y].node.status == "destination":
        next_node=grid[x+1][y]
    print(x,y)
    next_node.visit_node()
    return next_node

        
def bfs(grid,source,destination):
    q=Queue()
    current_node=search_next(grid,source)
    current_node.node.predecessor = source
    q.enqueue(current_node)
    
    while(current_node != destination):
        x,y = int(current_node.pos.x), int(current_node.pos.y)

        if x<cell_number-1 and x>0 and y<cell_number-1 and y>0:
            current_node=q.dequeue()

            if grid[x+1][y+1].node.status == "unvisited" or grid[x+1][y+1].node.status == "destination": 
                q.enqueue(grid[x+1][y+1])
                grid[x+1][y+1].visit_node()
                grid[x+1][y+1].node.predecessor = grid[x][y]

            if grid[x][y+1].node.status == "unvisited" or grid[x][y+1].node.status == "destination":
                q.enqueue(grid[x][y+1])
                grid[x][y+1].visit_node()
                grid[x][y+1].node.predecessor = grid[x][y]
                
            if grid[x+1][y].node.status == "unvisited" or grid[x+1][y].node.status == "destination":
                q.enqueue(grid[x+1][y])
                grid[x+1][y].visit_node()
                grid[x+1][y].node.predecessor = grid[x][y]

    current_node = destination
    current_node.trace_path()
    while(current_node != source):
       current_node = current_node.node.predecessor
       current_node.trace_path()
        
pygame.init()
cell_size = 20
cell_number = 20
screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size)) #origin top left corner
clock = pygame.time.Clock()
start_search = False
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE,2000)
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
                #pass
                bfs(grid,source,destination)
    pygame.display.update()
    clock.tick(100000)
