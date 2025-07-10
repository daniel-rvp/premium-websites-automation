PROMPT = """
I am currently writing content for a website. I have some questions and answers that the client who I am building the content for 
submitted. I will provide you this answers and questions, the instructions as a prompt, and a python readable dictionary with the content 
variable as the key, and the instructions as the value. Your task is to return the same python readable dictionary, changing the 
instructions by this optimized SEO content, where there are list put as many items as you gathered unless the prompt says otherwise.

The clients is {client} located in {address}, {state}.

Questions:
{relevant_info}

{page_specific}
"""

SYSTEM_PROMPT = """
I am currently writing content for a website. I have some questions and answers that the client who I am building the content 
for submitted. I will provide you this answers and questions, the instructions as a prompt, and a python readable dictionary with the 
content variable as the key, and the instructions as the value. Your task is to return the same python readable dictionary, changing the 
instructions by this optimized SEO content. 
Rememeber to return only a python readable dictionary.
"""

ABOUT = """
Prompt:
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
Write a second paragraph focusing on the park’s background and vision. Mention the owners (if known), the motivation behind building the park, and any unique touches (like restored buildings, Texas hospitality, or RV travel experience). Keep it natural and human but no longer than 5–6 lines.

5. "Discover Our Accommodations" Section
Write 4 accommodation boxes, each with:
Title: Name of the accommodation (e.g., RV Sites, Lodges, Tent Sites)
1-line description (max 110 characters) that highlights what guests can expect.
Examples: RV Sites – Spacious pull-through sites with hookups and room to unwind


Python dict:
{
    "hero_title": "Title encouraging to go to the camp, mention the name.",
    "hero_subtitle": "One clear, benefit-driven phrase that introduces the page and encourages guests to explore the accommodation options.",
    "intro_title": "One short sentence that gathers all the amenities and vibe.",
    "intro_subtitle": "short 3-line paragraph introducing the park’s accommodations. Mention variety (cabins, RV sites, tent sites, etc.), comfort, and access to amenities. Keep it general and location-relevant.",
    "amenities": [
        {
            "title": "Amenity short mention",
            "icon": "lucide-react related icon"
        },
        {
            "title": "Amenity short mention",
            "icon": "lucide-react related icon"
        },
        {
            "title": "Amenity short mention",
            "icon": "lucide-react related icon"
        },
        {
            "title": "Amenity short mention",
            "icon": "lucide-react related icon"
        },
        {
            "title": "Amenity short mention",
            "icon": "lucide-react related icon"
        },
        {
            "title": "Amenity short mention",
            "icon": "lucide-react related icon"
        },
        {
            "title": "Amenity short mention",
            "icon": "lucide-react related icon"
        }
    ],
    "accomodations": [
        {
            "title": "Acocommodation type short title.",
            "subtitle": "One sentence describing the accomodation in a inspiring way."
        },
        {
            "title": "Acocommodation type short title.",
            "subtitle": "One sentence describing the accomodation in a inspiring way."
        },
        {
            "title": "Acocommodation type short title.",
            "subtitle": "One sentence describing the accomodation in a inspiring way."
        },
        {
            "title": "Acocommodation type short title.",
            "subtitle": "One sentence describing the accomodation in a inspiring way."
        }
    ],
    "cta_title" : "Title to create interest in the park",
    "cta_subtitle" : "One-line call to action encouraging bookings or relaxing at the park"
}
"""

ACCOMMODATIONS = """
Prompt:
The tone should be clear, welcoming, and SEO-optimized. No em dashes. Content should be scannable and guest-focused. Please follow the 
structure below:

1. Hero Banner Phrase
Write one clear, benefit-driven phrase that introduces the page and encourages guests to explore the accommodation options.

2. Intro Paragraph
Write a short 3-line paragraph introducing the park’s accommodations.
Mention variety (cabins, RV sites, tent sites, etc.), comfort, and access to amenities. Keep it general and location-relevant.
Amenities List: 6–7 short bullet points of features for that accommodation (written like the example: “Full hookups (up to 50 amp)”)

3. Individual Accommodation Sections
For each accommodation type, include:
Title: (e.g., RV Sites, Cabins, Lodges, Tent Sites, Horse Hotel)
Short Description (2 lines max): Highlight the experience or setting.

Example Format:
RV Sites
Spacious pull-through and back-in sites with full hookups and fire pits, perfect for a relaxed and scenic stay.
Full hookups (up to 50 amp)
Pull-through and back-in options
Picnic table at every site
Free high-speed Wi-Fi
Access to pool, laundry, and restrooms
Pet-friendly with nearby dog park
Walking distance to park amenities


Python dict:
{
    "hero_title": "Inspiration encouraging title.",
    "hero_subtitle": "One clear, benefit-driven phrase that introduces the page and encourages guests to explore the accommodation options.",
    "cta_title" : "Title to create interest in the park",
    "cta_subtitle" : "One-line call to action encouraging bookings or relaxing at the park",
    "accommodations_list": [
        {
            "title": "Name of the accommodation",
            "description": "Short Description (2 lines max): Highlight the experience or setting.",
            "features":[
                {
                    "title":"Feature in 3-5 words",
                    "icon":"lucide-react related icon"
                },
                {
                    "title":"Feature in 3-5 words",
                    "icon":"lucide-react related icon"
                },
                {
                    "title":"Feature in 3-5 words",
                    "icon":"lucide-react related icon"
                },
                {
                    "title":"Feature in 3-5 words",
                    "icon":"lucide-react related icon"
                },
                {
                    "title":"Feature in 3-5 words",
                    "icon":"lucide-react related icon"
                },
                {
                    "title":"Feature in 3-5 words",
                    "icon":"lucide-react related icon"
                }
            ]
        }
    ]

}
"""

