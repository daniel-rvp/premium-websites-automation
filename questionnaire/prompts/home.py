HOME_PROMPT = """
Help me write the Home Page content for a Premium Website for {name} located in {location}. The tone should be clear, guest-friendly, 
and SEO-optimized. Focus on increasing bookings by highlighting the park’s amenities, experience, and location. Do not use em dashes. 
Keep all paragraphs under 400 characters. This Home Page includes the following sections:

1. Hero Banner
One SEO-friendly phrase or headline that captures the park’s experience and location
A short list of 6 key amenities, written in 2–3 words each (e.g., “Outdoor pool,” “Full hookups”)


2. Intro Paragraph
A 2–4 line paragraph introducing the park and its benefits (highlight RV sites, cabins, amenities, and location)

3. Amenities Section with Icons
Title for the section
Subtitle (1 sentence)
List of 8–10 amenities with 2–3 word descriptions for use with icons (e.g., “Pickleball court,” “Fishing pond”)

4. What to Do at the Park (Carousel Section)
Title (fun, clear, short)
Subtitle (1 line)
List of 6 activities with a title and a 1-line description each
(e.g., Title: “Swimming Pool” – “Cool off or relax by the water.”)

5. Park Rules Preview
Provide a short title for the section, then include 5 rules, each in 1 line:
Check-in / check-out times
Pet policy
Quiet hours
Campfires
Wi-Fi access

6. Rest Section with CTA
Title
1-line call to action encouraging bookings or relaxing at the park

7. Nearby Attractions Section
List of at least 10 local spots (can be a mix of outdoor areas, food, museums, etc.)
Each should include name + category (e.g., “Current River – Outdoor Adventure”)
No full sentences, just name + type of attraction


You should deliver a python dictionary with the requested information like this:
{
    "hero_banner": {
        "title": "Hero banner title",
        "subtitle": "Hero banner subtitle",
        "key_ammenities": [
            {
                "title": "Key amenity 1",
                "description": "Description amenity 1",
                "icon": "lucide-react related icon"
            },
            {
                "title": "Key amenity 2",
                "description": "Description amenity 2",
                "icon": "lucide-react related icon"
            },
            {
                "title": "Key amenity 3",
                "description": "Description amenity 3",
                "icon": "lucide-react related icon"
            },
            {
                "title": "Key amenity 4",
                "description": "Description amenity 4",
                "icon": "lucide-react related icon"
            },
            {
                "title": "Key amenity 5",
                "description": "Description amenity 5",
                "icon": "lucide-react related icon"
            },
            {
                "title": "Key amenity 6",
                "description": "Description amenity 6",
                "icon": "lucide-react related icon"
            }
        ]
    },
    "intro_paragraph": {
        "title": "Welcome section title",
        "description": "Welcome section description"
    },
    "ammenities_section": {
        "title": "Amenities section title",
        "subtitle": "One sentence introducing amenities",
        "ammenities_list": [
            {
                "title": "Amenity 1",
                "description": "Description amenity 1",
                "icon": "lucide-react related icon"
            },
            {
                "title": "Amenity 2",
                "description": "Description amenity 2",
                "icon": "lucide-react related icon"
            },
            {
                "title": "Amenity 3",
                "description": "Description amenity 3",
                "icon": "lucide-react related icon"
            },
            {
                "title": "Amenity 4",
                "description": "Description amenity 4",
                "icon": "lucide-react related icon"
            },
            {
                "title": "Amenity 5",
                "description": "Description amenity 5",
                "icon": "lucide-react related icon"
            },
            {
                "title": "Amenity 6",
                "description": "Description amenity 6",
                "icon": "lucide-react related icon"
            },
            {
                "title": "Amenity 7",
                "description": "Description amenity 6",
                "icon": "lucide-react related icon"
            },
            {
                "title": "Amenity 8",
                "description": "Description amenity 6",
                "icon": "lucide-react related icon"
            },
            {
                "title": "Amenity 9",
                "description": "Description amenity 6",
                "icon": "lucide-react related icon"
            }
        ]
    },
    "what_to_do": {
        "title": "Fun, clear, short title",
        "subtitle": "One sentence introducinig all activities",
        "what_to_do_list": [
            {
                "title": "Activity 1",
                "description": "Description Activity 1",
                "icon": "lucide-react related icon"
            },
            {
                "title": "Activity 2",
                "description": "Description Activity 2",
                "icon": "lucide-react related icon"
            },
            {
                "title": "Activity 3",
                "description": "Description Activity 3",
                "icon": "lucide-react related icon"
            },
            {
                "title": "Activity 4",
                "description": "Description Activity 4",
                "icon": "lucide-react related icon"
            },
            {
                "title": "Activity 5",
                "description": "Description Activity 5",
                "icon": "lucide-react related icon"
            },
            {
                "title": "Activity 6",
                "description": "Description Activity 6",
                "icon": "lucide-react related icon"
            },
        ]
    },
    "rules": [
        {
            "check_in_and_out": "Rule about check in and check out time"
        },
        {
            "pets": "Pet policy"
        },
        {
            "quiet_hours": "Time frame for quiter hours"
        },
        {
            "campfires": "Rules about campfires"
        },
        {
            "wifi": "Wi-fi availability"
        }
    ],
    "cta": {
        "title": "CTA Title",
        "description": "CTA description"
    },
    "attractions": [
        {
            "attraction_name": "Attraction name - Activity type (short)",
        },
        {
            "attraction_name": "Attraction name - Activity type (short)",
        },
        {
            "attraction_name": "Attraction name - Activity type (short)",
        },
        {
            "attraction_name": "Attraction name - Activity type (short)",
        },
        {
            "attraction_name": "Attraction name - Activity type (short)",
        },
        {
            "attraction_name": "Attraction name - Activity type (short)",
        },
        {
            "attraction_name": "Attraction name - Activity type (short)",
        },
        {
            "attraction_name": "Attraction name - Activity type (short)",
        },
        {
            "attraction_name": "Attraction name - Activity type (short)",
        },
        {
            "attraction_name": "Attraction name - Activity type (short)",
        }
    ]
}
"""