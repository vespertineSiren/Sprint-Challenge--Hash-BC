#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)


    """
    YOUR CODE HERE
    """

    if length < 2:
        return None

    for i in range(0, length):
        hash_table_insert(ht, weights[i], i)

    for i in range(0, length):
        target = limit - weights[i]
        if hash_table_retrieve(ht, target):
            found = hash_table_retrieve(ht, target)

            if i > found:
                tuple = (i, found)
                return tuple
            else:
                tuple = (found, i)
                return tuple
    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
