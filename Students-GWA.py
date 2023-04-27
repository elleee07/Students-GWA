# ELLA MARIE A. MALLARI
# BSCPE 1-4

# STUDENTS GWA
with open("students_gwa.txt") as input_file:
    # possible lowest students gwa
    highest_gwa = 4.00
    highest_student = ""
    # read the txt.file (students_gwa.txt) and split it 
    for line in input_file:
        names, gwa_str = line.strip().split("-")
        # to get highest gwa
        gwa = float(gwa_str)
        if gwa < highest_gwa:
            highest_gwa = gwa
            highest_student = names
# print students name with highest GWA
print("Name of student: ", highest_student)

