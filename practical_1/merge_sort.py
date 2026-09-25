def merge_sort(lst):

    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2

    left_partition = merge_sort(lst[:mid])
    right_partition = merge_sort(lst[mid:])

    # Start merging
    return merge(left_partition, right_partition)


def merge(left, right):

    output = []

    i = 0
    j = 0

    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            output.append(left[i])
            i += 1
        else:
            output.append(right[j])
            j += 1

    # Append the remaining elements
    output.extend(left[i:])
    output.extend(right[j:])

    return output


data_list = [6, 8, 1, 4, 5, 3, 7, 9]

print(f"Unsorted: {data_list}")

result = merge_sort(data_list)

print(f"Sorted: {result}")
