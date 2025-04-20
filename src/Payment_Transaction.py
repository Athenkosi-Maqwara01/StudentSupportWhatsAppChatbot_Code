from datetime import datetime, timedelta

class PaymentTransaction:
    def __init__(self, transaction_id, amount, payment_method, reference_number):
        self.__transaction_id = transaction_id
        self.__amount = amount
        self.__timestamp = datetime.now()
        self.__payment_method = payment_method
        self.__status = "Pending"
        self.__reference_number = reference_number
        self.__retries = 0

    # Getters and Setters
    def get_status(self):
        return self.__status

    def set_status(self, new_status):
        if new_status in ["Pending", "Completed", "Failed", "Disputed"]:
            self.__status = new_status

    # Methods
    def process_payment(self):
        if self.__retries >= 3:
            self.__status = "Failed"
            print(f"Payment failed after {self.__retries} attempts.")
            return

        try:
            # Simulated success logic
            self.__status = "Completed"
            print(f"Payment of R{self.__amount} processed successfully.")
        except Exception:
            self.__retries += 1
            self.__status = "Failed"
            print(f"Attempt {self.__retries} failed. Retrying...")

    def verify_payment(self):
        return self.__status == "Completed"

    def generate_receipt(self):
        if self.__status == "Completed":
            return {
                "Transaction ID": self.__transaction_id,
                "Amount": self.__amount,
                "Timestamp": self.__timestamp,
                "Reference": self.__reference_number
            }
        else:
            print("Cannot generate receipt: Payment not completed.")
            return None

    def reconcile(self):
        now = datetime.now()
        if now - self.__timestamp > timedelta(hours=24):
            print("Warning: Reconciliation overdue.")
        else:
            print("Transaction reconciled.")
