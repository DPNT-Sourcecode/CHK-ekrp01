from collections import Counter
from dataclasses import dataclass


@dataclass
class SpecialOffer:
    quantity: int
    price: int


@dataclass
class FreeOffer:
    required_quantity: int
    free_item: str
    free_quantity: int


@dataclass
class SKU:
    name: str
    price: int
    special_offers: list[SpecialOffer] | None = None
    free_offer: FreeOffer | None = None


@dataclass
class GroupDiscount:
    items: list[str]
    quantity: int
    price: int


GROUP_DISCOUNT_STXYZ = GroupDiscount(["S", "T", "X", "Y", "Z"], 3, 45)


SKUS = {
    "A": SKU("A", 50, special_offers=[SpecialOffer(3, 130), SpecialOffer(5, 200)]),
    "B": SKU("B", 30, special_offers=[SpecialOffer(2, 45)]),
    "C": SKU("C", 20),
    "D": SKU("D", 15),
    "E": SKU("E", 40, free_offer=FreeOffer(2, "B", 1)),
    "F": SKU("F", 10, special_offers=[SpecialOffer(3, 20)]),
    "G": SKU("G", 20),
    "H": SKU("H", 10, special_offers=[SpecialOffer(5, 45), SpecialOffer(10, 80)]),
    "I": SKU("I", 35),
    "J": SKU("J", 60),
    "K": SKU("K", 70, special_offers=[SpecialOffer(2, 120)]),
    "L": SKU("L", 90),
    "M": SKU("M", 15),
    "N": SKU("N", 40, free_offer=FreeOffer(3, "M", 1)),
    "O": SKU("O", 10),
    "P": SKU("P", 50, special_offers=[SpecialOffer(5, 200)]),
    "Q": SKU("Q", 30, special_offers=[SpecialOffer(3, 80)]),
    "R": SKU("R", 50, free_offer=FreeOffer(3, "Q", 1)),
    "S": SKU("S", 20),
    "T": SKU("T", 20),
    "U": SKU("U", 40, special_offers=[SpecialOffer(4, 120)]),
    "V": SKU("V", 50, special_offers=[SpecialOffer(2, 90), SpecialOffer(3, 130)]),
    "W": SKU("W", 20),
    "X": SKU("X", 17),
    "Y": SKU("Y", 20),
    "Z": SKU("Z", 21),
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
        # breakpoint()
        if sku not in SKUS:
            return -1

        sku_data = SKUS[sku]

        if sku_data.free_offer is not None:
            free_offer = sku_data.free_offer
            free_trigger_count = count // free_offer.required_quantity
            free_item_count = free_offer.free_quantity * free_trigger_count

            free_item = free_offer.free_item
            if free_item in sku_counts:
                sku_counts[free_item] = max(0, sku_counts[free_item] - free_item_count)

    group_items = GROUP_DISCOUNT_STXYZ.items
    group_count = sum(sku_counts.get(item, 0) for item in group_items)
    group_price = GROUP_DISCOUNT_STXYZ.price
    group_quantity = GROUP_DISCOUNT_STXYZ.quantity
    group_discount_count = group_count // group_quantity
    checkout_total += group_discount_count * group_price

    sku_counts_in_group_discount = {sku: count for sku, count in sku_counts.items() if sku in group_items}
    total_items_in_group_discount = sum(sku_counts_in_group_discount.values())
    skus_in_group_discount_by_price = sorted(sku_counts_in_group_discount, key=lambda x: SKUS[x].price, reverse=True)
    skus_in_group_discount: list[str] = []
    for sku in skus_in_group_discount_by_price:
        skus_in_group_discount.extend([sku] * sku_counts_in_group_discount[sku])

    for sku in sorted(group_items, key=lambda x: SKUS[x].price, reverse=True):


    for sku, count in sku_counts.items():
        special_offers = SKUS[sku].special_offers

        if special_offers:
            ordered_special_offers = sorted(
                special_offers, key=lambda x: x.quantity, reverse=True
            )

            for special_offer in ordered_special_offers:
                if count >= special_offer.quantity:
                    special_offer_count = count // special_offer.quantity
                    remaining_count = count % special_offer.quantity
                    checkout_total += special_offer_count * special_offer.price
                    count = remaining_count

        checkout_total += count * SKUS[sku].price

    return checkout_total

