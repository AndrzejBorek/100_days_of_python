import pandas

student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]
}

student_df = pandas.DataFrame(student_dict)
#
# for (key, value) in student_df.items():
#     print(key)
#
# for (key, value) in student_df.items():
#     print(value)

for (index, row) in student_df.iterrows():
    print(str(row.student) + " " + str(row.score))
