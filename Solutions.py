

# Question 1
'''Given two strings s and t, determine whether some anagram of t is a substring of s. For example: if s = "udacity" and 
t = "ad", then the function returns True. Your function definition should look like:question1(s, t) and return a boolean
True or False.'''


def count_dict(strng):
        dct = {}
        for i in strng:
            if i in dct: dct[i] += 1
            else: dct[i] = 1
        return dct
    
def question1(s,t): 
    if not t or not s: return "at least one of the input data are empty"
    count_t = count_dict(t.lower())
    count_s = count_dict(s.lower())
    #if a character in t doesn't exist in s or number of a given character in s is smaller than t then False
    for i in count_t: 
        if i not in count_s or count_s[i] < count_t[i]: return False
    return True


print question1("udacity","ad")
print question1("sohrab","bar")
print question1("nanodegree","regfn")
print question1("machinlearning","ninm")
print question1("sebastianthrun","abes")
print question1("sebastianthrun","")
print question1("","abes")

#True
#True
#False
#True
#True
#at least one of the input data are empty
#at least one of the input data are empty


# Question 2
'''Given a string a, find the longest palindromic substring contained in a. Your function definition should look like 
question2(a), and return a string.'''


def question2(a):
    
    a = str(a)
    if not a: 
        return "you input value is empty"
    
    max_len = 1 # we assume that a single character is a palindrome of length 1
    start_point = 0 
    
    # define the two pointers 
    low = 0
    high = 0
 
    for c in range(1, len(a)):
        
        # find the longest even palindrome centered at c and c-1
        low = c - 1
        high = c
        while low >= 0 and high < len(a) and a[low] == a[high]:
            if high - low + 1 > max_len:
                start_point = low
                max_len = high - low + 1
            low = low-1
            high += 1
 
        # find the longest odd palindrome centered at c
        low = c - 1
        high = c + 1
        while low >= 0 and high < len(a) and a[low] == a[high]:
            if high - low + 1 > max_len:
                start_point = low
                max_len = high - low + 1
            low = low-1
            high += 1
            
    return a[start_point:start_point + max_len]
 
print question2('aahaah')    
print question2('toyota') 
print question2('acrobats stab orca')
print question2('satan natasha!')  
print question2('foliated detail')  
print question2(1222187) 
print question2("")


#aahaa
#toyot
#bats stab
#satan natas
#liated detail
#12221
#you input value is empty




# Question 3
'''Given an undirected graph G, find the minimum spanning tree within G. A minimum spanning tree connects all vertices 
in a graph with the smallest possible total weight of edges. Your function should take in and return an adjacency list 
structured like this:

{'A': [('B', 2)],
 'B': [('A', 2), ('C', 5)], 
 'C': [('B', 5)]}
Vertices are represented as unique strings. The function definition should be question3(G)'''

def question3(G): 
    if not G: 
        return "your graph is empty"
    else:
        # reformat the data to separate edges and vertices
        adj = []
        for k,v in G.items(): 
            nodes = [i[0] for i in v]
            weights = [i[1] for i in v]
            lst = [(k,n,w) for n,w in zip(nodes,weights)]
            adj.append(lst)
        adj = [sorted(i) for j in adj for i in j]
        edges = sorted(map(tuple, adj))
        vertices = sorted(G.keys())
    
    
        MST=[]
        forming_edges = []
        for i in edges:
            for j in vertices:
                if i[1] in j: i1 = vertices.index(j) # get index of first node in edge j in vertices list
                if i[2] in j: i2 = vertices.index(j)# get index of second node in edge j in vertices list

            if i1 < i2:
                vertices[i1] = set.union(set(vertices[i1]), set(vertices[i2]))
                vertices.pop(i2)
                MST.append(i)
            if i1 > i2:
                vertices[i2] = set.union(set(vertices[i1]), set(vertices[i2]))
                vertices.pop(i1)
                MST.append(i)
            
        final_MST = {} 
        for weight,u,v in MST:
            if u not in final_MST:
                final_MST[u] = []
            final_MST[u].append((v, weight))
        
            if v not in final_MST:
                final_MST[v] = []
            final_MST[v].append((u, weight))
        
        for j in G: 
            if not j in final_MST.keys(): print j, " is not connected to other nodes"

        return "minimum spanning tree:",final_MST


G1 = {'A': [('B', 7), ('D', 5)],
         'B': [('A', 7), ('C', 8), ('D', 9), ('E', 7)],
         'C': [('B', 8), ('E', 5)],
         'D': [('A', 5), ('B', 9), ('E', 15), ('F', 6)],
         'E': [('B', 7), ('C', 5), ('D', 15), ('F', 8), ('G', 9)],
         'F': [('D', 6), ('E', 8), ('G', 11)],
         'G': [('E', 9), ('F', 11)]}

G2 = {'A': [('D', 5), ('B', 7)],
         'B': [('A', 7), ('E', 7)],
         'C': [('E', 5)],
         'D': [('A', 5), ('F', 6)],
         'E': [('C', 5), ('B', 7), ('G', 9)],
         'F': [('D', 6)],
         'G': [('E', 9)]} 

G3 = {'A':[('B',2),('C',4)],
     'B':[('A',2),('C',3),('D',4)],
     'C':[('A',4),('B',3),('D',1)],
     'D':[('B',4),('C',1)]}

G4 = {'A':[('B',4),('D',5),('E',3)],
     'B':[('A',4),('C',2),('D',6)],
     'C':[('B',2),('E',1)],
     'D':[('A',5),('B',6)],
     'E':[('A',3),('C',1)]}

