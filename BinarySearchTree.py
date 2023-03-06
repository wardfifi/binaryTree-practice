# BinarySearchTree.py

from TreeNode import TreeNode

class BinarySearchTree:
	def __init__(self):
		self.root = None # A BST just needs a reference to the root node
		self.size = 0 # Keeps track of number of nodes

	def length(self):
		return self.size

	def put(self,key,val):
		if self.root:
			self._put(key,val,self.root)
		else:
			self.root = TreeNode(key,val)
		self.size = self.size + 1

	# helper method to recursively walk down the tree
	def _put(self,key,val,currentNode):
		if key < currentNode.key:
			if currentNode.hasLeftChild():
				self._put(key,val,currentNode.leftChild)
			else:
				currentNode.leftChild = \
				TreeNode(key,val,parent=currentNode)
		else:
			if currentNode.hasRightChild():
				self._put(key,val,currentNode.rightChild)
			else:
				currentNode.rightChild = \
				TreeNode(key,val,parent=currentNode)


	def get(self,key): # returns payload for key if it exists
		if self.root:
			res = self._get(key,self.root)
			if res:
				return res.payload
			else:
				return None
		else:
			return None

	# helper method to recursively walk down the tree
	def _get(self,key,currentNode): 
		if not currentNode:
			return None
		elif currentNode.key == key:
			return currentNode
		elif key < currentNode.key:
			return self._get(key,currentNode.leftChild)
		else:
			return self._get(key,currentNode.rightChild)


	# BinarySearchTree.py (continued)

def delete(self,key):
	if self.size > 1:
		nodeToRemove = self._get(key,self.root)
		if nodeToRemove:
			self.remove(nodeToRemove) # remove modifies the tree
			self.size = self.size-1
		else:
			raise KeyError('Error, key not in tree')
	elif self.size == 1 and self.root.key == key:
		self.root = None
		self.size = self.size - 1
	else:
		raise KeyError('Error, key not in tree')

# Used to remove the node and account for BST deletion cases
def remove(self,currentNode):
	# Case 1: Node to remove is leaf
	if currentNode.isLeaf():
		if currentNode == currentNode.parent.leftChild:
			currentNode.parent.leftChild = None
		else:
			currentNode.parent.rightChild = None

	# Case 3: Node to remove has both children
	elif currentNode.hasBothChildren():
		# Need to find the successor, remove successor, and replace
		# currentNode with successor's data / payload
		succ = currentNode.findSuccessor()
		succ.spliceOut()
		currentNode.key = succ.key
		currentNode.payload = succ.payload
		

	# Case 2: Node to remove has one child
	else:
		# Node has leftChild
		if currentNode.hasLeftChild():
			if currentNode.isLeftChild():
				currentNode.leftChild.parent = currentNode.parent
				currentNode.parent.leftChild = currentNode.leftChild
			elif currentNode.isRightChild():
				currentNode.leftChild.parent = currentNode.parent
				currentNode.parent.rightChild = currentNode.leftChild
			else: # currentNode is the Root
				currentNode.replaceNodeData(currentNode.leftChild.key,
					currentNode.leftChild.payload,
					currentNode.leftChild.leftChild,
					currentNode.leftChild.rightChild)
            
		# Node has rightChild
		else:
			if currentNode.isLeftChild():
				currentNode.rightChild.parent = currentNode.parent
				currentNode.parent.leftChild = currentNode.rightChild
			elif currentNode.isRightChild():
				currentNode.rightChild.parent = currentNode.parent
				currentNode.parent.rightChild = currentNode.rightChild
			else:
				currentNode.replaceNodeData(currentNode.rightChild.key,
					currentNode.rightChild.payload,
					currentNode.rightChild.leftChild,
					currentNode.rightChild.rightChild)

	def findSuccessor(self):
		succ = None
		# Check if node has a right subtree...
		if self.hasRightChild():
			# traverse through left children (min)
			succ = self.rightChild.findMin()
		return succ

	# Find minimum value in a subtree by walking down the left children
	def findMin(self):
		current = self
		while current.hasLeftChild():
			current = current.leftChild
		return current

	# Used to delete the successor
	def spliceOut(self):
		# Case 1:
		# If node to be removed is a leaf, set parent's left or right
		# child references to None
		if self.isLeaf():
			if self.isLeftChild():
				self.parent.leftChild = None
			else:
				self.parent.rightChild = None

		# Case 2:
		# Not a leaf node. Should only have a right child for BST
		# removal
		elif self.hasAnyChildren():
			if self.hasRightChild():
				if self.isLeftChild():
					self.parent.leftChild = self.rightChild
				else:
					self.parent.rightChild = self.rightChild
				self.rightChild.parent = self.parent
# Used for pytesting
def inOrder(self, node):
        ret = ""
        if node != None:
            ret += self.inOrder(node.leftChild)
            ret += str(node.key) + " "
            ret += self.inOrder(node.rightChild)
        return ret
	
# pytests

def test_deleteSingleRoot():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    assert BST.inOrder(BST.root) == "10 "
    BST.delete(10)
    assert BST.size == 0
    assert BST.root == None

def test_deleteRootOneChild():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    BST.put(5, "five")
    assert BST.inOrder(BST.root) == "5 10 "
    BST.delete(10)
    assert BST.inOrder(BST.root) == "5 "
    assert BST.root.key == 5

def test_deleteLeaf():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    BST.put(15, "fifteen")
    BST.put(5, "five")
    BST.put(2, "two")
    assert BST.inOrder(BST.root) == "2 5 10 15 "
    BST.delete(15)
    assert BST.inOrder(BST.root) == "2 5 10 "

def test_deleteNodeOneChild():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    BST.put(15, "fifteen")
    BST.put(5, "five")
    BST.put(2, "two")
    assert BST.root.leftChild.key == 5
    BST.delete(5)
    assert BST.inOrder(BST.root) == "2 10 15 "
    assert BST.root.leftChild.key == 2
    assert BST.root.leftChild.parent.key == 10
    
def test_deleteRootWithTwoChildren():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    BST.put(15, "fifteen")
    BST.put(5, "five")
    BST.put(3, "three")
    BST.put(7, "seven")
    BST.put(12, "twelve")
    BST.put(17, "seventeen")
    assert BST.inOrder(BST.root) == "3 5 7 10 12 15 17 "
    BST.delete(10)
    assert BST.inOrder(BST.root) == "3 5 7 12 15 17 "

def test_deleteNodeWithTwoChildren():
    BST = BinarySearchTree()
    BST.put(10, "ten")
    BST.put(15, "fifteen")
    BST.put(5, "five")
    BST.put(3, "three")
    BST.put(7, "seven")
    BST.put(12, "twelve")
    BST.put(17, "seventeen")
    BST.delete(15)
    assert BST.inOrder(BST.root) == "3 5 7 10 12 17 "
    BST.delete(5)
    assert BST.inOrder(BST.root) == "3 7 10 12 17 "