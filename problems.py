def one():
    print("Welcome to problem 1.")

    # create and fill the list from input
    list_length = int(input("How many number will you enter in the list? "))
    input_list = []
    for i in range(list_length):
        num = int(input("Enter a number for the list: "))
        input_list.append(num)

    # input the anser k
    k = int(input("Enter the answer integer: "))

    # loop through list elements and check if the result k can be found
    for x in range(len(input_list)):
        for y in range(len(input_list) - 1):
            elem1 = input_list[x]
            elem2 = input_list[y + 1]
            if elem1 + elem2 == k:
                print(f"{k} can be obtained by the sum of {elem1} and {elem2}.")
                return True
    print(f"{k} can not be summed by any two numbers from the list {input_list}.")
    return False


def two():
    # input integer array
    # output integer array where element i is the product of all numbers except i.
    list_length = int(input("Enter the amount of numbers which are in the list: "))
    input_list = []
    output_list = [1]*list_length

    for i in range(list_length):
        num = int(input("Enter a number for the list: "))
        input_list.append(num)

    for i in range(list_length):
        for j in range(list_length):
            if not i == j:
                output_list[i] = output_list[i]*input_list[j]

    print(f"The output is {output_list}")
    return output_list


def three():
    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def serialize(root: Node):
        def helper(node: Node):
            if node is None:
                serialized.append("#") # indicate leaf node
            else:
                serialized.append(str(node.val))
                helper(node.left)
                helper(node.right)

        serialized = []
        helper(root)
        return ",".join(serialized)

    def deserialize(data):
        def helper():
            val = next(values)

            if val == "#":
                return None
            
            node = Node(val)
            node.left = helper()
            node.right = helper()
            return node
        
        values = iter(data.split(","))
        return helper()

    #serialize a binary tree class to text.
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'


def four():
    input_list = [3,4,-1,1]
    input_list = [x for x in input_list if x > 0]
    # sort list
    input_list.sort()

    item = input_list[0]
    while input_list:
        item += 1
        if item not in input_list:
            print(f"The lowest number not in the array is {item}.")
            return







    print(new_list)

