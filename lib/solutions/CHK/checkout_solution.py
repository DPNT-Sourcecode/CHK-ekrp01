from collections import Counter
from dataclasses import dataclass


@dataclass
class SpecialOffer:
    quantity: int
    price: int


@dataclass
class SKU:
    name: str
    price: int
    special_offer: SpecialOffer | None = None


SKUS = {
    "A": SKU("A", 50, SpecialOffer(3, 130)),
    "B": SKU("B", 30, SpecialOffer(2, 45)),
    "C": SKU("C", 20),
    "D": SKU("D", 15),
}


# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if skus == "":
        return 0

    if not isinstance(skus, str) or not skus.isalpha():
        return -1

    checkout_total = 0

    sku_counts = Counter(skus)

    for sku, count in sku_counts.items():
        if sku not in SKUS:
            return -1

        special_offer = SKUS[sku].special_offer

        if special_offer is not None:
            special_offer_count = count // special_offer.quantity
            remaining_count = count % special_offer.quantity
            checkout_total += special_offer_count * special_offer.price
            checkout_total += remaining_count * SKUS[sku].price
        else:
            checkout_total += count * SKUS[sku].price

    return checkout_total
