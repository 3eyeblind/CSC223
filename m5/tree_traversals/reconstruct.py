from typing import Optional, List, Dict
from .traversals import Node


def build_from_pre_in(pre: List[str], ino: List[str]) -> Optional[Node]:
    if not pre or not ino:
        return None

    index: Dict[str, int] = {v: i for i, v in enumerate(ino)}
    pre_i = 0

    def helper(lo: int, hi: int) -> Optional[Node]:
        nonlocal pre_i
        if lo > hi:
            return None
        root_val = pre[pre_i]
        pre_i += 1
        mid = index[root_val]
        root = Node(root_val)
        root.left = helper(lo, mid - 1)
        root.right = helper(mid + 1, hi)
        return root

    return helper(0, len(ino) - 1)

def build_from_post_in(post: List[str], ino: List[str]) -> Optional[Node]:
    if not post or not ino:
        return None
    index: Dict[str, int] = {v: i for i, v in enumerate(ino)}
    post_i = len(post) - 1

    def helper(lo: int, hi: int) -> Optional[Node]:
        nonlocal post_i
        if lo > hi:
            return None
        root_val = post[post_i]
        post_i -= 1
        mid = index[root_val]
        root = Node(root_val)
        root.right = helper(mid + 1, hi)
        root.left = helper(lo, mid - 1)
        return root

    return helper(0, len(ino) - 1)