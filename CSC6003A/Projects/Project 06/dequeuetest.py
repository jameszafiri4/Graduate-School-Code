from dequeue import Dequeue
import unittest

# using python module unit test class
class TestQueue(unittest.TestCase):
    # this will test the insertFront method from Dequeue class
    def testInsertFront(self):
        # creating a sample list for the test
        ogList = ["Apple", 1 , "Orange" , 2 , "Banana"]
        # creating an empty list of type Dequeue class
        fakeList = Dequeue()
        # for loop in range of sample list 
        for i in range(0, len(ogList)):
            # uses insertFront method to add elements from sample list into new one
            fakeList.insertFront(ogList[i])
            # checks if new list item is in correct spot
            self.assertEqual(fakeList.items[0], ogList[i])
    # this will test the insertRear method from Dequeue class
    def testInsertRear(self):
        # creating a sample list for the test
        ogList = ["Apple", 1 , "Orange" , 2 , "Banana"]
        # creating an empty list of type Dequeue class
        fakeList = Dequeue()
        # for loop in range of sample list
        for i in range(0, len(ogList)):
            # uses insertRear method to add elements from sample list into new one
            fakeList.insertRear(ogList[i])
            # checks if new list item is in correct spot
            self.assertEqual(fakeList.items[-1], ogList[i])
            
if __name__ == "__main__":
    unittest.main()
