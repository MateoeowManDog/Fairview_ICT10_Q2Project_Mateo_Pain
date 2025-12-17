#GWA CALCULATOR
def calculate_gwa(science, math, english, filipino, ict, pe):
    grades = [science, math, english, filipino, ict, pe]
    gwa = sum(grades) / len(grades)
    return round(gwa, 2)
