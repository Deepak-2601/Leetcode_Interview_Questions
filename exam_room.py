class ExamRoom(object):
    def __init__(self, n):
        self.n = n
        self.students = []

    def seat(self):
        if not self.students:
            self.students.append(0)
            return 0
        max_distance = 0
        seat_to_take = 0
        if self.students[0] != 0:
            max_distance = self.students[0]
            seat_to_take = 0
        for i in range(len(self.students) - 1):
            distance = (self.students[i + 1] - self.students[i]) // 2
            if distance > max_distance:
                max_distance = distance
                seat_to_take = self.students[i] + distance
        if self.n - 1 - self.students[-1] > max_distance:
            seat_to_take = self.n - 1
        self.students.append(seat_to_take)
        self.students.sort()
        return seat_to_take
    
    def leave(self, p):
        self.students.remove(p)

My_ExamRoom = ExamRoom(10)

print(My_ExamRoom.seat())