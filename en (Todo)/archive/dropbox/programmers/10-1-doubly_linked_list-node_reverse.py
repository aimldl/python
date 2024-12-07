# 10-1-doubly_linked_list-node_reverse.py
# -*- coding: utf-8 -*-
# 문제 설명
# 제 10 강에서 소개된 추상적 자료구조 DoublyLinkedList 에 대하여, 또한 강의 내용에서 언급한 reverse() 메서드를 구현하세요.
# 이 reverse() 메서드는 양방향 연결 리스트를 끝에서부터 시작해서 맨 앞에 도달할 때까지 (tail 방향에서 head 방향으로) 순회하면서, 
# 방문하게 되는 node 에 들어 있는 data item 을 순회 순서에 따라 리스트에 담아 리턴합니다.
# 예를 들어, DoublyLinkedList L 에 들어 있는 노드들이 43 -> 85 -> 62 라면, 올바른 리턴 값은 [62, 85, 43] 입니다.
# 이 규칙을 적용하면, 빈 연결 리스트에 대한 역방향 순회 결과로 reverse() 메서드라 리턴해야 할 올바른 결과는 [] 입니다. 
# 만약, popAt() 메서드에 인자로 주어진 pos 가 올바른 범위의 값을 가지지 않는 경우에는 IndexError exception 을 발생시키도록 합니다. 
# 이렇게 하기 위한 코드는 raise IndexError 입니다.

class Node:

    def __init__(self, item):
        self.data = item
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = Node(None)
        self.tail = Node(None)
        self.head.prev = None
        self.head.next = self.tail
        self.tail.prev = self.head
        self.tail.next = None


    def reverse(self):
        pass


    def getAt(self, pos):
        if pos < 0 or pos > self.nodeCount:
            return None

        if pos > self.nodeCount // 2:
            i = 0
            curr = self.tail
            while i < self.nodeCount - pos + 1:
                curr = curr.prev
                i += 1
        else:
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr


    def insertAfter(self, prev, newNode):
        next = prev.next
        newNode.prev = prev
        newNode.next = next
        prev.next = newNode
        next.prev = newNode
        self.nodeCount += 1
        return True


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        prev = self.getAt(pos - 1)
        return self.insertAfter(prev, newNode)


def solution(x):
    return 0