G5 = {'A':[('B',2)],'B':[('A',2),('C',2)],'C':[('B',2)],'D':[]}


print question3(G1),"\n"

#('minimum spanning tree:', {'A': [('D', 5), ('B', 7)], 'C': [('E', 5)], 'B': [('A', 7), ('E', 7)], 'E': [('C', 5), ('B', 7), ('G', 9)], 
#'D': [('A', 5), ('F', 6)], 'G': [('E', 9)], 'F': [('D', 6)]}) 

print question3(G2),"\n"

#('minimum spanning tree:', {'A': [('D', 5), ('B', 7)], 'C': [('E', 5)], 'B': [('A', 7), ('E', 7)], 
 # 'E': [('C', 5), ('B', 7), ('G', 9)], 'D': [('A', 5), ('F', 6)], 'G': [('E', 9)], 'F': [('D', 6)]}) 

print question3(G3),"\n"

#('minimum spanning tree:', {'A': [('B', 2)], 'C': [('D', 1), ('B', 3)], 'B': [('A', 2), ('C', 3)], 'D': [('C', 1)]}) 

print question3(G4),"\n"

#('minimum spanning tree:', {'A': [('E', 3), ('D', 5)], 'C': [('E', 1), ('B', 2)], 'B': [('C', 2)], 'E': [('C', 1), ('A', 3)], 'D': [('A', 5)]}) 


print question3(G5),"\n"

#D  is not connected to other nodes
#('minimum spanning tree:', {'A': [('B', 2)], 'C': [('B', 2)], 'B': [('A', 2), ('C', 2)]}) 

print question3({}),"\n"

#your graph is empty 


# In[11]:

# Question 4
'''Find the least common ancestor between two nodes on a binary search tree. The least common ancestor is the farthest
node from the root that is an ancestor of both nodes. For example, the root is a common ancestor of all nodes on the 
tree, but if both nodes are descendents of the root's left child, then that left child might be the lowest common ancestor
. You can assume that both nodes are in the tree, and the tree itself adheres to all BST properties. The function definition 
should look like question4(T, r, n1, n2), where T is the tree represented as a matrix, where the index of the list is 
equal to the integer stored in that node and a 1 represents a child node, r is a non-negative integer representing the root,
and n1 and n2 are non-negative integers representing the two nodes in no particular order. For example, one test case 
might be:

question4([[0, 1, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 0, 0],
           [1, 0, 0, 0, 1],
           [0, 0, 0, 0, 0]],
          3,
          1,
          4)
and the answer would be 3.'''

def find_parent(T, n):
    rows_len = len(T)
    for j in range(rows_len):
        if T[j][n] == 1: return j
    return

def question4(T, r, n1, n2):
    if not T: 
        return "Input matrix is empty"
    else: 
        parent_lst = []
        while not n1 == r:
            n1 = find_parent(T, n1)
            parent_lst.append(n1)
        if not parent_lst:
            return "one or two nodes have no parents"
        while not n2 == r:
            n2 = find_parent(T, n2)
            if n2 in parent_lst:
                return "Node {} is the least common ancestor".format(n2)
        return "One or two nodes are roots"
    
print question4([[0,1,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[1,0,0,0,1],[0,0,0,0,0]],3,1,4),"\n"

#Node 3 is the least common ancestor 

print question4([[0,0,0,0,0],[1,0,1,0,0],[0,0,0,0,0],[0,1,0,0,1],[0,0,0,0,0]],3,2,2),"\n"

#Node 1 is the least common ancestor 

print question4([[0,1,1,0,0],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],0,3,4),"\n"

#Node 1 is the least common ancestor

print question4([[0,1,1,0,0],[0,0,0,1,1],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]],0,3,4),"\n"

#Node 1 is the least common ancestor

print question4([[0,1,1,0,0,0,0],[0,0,0,1,1,0,0],[0,0,0,0,0,1,1],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],0,5,6),"\n"

#Node 2 is the least common ancestor

print question4([[0,1,1,0,0,0,0],[0,0,0,1,1,0,0],[0,0,0,0,0,1,1],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]],0,0,1),"\n"

#one or two nodes have no parents

print question4([],3,1,4)

#Input matrix is empty




# Question 5
'''Find the element in a singly linked list that's m elements from the end. For example, if a linked list has 5 elements,
the 3rd element from the end is the 3rd element. The function definition should look like question5(ll, m), where ll is
the first node of a linked list and m is the "mth number from the end". You should copy/paste the Node class below to use 
as a representation of a node in the linked list. Return the value of the node at that position.

class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def question5(ll, m):
    
    ll1 = ll
    ll2 = ll
    
    if m<=0: 
        return "second input should be a positive number"
    else: 
        
        for a in range(m):
            if not ll1: return None
            ll1 = ll1.next
            
        while ll1:
            ll1 = ll1.next
            ll2 = ll2.next
            
        return ll2.data

# construct the linked list
ll1 = Node(1)
ll2 = Node(2)
ll3 = Node(3)
ll4 = Node(4)
ll5 = Node(5)
ll4.next = ll5
ll3.next = ll4
ll2.next = ll3
ll1.next = ll2

print question5(ll1, 2)
#4
print question5(ll3, 1)
#5
print question5(ll2, 2)
#4
print question5(ll2, 3) 
#3
print question5(ll2, 3) 
#3
print question5(ll2, 0)
#second input should be a positive number
print question5(ll2, 10)
#None