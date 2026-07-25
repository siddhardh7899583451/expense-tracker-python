from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class Expense:
    title: str
    amount: float
    category: str
    date: str = field(default_factory=lambda: datetime.now().strftime("%Y-%m-%d"))
    expense_id: str = field(default_factory=lambda: str(uuid4()))

    def __post_init__(self):
        if not self.title.strip():
            raise ValueError("Title cannot be empty.")

        if self.amount <= 0:
            raise ValueError("Amount must be greater than zero.")

        if not self.category.strip():
            raise ValueError("Category cannot be empty.")