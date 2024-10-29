set1 = {2, 5, 8, 9, 6, 3, 6, 5, 4}
set2 = {9, 8, 7, 6, 3, 4, 8, 1, 8}
set3 = {7, 3, 6, 9, 8, 4, 5, 8, 3}

union_set = set1.union(set2, set3)
intersection_result = set1.intersection(set2, set3)
symmetric_difference_result = set1.symmetric_difference(set2)

print("Union of Sets:", union_set)
print("Intersection of Sets:", intersection_result)
print("Symmetric Difference between set1 and set2:", symmetric_difference_result)
