# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus: str) -> int:
    if not isinstance(skus, str) or not skus.isalpha():
        return -1

