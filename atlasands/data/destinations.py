# data/destinations.py
# Master list of featured destinations. Each item is a Python dict.
# Images are high-quality Unsplash URLs (no API key needed, never blurry).

DESTINATIONS = [
    {
        "name": "Goa", "state": "Goa", "budget": 18000, "season": "Nov - Feb",
        "category": "Beach",
        "image": "https://images.unsplash.com/photo-1512343879784-a960bf40e7f2?w=1600&q=90",
        "desc": "Sun-kissed beaches, Portuguese heritage and vibrant nightlife.",
        "attractions": ["Baga Beach", "Fort Aguada", "Dudhsagar Falls"],
    },
    {
        "name": "Manali", "state": "Himachal Pradesh", "budget": 15000, "season": "Mar - Jun, Dec - Feb",
        "category": "Hill Station",
        "image": "https://images.unsplash.com/photo-1626621341517-bbf3d9990a23?w=1600&q=90",
        "desc": "Snow-capped peaks, apple orchards and an adventure paradise.",
        "attractions": ["Solang Valley", "Rohtang Pass", "Hadimba Temple"],
    },
    {
        "name": "Jaipur", "state": "Rajasthan", "budget": 12000, "season": "Oct - Mar",
        "category": "Heritage",
        "image": "https://images.unsplash.com/photo-1599661046289-e31897846e41?w=1600&q=90",
        "desc": "The Pink City — palaces, forts and royal Rajputana culture.",
        "attractions": ["Hawa Mahal", "Amer Fort", "City Palace"],
    },
    {
        "name": "Kerala", "state": "Kerala", "budget": 22000, "season": "Sep - Mar",
        "category": "Nature",
        "image": "https://images.unsplash.com/photo-1602216056096-3b40cc0c9944?w=1600&q=90",
        "desc": "Backwaters, houseboats, spice gardens and timeless Ayurveda.",
        "attractions": ["Alleppey Backwaters", "Munnar Tea Estates", "Fort Kochi"],
    },
    {
        "name": "Ladakh", "state": "Ladakh", "budget": 30000, "season": "May - Sep",
        "category": "Adventure",
        "image": "https://images.unsplash.com/photo-1589793907316-f94025b46850?w=1600&q=90",
        "desc": "Surreal high-altitude desert with monasteries and turquoise lakes.",
        "attractions": ["Pangong Lake", "Nubra Valley", "Magnetic Hill"],
    },
    {
        "name": "Varanasi", "state": "Uttar Pradesh", "budget": 10000, "season": "Oct - Mar",
        "category": "Spiritual",
        "image": "https://images.unsplash.com/photo-1561361513-2d000a50f0dc?w=1600&q=90",
        "desc": "The oldest living city — ghats, aartis and timeless spirituality.",
        "attractions": ["Dashashwamedh Ghat", "Kashi Vishwanath", "Sarnath"],
    },
    {
        "name": "Andaman", "state": "Andaman & Nicobar", "budget": 35000, "season": "Oct - May",
        "category": "Beach",
        "image": "https://images.unsplash.com/photo-1583212292454-1fe6229603b7?w=1600&q=90",
        "desc": "Crystal waters, coral reefs and pristine white sandy shores.",
        "attractions": ["Radhanagar Beach", "Cellular Jail", "Havelock Island"],
    },
    {
        "name": "Jim Corbett", "state": "Uttarakhand", "budget": 14000, "season": "Nov - Jun",
        "category": "Wildlife",
        "image": "https://images.unsplash.com/photo-1549366021-9f761d450615?w=1600&q=90",
        "desc": "India's oldest national park — home to the Royal Bengal Tiger.",
        "attractions": ["Tiger Safari", "Dhikala Zone", "Corbett Falls"],
    },
    {
        "name": "Udaipur", "state": "Rajasthan", "budget": 16000, "season": "Sep - Mar",
        "category": "Heritage",
        "image": "https://images.unsplash.com/photo-1568526381923-caf3fd520382?w=1600&q=90",
        "desc": "City of Lakes — romantic palaces seemingly floating on water.",
        "attractions": ["Lake Pichola", "City Palace", "Jag Mandir"],
    },
    {
        "name": "Kashmir", "state": "Jammu & Kashmir", "budget": 25000, "season": "Apr - Oct",
        "category": "Hill Station",
        "image": "https://images.unsplash.com/photo-1593181629936-11c609b8db9b?w=1600&q=90",
        "desc": "Paradise on Earth — Dal Lake, gardens and snowy mountains.",
        "attractions": ["Dal Lake", "Gulmarg", "Pahalgam"],
    },
    {
        "name": "Coorg", "state": "Karnataka", "budget": 13000, "season": "Oct - Mar",
        "category": "Hill Station",
        "image": "https://images.unsplash.com/photo-1580674684081-7617fbf3d745?w=1600&q=90",
        "desc": "Scotland of India — coffee plantations and misty rolling hills.",
        "attractions": ["Abbey Falls", "Raja's Seat", "Dubare Elephant Camp"],
    },
    {
        "name": "Rishikesh", "state": "Uttarakhand", "budget": 11000, "season": "Sep - Apr",
        "category": "Adventure",
        "image": "https://images.unsplash.com/photo-1591018533402-1ec99d40c2e2?w=1600&q=90",
        "desc": "Yoga capital of the world with river rafting and Himalayan vibes.",
        "attractions": ["Laxman Jhula", "Triveni Ghat", "Neelkanth Temple"],
    },
]

CATEGORIES = ["All", "Beach", "Hill Station", "Heritage", "Wildlife",
              "Adventure", "Spiritual", "Nature"]

HERO_IMAGES = [
    "https://images.unsplash.com/photo-1524492412937-b28074a5d7da?w=2000&q=95",
    "https://images.unsplash.com/photo-1587474260584-136574528ed5?w=2000&q=95",
    "https://images.unsplash.com/photo-1477587458883-47145ed94245?w=2000&q=95",
]
