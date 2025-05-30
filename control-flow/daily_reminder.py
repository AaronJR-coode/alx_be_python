task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case 'high':
        message = "Reminder: "
    case 'medium':
        message = "Reminder: "
    case 'low':
        message = "Note: "
    case _:
        message = "Task: "

if time_bound == 'yes':
    message += f"'{task}' is time-sensitive and requires immediate attention today!"
elif time_bound == 'no':
    message += f"'{task}' is a low priority task. Consider completing it when you have free time"

print(Reminder)
print(message)