ACTIVITIES = """
Prompt:
The tone should be inviting, simple, and SEO-optimized. Avoid em dashes. This page helps guests explore top local attractions during
their stay. Follow this structure:

1. Hero Banner Phrase (Heading Style)
Write a bold, friendly phrase that introduces the page’s purpose.
Example:  Adventure, History, and Small-Town Fun

2. Intro Paragraph (3 Lines Max)
Write a short paragraph (around 300 characters) introducing the types of nearby attractions. Mention local nature, family-friendly 
spots, and cultural highlights.
Example: Explore local outdoor adventures, small-town charm, and cultural highlights—all just a short drive from the campground. 
From river trips to museums and local restaurants, there’s something for every kind of traveler.

3. Attractions List (Bulleted or Section Style)
Include 10 attractions in total. For each, write:
Attraction Name
1–2 sentence description (around 200 characters) that makes it sound appealing and useful to travelers.
Category: Number from 0 to 3, if outdoors 0, if family 1, if cultural 2, if recommended by staff 3.
Example: Current River – Float, swim, or fish along one of Missouri’s most scenic rivers, just minutes from the park.


Python dict:
{
    "hero_description": "One bold, friendly phrase that introduces the page’s purpose",
    "activities" [
        {
            "title": "Activty name",
            "description": "Inspiring one short sentence description",
            "icon": "lucide-react related icon",
            "category": "outdoor = 0 | family = 1 | cultural = 2 | recommendation = 3"
        },
        {
            "title": "Activty name",
            "description": "Inspiring one short sentence description",
            "icon": "lucide-react related icon",
            "category": "outdoor = 0 | family = 1 | cultural = 2 | recommendation = 3"
        },
        {
            "title": "Activty name",
            "description": "Inspiring one short sentence description",
            "icon": "lucide-react related icon",
            "category": "outdoor = 0 | family = 1 | cultural = 2 | recommendation = 3"
        },
        {
            "title": "Activty name",
            "description": "Inspiring one short sentence description",
            "icon": "lucide-react related icon",
            "category": "outdoor = 0 | family = 1 | cultural = 2 | recommendation = 3"
        },
        {
            "title": "Activty name",
            "description": "Inspiring one short sentence description",
            "icon": "lucide-react related icon",
            "category": "outdoor = 0 | family = 1 | cultural = 2 | recommendation = 3"
        },
        {
            "title": "Activty name",
            "description": "Inspiring one short sentence description",
            "icon": "lucide-react related icon",
            "category": "outdoor = 0 | family = 1 | cultural = 2 | recommendation = 3"
        }
    ]
}
"""

