import sqlite3

# Attach to (or create) the database
connection = sqlite3.connect("./studentRecords.db")

# Create a new table with 3 fields
cursor = connection.cursor()
cursor.execute("""CREATE TABLE StudentSubjects (studentName text, year integer, subject text)""")

print("Database table StudentSubjects has been created")

# Create some test data, and write rows to the table.
test_data = [
    ("John", 2012, ["CompSci", "Physics"]),
    ("Kelly", 2012, ["Maths", "CompSci", "Stats"]),
    ("Kate", 2011, ["CompSci", "Accounting", "Economics", "Management"]),
    ("Sarah", 2011, ["InfSys", "Accounting", "Economics", "CommLaw"]),
    ("Ann", 2011, ["Sociology", "Economics", "Law", "Stats", "Music"])
]

for (student, yr, subjects) in test_data:
    for subj in subjects:
        t = (student, yr, subj)
        cursor.execute("INSERT INTO StudentSubjects VALUES (?,?,?)", t)

connection.commit()

# Now, verify that we did write the data
cursor.execute("SELECT COUNT(*) FROM StudentSubjects")
result = cursor.fetchall()
numrecs = result[0][0]
cursor.close()

print("StudentSubjects table now has {0} rows of data.".format(numrecs))

