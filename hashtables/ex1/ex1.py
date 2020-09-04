def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here
    # Run through the array and get the difference of the value and the limit.
    # Use that difference as a key and the value as an index for our cache.
    # If an item is in our cache that means that we found a pair of items that equal the limit
    # We can get access to that pair by accessing our cache. 
    cache = {}
    for i in range(length):
        if weights[i] not in cache:
            difference = limit - weights[i]
            cache[difference] = i
        else:
            value = cache[weights[i]]
            return (i, value)

    return None

