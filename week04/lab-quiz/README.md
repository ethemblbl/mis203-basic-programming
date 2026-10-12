# Lab 04: Savings Goal Planner

A Python simulation tool that calculates month-by-month compound savings growth with periodic monthly deposits and interest until a defined financial goal is met (or until reaching the 60-month cap).

---

## Testing & Iteration Notes

### 1. Test Scenario (Boundary Case)
- **Inputs Tested:**
  - Starting balance: `3000.0`
  - Monthly deposit: `500.0`
  - Monthly interest rate (%): `1.0`
  - Savings goal: `3000.0`
- **Expected Behavior:** Acceptance Check 4 states that if the starting balance already meets or exceeds the savings goal, no table rows should be printed, and an early exit message should be displayed.

### 2. Changes Made After Testing
- **Floating-Point Precision Fix (`EPSILON`):** During testing of the equality condition (`starting_balance == goal` or `balance == goal`), standard binary float representation could cause subtle precision mismatches (e.g., `2999.9999999999995 < 3000`). Introduced a small threshold constant `EPSILON = 1e-9` so that boundary comparisons (`balance >= goal - EPSILON`) evaluate accurately.
- **Immediate Return on Met Goal:** Added an upfront conditional check prior to table header printing to prevent generating empty tables when the user already meets the target.

---

## Acceptance Checks Coverage

| Test Case | Inputs (`balance`, `deposit`, `rate`, `goal`) | Result |
| :--- | :--- | :--- |
| **Check 1: Exact Match** | `0`, `1000`, `0%`, `3000` | Reached in 3 months. |
| **Check 2: Compound Interest** | `1000`, `500`, `1%`, `3000` | Reached in 4 months (Final: `3070.80`, Interest: `70.80`). |
| **Check 3: Max Cap** | `0`, `10`, `0%`, `10000` | Stops after 60 months (Final: `600.00`, Goal NOT reached). |
| **Check 4: Already Met** | `3000`, `500`, `1%`, `3000` | Exits early with message, no table printed. |
| **Check 5: Validation** | Negative balances/rates or non-positive deposit/goals | Reprompts until valid. Early loop exit via `break`. |
