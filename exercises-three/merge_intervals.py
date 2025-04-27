# Time complexity is O(n log n) due to sorting, where n is the number of intervals, with O(n) space for the merged intervals list.
def merge_intervals(intervals):
    """
    Merges all overlapping intervals in a list of intervals.

    Args:
        intervals (List[List[int]]): A list of intervals,
        where each interval is a list of two integers [start, end].

    Returns:
        List[List[int]]: A list of merged intervals with no overlaps.
    """
    intervals.sort(key=lambda sublist: sublist[0])
    merged_intervals = []

    current_interval = intervals[0]
    merged_intervals.append(current_interval)

    for next_interval in intervals[1:]:
        _, current_end = current_interval
        next_start, next_end = next_interval

        if next_start <= current_end:
            current_interval[1] = max(current_end, next_end)
        else:
            current_interval = next_interval
            merged_intervals.append(current_interval)

    return merged_intervals
