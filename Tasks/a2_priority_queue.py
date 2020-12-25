"""
Priority Queue

Queue priorities are from 0 to 10
"""
from typing import Any

_queue = {}


def enqueue(elem: Any, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    if priority not in _queue:
        _queue[priority] = []
    _queue[priority].append(elem)


def dequeue() -> Any:
    """
    Return element from the beginning of the queue. Should return None if not elements.

    :return: dequeued element
    """
    if len(_queue):
        if len(_queue[min(_queue.keys())]):
            return _queue[min(_queue.keys())].pop(0)
        else:
            _queue.pop(min(_queue.keys()))
            return _queue[min(_queue.keys())].pop(0)


def peek(ind: int = 0, priority: int = 0) -> Any:
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    if ind < len(_queue[priority]):
        return _queue[priority][ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    _queue.clear()
