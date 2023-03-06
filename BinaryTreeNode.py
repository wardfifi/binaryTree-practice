#BinaryTreeNode

class BinaryTreeNode:
	def __init__(self, rootObj):
		self.key = rootObj
		self.leftChild = None
		self.rightChild = None

	def insertLeft(self, newNode):
		# Case 1: Node does not have a left child
		if self.leftChild == None:
			self.leftChild = BinaryTreeNode(newNode)
		else: # Case 2: Node has a left child
			t = BinaryTreeNode(newNode)
			t.leftChild = self.leftChild # Links the left sub tree
			self.leftChild = t

	def insertRight(self, newNode):
		# Case 1: Node does not have a right child
		if self.rightChild == None:
			self.rightChild = BinaryTreeNode(newNode)
		else: # Case 2: Node has a right child
			t = BinaryTreeNode(newNode)
			t.rightChild = self.rightChild # Links the right sub tree
			self.rightChild = t

	def getRightChild(self):
		return self.rightChild

	def getLeftChild(self):
		return self.leftChild

	def setRootVal(self, obj):
		self.key = obj

	def getRootValue(self):
		return self.key
# PYTESTS
def test_createNode():
	node = BinaryTreeNode("A")
	assert node.getRootValue() == "A"
	assert node.getLeftChild() == None
	assert node.getRightChild() == None

def test_leftNode():
	node = BinaryTreeNode("A")
	node.insertLeft("B")
	assert node.getLeftChild().getRootValue() == "B"
	assert node.getRootValue() == "A"
	assert node.getRightChild() == None
	assert node.getLeftChild().getLeftChild() == None
	assert node.getLeftChild().getRightChild() == None

def test_rightNode():
	node = BinaryTreeNode("A")
	node.insertRight("B")
	assert node.getRightChild().getRootValue() == "B"
	assert node.getRootValue() == "A"
	assert node.getLeftChild() == None
	assert node.getRightChild().getLeftChild() == None
	assert node.getRightChild().getRightChild() == None

def test_insertLeft():
	node = BinaryTreeNode("A")
	node.insertLeft("B")
	node.insertLeft("C")
	node.insertLeft("D")

	temp = node
	s = ""
	while temp != None:
		s = s + temp.getRootValue()
		temp = temp.getLeftChild()
	assert s == "ADCB"

def preorder(tree):
	ret = ""
	if tree != None:
		ret += tree.getRootValue()
		ret += preorder(tree.getLeftChild())
		ret += preorder(tree.getRightChild())
	return ret

def inorder(tree):
	ret = ""
	if tree != None:
		ret += inorder(tree.getLeftChild())
		ret += tree.getRootValue()
		ret += inorder(tree.getRightChild())
	return ret

def postorder(tree):
	ret = ""
	if tree != None:
		ret += postorder(tree.getLeftChild())
		ret += postorder(tree.getRightChild())
		ret += tree.getRootValue()
	return ret
#pytests
def test_preorder():
	# Create tree
	root = BinaryTreeNode("A")
	root.insertLeft("B")
	root.getLeftChild().insertLeft("D")
	root.insertRight("C")
	root.getRightChild().insertLeft("E")
	root.getRightChild().insertRight("F")
	assert preorder(root) == "ABDCEF"

def test_inorder():
	# Create tree
	root = BinaryTreeNode("A")
	root.insertLeft("B")
	root.getLeftChild().insertLeft("D")
	root.insertRight("C")
	root.getRightChild().insertLeft("E")
	root.getRightChild().insertRight("F")
	assert inorder(root) == "DBAECF"

def test_postorder():
	# Create tree
	root = BinaryTreeNode("A")
	root.insertLeft("B")
	root.getLeftChild().insertLeft("D")
	root.insertRight("C")
	root.getRightChild().insertLeft("E")
	root.getRightChild().insertRight("F")
	assert postorder(root) == "DBEFCA"