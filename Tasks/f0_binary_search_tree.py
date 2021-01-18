"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, value: 123, 'left': {...}, 'right':{...}})
"""

from typing import Any, Optional, Tuple
# import networkx as nx


_root = {}


def insert(key: int, value: Any) -> None:
    """
    Insert (key, value) pair to binary search tree

    :param key: key from pair (key is used for positioning node in the tree)
    :param value: value associated with key
    :return: None
    """
    if not _root:
        _root['key'] = key
        _root['value'] = value
        _root['left'] = {}
        _root['right'] = {}
    else:
        found, node = _find(key)
        if found:
            node['value'] = value
        else:
            if key < node['key']:
                node['left'] = {'key': key, 'value': value, 'left': {}, 'right': {}}
            else:
                node['right'] = {'key': key, 'value': value, 'left': {}, 'right': {}}
    return None


def _find(key: int) -> Tuple[bool, dict]:
    """
    Find key in tree

    :param key: key to find
    :return: tuple of search success and found key
    """
    current_node = _root
    while current_node:
        if key == current_node['key']:
            return True, current_node
        elif key < current_node['key']:
            if not current_node['left']:
                return False, current_node
            else:
                current_node = current_node['left']
        else:
            if not current_node['right']:
                return False, current_node
            else:
                current_node = current_node['right']


def remove(key: int) -> Optional[Tuple[int, Any]]:
    """
    Remove key and associated value from the BST if exists

    :param key: key to be removed
    :return: deleted (key, value) pair or None
    """
    if not _root:
        return None
    else:
        found, node = _find(key)
        if not found:
            return None
        else:
            remove_if_found(node)


def remove_if_found(node: dict):
    """
    Remove of found node from tree

    :param node: found mode
    :return: None
    """
    if not node['left'] and not node['right']:
        node.clear()
    elif not node['left']:
        node = node['right']
        return None
    elif not node['right']:
        node = node['left']
        return None
    else:
        current_node = node['right']
        if not current_node['left']:
            remove_if_found(current_node)
        else:
            min_in_branch = current_node['left']
            while min_in_branch['left']:
                min_in_branch = min_in_branch['left']
            node['key'] = min_in_branch['key']
            node['value'] = min_in_branch['value']
            remove_if_found(min_in_branch)


def find(key: int) -> Optional[Any]:
    """
    Find value by given key in the BST

    :param key: key for search in the BST
    :return: value associated with the corresponding key
    """
    found, node = _find(key)
    if not found:
        raise KeyError
    else:
        return node['value']


def clear() -> None:
    """
    Clear the tree

    :return: None
    """
    _root.clear()


if __name__ == '__main__':
    insert(42, 'The meaning of life, the universe and everything.')
    insert(0, 'ZERO!')
    insert(13, "Devil's sign here")
    insert(43, "blabla")
    insert(60, "blabla")
    insert(44, "blabla")
    insert(55, "blabla")
    # print(_root)
    clear()
    insert(50, "blabla1")
    insert(25, "blabla2")
    insert(75, "blabla3")
    insert(62, "blabla4")
    insert(87, "blabla5")
    insert(56, "blabla6")
    insert(68, "blabla7")
    insert(81, "blabla8")
    insert(93, "blabla9")
    print('Initial: ', _root)
    remove(75)
    print('After delete 75: ', _root)  # On the place of 75 must be 81
    remove(50)
    print('Root delete: ', _root)  # Root delete. New root must be 56