AMENITIES = """
Prompt:
The tone should be friendly, helpful, and SEO-optimized. Do not use em dashes. Please follow this structure:

1. Page Title (Hero Heading)
Write a short, benefit-driven title that summarizes what guests can expect from the park’s amenities. 
Examples: Everything You Need, Right on Site

2. List of Amenities
Provide a list of at least 8 amenities, each with:
Amenity Name (Title style)
2-line Description (max 180 characters)
Category: Each amenity should have on category: essential, activity, special:
    Essenntial, when is about basic features for stay.
    Activitities, when it involves recreation or leisure.
    Special. when it describes the unique experience of the camp.
Keep each one consistent in style and focused on real guest benefits. 
Example:
Pickleball Court: Challenge your friends to a game of pickleball on our full-size court, located near the pool and playground.


Python dict:
{
    "amenities_description": "One short, benefit-driven title that summarizes what guests can expect from the park’s amenities",
    "cta_title" : "Title to create interest in the park",
    "cta_subtitle" : "One-line call to action encouraging bookings or relaxing at the park",
    "amenities": [
        {
            "title": "Amenity Name (Title style)",
            "description": "2-line Description (max 180 characters)",
            "category": "if essential 0 | if activity 1 | if special 2"
        },
        {
            "title": "Amenity Name (Title style)",
            "description": "2-line Description (max 180 characters)",
            "category": "if essential 0 | if activity 1 | if special 2"
        },
        {
            "title": "Amenity Name (Title style)",
            "description": "2-line Description (max 180 characters)",
            "category": "if essential 0 | if activity 1 | if special 2"
        },
        {
            "title": "Amenity Name (Title style)",
            "description": "2-line Description (max 180 characters)",
            "category": "if essential 0 | if activity 1 | if special 2"
        },
        {
            "title": "Amenity Name (Title style)",
            "description": "2-line Description (max 180 characters)",
            "category": "if essential 0 | if activity 1 | if special 2"
        },
        {
            "title": "Amenity Name (Title style)",
            "description": "2-line Description (max 180 characters)",
            "category": "if essential 0 | if activity 1 | if special 2"
        },
        {
            "title": "Amenity Name (Title style)",
            "description": "2-line Description (max 180 characters)",
            "category": "if essential 0 | if activity 1 | if special 2"
        }
    ]
}
"""

CONTACT_US = """
Prompt:
This page should include a friendly heading and the contact information clearly listed. No em dashes. Follow this structure:

1. Heading (Not a full hero banner)
Contact Us. Let's Chat.

2. Contact Form Block (to be visually designed)
Add a form with fields for:
Name
Phone
Email
Message
Below the message box, include a friendly sentence like:
For questions about our rates or availability, we’d love to chat!

3. Contact Information Block
List the following with proper formatting:
Business Name
Full address
Phone number
Email address



Python dict:
{
    "address": "Park address",
    "phone": "Park phone",
    "mail": "Park mail",
    "hours": "Park attention hours for contact",
    "find_us": "Brief 1-2 sentence description on how to get there"
}
"""

HOME = """
Prompt:
The tone should be clear, guest-friendly, and SEO-optimized. Focus on increasing bookings by highlighting the park’s amenities, experience, and location. Do not use em dashes. Keep all paragraphs under 400 characters. This Home Page includes the following sections:

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


Python dict:
{
    "hero_title" : "Title that captures the park’s experience and location.",
    "hero_subtitle" : "One SEO-friendly phrase or headline that captures the park’s experience and location.",
    "hero_amenity_list" : [
        {"title" : "Amenity in 2–3 words inspiring description."},
        {"title" : "Amenity in 2–3 words inspiring description."},
        {"title" : "Amenity in 2–3 words inspiring description."},
        {"title" : "Amenity in 2–3 words inspiring description."},
        {"title" : "Amenity in 2–3 words inspiring description."},
        {"title" : "Amenity in 2–3 words inspiring description."}
    ],
    "intro_title" : "Title  introducing the park's essence.",
    "intro_subtitle" : "A 2–4 line paragraph introducing the park and its benefits (highlight RV sites, cabins, amenities, and location).",
    "amenities_gallery_subtitle" : "One sentence with a brief summary of key amenities and features and inviting to experience it.",
    "activities_subtitle" : "1-3 sentences introducing the park activities.",
    "activities": [
        {
            "title" : "Activity in a sentence that invites to do it.",
            "icon": "lucide-react related ico"
        },
        {
            "title" : "Activity in a sentence that invites to do it.",
            "icon": "lucide-react related ico"
        },
        {
            "title" : "Activity in a sentence that invites to do it.",
            "icon": "lucide-react related ico"
        },
        {
            "title" : "Activity in a sentence that invites to do it.",
            "icon": "lucide-react related ico"
        },
        {
            "title" : "Activity in a sentence that invites to do it.",
            "icon": "lucide-react related ico"
        },
        {"title" : "Activity in a sentence that invites to do it."}
    ],
    "amenities_subtitle" : "One sentence introducing the amenities.",
    "amenities": [
        {
            "title" : "Amenity name.",
            "description" : "One sentence describing the amenity"
        },
        {
            "title" : "Amenity name.",
            "description" : "One sentence describing the amenity"
        },
        {
            "title" : "Amenity name.",
            "description" : "One sentence describing the amenity"
        },
        {
            "title" : "Amenity name.",
            "description" : "One sentence describing the amenity"
        },
        {
            "title" : "Amenity name.",
            "description" : "One sentence describing the amenity"
        },
        {
            "title" : "Amenity name.",
            "description" : "One sentence describing the amenity"
        }
    ],
    "rule_check_in_out_time" : "Check in and check out time",
    "rule_quiet_time" : "Quiet time range",
    "rule_campfire" : "Camp fire regulation",
    "rule_pets" : "Pets policy",
    "rule_wifi" : "Wi-fi policy",
    "cta_title" : "Title to create interest in the park",
    "cta_subtitle" : "One-line call to action encouraging bookings or relaxing at the park",
    "attractions_subtitle": "One brief sentence describing nearby activites and park location",
    "attractions": [
        {
            "title" : "Attraction name.",
            "distance": "Distance in minutes from park",
            "description" : "One sentence describing the amenity"
        },
        {
            "title" : "Attraction name.",
            "distance": "Distance in minutes from park",
            "description" : "One sentence describing the amenity"
        },
        {
            "title" : "Attraction name.",
            "distance": "Distance in minutes from park",
            "description" : "One sentence describing the amenity"
        },
        {
            "title" : "Attraction name.",
            "distance": "Distance in minutes from park",
            "description" : "One sentence describing the amenity"
        },
        {
            "title" : "Attraction name.",
            "distance": "Distance in minutes from park",
            "description" : "One sentence describing the amenity"
        },
        {
            "title" : "Attraction name.",
            "distance": "Distance in minutes from park",
            "description" : "One sentence describing the amenity"
        },
        {
            "title" : "Attraction name.",
            "distance": "Distance in minutes from park",
            "description" : "One sentence describing the amenity"
        },
        {
            "title" : "Attraction name.",
            "distance": "Distance in minutes from park",
            "description" : "One sentence describing the amenity"
        },
        {
            "title" : "Attraction name.",
            "distance": "Distance in minutes from park",
            "description" : "One sentence describing the amenity"
        },
        {
            "title" : "Attraction name.",
            "distance": "Distance in minutes from park",
            "description" : "One sentence describing the amenity"
        }
    ]
}
"""

