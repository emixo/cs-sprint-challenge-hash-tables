def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    output = []
    
    for i in a:
        if (i >= 0):
            result.append(i)
            
    for j in a:
        if (j < 0) and (-j in result):
            output.append(-j)
    
    return output         


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
