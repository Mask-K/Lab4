from collections import namedtuple

week_schedule = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday"}
time_schedule = {
    1: "8:40-10:15",
    2: "10:35-12:10",
    3: "12:20-13:55",
}

Classroom = namedtuple("Classroom", "room is_big")
Time = namedtuple("Time", "weekday time")
Teacher = namedtuple("Teacher", "name")
Subject = namedtuple("Subject", "name")
Group = namedtuple("Group", "name")
Lesson = namedtuple("Lesson", "teacher subject group is_lecture per_week")
Schedule = namedtuple("Schedule", "lessons classrooms times")
DomainEl = namedtuple("DomainEl", "day time room")

Classroom.__repr__ = lambda c: f"{c.room} ({'big' if c.is_big else 'small'})"
Teacher.__repr__ = lambda t: f"{t.name.split()[1]}"
Subject.__repr__ = lambda s: f"{s.name.split()[1]}"
Group.__repr__ = lambda g: f"{g.name}"
Lesson.__repr__ = (
    lambda l: f"{l.teacher} | {l.subject} | {l.group} | "
    f"{'Lecture' if l.is_lecture else 'Seminar'} {l.per_week}/week"
)

def gen_repr(g: Schedule):
    output = ""
    for i in range(len(g.lessons)):
        output += f"{g.lessons[i]},   {g.classrooms[i]},   {g.times[i]}\n"
    return output

Schedule.__repr__ = lambda g: gen_repr(g)


classrooms = [
    Classroom(43, True),
    Classroom(42, True),
    Classroom(41, True),
    Classroom(228, False),
    Classroom(217, False),
    Classroom(206, False),
]

schedule = [
    Time(w, n)
    for w in range(1, len(week_schedule.keys()) + 1)
    for n in range(1, len(week_schedule.keys()) + 1)
]

teachers = [
    Teacher(name)
    for name in (
        "0 John_Smith",
        "1 Alice_Johnson",
        "2 Bob_Williams",
        "3 Eva_Davis",
        "4 Michael_Brown",
        "5 Olivia_White",
        "6 Daniel_Miller",
        "7 Sophia_Wilson",
        "8 Matthew_Taylor",
        "9 Emily_Anderson",
        "10 David_Martinez",
        "11 Emma_Jackson",
        "12 Christopher_Garcia",
        "13 Ava_Thomas",
        "14 Andrew_Moore",
        "15 Isabella_Lee",
        "16 James_Harris",
        "17 Sophie_Clark",
        "18 Benjamin_Turner",
    )
]

subjects = [
    Subject(name)
    for name in (
        "0 Mathematics",
        "1 Physics",
        "2 Chemistry",
        "3 Biology",
        "4 History",
        "5 English",
        "6 Computer_Science",
        "7 Geography",
        "8 Economics",
        "9 Psychology",
        "10 Sociology",
        "11 Political_Science",
        "12 Art",
        "13 Music",
        "14 Physical_Education",
        "15 Foreign_Language",
        "16 Statistics",
        "17 Philosophy"
    )
]

groups = [
    Group(name)
    for name in (
        "Group-A",
        "Group-B",
        "Group-C",
        "Group-D",
        "Group-E",
    )
]


lessons = [
    Lesson(teachers[0], subjects[0], groups[0], False, 1),
    Lesson(teachers[1], subjects[1], groups[0:5], True, 1),
    Lesson(teachers[2], subjects[2], groups[0], True, 2),
    Lesson(teachers[2], subjects[2], groups[0], True, 2),
    Lesson(teachers[3], subjects[12], groups[0], True, 1),
    Lesson(teachers[4], subjects[4], groups[0:5], True, 1),
    Lesson(teachers[5], subjects[4], groups[0], False, 1),
    Lesson(teachers[5], subjects[15], groups[0], True, 1),
    Lesson(teachers[9], subjects[6], groups[0:5], True, 1),
    Lesson(teachers[13], subjects[4], groups[0], False, 1),
    Lesson(teachers[13], subjects[16], groups[0], True, 2),
    Lesson(teachers[13], subjects[16], groups[0], True, 2),
    Lesson(teachers[5], subjects[4], groups[1], False, 1),
    Lesson(teachers[5], subjects[4], groups[2], False, 1),
    Lesson(teachers[6], subjects[4], groups[1], False, 1),
    Lesson(teachers[7], subjects[4], groups[2], False, 1),
    Lesson(teachers[8], subjects[3], groups[1:3], True, 1),
    Lesson(teachers[10], subjects[7], groups[1], False, 2),
    Lesson(teachers[10], subjects[7], groups[1], False, 2),
    Lesson(teachers[10], subjects[7], groups[2], False, 2),
    Lesson(teachers[10], subjects[7], groups[2], False, 2),
    Lesson(teachers[11], subjects[8], groups[1:3], True, 2),
    Lesson(teachers[11], subjects[8], groups[1:3], True, 2),
    Lesson(teachers[12], subjects[9], groups[1:3], True, 2),
    Lesson(teachers[12], subjects[9], groups[1:3], True, 2),
    Lesson(teachers[18], subjects[10], groups[1:3], True, 1),
    Lesson(teachers[5], subjects[4], groups[3], False, 1),
    Lesson(teachers[5], subjects[4], groups[4], False, 1),
    Lesson(teachers[6], subjects[4], groups[3], False, 1),
    Lesson(teachers[6], subjects[4], groups[4], False, 1),
    Lesson(teachers[14], subjects[12], groups[3:5], True, 2),
    Lesson(teachers[14], subjects[12], groups[3:5], True, 2),
    Lesson(teachers[15], subjects[13], groups[3:5], False, 1),
    Lesson(teachers[16], subjects[11], groups[3:5], True, 2),
    Lesson(teachers[16], subjects[11], groups[3:5], True, 2),
    Lesson(teachers[17], subjects[14], groups[3:5], True, 1),
    Lesson(teachers[17], subjects[17], groups[3:5], True, 1),
]