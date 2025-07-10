ABOUT_US_PROMPT = """
Help me write the About Us page for a campground or RV park called {name}, located in {location}. 
The tone should be warm, welcoming, and SEO-optimized. No em dashes. Please follow this structure:

1. Hero Banner Phrase (Headline Style)
Write one short, engaging sentence that highlights the uniqueness of the park (location, charm, or design).

2. Intro Paragraph
Write a 3–4 line paragraph introducing the property. Focus on what guests can expect: amenities, size, layout, scenery, and guest 
experience. Mention features like RV sites, cabins, open space, or proximity to nature or nearby towns.

3. Amenities List (Icon Section)
Create a list of 10–12 key amenities. Each item should be 2–4 words max.
Keep it uniform for visual consistency, like:
Full hookups
Swimming pool
Pickleball court
Dog park
Camp store
Free Wi-Fi

4. History & Inspiration Paragraph
Write a second paragraph focusing on the park’s background and vision. Mention the owners (if known), the motivation behind 
building the park, and any unique touches (like restored buildings, Texas hospitality, or RV travel experience). Keep it natural 
and human but no longer than 5–6 lines.

5. "Discover Our Accommodations" Section
Write 4 accommodation boxes, each with:
Title: Name of the accommodation (e.g., RV Sites, Lodges, Tent Sites)
1-line description (max 110 characters) that highlights what guests can expect.
Examples: RV Sites – Spacious pull-through sites with hookups and room to unwind

You should deliver a python dictionary with the requested information like this:
{
    "hero_banner": {
        "title": "Hero banner title",
        "description": "One short, engaging sentence that highlights the uniqueness of the park (location, charm, or design)."
    },
    "intro_paragraph": {
        "title": "Property introduction title",
        "description": "A 3–4 line paragraph introducing the property. Focus on what guests can expect: amenities, size, layout, 
        scenery, and guest experience. Mention features like RV sites, cabins, open space, or proximity to nature or nearby towns."
    },
    "amenities_list": [
        {
            "title": "Ammenity 1",
            "icon": "lucide-react related icon"
        },
        {
            "title": "Ammenity 2",
            "icon": "lucide-react related icon"
        },
        {
            "title": "Ammenity 3",
            "icon": "lucide-react related icon"
        },
        {
            "title": "Ammenity 4",
            "icon": "lucide-react related icon"
        },
        {
            "title": "Ammenity 5",
            "icon": "lucide-react related icon"
        },
        {
            "title": "Ammenity 6",
            "icon": "lucide-react related icon"
        },
        {
            "title": "Ammenity 7",
            "icon": "lucide-react related icon"
        },
        {
            "title": "Ammenity 8",
            "icon": "lucide-react related icon"
        }
        ,
        {
            "title": "Ammenity 9",
            "icon": "lucide-react related icon"
        },
        {
            "title": "Ammenity 10",
            "icon": "lucide-react related icon"
        }
    ],
    "history_and_inspiration": "",
    "accomodations": [
        {
            "accomodations": "Accomodation 1 title",
            "description": "Accomodation 1 description"
        },
        {
            "accomodations": "Accomodation 2 title",
            "description": "Accomodation 2 description"
        },
        {
            "accomodations": "Accomodation 3 title",
            "description": "Accomodation 3 description"
        },
        {
            "accomodations": "Accomodation 4 title",
            "description": "Accomodation 4 description"
        }
    ],
    "cta": {
        "title": "CTA title",
        "description": "CTA description"
    }
}
"""