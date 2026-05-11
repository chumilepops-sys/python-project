# ============================================
# QUESTION 2
# Online Purchase Summariser
# ============================================

import datetime
import pickle


# Calculate VAT (15%)
def calculate_vat(price):
    return price * 0.15


# Calculate discount
def calculate_discount(price, discount_percentage):
    return price * (discount_percentage / 100)


# Calculate final amount
def calculate_final_amount(price, vat_amount, discount_amount):
    return price + vat_amount - discount_amount


def main():

    # User input
    price = float(input("Enter item price: "))
    discount_percentage = float(input("Enter discount percentage: "))

    # Calculations
    vat_amount = calculate_vat(price)
    discount_amount = calculate_discount(price, discount_percentage)
    final_amount = calculate_final_amount(price, vat_amount, discount_amount)

    # Timestamp
    timestamp = datetime.datetime.now()

    # Receipt dictionary
    receipt_data = {
        "price": price,
        "vat": vat_amount,
        "discount": discount_amount,
        "final_amount": final_amount,
        "timestamp": str(timestamp)
    }

    # Print receipt
    print("\n================ RECEIPT ================\n")
    print(f"Original Price : R{price}")
    print(f"VAT (15%)      : R{vat_amount}")
    print(f"Discount       : R{discount_amount}")
    print(f"Final Amount   : R{final_amount}")
    print(f"Timestamp      : {timestamp}")
    print("\n========================================\n")

    # Write to text file
    with open("receipt.txt", "w") as file:
        file.write("RECEIPT\n\n")
        file.write(f"Original Price: R{price}\n")
        file.write(f"VAT: R{vat_amount}\n")
        file.write(f"Discount: R{discount_amount}\n")
        file.write(f"Final Amount: R{final_amount}\n")
        file.write(f"Timestamp: {timestamp}\n")

    # Save using pickle
    with open("receipt.pkl", "wb") as file:
        pickle.dump(receipt_data, file)

    print("Receipt successfully saved to receipt.txt and receipt.pkl")


# Run program
main()