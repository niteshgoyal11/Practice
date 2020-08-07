class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def push_nodes_front(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.next = None
            self.prev = None
            return self.head
        new_node.next = self.head
        self.head.prev = new_node
        new_node.prev = None
        self.head = new_node
        return self.head

    def print_nodes(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def mid_node(self):
        fast_pointer = self.head
        slow_pointer = self.head
        l_len = 1
        while fast_pointer.next is not None and fast_pointer.next.next is not None :
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            l_len += 2
        if fast_pointer.next is not None:
            l_len += 1
        #print("*****", slow_pointer.data, l_len)
        return [slow_pointer, l_len]
    #
    # def check_prev_node_data(self, node):
    #     if node == self.head:
    #         return None
    #     current = self.head
    #     prev = None
    #     while current:
    #         if current == node:
    #             return prev
    #         prev = current
    #         current = current.next
    #
    def last_node(self):
        temp = self.head
        while temp:
            if temp.next is None:
                return temp
            temp = temp.next
    def check_palindrome(self):

        mid_node = self.mid_node()[0]
        print("mid node datr", mid_node.data)
        start = self.head
        start_mid = mid_node.next
        print("star_mid data", start_mid.data)
        prev_node = self.last_node()
        while start != start_mid:
            print("prev data", prev_node.data)
            print("start data", start.data)
            if start.data == prev_node.data:
                pass
            else:
                return False
            start = start.next
            prev_node = prev_node.prev
        return True


llist = LinkedList()
llist.push_nodes_front(1)
llist.push_nodes_front(2)
llist.push_nodes_front(3)
llist.push_nodes_front(4)
llist.push_nodes_front(5)
llist.push_nodes_front(6)
llist.push_nodes_front(7)
llist.push_nodes_front(7)
llist.push_nodes_front(6)
llist.push_nodes_front(5)
llist.push_nodes_front(4)
llist.push_nodes_front(3)
llist.push_nodes_front(2)
llist.push_nodes_front(1)
llist.print_nodes()
print(llist.last_node().data)
print("last_node prev data", llist.last_node().prev.data)
#print("previous node is ", llist.check_prev_node_data(llist.last_node()))
# print(llist.mid_node()[0].data)
print(llist.check_palindrome())
