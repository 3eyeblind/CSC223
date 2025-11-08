from dataclasses import dataclass
from typing import Optional, List

# Traversal order definitions 
@dataclass
class Node:
    val: str
    left: Optional["Node"] = None
    right: Optional["Node"] = None

def preorder(node: Optional[Node], out: List[str]) -> None:
    if not node: return
    out.append(node.val)
    preorder(node.left, out)
    preorder(node.right, out)

def inorder(node: Optional[Node], out: List[str]) -> None:
    if not node: return
    inorder(node.left, out)
    out.append(node.val)
    inorder(node.right, out)

def postorder(node: Optional[Node], out: List[str]) -> None:
    if not node: return
    postorder(node.left, out)
    postorder(node.right, out)
    out.append(node.val)