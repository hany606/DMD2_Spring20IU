from DB import Hospital

db = Hospital(database="Hospital")
# db.clean_schema_files()
db.generate()
db.pg_query("schema.sql")
# db.pg_query("data/dep_lab.sql")
# db.pg_query("data/person_member.sql")
# db.pg_query("data/contact_details.sql")
# db.pg_query("data/appointment.sql")
# db.pg_query("data/complaint.sql")
# db.pg_query("data/medicine_surgery.sql")
# db.pg_query("data/events_other.sql")
# db.pg_query("data/feedback.sql")
# db.pg_query("data/schedule.sql")
# db.pg_query("data/appointment_q3_sick.sql")