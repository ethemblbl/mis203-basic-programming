# Lab 03: Order Approval Policy

## Boundary Test Cases

| Scenario | Requested Qty / Stock | Amount (TRY) | Member? | Expected Result |
| :--- | :--- | :--- | :--- | :--- |
| **Boundary Below (499 TRY)** | 2 / 10 | 499.00 | Yes | Approved, No discount, Final: 499.00 TRY |
| **Boundary Exactly At (500 TRY)** | 2 / 10 | 500.00 | Yes | Approved, 10% discount, Final: 450.00 TRY |
| **Boundary Above (501 TRY)** | 2 / 10 | 501.00 | Yes | Approved, 10% discount, Final: 450.90 TRY |
| **Error / Rejection Case** | 12 / 10 | 600.00 | Yes | Rejected (Insufficient stock, no price shown) |

## Testing & Adjustments Note
- **Test Run:** Tested boundary case with 500 TRY as a member.
- **Change Made After Testing:** Initially, the condition used `order_amount > 500`, which excluded orders exactly at 500 TRY.
-  After running the boundary test, updated the condition to `order_amount >= 500` to correctly meet the policy requirements.

AI Tool: Gemini,
  Propmt: Ödevin mantığını anlamam için örnekleyerek anlat. Ardından kodu yazacağız.
