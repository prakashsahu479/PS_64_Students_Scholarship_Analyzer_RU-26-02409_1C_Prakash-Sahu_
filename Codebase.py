students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print("\nStudent", i + 1)
    name = input("Name: ")
    marks = input("Marks: ")
    income = input("Income: ")
    attendance = input("Attendance: ")

    try:
        marks = float(marks)
    except ValueError:
        print("Invalid marks for " + name + ": '" + marks + "'. Row skipped.")
        continue
    try:
        income = float(income)
    except ValueError:
        print("Invalid income for " + name + ": '" + income + "'. Row skipped.")
        continue
    try:
        attendance = float(attendance)
    except ValueError:
        print("Invalid attendance for " + name + ": '" + attendance + "'. Row skipped.")
        continue

    if attendance >= 75 and marks >= 75 and income <= 500000:
        eligible = True
        if marks >= 90 and income <= 300000:
            scholarship = "Full"
            amount = 50000
        else:
            scholarship = "Partial"
            amount = 25000
    else:
        eligible = False
        scholarship = "Not Eligible"
        amount = 0

    students.append({
        "name": name,
        "marks": marks,
        "eligible": eligible,
        "scholarship": scholarship,
        "amount": amount,
    })

if len(students) == 0:
    print("\nNo valid records to process.")
else:
    print("\nMenu:")
    print("1. Eligibility")
    print("2. Summary")
    print("3. Filter by minimum marks")
    choice = input("Enter menu option: ")
    print()

    if choice == "1":
        for s in students:
            if s["eligible"]:
                print(s["name"], "|", s["scholarship"], "| Rs.", int(s["amount"]))
            else:
                print(s["name"], "| Not Eligible")

    elif choice == "2":
        eligible_count = 0
        not_eligible_count = 0
        full_count = 0
        partial_count = 0
        total_amount = 0
        marks_sum = 0

        for s in students:
            if s["eligible"]:
                eligible_count += 1
                marks_sum += s["marks"]
                total_amount += s["amount"]
                if s["scholarship"] == "Full":
                    full_count += 1
                else:
                    partial_count += 1
            else:
                not_eligible_count += 1

        if eligible_count > 0:
            average = marks_sum / eligible_count
        else:
            average = 0

        print("Eligible:", eligible_count, "| Not Eligible:", not_eligible_count,
              "| Full:", full_count, "| Partial:", partial_count)
        print("Total scholarship: Rs.", int(total_amount),
              "| Average marks (eligible):", format(average, ".2f"))

    elif choice == "3":
        min_marks = float(input("Enter minimum marks: "))
        for s in students:
            if s["marks"] >= min_marks:
                print(s["name"], "|", int(s["marks"]))

    else:
        print("Invalid menu option.")
