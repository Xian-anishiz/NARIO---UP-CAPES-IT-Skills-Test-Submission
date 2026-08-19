class Account:
    def __init__(self, id: str, name: str) -> None:
        self._id = id
        self._name = name

        self.validateInstance()

    def validateInstance(self):
        if len(self._id) != 5:
            raise AttributeError

        if not self._name:
            raise AttributeError

    @property
    def name(self) -> str:
        return self._name

class StudentAccount(Account):
    def __init__(self, id: str, name: str) -> None:
        super().__init__(id, name)
        self._classes: list[str] = []
        self._is_enlistment_locked: bool = False
        self._is_enlisted: bool = False
    
    def add_class(self, course: str) -> None:
        self._classes.append(course)

    def lock_enlistment(self) -> None:
        self._is_enlistment_locked = True
        print(f'{self._name} has locked enlistment.')

    @property
    def is_enlistment_locked(self) -> bool:
        return self._is_enlistment_locked

    @property
    def is_enlisted(self) -> bool:
        return self._is_enlisted

    @is_enlisted.setter
    def is_enlisted(self, x: bool) -> None:
        self._is_enlisted = x

class AdviserAccount(Account):
    def __init__(self, id: str, name: str) -> None:
        super().__init__(id, name)
        self._advisees: set[StudentAccount] = set()
        self._enlisted_advisees: list[str] = []

    def add_advisee(self, student: StudentAccount) -> None:
        self._advisees.add(student)
        print(f'{self._name} has added {student.name} as an advisee.')

    def print_advisees(self) -> None:
        print(self._advisees)

    def lock_enlistment_for(self, student: StudentAccount) -> None:
        if student not in self._advisees:
            print(f'Error: {student.name} is not an advisee of {self.name}.')
        elif not student.is_enlistment_locked:
            print(f'Error: {student.name}\'s enlistment is not locked yet.') 
        else:
            print(f'{student.name} is now enlisted.')
            student.is_enlisted = True


if __name__ == "__main__":
    student1 = StudentAccount("05524", "Ross")
    student1.add_class("Class 1")
    student1.add_class("Class 2")
    student1.add_class("Class 4")
    student1.lock_enlistment()


    adviser = AdviserAccount("01341", "Rachel")
    adviser.add_advisee(student1)
    adviser.lock_enlistment_for(student1)


    student2 = StudentAccount("12345", "Chandler")
    student2.add_class("Class 1")
    student2.add_class("Class 3")


    adviser.add_advisee(student2)
    adviser.lock_enlistment_for(student2)


    student3 = StudentAccount("01353", "Joey")
    student3.add_class("Class 5")
    student3.add_class("Class 9")


    adviser.lock_enlistment_for(student3)