RESERVATIONS = """
Prompt:
Use the rate values provided in the questions section. The tone should be clear and informative. No em dashes. Follow this structure:

1. Intro Paragraph (2 sentences max)
Write a short intro that sets guest expectations. Mention that multiple stay lengths are available and clarify what's included (Wi-Fi, utilities, etc.). Example: We offer nightly, weekly, and monthly RV rates to fit every type of traveler. Utilities are included in most short-term stays, and long-term guests enjoy free Wi-Fi with utilities billed separately.

2. Rate Details Section (Dynamic Content from Form)
Create a visual-friendly breakdown of rates based on the form input. Use the correct pricing and structure based on what's provided per site type and length of stay. For each entry, format like this:

[Site or Accommodation Type]
Nightly Rate
Starting at $[price] / night
[What’s included, e.g., Includes utilities and Wi-Fi]

Weekly Rate
Starting at $[price] / week
[What’s included]

Monthly Rate
Starting at $[price] / month
[What’s included or not included]


Example:

RV Sites

Nightly Rate
Starting at $45 / night
Includes utilities and free Wi-Fi

Weekly Rate
Starting at $250 / week
Includes utilities and free Wi-Fi

Monthly Rate
Starting at $600 / month
Includes Wi-Fi; utilities billed separately


Python dict:
{
    "reservations_description": "short intro that sets guest expectations. Mention that multiple stay lengths are available and clarify what's included (Wi-Fi, utilities, etc.).",
    "cta_description": "One-line call to action encouraging bookings or relaxing at the park",
    "accommodations": [
                        {
                            "title": "",
                            "subtitle": "",
                            "fares":[
                                {
                                    "fare": "$X / NIGHT",
                                    "title": "Daily Rate",
                                    "description": "Brief description of what is included"
                                },
                                {
                                    "fare": "$X / WEEK",
                                    "title": "Weekly Rate",
                                    "description": "Brief description of what is included"
                                },
                                {
                                    "fare": "$X / WEEK",
                                    "title": "Weekly Rate",
                                    "description": "Brief description of what is included"
                                }]
                        },
                        {
                            "title": "",
                            "subtitle": "",
                            "fares":[
                                {
                                    "fare": "$X / NIGHT",
                                    "title": "Daily Rate",
                                    "description": "Brief description of what is included"
                                },
                                {
                                    "fare": "$X / WEEK",
                                    "title": "Weekly Rate",
                                    "description": "Brief description of what is included"
                                },
                                {
                                    "fare": "$X / WEEK",
                                    "title": "Weekly Rate",
                                    "description": "Brief description of what is included"
                                }]
                        },
                        {
                            "title": "",
                            "subtitle": "",
                            "fares":[
                                {
                                    "fare": "$X / NIGHT",
                                    "title": "Daily Rate",
                                    "description": "Brief description of what is included"
                                },
                                {
                                    "fare": "$X / WEEK",
                                    "title": "Weekly Rate",
                                    "description": "Brief description of what is included"
                                },
                                {
                                    "fare": "$X / WEEK",
                                    "title": "Weekly Rate",
                                    "description": "Brief description of what is included"
                                }]
                        }
                    ]
}
"""

