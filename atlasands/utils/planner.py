# utils/planner.py
def quick_itinerary(city: str, days: int, interests: str) -> list:
    """A fallback rule-based itinerary used when AI is unavailable."""
    days = max(1, int(days))
    plan = []
    for d in range(1, days + 1):
        plan.append({
            "day": d,
            "morning": f"Explore top {interests or 'sightseeing'} spot #{d} in {city}",
            "afternoon": f"Local cuisine + cultural walk in {city}",
            "evening": f"Sunset point / leisure / shopping in {city}",
        })
    return plan
