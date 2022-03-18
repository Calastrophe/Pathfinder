import numpy as np

class Node:
    def __init__(self, node_count, connections):
        self.nodeNum = node_count
        self.connections = connections

def returnConnections(node):
    connections = []
    which_edge = 0
    for edge in node:
        which_edge += 1
        if edge == 1:
            connections.append(which_edge)
    return connections

def returnNodeList(matrix):
    node_count = 0
    nodeList = []
    for node in matrix:
        node_count += 1
        nodeList.append(Node(node_count,returnConnections(node)))
    return nodeList

def returnPath(nodeList, start, end):
    used_nodes = [start]
    path = [start]
    for node in nodeList:
        if node.nodeNum == start:
            scavengeNodes(node, nodeList, end, path, used_nodes)


# This will solve all paths that don't make a visit to node twice, larger matrices will take more time.
def scavengeNodes(node, nodeList, end, cur_path, used_nodes):
    for connection in node.connections: # Iterate over the connections to the node
        cust_path = cur_path[:]
        if end == connection:
            cust_path.append(end)
            print("New path:", cust_path)
        for obj_node in nodeList: # Match with the class object that contains its number
            if obj_node.nodeNum == connection:
                if obj_node.nodeNum not in cust_path: # Make sure we haven't visited this node yet in our path
                    cust_path.append(obj_node.nodeNum)
                    scavengeNodes(obj_node, nodeList, end, cust_path, used_nodes)

## No specific algorithim involved. Just handmade.
## Unweighted directional graph
if __name__ == "__main__":
    edges = np.random.randint(2, size=81) # Random generation of edges
    matrix = np.reshape(edges, (9,9)) # Reformation of edges
    nodeList = returnNodeList(matrix)
    for node in nodeList:
        print(node.nodeNum, ": ", node.connections)
    path = returnPath(nodeList, 1, 3) ## From 1 to 3 paths, make sure your to is included in the size of your matrix if you change this.
