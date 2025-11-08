from .traversals import preorder, inorder, postorder
from .reconstruct import build_from_pre_in, build_from_post_in
from .traversals import Node

def test_roundtrip_pre_in():
    # small tree
    pre = list("ABDCE")
    ino = list("DBAEC")
    root = build_from_pre_in(pre, ino)
    out = []
    inorder(root, out)
    assert "".join(out) == "DBAEC"

def test_roundtrip_post_in():
    post = list("DBECA")
    ino = list("DBAEC")
    root = build_from_post_in(post, ino)
    out = []
    preorder(root, out)
    assert "".join(out) == "ABCDE"

def test_traversal_orders():
    #      A
    #     / \
    #    B   C
    #       /
    #      D
    root = Node("A", Node("B"), Node("C", Node("D"), None))
    pre, ino, post = [], [], []
    preorder(root, pre); inorder(root, ino); postorder(root, post)
    assert pre == ["A", "B", "C", "D"]
    assert ino == ["B", "A", "D", "C"]
    assert post == ["B", "D", "C", "A"]