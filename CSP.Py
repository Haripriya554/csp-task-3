subjects = ["Maths", "Python", "DBMS", "AI"]

time_slots = ["9:00 AM", "11:00 AM", "2:00 PM"]

constraints = [
    ("Maths", "Python"),
    ("DBMS", "AI")
]

timetable = {}

def is_valid(subject, time):
    for s1, s2 in constraints:
        if subject == s1 and s2 in timetable and timetable[s2] == time:
            return False
        if subject == s2 and s1 in timetable and timetable[s1] == time:
            return False
    return True

def backtrack(index):
    if index == len(subjects):
        return True

    subject = subjects[index]

    for time in time_slots:
        if is_valid(subject, time):
            timetable[subject] = time

            if backtrack(index + 1):
                return True

            del timetable[subject]

    return False

if backtrack(0):
    print("Final Timetable")
    print("----------------")
    for subject in subjects:
        print(subject, "->", timetable[subject])
else:
    print("No valid timetable found.")