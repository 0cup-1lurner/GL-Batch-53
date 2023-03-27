

def main():
    student_name = get_name()
    student_roll_no = get_roll_no()
    print(f"{student_name}'s roll no. is {student_roll_no}")

def get_name():
    name = input("Name: ")
    return name

def get_roll_no():
    roll_no = input("Roll No.: ")
    return roll_no
