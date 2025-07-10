ACCOMODATIONS_PROMT = """
Help me write the Accommodations page for a campground or RV park called [Campground Name], located in [City, State]. The tone should be 
clear, welcoming, and SEO-optimized. No em dashes. Content should be scannable and guest-focused. Please follow the structure below:

1. Hero Banner Phrase
Write one clear, benefit-driven phrase that introduces the page and encourages guests to explore the accommodation options.

2. Intro Paragraph
Write a short 3-line paragraph introducing the park’s accommodations.
Mention variety (cabins, RV sites, tent sites, etc.), comfort, and access to amenities. Keep it general and location-relevant.

3. Individual Accommodation Sections
For each accommodation type, include:
Title: (e.g., RV Sites, Cabins, Lodges, Tent Sites, Horse Hotel)

Short Description (2 lines max): Highlight the experience or setting.

Amenities List: 6–7 short bullet points of features for that accommodation (written like the example: “Full hookups (up to 50 amp)”)

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
    "acommodations": [
        {
            "title": "Accomodation 1",
            "description": "Description accomodation 1",
            "features": [
                {
                    "feature": "Feature 1",
                    "icon": "lucide-react related icon"
                },
                {
                    "feature": "Feature 2",
                    "icon": "lucide-react related icon"
                },
                {
                    "feature": "Feature 3",
                    "icon": "lucide-react related icon"
                },
                {
                    "feature": "Feature 4",
                    "icon": "lucide-react related icon"
                },
                {
                    "feature": "Feature 5",
                    "icon": "lucide-react related icon"
                },
                {
                    "feature": "Feature 6",
                    "icon": "lucide-react related icon"
                }
            ]
        },
        {
            "title": "Accomodation 2",
            "description": "Description accomodation 2",
            "features": [
                {
                    "feature": "Feature 1",
                    "icon": "lucide-react related icon"
                },
                {
                    "feature": "Feature 2",
                    "icon": "lucide-react related icon"
                },
                {
                    "feature": "Feature 3",
                    "icon": "lucide-react related icon"
                },
                {
                    "feature": "Feature 4",
                    "icon": "lucide-react related icon"
                },
                {
                    "feature": "Feature 5",
                    "icon": "lucide-react related icon"
                },
                {
                    "feature": "Feature 6",
                    "icon": "lucide-react related icon"
                }
            ]
        }
    ],
    "cta": {
        "title": "CTA title",
        "description": "CTA description"
    }
}
"""