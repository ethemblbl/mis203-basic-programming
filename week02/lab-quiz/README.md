# Lab 02 - Purchase Quote

This program calculates a purchase quote for two items.

The program asks the user for:

* Two item names
* Quantities
* Unit prices
* Delivery fee
* Tax percentage

It calculates the total for each item, the subtotal, the tax, and the final total.

Tax is calculated only on the item subtotal. The delivery fee is added after the tax is calculated.

## Test

I tested the program with:

* First item: 2 × 50 TRY
* Second item: 1 × 80 TRY
* Delivery fee: 20 TRY
* Tax: 10%

Expected final total:

`218.00 TRY`

The program produced `218.00 TRY`.

## Change After Testing

After testing, I changed the quantity inputs to use `int()` because `input()` returns text. I also corrected the final total calculation so that the delivery fee is added after the tax.
AI(ChatGPT) has been used.
