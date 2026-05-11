from __future__ import annotations

from icecream import ic

class Node:
    _data: str
    _children: list[Node]

    def __init__(self, data: str) -> None:
        self._data = data
        self._children = []

    def __bool__(self) -> bool:
        return bool(self._data) or bool(self._children)

    @property
    def data(self) -> str:
        return self._data

    
    @property
    def is_leaf(self) -> bool:
        return not self._children
    
    def __iter__(self):
        return iter(self._children)
    
    def add_child(self, child: Node) -> None:
        self._children.append(child)
  
class RadixTree:
    _root: Node

    def __init__(self) -> None:
        self._root = Node('')

    def add(self, data: str) -> None:
        RadixTree._add(self._root, data + "")

    def print_tree(self) -> None:
        RadixTree._preorder_visit(self._root)

    def print_items(self) -> None:
        RadixTree._preorder_print_items(self._root)

    @staticmethod
    def _add(node: Node, data: str) -> None:

        prefix = RadixTree.common_prefix(node.data, data)
        ic(node.data, data)
        # if not node:
        #    node._data = data
        if len(prefix) < len(node.data):
            old_node = Node(node._data[len(prefix):])
            old_node._children = node._children
            new_node = Node(data[len(prefix):])
            node._data = prefix
            node._children = [old_node, new_node]
        elif prefix == node._data and prefix != data:
            new_data = data[len(prefix):]
            for child in node:
                if RadixTree.common_prefix(child.data, new_data):
                    RadixTree._add(child, new_data)
                    return
            else:
                node.add_child(Node(new_data))    

    @staticmethod        
    def _preorder_visit(node: Node, prefix: str = '', is_last: bool = True) -> None:
        connector = "└── " if is_last else "├── "
        print(f"{prefix}{connector}{node.data!r}")
        new_prefix = prefix + ("    " if is_last else "│   ")
        for i, child in enumerate(node):
            is_last_child = (i == len(node._children) - 1)
            RadixTree._preorder_visit(child, new_prefix, is_last_child)

    @staticmethod        
    def _preorder_print_items(node: Node, prefix: str = '') -> None:
        if node.is_leaf:
            print(prefix + node.data)
        else:
            for child in node:
                RadixTree._preorder_print_items(child, prefix + node.data)

    @staticmethod
    def _items_generator(node: Node, prefix: str = ''):
        if node.is_leaf:
            yield prefix + node.data
        else:
            for child in node:
                yield from RadixTree._items_generator(child, prefix + node.data)

    def items(self):
        return RadixTree._items_generator(self._root)

    @staticmethod
    def common_prefix(a: str, b: str) -> str:
        prefix = ''
        for c1, c2 in zip(a, b):
            if c1 == c2:
                prefix += c1
            else:
                break
        return prefix


def main():
    trie = RadixTree()
    trie.add('ROMANE$')

    trie.add('GALLUS$')
    trie.add('ROMANUS$')
    trie.add('BARBARUM$')
    trie.add('RUBBICUNDUS$')
    trie.add('ROST$') 
    trie.add('BARABBA$')
    trie.add('ROMA$')
    trie.print_tree()
    print(list(trie.items()))

if __name__ == "__main__":
    main()