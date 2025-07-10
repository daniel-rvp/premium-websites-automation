RULES_PROMPT = """
Help me write the FAQ’s and Park Regulations page for a campground or RV park called [Campground Name], located in [City, State]. 
Use a clear and helpful tone. No em dashes. Each section should include 6–8 short, guest-friendly rules or policies rewritten from 
provided onboarding info. Organize the content by section as follows:

1. Hero Banner Title
FAQ’S and Park Regulations

2. Section: General Rules
Write 6–8 general policies that apply to all guests. These may include check-in/check-out times, payment, speed limits, conduct, trash 
disposal, etc.

3. Section: RV Site Rules
Write 6–8 rules that apply specifically to guests staying in RV sites. Include details like pet rules, guest limits, noise policies, 
vehicle limits, site cleanliness, etc.

4. Section: Cabin or Lodging Rules (adjust based on property)
Write 6–8 rules that apply specifically to guests staying in cabins or other lodging. Include rules about pets, occupancy limits, 
cleaning, trash, and quiet hours.

5. Section: Cancellation Policy
Write a clear breakdown of the cancellation window and refund policy. Include when partial refunds apply and when cancellations are 
non-refundable.

6. Section: Shared Amenities & Common Areas
Write 6–8 simple rules about the use of pool, laundry, dog park, showers, playground, or shuttle. Include basic etiquette, hours, 
safety notes, or clean-up reminders.

You should deliver a python dictionary, if there are no cabins the value is None, with the requested information like this:
{
    "hero_banner": {
        "title": "Hero banner title",
        "description": "One short, engaging sentence that highlights the uniqueness of the park (location, charm, or design)."
    },
    "general_rules": [
        {
            "rule": "General rule 1",
        },
        {
            "rule": "General rule 2",
        },
        {
            "rule": "General rule 3",
        },
        {
            "rule": "General rule 4",
        },
        {
            "rule": "General rule 5",
        },
        {
            "rule": "General rule 6",
        }
    ],
    "rv_rules": [
        {
            "rule": "RV rule 1",
        },
        {
            "rule": "RV rule 2",
        },
        {
            "rule": "RV rule 3",
        },
        {
            "rule": "RV rule 4",
        },
        {
            "rule": "RV rule 5",
        },
        {
            "rule": "RV rule 6",
        }
    ],
    "cabin_rules": [
        {
            "rule": "Cabin rule 1",
        },
        {
            "rule": "Cabin rule 2",
        },
        {
            "rule": "Cabin rule 3",
        },
        {
            "rule": "Cabin rule 4",
        },
        {
            "rule": "Cabin rule 5",
        },
        {
            "rule": "Cabin rule 6",
        }
    ],
    "cancelation_policy": "Clear breakdown of the cancellation window and refund policy. Include when partial refunds apply and when 
    cancellations are non-refundable",
    "common_areas": [
        {
            "rule": "Common areas rule 1",
        },
        {
            "rule": "Common areas rule 2",
        },
        {
            "rule": "Common areas rule 3",
        },
        {
            "rule": "Common areas rule 4",
        },
        {
            "rule": "Common areas rule 5",
        },
        {
            "rule": "Common areas rule 6",
        }
    ],
}
"""