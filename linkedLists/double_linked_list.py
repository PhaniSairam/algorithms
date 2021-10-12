class Node(object):
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None


class DoubleLinkedList(object):
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
                    node.prev = present
                    break
                present = present.next

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
                node.prev = before
                node.next = present
                present.prev = node

    def show(self):
        if self.head is None:
            print("List is Empty")
        else:
            temp = self.head
            while temp:
                print(" => ", str(temp.data), end=" ")
                temp = temp.next
            print()


if __name__ == "__main__":
    doubleLinkedList = DoubleLinkedList()
    doubleLinkedList.insert(Node(10))
    doubleLinkedList.insert(Node(20))
    doubleLinkedList.insert(Node(30))
    doubleLinkedList.show()
    doubleLinkedList.insertAt(Node(15), 2)
    doubleLinkedList.show()
