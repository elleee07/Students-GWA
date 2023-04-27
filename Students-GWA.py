# ELLA MARIE A. MALLARI
# BSCPE 1-4

# STUDENTS GWA
with open("students_gwa.txt") as input_file:
    # lowest GWA     
    students_gwa = 4.00
    highest_student = ""
    # read the txt.file (students_gwa.txt) and split it 
    for line in input_file:
        names, gwa_str = line.strip().split("-")
        # to get highest gwa
        gwa = float(gwa_str)
        if gwa < students_gwa:
            students_gwa = gwa
            highest_student = names
# print students name with highest GWA
print("\033[90m=" * 50)
print("\033[33mName of student: ", highest_student)
print("\033[90m=" * 50)
print("\033[92mGeneral Weighted Average : ", students_gwa)