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
        return self.head

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
        if temp.data == key and temp == self.head:
            self.del_head_node()
            return None
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

    def reverse_linked_list(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
    # Function to reverse linked list based on group size

    def kAltReverse(self, head, k):
        current = head
        next = None
        prev = None
        count = 0

        # 1) reverse first k nodes of the linked list
        while (current != None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count = count + 1;

            # 2) Now head pos to the kth node.
        # So change next of head to (k+1)th node
        if (head != None):
            head.next = current

            # 3) We do not want to reverse next k
        # nodes. So move the current
        # poer to skip next k nodes
        count = 0
        while (count < k - 1 and current != None):
            current = current.next
            print ("******** current data", current.data)
            count = count + 1

        # 4) Recursively call for the list
        # starting from current.next. And make
        # rest of the list as next of first node
        if (current != None):
            current.next = self.kAltReverse(current.next, k)

            # 5) prev is new head of the input list
        return prev



    def print_nodes(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

llist = LinkedList()
head = llist.push_at_front(1)
head = llist.push_at_front(2)
head = llist.push_at_front(3)
head = llist.push_at_front(4)
head = llist.push_at_front(5)
head = llist.push_at_front(6)
head = llist.push_at_front(7)
llist.print_nodes()
print("**************************************")
llist.kAltReverse(head, 2)
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




