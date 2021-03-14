## Recursive TREE
class TreeNode:
    def __init__(self, idata):
        self.data = idata
        self.children = []

    def add_child(self, childnode):
        self.children.append(childnode)

    def get_data(self):
        return self.data

    def get_children(self):
        return self.children

class Tree:
    def __init__(self, rootvalue):
        self.root =  TreeNode(rootvalue)

    def rec_depth_first_search(self, searchvalue, current_node):
        if current_node.get_data() = searchvalue:
            return True
        cur_children = current_node.get_children()
        for child in cur_children:
            if rec_depth_first_search(searchvalue, child):
                return True
        return False

    def depth_first_search(self, searchvalue):
        currentnode = self.root
        return rec_depth_first_search(searchvalue, currentnode)

## Deepth First Search (wild loop) Not Recursive - Using Stacks

    def dfs_w(self, searchvalue):
        currentnode = root
        searchstack = [root]
        while len(searchstack > 0):
            currentnode = searchstack.pop()
            if currentnode.getdata() == searchvalue:
                return True
            for child in currentnode.getchildren():
                searchstack.append(child)
        return False

## Breath Search (wild loop) Not Recursive -  Using Queue
    
    def bfs_w(self, searchvalue):
        currentnode = root
        searchqueue = [root]
        while len(searchqueue > 0):
            currentnode = searchqueue.pop(0)
            if currentnode.getdata() == searchvalue:
                return True
            for child in currentnode.getchildren():
                searchqueue.append(child)
        return False

## Graph ###
    
class GraphNode:
    def __init__(self, idata):
        self.data = idata
        self.children = []
        self.seen_flag = False

    def add_child(self, childnode):
        self.children.append(childnode)

    def get_data(self):
        return self.data

    def get_children(self):
        return self.children
    
    def mark_seen(self):
        self.seen_flag = True

    def is_seen(self):
        return self.seen_flag 
class Graph:
    def __init__(self, rootvalue):
        self.root =  GraphNode(rootvalue)

    def rec_depth_first_search(self, searchvalue, current_node):
        if current_node.get_data() = searchvalue:
            return True
        else:
            current_node.mark_seen()
            
        cur_children = current_node.get_children()
        for child in cur_children:
            if not child.is_seen()  
                if rec_depth_first_search(searchvalue, child):
                    return True
        return False

    def depth_first_search(self, searchvalue):
        currentnode = self.root
        return rec_depth_first_search(searchvalue, currentnode)

## Deepth First Search (wild loop) Not Recursive - Using Stacks

    def dfs_w(self, searchvalue):
        currentnode = root
        searchstack = [root]
        while len(searchstack > 0):
            currentnode = searchstack.pop()
            if currentnode.getdata() == searchvalue:
                return True
            for child in currentnode.getchildren():
                if not child.is_seen():
                    searchstack.append(child)
        return False

## Breath Search (wild loop) Not Recursive -  Using Queue SHORTEST SOLUTION
    
    def bfs_w(self, searchvalue):
        currentnode = root
        searchqueue = [root]
        while len(searchqueue > 0):
            currentnode = searchqueue.pop(0)
            if currentnode.getdata() == searchvalue:
                return True
            for child in currentnode.getchildren():
                if not child.is_seen():
                    searchqueue.append(child)
        return False
