"""Lab 04 - Savings Goal Planner.

Simulates monthly savings: interest is added first, then the deposit.
Stops when the goal is reached or after MAX_MONTHS months.
"""

MAX_MONTHS = 60
EPSILON = 1e-9  # protects the "balance == goal" check from float rounding


def read_number(prompt, allow_zero):
    """Keep asking until the user enters a valid number.

    allow_zero=True  -> value must be >= 0
    allow_zero=False -> value must be > 0
    """
    while True:
        text = input(prompt).strip()
        try:
            value = float(text)
        except ValueError:
            print("  Invalid input: please enter a number.")
            continue

        if allow_zero and value < 0:
            print("  Value cannot be negative. Try again.")
        elif not allow_zero and value <= 0:
            print("  Value must be greater than zero. Try again.")
        else:
            return value


def main():
    starting_balance = read_number("Starting balance: ", allow_zero=True)
    monthly_deposit = read_number("Monthly deposit: ", allow_zero=False)
    monthly_rate = read_number("Monthly interest rate (%): ", allow_zero=True)
    goal = read_number("Savings goal: ", allow_zero=False)

    # Boundary case: already at the goal, no simulation needed.
    if starting_balance >= goal - EPSILON:
        print(f"\nYour starting balance ({starting_balance:.2f}) already "
              f"meets the goal ({goal:.2f}). No savings months needed.")
        return

    balance = starting_balance
    total_interest = 0.0
    goal_reached = False
    months_used = 0

    print(f"\n{'Month':>5} | {'Interest':>12} | {'Balance':>14}")
    print("-" * 38)

    for month in range(1, MAX_MONTHS + 1):
        interest = balance * monthly_rate / 100
        balance += interest      # 1) interest on the current balance
        balance += monthly_deposit  # 2) then the deposit
        total_interest += interest
        months_used = month

        print(f"{month:>5} | {interest:>12.2f} | {balance:>14.2f}")

        if balance >= goal - EPSILON:
            goal_reached = True
            break

    print("-" * 38)
    if goal_reached:
        print(f"Goal of {goal:.2f} reached in {months_used} month(s).")
    else:
        print(f"Goal of {goal:.2f} NOT reached after {MAX_MONTHS} months.")
    print(f"Final balance:  {balance:.2f}")
    print(f"Total interest: {total_interest:.2f}")


if __name__ == "__main__":
    main()