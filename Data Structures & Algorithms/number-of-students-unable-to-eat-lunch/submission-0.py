class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        students_queue = StudentsQueue(students=students)
        for sandwich in sandwiches:
            found = False
            for i in range(students_queue.length):
                if students_queue.get_current_student_preference() == sandwich:
                    students_queue.deque()
                    found = True
                    break
                else:
                    students_queue.move_to_back()
            if found:
                continue
            return students_queue.length
        return 0


class StudentsQueue:
    def __init__(self, students: List[int]) -> None:
        self.length = len(students)
        self.head = Student(preference=students[0])
        prev = self.head
        for i in range(len(students) - 1):
            prev.next = Student(preference=students[i + 1])
            prev = prev.next
        self.tail = prev

    def get_current_student_preference(self) -> int:
        return self.head.preference

    def move_to_back(self) -> None:
        current_head = self.head
        self.head = current_head.next
        self.tail.next = current_head
        self.tail = self.tail.next
        self.tail.next = None

    def deque(self) -> None:
        self.head = self.head.next
        self.length -= 1


class Student:
    def __init__(self, preference: int, next=None):
        self.preference = preference
        self.next = next
