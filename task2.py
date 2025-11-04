def get_top_n_frequent(items, n):
    list_of_items = []
    unique_items = []
    result = []
    for item in items:
        if item not in unique_items:
            unique_items.append(item)
    for item in unique_items:
        list_of_items.append((-items.count(item),item ))
    list_of_items.sort()
    for i in range(n):
        result.append(list_of_items[i][1])

    return result

    
votes = ['orange', 'banana', 'apple', 'orange', 'apple', 'grape', 'apple']
n = 2
print(get_top_n_frequent(votes,n))
