import sqlite3

class Database:
    def __init__(self, db_name="patient.dataset.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def fetch_patients(self):
        self.cursor.execute("SELECT * FROM personality_dataset")
        return self.cursor.fetchall()

    def insert_patient(self, name_surname, gender, age,
                       Time_spent_alone, Social_event_attendance,
                       Drained_after_socializing, Friends, Personality):


# ბოლო patient id -ს მოძებნა
        self.cursor.execute("SELECT MAX(patient_Id) FROM personality_dataset")
        last_id = self.cursor.fetchone()[0]
        new_id = (last_id or 0) + 1

        self.cursor.execute("""
            INSERT INTO personality_dataset (
            patient_Id, name_surname, gender, age,
            Time_spent_alone, Social_event_attendance,
            Drained_after_socializing, Friends, Personality
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        new_id, name_surname, gender, age,
        Time_spent_alone, Social_event_attendance,
        Drained_after_socializing, Friends, Personality))
        self.conn.commit()

    def update_patient(self, patient_Id, age, Time_spent_alone,
                       Social_event_attendance, Drained_after_socializing,
                       Friends, Personality):
        self.cursor.execute("""
            UPDATE personality_dataset 
            SET age=?, Time_spent_alone=?, Social_event_attendance=?,
                Drained_after_socializing=?, Friends=?, Personality=?
            WHERE patient_Id=?
        """, (
            age, Time_spent_alone, Social_event_attendance,
            Drained_after_socializing, Friends, Personality, patient_Id
        ))
        self.conn.commit()

    def delete_patient(self, patient_Id):
        self.cursor.execute("DELETE FROM personality_dataset WHERE patient_Id=?", (patient_Id,))
        self.conn.commit()
