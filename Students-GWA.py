# ELLA MARIE A. MALLARI
# BSCPE 1-4

# STUDENTS GWA
with open("students_gwa.txt") as input_file:
    # possible lowest students gwa
    highest_gwa = 4.00
    highest_student = ""
    # read the txt.file (students_gwa.txt) and split it 
    for line in input_file:
        