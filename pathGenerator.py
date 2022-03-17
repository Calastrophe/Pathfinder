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
            if end in node.connections:
                node.connections.remove(end) ## Otherwise you'll just get a singular path...
            scavengeNodes(node, nodeList, end, path, used_nodes)

def scavengeNodes(node, nodeList, end, cur_path, used_nodes):
    for search_node in node.connections: # Iterating over our connections to node
        if search_node not in used_nodes: # If those nodes are not in used_nodes, continue
            for obj_node in nodeList: # Finding our object
                if obj_node.nodeNum == search_node: ## Finding our object that matches our search number
                    curSearch = searchNode(obj_node, end, cur_path) # Search that number for our end node...
                    if curSearch == None:
                        used_nodes.append(search_node)
                        cur_path.append(search_node)
                        scavengeNodes(obj_node, nodeList, end, cur_path, used_nodes)
                    else:
                        used_nodes.append(search_node)
                        print("New path: ", curSearch)

def searchNode(node, end, cur_path):
    cust_path = cur_path[:]
    if end in node.connections:
        cust_path.append(node.nodeNum)
        cust_path.append(end)
        return cust_path
    else:
        return None


## No specific algorithim involved, just a linear search of every path possible.
## Unweighted directional graph
if __name__ == "__main__":
    edges = np.random.randint(2, size=3600) # Random generation of edges
    matrix = np.reshape(edges, (60,60)) # Reformation of edges
    nodeList = returnNodeList(matrix)
    for node in nodeList:
        print(node.nodeNum, ": ", node.connections)
    path = returnPath(nodeList, 1, 40)
