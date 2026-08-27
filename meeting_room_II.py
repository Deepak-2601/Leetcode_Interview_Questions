def minMeetingRooms(intervals):
    if not intervals:
        return 0
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])
    start_pointer, end_pointer = 0, 0
    used_rooms = 0
    while start_pointer < len(intervals):
        if starts[start_pointer] >= ends[end_pointer]:
            used_rooms -= 1
            end_pointer += 1
        used_rooms += 1    
        start_pointer += 1
    return used_rooms

intervals = [[0, 30], [5, 10], [15, 20]]
print(minMeetingRooms(intervals))