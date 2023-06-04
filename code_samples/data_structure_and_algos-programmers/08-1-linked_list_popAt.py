#
# -*- coding: utf-8 -*-
#
# 08-1-linked_list_popAt.py

# 8강 실습: 연결 리스트 노드 삭제하기
# 문제 설명
# 제 8 강에서 소개된 추상적 자료구조 LinkedList 클래스의 메서드로서 popAt() 메서드를 강의 내용에 소개된 요구조건을 만족시키도록 구현하세요.
# 초기 코드로 들어 있는 것은 solution() 함수를 포함하여 다른 부분은 수정하지 말고, def popAt(self, pos): 의 메서드 몸체만 구현하세요.
# 만약, 인자로 주어진 pos가 올바른 범위의 값을 가지지 않는 경우에는 IndexError exception 을 발생시키도록 합니다.
# 이렇게 하기 위한 코드는 raise IndexError 입니다.


class Node:

    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:

    def __init__(self):
        self.nodeCount = 0
        self.head = None
        self.tail = None


    def getAt(self, pos):
        if pos < 1 or pos > self.nodeCount:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1

        return curr


    def insertAt(self, pos, newNode):
        if pos < 1 or pos > self.nodeCount + 1:
            return False

        if pos == 1:
            newNode.next = self.head
            self.head = newNode

        else:
            if pos == self.nodeCount + 1:
                prev = self.tail
            else:
                prev = self.getAt(pos - 1)
            newNode.next = prev.next
            prev.next = newNode

        if pos == self.nodeCount + 1:
            self.tail = newNode

        self.nodeCount += 1
        return True


    def popAt(self, pos):
        pass


    def traverse(self):
        result = []
        curr = self.head
        while curr is not None:
            result.append(curr.data)
            curr = curr.next
        return result


def solution(x):
    return 0