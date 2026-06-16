# utils/packing.py
def default_packing(season: str, activities: str) -> list:
    """Return a baseline packing list based on season and planned activities."""
    base = ["ID proof", "Phone & charger", "Power bank",
            "Toiletries", "Medicines", "Cash + Card"]
    s = (season or "").lower()
    a = (activities or "").lower()
    if s in ["winter", "snowy", "cool"]:
        base += ["Thermal wear", "Heavy jacket", "Gloves", "Woollen socks", "Beanie"]
    elif s in ["summer", "warm", "tropical"]:
        base += ["Sunscreen", "Cap", "Sunglasses", "Light cottons", "Water bottle"]
    elif s == "monsoon":
        base += ["Raincoat", "Waterproof shoes", "Quick-dry clothes", "Plastic pouches"]
    if "trek" in a or "adventure" in a or "hike" in a:
        base += ["Trekking shoes", "Backpack", "Torch", "Energy bars"]
    if "beach" in a:
        base += ["Swimwear", "Flip-flops", "Beach towel"]
    return base
