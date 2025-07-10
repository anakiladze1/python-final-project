class Patient:
    def __init__(self, patient_Id, name_surname, gender, age, Time_spent_alone, Social_event_attendance,
                 Drained_after_socializing, Friends, Personality):
        self.id = patient_Id
        self.name = name_surname
        self.gender = gender
        self.age = age
        self.time_spent_alone = Time_spent_alone
        self.social_event_attendance = Social_event_attendance
        self.drained_after_socializing = Drained_after_socializing
        self.friends = Friends
        self.personality = Personality

