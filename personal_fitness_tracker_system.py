# Personal Fitness Tracker System 🏋️‍♂️

# Lists to store fitness data
workouts = []  # To store workout types and durations
calories = []  # To store calorie intake for meals

# Variables for daily goals
workout_goal = 0  # Daily workout goal in minutes
calorie_goal = 0  # Daily calorie intake goal


def log_workout():
    workout_type = input("Enter workout type: ")
    try:
        duration = int(input("Enter workout duration in minutes: "))
        workouts.append((workout_type, duration))
        return f"Logged: {workout_type} for {duration}"
    except ValueError:
        return "❌ Invalid input! Duration should be a number.\n"


def log_calorie_intake():
    try:
        calories_consumed = int(input("Enter calories consumed: "))
        calories.append(calories_consumed)
        return f"Logged: {calories_consumed} calories.\n"
    except ValueError:
        return "❌ Invalid input! Calories should be a number.\n"



def view_progress():
    total_workout = sum(duration for _, duration in workouts)
    total_calories = sum(calories)

    print(f"\n===== Today's Progress =====")
    print(f"Total Workout Time: {total_workout} minutes")
    print(f"Total Calories Consumed: {total_calories} calories")
    print(encouragement_system(total_workout, total_calories))
    print("============================")


def reset_progress():
    while True:
        confirmation = input("Are you sure you want to reset your progress?(y/n)").lower()
        if confirmation == 'y':
            workouts.clear()
            calories.clear()
            return "Progress reset for the day. Let's start fresh! 💪"
        elif confirmation == 'n':
            return "Reset canceled. Keep up the good work!"
        else:
            print("❌ Invalid input! Please enter 'y' for Yes or 'n' for No.")


def set_daily_goals():
    global workout_goal, calorie_goal
    try:
        workout_goal = int(input("Enter daily workout goal(in minutes): "))
        calorie_goal = int(input("Enter daily calorie limit: "))
        return f"Daily goals set: {workout_goal} minutes workout, {calorie_goal} calories."
    except ValueError:
        return "❌ Invalid input! Please enter numeric values."


def encouragement_system(total_workout, total_calories):
    message = ""
    if workout_goal > 0:
        if total_workout >= workout_goal:
            message += "🎉 Awesome! You've achieved your workout goal!\n"
        else:
            message += f"🔥 Almost there! Just {workout_goal - total_workout} minutes left to reach your goal.\n"

    if calorie_goal > 0:
        if total_calories <= calorie_goal:
            message += "🍏 Great job! You're within your calorie limit!\n"
        else:
            message += f"⚠️ Careful! You've exceeded your calorie limit by {total_calories - calorie_goal} calories.\n"

    if not message:
        message = "💪 Keep going! Set some goals to get started.\n"
    return message


def main():
    print("Welcome to the Personal Fitness Tracker System 🏋️‍♂️\n")

    while True:
        # Display menu options
        print("1. Log Workout")
        print("2. Log Calorie Intake")
        print("3. View Progress")
        print("4. Reset Progress")
        print("5. Set Daily Goals")
        print("6. Exit")

        choice = input("\nEnter your choice: ")

        if choice == '1':
            log_workout()
        elif choice == '2':
            log_calorie_intake()
        elif choice == '3':
            view_progress()
        elif choice == '4':
            reset_progress()
        elif choice == '5':
            set_daily_goals()
        elif choice == '6':
            encouragement_system(total_workout, total_calories)
            print("Thank you for using the Fitness Tracker. Stay healthy! 💪")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
