# utils/budget.py
def estimate_budget(days: int, style: str, level: str) -> int:
    """Rough per-trip budget in INR based on style + adventure level."""
    base = {"Solo": 1500, "Couple": 2800, "Family": 4500,
            "Group": 3500, "Backpacker": 900}
    mult = {"Relaxed": 1.0, "Moderate": 1.3, "Adventurous": 1.6, "Extreme": 2.0}
    return int(base.get(style, 1500) * mult.get(level, 1.0) * max(1, int(days)))
