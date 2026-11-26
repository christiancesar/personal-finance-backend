from entities.payment_type import PaymentType

payment_types: list[PaymentType] = [
    PaymentType(name="Credit Card"),
    PaymentType(name="Debit Card"),
    PaymentType(name="Cash"),
    PaymentType(name="Transfer"),
    PaymentType(name="Deposit"),
    PaymentType(name="Boleto"),
]
