class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def insert(self, node):
        if self.head is None:
            self.head = node
        else:
            present = self.head
            while True:
                if present.next is None:
                    present.next = node
                    break
                present = present.next

    def show(self):
        if self.head is None:
            print("List Empty")
        temp = self.head
        while temp:
            print(" => " + str(temp.data), end=" ")
            temp = temp.next
        print()

    def insertAt(self, node, pos):
        if self.head is None:
            print("List Empty")
            self.insert(node)
        else:
            present = self.head
            before = self.head
            cur = 1
            while cur < pos:
                if present.next is None:
                    print(
                        "Only {cur} positions in lists, but you were looking to insert at {pos}".format(
                            cur=cur, pos=pos
                        )
                    )
                    break
                else:
                    before = present
                    present = present.next
                    cur += 1
            if cur == pos:
                before.next = node
                node.next = present

    def reverseList(self):
        if self.head is None:
            print("List Empty")
        previous = None
        current = self.head
        following = None
        while current is not None:
            following = current.next
            current.next = previous
            previous = current
            current = following
        self.head = previous

    def detectLoopUsingHash(self):
        s = set()
        temp = self.head
        while temp:
            if temp in s:
                return True
            s.add(temp)
            temp = temp.next
        return False

    def detectLoopUsingFloydAlgorithm(self):
        slow_p = self.head
        fast_p = self.head
        while slow_p and fast_p and fast_p.next:
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                return True
        return False

    def isPalindrome(self):
        temp = self.head
        ispalin = True
        stack = []
        while temp:
            stack.append(temp.data)
            temp = temp.next
        temp = self.head
        while temp:
            data = stack.pop()
            if temp.data == data:
                ispalin = True
            else:
                ispalin = False
                break
            temp = temp.next
        return ispalin

    def sort_insert(self, node):
        if self.head is None:
            self.insert(node)
        else:
            before = self.head
            present = self.head
            while present is not None:
                if node.data > present.data and present.next is not None:
                    before = present
                    present = present.next
                elif node.data < present.data:
                    before.next = node
                    node.next = present
                    self.head = node
                    break
                present.next = node


if __name__ == "__main__":
    linkedlist = LinkedList()
    node = Node(10)
    linkedlist.insert(node)
    linkedlist.insert(Node(20))
    linkedlist.insert(Node(20))
    linkedlist.insert(Node(10))
    # linkedlist.show()
    linkedlist.insertAt(Node(25), 3)
    # linkedlist.show()
    linkedlist.reverseList()
    # linkedlist.show()
    # print("Loop Detected : ", linkedlist.detectLoopUsingFloydAlgorithm())
    # print("Loop Detected : ", linkedlist.detectLoopUsingHash())
    # print("List is Palindrome : ", linkedlist.isPalindrome())
    sorted_list = LinkedList()
    sorted_list.sort_insert(Node(10))
    sorted_list.sort_insert(Node(5))
    sorted_list.sort_insert(Node(7))
    sorted_list.sort_insert(Node(1))
    sorted_list.sort_insert(Node(100))
    sorted_list.show()
