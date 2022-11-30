#User function Template for python3

#User function Template for python3

# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None


#Back-end complete function Template for Python 3
class Solution:
    
    def reorderList(self,head):
        if not head or not head.next: return

        slow, fast = head, head.next
            
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        # 1 2 3 4 5 6 7 8 9
        
        # Separate both lists until middle node
        second = slow.next
        slow.next = None
        
        # first list -- 1 2 3 4 5->null    second list -- 6 7 8 9->null
        
        # reverse the second list
        
        p = second
        q = r = None
        while p:
            r = q
            q = p
            p = p.next
            q.next = r
            
        first, second = head, q
        
        # 1 2 3 4 5->null 9 8 7 6->null
        
        # 1->9->2->8->3_7....
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
 


#{ 
 # Driver Code Starts
#Initial Template for Python 3

# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.tail = self.head
        else:
            new_node = node(val)
            self.tail.next = new_node
            self.tail = new_node

    def createList(self, arr, n):
        for i in range(n):
            self.insert(arr[i])
        return self.head

    def printList(self,head):
        tmp = head
        while tmp is not None:
            print(tmp.data, end=" ")
            tmp=tmp.next
        print()

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        lis = Linked_List()
        head = lis.createList(arr, n)
        ob=Solution()
        ob.reorderList(head)

        lis.printList(head)

# } Driver Code Ends