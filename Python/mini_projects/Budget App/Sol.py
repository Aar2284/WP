from typing import Any

class Category:
    def __init__(self, name: str):
        self.name = name
        self.ledger: list[dict[str, Any]] = []

    def deposit(self, amount: float, description: str = "") -> None:
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description: str = "") -> bool:
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self) -> float:
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount: float, other_category: "Category") -> bool:
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {other_category.name}")
            other_category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount: float) -> bool:
        return amount <= self.get_balance()

    def __str__(self) -> str:
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            desc = item["description"][:23]
            amt = "{:.2f}".format(item["amount"])
            items += f"{desc:<23}{amt:>7}\n"
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories: list[Category]) -> str:
    spendings: list[float] = []
    for cat in categories:
        spent = sum(-item["amount"] for item in cat.ledger if item["amount"] < 0 and not item["description"].startswith("Transfer to"))
        spendings.append(spent)
    
    total_spent = sum(spendings)
    
    percentages: list[int] = [int((s / total_spent) * 100) // 10 * 10 if total_spent > 0 else 0 for s in spendings]
    
    chart = "Percentage spent by category\n"
    
    for i in range(100, -1, -10):
        chart += f"{i:>3}|"
        for p in percentages:
            chart += " o " if p >= i else "   "
        chart += " \n"
        
    chart += "    " + "-" * (3 * len(categories) + 1) + "\n"
    
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)
    
    for i in range(max_len):
        chart += "     "
        for name in names:
            chart += (name[i] if i < len(name) else " ") + "  "
        
        if i < max_len - 1:
            chart += "\n"
            
    return chart


if __name__ == "__main__":
    food = Category("Food")
    clothing = Category("Clothing")
    auto = Category("Auto")

    food.deposit(1000, "initial deposit")
    food.withdraw(10.15, "groceries")
    food.withdraw(15.89, "restaurant and more food for dessert")
    food.transfer(50, clothing)
    
    clothing.withdraw(25.55)
    clothing.withdraw(100)
    
    auto.deposit(1000, "initial deposit")
    auto.withdraw(15)

    print(food)
    print("\n" + "="*30 + "\n")
    
    print(create_spend_chart([food, clothing, auto]))