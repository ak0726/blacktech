class Habit:
    def __init__(self, name, spent, times, frequency, category):
        self.name = name
        self.spent = spent
        self.times = times
        self.frequency = frequency
        self.category = category

category_spending = {}
habits = []
total = 0
small_screen = False

def to_dollar_string(num):
    return '{:.2f}'.format(num)

def reset_inputs():
    pass  # Clear inputs (implementation may vary based on your requirements)

def print_category_spending():
    print("Category Spending:")
    for category, amount in category_spending.items():
        print("I have spent Rs " + to_dollar_string(amount) + " on " + category)
    print("How can I improve my expenditure. Give me tips and financial advice regarding the same")

while True:
    input_spent = input("Enter amount spent: ")
    input_habit = input("Enter habit name: ")
    input_times = input("Enter number of times: ")
    input_frequency = input("Enter frequency (daily/weekly/monthly/yearly): ")
    input_category = input("Enter category: ")

    # Calculate expenditure
    freq_multiplier = 0
    if input_frequency == "daily":
        freq_multiplier = 365
    elif input_frequency == "weekly":
        freq_multiplier = 52
    elif input_frequency == "monthly":
        freq_multiplier = 12
    elif input_frequency == "yearly":
        freq_multiplier = 1

    spent = float(input_spent)
    times = int(input_times)

    habit_total = spent * times * freq_multiplier
    total += habit_total

    # Store habit
    habit = Habit(input_habit, spent, times, input_frequency, input_category)
    habits.append(habit)

    # Update category spending
    if input_category in category_spending:
        category_spending[input_category] += habit_total
    else:
        category_spending[input_category] = habit_total

    # Print results
    habit_total_text = to_dollar_string(habit_total)
    total_text = to_dollar_string(total)
    spent_text = to_dollar_string(spent)

    if small_screen:
        print(input_habit + " annual cost: Rs " + habit_total_text)
        print("Total spent: Rs " + total_text)
    else:
        print("You spend Rs " + spent_text + " on " + input_habit + " - " + input_times, end="")
        if times < 2:
            print(" time ", end="")
        else:
            print(" times ", end="")
        print(input_frequency + " - yearly cost is: Rs " + habit_total_text)
        print("Total spent: Rs " + total_text)

    # Print category spending
    print_category_spending()

    # Reset inputs
    reset_inputs()
