class LinkedListElement:
    def __init__(self, val, p, n) :
        '''
        큐 myQueue을 만듭니다.
        '''
        self.value = val
        self.prev = p
        self.next = n


class Queue:
    def __init__(self):
        self.start = None
        self.end = None
        self.count = 0

    def push(self, n) :
        '''
        queue에 정수 n을 넣습니다.
        '''
        if self.start == None and self.end == None:
            elem = LinkedListElement(n, None, None)
            self.start = elem
            self.end = elem
        else:
            elem = LinkedListElement(n, self.end, None)
            self.end.next = elem
            self.end = elem
            
        self.count += 1
        return None

    def pop(self) :
        '''
        queue에서 가장 앞에 있는 정수를 제거합니다. 만약 queue에 들어있는 값이 없을 경우에는 아무 일도 하지 않습니다. 
        '''
        if self.empty() == 1: return None
        if self.count >= 2:
            nextNode = self.start.next
            nextNode.prev = None
            self.start = nextNode
        else:
            self.start = None
            self.end = None
        
        self.count -= 1
        return None

    def size(self) :
        '''
        queue에 들어 있는 정수의 개수를 return 합니다.
        '''
        return self.count

    def empty(self) :
        '''
        queue이 비어있다면 1, 아니면 0을 return 합니다.
        '''
        if self.size() == 0: return 1
        else: return 0

    def front(self) :
        '''
        queue의 가장 앞에 있는 정수를 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if self.empty() == 1: return -1
        else: return self.start.value

    def back(self) :
        '''
        queue의 가장 뒤에 있는 정수를 return 합니다. 만약 queue에 들어있는 값이 없을 경우에는 -1을 return 합니다.
        '''
        if self.empty() == 1: return -1
        else: return self.end.value