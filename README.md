
# path-finding
Path Finding using Breadth First Search

This is a path finding implementation using Breadth First Search
Details:
1. Visualization is implemented using Pygame module
- the red node corresponds to the source
- the violate node correspons to the destination
- user has the ability to click each gray node to convert to a wall (represented as green node)
<img width="298" alt="Capture" src="https://user-images.githubusercontent.com/59645751/115138151-0d459a00-a05d-11eb-88cd-825a98944757.PNG">

2. Once the walls are setup by the user, they can hit space for the BFS routine to start searching
- the yellow nodes corresponds to the visited nodes
- the implementation uses an exhaustive search to try all neighboring nodes of the current node until the destination is found

3. After the search, the program will highlight the optimized path from source to destination in violet
<img width="299" alt="Finished_search" src="https://user-images.githubusercontent.com/59645751/115138292-c0ae8e80-a05d-11eb-9685-5889fd7e13d9.PNG">

