from .traversals import preorder, inorder, postorder, Node
from .reconstruct import build_from_pre_in, build_from_post_in

def build_sample_tree():
    #        8
    #       / \
    #      3  10
    #     / \   \
    #    1   6   14
    #       / \  /
    #      4  7 13
    n1 = Node("1"); n4 = Node("4"); n7 = Node("7"); n13 = Node("13")
    n6 = Node("6", n4, n7)
    n3 = Node("3", n1, n6)
    n14 = Node("14", Node("13"), None)
    n10 = Node("10", None, n14)
    root = Node("8", n3, n10)
    return root

def run_traversals():
    root = build_sample_tree()
    pre, ino, post = [], [], []
    preorder(root, pre)
    inorder(root, ino)
    postorder(root, post)
    print("Preorder :", " ".join(pre))
    print("Inorder  :", " ".join(ino))
    print("Postorder:", " ".join(post))

def run_reconstruction_examples():
   
    print("\nReconstructing from Preorder + Inorder:")
    pre = "Q W E R T Y U I".split()
    ino = "E W T R Q Y U I".split()
    r1 = build_from_pre_in(pre, ino)
    out = []
    inorder(r1, out)
    print("Inorder check:", " ".join(out))

    print("\nReconstructing from Postorder + Inorder:")
    post = "J I L M N K H".split()
    ino2 = "J I H L K M N".split()
    r2 = build_from_post_in(post, ino2)
    out2 = []
    preorder(r2, out2)
    print("Preorder check:", " ".join(out2))

if __name__ == "__main__":
    run_traversals()
    run_reconstruction_examples()