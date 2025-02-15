'''
On this file we have the implementation of a Linked List Data Structure

The program will use two classes to accomplish this; Node and LinkedList

The methods will allow a user to enter/remove items in the correct spots of the list

'''


class Node:
    def __init__(self, d):
        self.Data = d
        self.Next = None


class LinkedList:
    def __init__(self, d = None):
        if (d == None):  # an empty list
            self.Header = None
            self.Current = None
        else:
            self.Header = Node(d)
            self.Current = self.Header

    def insertBeginning(self, d):
        if (self.Header is None):  # if the list is empty
            self.Header = Node(d)
            self.Current = self.Header
        else:  # if the list is not empty
            Tmp = Node(d)
            Tmp.Next = self.Header
            self.Header = Tmp

    def insertEnd(self, d):
        if (self.Header is None):  # if the list is empty
            self.Header = Node(d)
            self.Current = self.Header
        else:  # if the list is not empty
            Tmp = Node(d)
            while Tmp.Next is not None:
                Tmp.Next = self.Current.Next
                self.Current.Next = Tmp
            self.Current.Next = Node(d)

    def insertCurrentNext(self, d):
        if (self.Header is None):  # if the list is empty
            self.Header = Node(d)
            self.Current = self.Header
        else:  # if the list is not empty
            Tmp = Node(d)
            Tmp.Next = self.Current.Next
            self.Current.Next = Tmp

    def removeBeginning(self):
        if (self.Header is None):  # if the list is empty
            return None
        else:  # if the list is not empty
            ans = self.Header.Data
            self.Header = self.Header.Next
            self.Current = self.Header
            return ans

    def removeCurrentNext(self):
        if (self.Current.Next is None):  # if there is no node
            return None  # after Current
        else:  # if there is a node
            ans = self.Current.Next.Data
            self.Current.Next = self.Current.Next.Next
            return ans

    def nextCurrent(self):
        if (self.Current.Next is not None):
            self.Current = self.Current.Next
        else:
            self.Current = self.Header

    def resetCurrent(self):
        self.Current = self.Header

    def getCurrent(self):
        if (self.Current is not None):
            return self.Current.Data
        else:
            return None

    def printList(self, msg = "====="):
        p = self.Header
        print("====", msg)

        while (p is not None):
            print(p.Data, end = " ")
            p = p.Next
        if (self.Current is not None):
            print("")
        else:
            print("Empty Linked List")
            
