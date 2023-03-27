

def main():
    student_name = get_name()
    student_roll_no = get_roll_no()
    print(f"{student_name}'s roll no. is {student_roll_no}")

def get_name():
    return input("Name: ")

def get_roll_no():
    return input("Roll No.: ")
   
