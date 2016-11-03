from linked_list import LinkedList


def proper_parenthetics(input):
    """
    This function returns 1 if input is open,-1 if closed, and 0 if balanced.
    """
    temp = []
    for character in input:
        if character == ')' or character == '(':
            temp.append(character)

    sequence = LinkedList(temp[::-1])

    while True:
        if sequence.length == 0:
            return 0
        if sequence.head.data == ')':
            return -1
        if sequence.search('(') is None:
            return -1
        if sequence.search(')') is None:
            return 1

        current = sequence.head
        while current.data is not None:
            if current.data == '(' and current.next_node.data == ')':
                sequence.remove(current.next_node)
                sequence.remove(current)
                continue
            current = current.next_node
