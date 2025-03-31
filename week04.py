class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class LinkedList:
    def __init__(self):
        self.head = None


    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.link:
            current = current.link  # move current
        current.link = Node(data)


    def remove(self, target):
        current = self.head
        if self.head.data == target:
            self.head = self.head.link
            current.link = None
            return

        previous = None
        while current:
            if target == current.data:
                previous.link = current.link
                current.link = None
            previous = current
            current = current.link



    def search(self, target):
        current = self.head
        while current:  # bug fix
            if target == current.data:
                return f"{target}을(를) 찾았습니다!"
            else:
                current = current.link
        return  f"{target}은(는) 링크드 리스트 안에 존재하지 않습니다."


    def __str__(self):
        current = self.head
        result = ""
        while current is not None:
            result = result + f"{current.data} -> "
            current = current.link
        return result + "END"


ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)
print(ll)
# print(ll.is_find(99))
# print(ll.is_find(10))
print(ll.search(99))
print(ll.search(-9))
ll.remove(-9)
ll.remove(77)
print(ll)
