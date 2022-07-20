#!/usr/bin/python3
# 100-singly_linked_list.py
# John Rumide <johnrumide6@gmail.com>
"""Defines a singly linked list class and a Node class"""


class Node:
    """Class representing a Node of a singly linked list"""
    def __init__(self, data, next_node=None):
        """Initialize method that stores a Node of a singly linked list

        Args:
            param1 (int): data to save in node
            param2 (Node): next node in a singly linked list
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""
    def __init__(self):
        """Initialize method of a singly linked list

        Args:
            param1 (int): head of the singly linked list
        """
        self.__head = None

    def __str__(self):
        rtn_str = ""
        ptr = self.__head

        while ptr is not None:
            rtn_str += str(ptr.data)
            if ptr.next_node is not None:
                rtn_str += "\n"
            ptr = ptr.next_node
        return rtn_str

    def sorted_insert(self, value):
        ptr = self.__head

        while ptr is not None:
            if ptr.data < value:
                tmp = ptr
                ptr = ptr.next_node
            else:
                break
        new_node = Node(value, ptr)
        if ptr != self.__head:
            tmp.next_node = new_node
        else:
            self.__head = new_node
