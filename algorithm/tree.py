# 二叉树中的节点类
class BinaryTreeNode(object):
    def __init__(self,data=None,left=None,right=None) -> None:
        self.data = data
        self.left = left
        self.right = right
# 二叉树
class BinaryTree(object):
    def __init__(self) -> None:
        self.root = None
    def create(self,show_data=-1,show_node='根节点'):
        print(("当前父节点为%d" + show_node) % show_data)
        input_text = input('输入二叉树节点的值,空值直接回车:')
        if input_text is '':
            return
        t_bi_t = BinaryTreeNode(data=int(input_text))
        if self.root is None:
            self.root = t_bi_t
        # 创建节点
        t_bi_t.left = self.create(t_bi_t.data,"创建左节点")
        t_bi_t.right = self.create(t_bi_t.data,"创建右节点")
        return t_bi_t
    # 获得二叉树的深度
    def getHeight(self,node=None):
        if node is None:
            print("空树!")
            return 0
        elif node.left is None and node.right is None:
            return 1
        elif node.left is not None and node.right is None:
            return 1 + self.getHeight(node.left)
        elif node.right is not None and node.left is None:
            return 1 + self.getHeight(node.right)
        else:
            return 1 + max(self.getHeight(node.left),self.getHeight(node.right))
    # 
    def getDataByLine(self,node=None):
        if node is None:
            return
        else:
            print(node.data,end=',')
            self.getDataByLine(node.right)
            self.getDataByLine(node.left)
    # 先序遍历
    # 先访问根节点,再遍历左子树,最后遍历右子树.
    def prOrderTraverse(self,node=None):
        if node is None:
            return
        else:
            print(node.data,end=',')
            self.prOrderTraverse(node.left)
            self.prOrderTraverse(node.right)
    # 中序遍历
    # 先遍历左子树,再访问根节点,最后遍历右子树
    def midOrderTraverse(self,node=None):
        if node is None:
            return
        else:
            self.midOrderTraverse(node.left)
            print(node.data,end=',')
            self.midOrderTraverse(node.right)
    # 后序遍历
    # 先遍历左子树,再遍历右子树,最后访问根节点
    def behOrderTraverse(self,node=None):
        if node is None:
            return
        else:
            self.behOrderTraverse(node.left)
            self.behOrderTraverse(node.right)
            print(node.data,end=',')
# 测试
bi_t = BinaryTree()
bi_t.create()
print("二叉树的深度是:",bi_t.getHeight(bi_t.root))
print("________下方是二叉树中的元素________")
bi_t.getDataByLine(bi_t.root)