task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case 'high':
        message = f"High-priority task: '{task}'."
    case 'medium':
        message = f"Medium-priority task: '{task}'."
    case 'low':
        message = f"Low-priority task: '{task}'."
    case _:
        message = f"Task: '{task}'."

if time_bound == 'yes':
    message += " This is time-sensitive and requires immediate attention today!"
elif time_bound == 'no':
    message += f"Note: {task} is a low priority task. Consider completing it when you have free time"

print("\nReminder ")
print(message)