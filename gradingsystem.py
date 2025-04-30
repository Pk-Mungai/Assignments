import math

def get_names_score()->tuple[list[str],list[float]]:
    while True:
        #error handling
        try:
            count=int(input("Number of Students: "))
            if count <=0:
                print("Please enter a greater number than zero")
                continue
            break
        except ValueError:
            print("invalid Input!")

    names_of_students = []
    scores = []

    print("\nEnter student names and their scores: ")

    for i in range(count):
        name = input(f'Student name {i+1} : ').strip() #strip removes all the white spaces
        if not name:
            name = f'Student:{i+1}'
        names_of_students.append(name)

        while True:
            try:
                score = float(input(f"Enter the score for {name}: "))
                if 0 <= score <=100:
                    scores.append(score)
                    break
                else:
                    print("Score must be between 0 and 100")

            except ValueError:
                print("Invalid Input")

    return names_of_students, scores
def match_grade(score: float) -> str:
    match True:

        case _ if score >= 70:
            return "A"

        case _ if score >= 60:
            return "B"

        case _ if score >= 50:
            return "C"

        case _ if score >= 40:
            return "D"

        case _:
            return "F"

def calculate_avg(scores: list[float]) -> float:
    return round(sum(scores) / len(scores), 2)

def results_table(names_of_students: list[str], scores: list[float]) -> None:

    print("\n== Students Results ==")

    print(f"{'Name':<15} {'Score':<10} {'Grade'}")

    print("-" * 30)
    
    for i in range(len(names_of_students)):
        name = names_of_students[i]
        score = scores[i]
        grade = match_grade(score)
        print(f"{name:<15} {score:<10.2f} {grade}")

    avg_score = calculate_avg(scores)
    print("\nClass Average: ", avg_score)
    print("\nRound Up: ", math.ceil(avg_score))
    print("\nRound Down: ", math.floor(avg_score))

def main():
    print("== Grading System ==")

    while True:

        names_of_students,scores = get_names_score()
        results_table(names_of_students, scores)
        looper = input("\nGrade another class? (input yes/no): ").strip().lower()

        if looper != "yes":
            print("Thank you for using Python grading system!")

            break

if __name__ == "__main__":
    main()
    
        
    
# show_history()
# names, scores = get_names_score()_score))
#     print("\nRounded Down:", math.floor(average
# def calculator_average(scores: list[int]) -> float:
#     return sum(scores) / len(scores)
# print(f"\n Average score: {calculator_average(scores): .2f}")