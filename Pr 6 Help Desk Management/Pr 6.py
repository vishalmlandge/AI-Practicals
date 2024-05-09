def evaluate_performance(presentation,communication,productivity,leadership,coding):

    # Weightage for each skill
    presentation_weight = 0.15
    communication_weight = 0.2
    productivity_weight = 0.2
    leadership_weight = 0.2
    coding_weight = 0.25

    # Calculate the overall score
    overall_score = (
        presentation * presentation_weight +
        communication * communication_weight +
        productivity * productivity_weight +
        coding * coding_weight
    )
    return overall_score

# Calculate Employee of the Year
def eof(employees):
    best_emp = None
    best_performance = -1
    for emp, skills in employees.items():
        performance = evaluate_performance(
            skills["presentation"],
            skills["communication"],
            skills["productivity"],
            skills["leadership"],
            skills["coding_skills"],
        )

        if performance > best_performance:
            best_emp = emp
            best_performance = performance
    return best_emp

# Calculate Best Employee by Skill
def best_employee_by_skill(employees, skill):
    best_emp = None
    best_performance = -1
    for emp, skills in employees.items():
        performance = skills[skill]
        if performance > best_performance:
            best_emp = emp
            best_performance = performance
    return best_emp

# Store skills for 5 employees
employees = {
    "Employee 1": {"presentation": 85, "communication": 90, "productivity": 80, "leadership": 75, "coding_skills": 80},
    "Employee 2": {"presentation": 70, "communication": 80, "productivity": 90, "leadership": 85, "coding_skills": 85},
    "Employee 3": {"presentation": 80, "communication": 75, "productivity": 85, "leadership": 90, "coding_skills": 75},
    "Employee 4": {"presentation": 90, "communication": 85, "productivity": 70, "leadership": 80, "coding_skills": 95},
    "Employee 5": {"presentation": 75, "communication": 70, "productivity": 95, "leadership": 85, "coding_skills": 70}
}

# Calculate performance for each employee
for emp, skills in employees.items():
    performance = evaluate_performance(
        skills["presentation"],
        skills["communication"],
        skills["productivity"],
        skills["leadership"],
        skills.get("coding_skills", 0) # If "coding_skills" is not present return default value 0
)
employees[emp]["performance"] = performance # Store the Performance of each Employee in Dictionary

# Prompt for Action
print("\nWhat do you want to know ? : \n")
print("1. Employee of the year")
print("2. Best employee by skill")
print("3. Best Employee by Coding Skills")
print("4. Exit")

while True:
    choice = input("\nEnter your choice (1-4): ")
    if choice == "1":
        best_employee_year = eof(employees)
        print("Employee of the Year:", best_employee_year)
    elif choice == "2":
        skill = input("Enter the skill name (presentation, communication,productivity, leadership): ").lower()
        if skill in ["presentation", "communication", "productivity","leadership"]:
            best_employee_skill = best_employee_by_skill(employees, skill)
            print(f"Best Employee for {skill.capitalize()}:{best_employee_skill}")
        else:
            print("Invalid skill name.")
    elif choice == "3":
        best_employee_coding = best_employee_by_skill(employees,"coding_skills")
        print(f"Best Employee for Coding Skills: {best_employee_coding}")
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")






