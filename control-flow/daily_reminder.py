task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case 'high':
        message = f"Reminder: "
    case 'medium':
        message = f"Reminder: "
    case 'low':
        message = f"Note: "
    case _:
        message = f"Task: "

if time_bound == 'yes':
    message += f"'{task}' is time-sensitive and requires immediate attention today!"
elif time_bound == 'no':
    message += f"'{task}' is a low priority task. Consider completing it when you have free time"

print(message)