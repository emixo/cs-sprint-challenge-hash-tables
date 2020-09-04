def intersection(arrays):
    """
    YOUR CODE HERE
    """
    # Your code here
    newarr = {}
    doubles = {}
    triples = {}

    results = []
    doubles_array = []
    for num in arrays[0]:
        if num not in newarr:
            newarr[num] = 1
        else:
            newarr[num] += 1
    for num in arrays[1]:
        if num in newarr:
            doubles[num] = 1
            doubles_array.append(num)
    if len(arrays) > 2:
        for num in arrays[2]:
            if num in newarr and num in doubles:
                triples[num] = 1
        for key in triples.keys():
            results.append(int(key))
        return results
    else:
        return doubles_array    


    return results


if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
