def apply_discount(price: int, discount: float = 0.0) -> int:
    """Apply Discount Percent and Calculate Final Price"""
    if price <= 0:
        raise ValueError("Price must be a positive integer")
    if not 0 <= discount <= 1:
        raise ValueError("Discount must be a number between 0 and 1")

    final_price = int(price * (1 - discount))
    if not 0 < final_price <= price:
        raise ValueError(f"Final price {final_price} is not between 0 and {price}")

    return final_price