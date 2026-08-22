class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sum_of_students = sum(students)
        len_of_students = len(students)
        for sandwich in sandwiches:
            print(f"sum_of_students : {sum_of_students}")
            print(f"len_of_students : {len_of_students}")
            if sandwich == 1 and sum_of_students > 0:
                sum_of_students -= 1
                len_of_students -= 1
                continue
            if sandwich == 0 and sum_of_students < len_of_students:
                len_of_students -= 1
                continue
            return len_of_students
        return 0