class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def insert_after(self, prev_node, new_data):
        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def insert_after_key(self, key, new_data):
        temp = self.head
        while temp:
            if temp.data == key:
                new_node = Node(new_data)
                new_node.next = temp.next
                temp.next = new_node
                break
            else:
                temp = temp.next

    def insert_at_last(self, data):
        new_node = Node(data)
        temp = self.head
        while temp:
            if temp.next is None:
                temp.next = new_node
                new_node.next = None
                break
            temp = temp.next

    def del_last_node(self):
        temp = self.head
        second_last = None
        last = None
        while temp.next.next:
            second_last = temp.next
            last = temp.next.next
            temp = temp.next
        second_last.next = None

    def del_head_node(self):
        self.head = self.head.next

    def del_specifi_key_node(self, key):
        temp = self.head
        prev_node = None
        next_node = None
        if temp.data == key and temp == self.head:
            self.del_head_node()
            return
        while temp:
            prev_node = temp
            if temp.next is None and temp.data == key:
                self.del_last_node()
                break
            else:
                next_node = temp.next.next
                if temp.next.data == key:
                    prev_node.next = next_node
                    break
                temp = temp.next

    # def reverse_linked_list(self):
    #     prev = None
    #     current = self.head
    #     while current is not None:
    #         next = current.next
    #         current.next = prev
    #         prev = current
    #         current = next
    #     self.head = prev

    def print_nodes(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


    def reverse_linked_list(self):
        current = self.head
        prev = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
































llist = LinkedList()
llist.push_at_front(1)
llist.push_at_front(2)
llist.push_at_front(3)
llist.push_at_front(4)
llist.insert_after_key(2,7)
llist.insert_at_last(10)
#llist.del_head_node()
#llist.del_last_node()
#llist.del_specifi_key_node(10)
llist.reverse_linked_list()
llist.print_nodes()

####Removing Head###################
# llist.head = second
# temp = llist.head
# while temp:
#     print(temp.data)
#     temp = temp.next

###############################

####Removing Tail###################

# temp = llist.head
# last = None
# second_last = None
# while temp.next.next:
#     second_last = temp.next
#     last = temp.next.next
#     temp = temp.next
#
# second_last.next = None
# temp = llist.head
# while temp:
#     print(temp.data)
#     temp = temp.next

#########End of Removing tail####################




