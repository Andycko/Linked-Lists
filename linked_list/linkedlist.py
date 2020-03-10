from linked_list.node import Node


class LinkedList:
    def __init__(self):
        self._root = None
        self._size = 0

    def get_size(self):
        return self._size

    def get_root(self):
        return self._root

    def add(self, data):
        new_node = Node(data, self._root)
        self._root = new_node
        self._size += 1
        return data

    def remove(self, data):
        node = self._root
        prev_node = None
        while node:
            if node.get_data() == data:
                if prev_node:
                    prev_node.set_next(node.get_next())
                else:
                    self._root = node.get_next()
                self._size -= 1
                return True
            else:
                prev_node = node
                node = node.get_next()
        return False

        # while node.get_data() != data:
        #     prev_node = node
        #     if node.get_next() is None:
        #         return False
        #     node = node.get_next()
        #
        # if prev_node:
        #     prev_node.set_next(node.get_next())
        # else:
        #     self._root = node.get_next()
        # self._size -= 1
        # return True

    def find(self, data):
        node = self._root
        while node:
            if node.get_data() == data:
                return data
            else:
                node = node.get_next()
        return None

    def __str__(self):
        node = self._root
        data_arr = []
        while node:
            data_arr.append(node.get_data())
            node = node.get_next()

        return str(data_arr)


