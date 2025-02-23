from typing import List

from entities.bank import Bank

banks: List[Bank] = [
    Bank(
        ispb="18236120",
        name="Nubank",
        code=260,
        fullName="Nu Pagamentos S.A.",
    ),
    Bank(
        ispb="60701190",
        name="Itaú",
        code=341,
        fullName="Itaú Unibanco S.A.",
    ),
    Bank(ispb="00416968", name="Inter", code=77, fullName="Banco Inter S.A."),
]