RULES = """
Prompt:
This page has two sectons:

1. Rules:
List and classify all rules in a short and concise way.
The categories are:
1. Genarl Rules: This includes check out and check in times, campfires, washing car rules, and all behaviors allowed or forbidden.
2. Pet rules: All those related to pets.
3. Facility and amenities rules: Regarding the use of the facilities, like pool times, minors using the facilitites, and so on.

2. FAQ's
You task is to find the answers of the following questions:
What is your cancellation policy?
Do you allow pets?
Do all RV sites have full hookups?
What amenities are included with my stay?
Can I have visitors during my stay?
Is WiFi available?
What is your check-in and check-out time?
Do I need to bring my own linens for cabin stays?
Are campfires allowed?
Is there a camp store on-site?
Do you have laundry facilities?
Are there restaurants nearby?


Python dict:
{   "rules": [
        {
            "title": "Concise sentence wiht the rule",
            "category": "0 if general rule | 1 if pet policy rule | 2 if facilities rule"
        },
        {
            "title": "Concise sentence wiht the rule",
            "category": "0 if general rule | 1 if pet policy rule | 2 if facilities rule"
        },
        {
            "title": "Concise sentence wiht the rule",
            "category": "0 if general rule | 1 if pet policy rule | 2 if facilities rule"
        },
        {
            "title": "Concise sentence wiht the rule",
            "category": "0 if general rule | 1 if pet policy rule | 2 if facilities rule"
        },
        {
            "title": "Concise sentence wiht the rule",
            "category": "0 if general rule | 1 if pet policy rule | 2 if facilities rule"
        },
        {
            "title": "Concise sentence wiht the rule",
            "category": "0 if general rule | 1 if pet policy rule | 2 if facilities rule"
        },
        {
            "title": "Concise sentence wiht the rule",
            "category": "0 if general rule | 1 if pet policy rule | 2 if facilities rule"
        },
        {
            "title": "Concise sentence wiht the rule",
            "category": "0 if general rule | 1 if pet policy rule | 2 if facilities rule"
        }
    ],
    "faqs": [
        {
            "question": "What is your cancellation policy?",
            "answer": "Find the answer in the questions section",
            "type": 0
        },
        {
            "question": "Do you allow pets?",
            "answer": "Find the answer in the questions section",
            "type": 1
        },
        {
            "question": "Do all RV sites have full hookups?",
            "answer": "Find the answer in the questions section",
            "type": 2
        },
        {
            "question": "What amenities are included with my stay?",
            "answer": "Find the answer in the questions section",
            "type": 3
        },
        {
            "question": "Can I have visitors during my stay?",
            "answer": "Find the answer in the questions section",
            "type": 4
        },
        {
            "question": "Is WiFi available?",
            "answer": "Find the answer in the questions section",
            "type": 5
        },
        {
            "question": "What is your check-in and check-out time?",
            "answer": "Find the answer in the questions section",
            "type": 6
        },
        {
            "question": "Do I need to bring my own linens for cabin stays?",
            "answer": "Find the answer in the questions section",
            "type": 7
        },
        {
            "question": "Are campfires allowed?",
            "answer": "Find the answer in the questions section",
            "type": 8
        },
        {
            "question": "Is there a camp store on-site?",
            "answer": "Find the answer in the questions section",
            "type": 9
        },
        {
            "question": "Do you have laundry facilities?",
            "answer": "Do you have laundry facilities ?",
            "type": 10
        },
        {
            "question": "Are there restaurants nearby",
            "answer": "Find the answer in the questions section",
            "type": 11
        }
    ]
}
"""

PROMPT_PAGES = {
    "amenities": AMENITIES,
    "about": ABOUT,
    "accommodations": ACCOMMODATIONS,
    "activities": ACTIVITIES,
    "amenities": AMENITIES,
    "contact_us": CONTACT_US,
    "home": HOME,
    "reservations": RESERVATIONS,
    "rules": RULES
}
