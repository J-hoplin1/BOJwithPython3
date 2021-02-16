import json
import os
from typing import Any, MutableSequence
#from __future__ import annotations


class Node(object):
    def __init__(self, a : Any):
        self.value = a
        self.next = None # Node reference it self


class LinkedList(object):

    def __init__(self, capacity : int = 256):
        self.capacity = capacity
        self.listBody = None # 링크드 리스트 본체

    def addData(self,data):
        if not self.listBody:
            newNode = Node(data)
            self.listBody = newNode
        else:
            nodeCheck = self.listBody
            while nodeCheck.next: # 주목하고있는 노드의 next 속성값이 None일때까지
                nodeCheck = nodeCheck.next
            newNode = Node(data)
            nodeCheck.next = newNode
    
    def dump(self):
        count = 1
        nodeCheck = self.listBody
        while nodeCheck: # 모든 노드가 나올때 까지
            print(f'{count} - Value : {nodeCheck.value}')
            nodeCheck = nodeCheck.next
            count += 1

def tester():
    ll = LinkedList()
    for t in range(1,11):
        ll.addData(t)
    ll.dump()

if __name__=="__main__":
    tester()
