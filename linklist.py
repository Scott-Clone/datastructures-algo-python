class Node:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

class LinkList:
    def __init__(self, head = None):
        self.head = head

    def insert(self, data):
        """Insert a value into linklist (always at the end)"""
        if self.head is None:
            self.head = Node(data)
        else:
            current_value = self.head
            while True:    
                if current_value.next is None:
                    break
                current_value = current_value.next
            current_value.next = Node(data)

    def add_head(self, data):
        """This function will add the head 
        value to the linklist"""
        temp = self.head
        self.head = Node(data)
        self.head.next = temp

    def delete_end(self):
        """This function will delete the end node completely"""
        current_value = self.head
        previous_value = self.head
        while True:
            if current_value.next is None:
                break
            previous_value = current_value
            current_value = current_value.next
        previous_value.next = None

    def remove_duplicates(self):
        """This function will remove any duplicates if there is any"""
        current_value = self.head
        previous_value = None

        duplicates = {}

        while True:
            if current_value is None:
                break
            elif current_value.data in duplicates:
                previous_value.next = current_value.next
                del current_value.data
            elif current_value.data not in duplicates:
                duplicates[current_value.data] = 1
                previous_value = current_value
            current_value = current_value.next

    def insert_at(self, data, position):
        """This function will insert a value at a given positoin by the user"""
        current_position = 0
        if self.head is None:
            self.head = Node(data)
        elif position == current_position:
            LinkList.add_head(self, data)
        
        else:
            current_value = self.head
            previous_value = None
            while True:
                if current_position == position:
                    break
                elif current_value.next is None:
                    current_value.next = Node(data)
                    return
                previous_value = current_value                                               
                current_value = current_value.next
                current_position += 1
            new_value = Node(data)
            previous_value.next = new_value
            new_value.next = current_value

    def delete_at(self, position):
        """This function will delete a value at any given position"""
        current_position = 0
        if current_position == position:
            self.head = self.head.next
        else:
            current_value = self.head
            previous_value = self.head

            while True:
                if current_position == position:
                    break
                previous_value = current_value
                current_value = current_value.next
                current_position += 1
            previous_value.next = current_value.next


    def delete_node(self, data):
        """This function will delete a given value by the user """
        to_delete = Node(data)
        if self.head.data is to_delete.data:
            self.head = self.head.next
        else:
            current_value = self.head
            previous_value = self.head

            while True:
                if current_value.data is to_delete.data:
                    break
                previous_value = current_value
                current_value = current_value.next
            previous_value.next = current_value.next


    def display(self):
        """This function will display all the values of the linklist"""
        list = []
        while self.head is not None:
            list.append(self.head.data)
            self.head = self.head.next
        print(list)

    def bubble_sort(self):
        """This function will sort the linklist using bubble_sort"""
        previous_value = self.head
        current_value = self.head
        while previous_value.next is not None:
            current_value = current_value.next
            while True:
                if current_value is None:
                    current_value = previous_value.next
                    break
                elif previous_value.data > current_value.data:
                    current_value.data, previous_value.data = previous_value.data, current_value.data
                current_value = current_value.next
            previous_value = previous_value.next
    
    def linear_search(self, number):
        """Search the linklist for a value using linear search"""
        current_index = 0
        current_value = self.head
        while current_value is not None:
            if current_value.data == number:
                print(f"{number} found at index {current_index}")
                return
            current_value = current_value.next
            current_index += 1
        print(f"{number} Not in the linklist")
    
    def swap_node_data(self, vice, versa):
        """Swap the data at any two given nodes by passing in the index"""
        current_position, first_value, second_value = 0, self.head, self.head
        while True:
            if vice == current_position:
                current_position = 0
                while True:
                    if versa == current_position:
                        break
                    second_value = second_value.next
                    current_position += 1
                break
            first_value = first_value.next
            current_position += 1
        first_value.data, second_value.data = second_value.data, first_value.data

    def get_len_linklist(self):
        while self.head is not None:
            current_value = self.head
            len_linklist = 1
            while True:
                if current_value.next is None:
                    break
                current_value = current_value.next
                len_linklist += 1
            return len_linklist

    def binary_search(self, number):
        """Find a specific value in the linklist using binary search"""
        length = LinkList.get_len_linklist(self)
        start, end = 1, length
        
        while start <= end:
            middle_index = (start + end) // 2
            current_position, current_value = 1, self.head
            
            while True:
                if current_position == middle_index:
                    break
                current_value = current_value.next
                current_position += 1
            if current_value.data == number:
                print(f"{number} found at index {middle_index-1}")
                return
            elif current_value.data < number:
                start = current_position + 1
            elif current_value.data > number:
                end = current_position - 1


    

linklist = LinkList()
linklist.insert(4)
linklist.insert(15)
linklist.insert(0)
linklist.insert(55)
linklist.insert(78)
linklist.insert(3)
linklist.insert(105)
linklist.insert(99)
linklist.insert(2)
linklist.insert(100)
linklist.bubble_sort()
linklist.binary_search(2)
linklist.display()
