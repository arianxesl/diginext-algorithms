def merge(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])

    merged_intervals = [intervals[0]]

    for current in intervals[1:]:
        last_merged = merged_intervals[-1]

        if current[0] <= last_merged[1]:
            merged_intervals[-1] = (last_merged[0], max(last_merged[1], current[1]))
        else:
            merged_intervals.append(current)

    return merged_intervals

# example:
input_intervals = [(1, 3), (2, 6), (8, 10)]
output = merge(input_intervals)

print(output)  # output: [(1, 6), (8, 10)]
