class Class:

    def __init__(self, groups, teacher, subject, type, duration, classrooms):
        self.groups = groups
        self.teacher = teacher
        self.subject = subject
        self.type = type
        self.duration = duration
        self.classrooms = classrooms

    def __str__(self):
        return "Groups {} | Teacher '{}' | Subject '{}' | Type {} | {} hours | Classrooms {} \n"\
            .format(self.groups, self.teacher, self.subject, self.type, self.duration, self.classrooms)

    def __repr__(self):
        return str(self)