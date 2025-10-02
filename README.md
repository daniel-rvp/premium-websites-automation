# Premium Websites Automation

## Overview

This Django-based application automates the creation of premium websites for campgrounds and RV parks using AI-generated content. The system collects detailed information through a comprehensive questionnaire and generates complete website content using Google's Gemini AI model.

## Project Purpose

The **Premium Websites Automation** system is designed to help RV parks and campgrounds create professional, SEO-optimized websites automatically. Here's how it works step-by-step:

### 1. User Registration & Questionnaire Setup
- Campground owners register with their basic information (name, phone, address, state)
- Upon registration, the system automatically:
  - Creates a unique subdomain (e.g., `campgroundname.surge.sh`)
  - Generates an authentication token
  - Creates a comprehensive questionnaire with 42 pre-defined questions
  - Stores the client information in both local database and external Supabase database

### 2. Questionnaire Collection
- The system presents 42 detailed questions covering all aspects of the campground:
  - Basic information (location, contact details, seasonality)
  - Property details (size, surroundings, vegetation, wildlife)
  - Accommodations and amenities
  - Activities and attractions
  - Rules and policies
  - Rates and pricing
  - Guest feedback and reviews

### 3. AI-Powered Content Generation
- Once the questionnaire is completed, the system uses Google's Gemini AI to generate content for multiple website pages:
  - **Home Page**: Hero section, amenities overview, activities preview
  - **About Page**: Park history, owner story, accommodations overview
  - **Accommodations Page**: Detailed site descriptions and features
  - **Activities Page**: Local attractions and things to do
  - **Amenities Page**: Comprehensive facility descriptions
  - **Reservations Page**: Pricing and booking information
  - **Contact Page**: Contact information and location details
  - **Rules & FAQ Page**: Park rules and frequently asked questions

### 4. Structured Data Storage
- Generated content is stored in Supabase database with proper relationships
- Content is organized by page type and client
- Data includes categorized amenities, activities, accommodations, and pricing structures

### 5. Website Deployment
- The system automatically creates a React-based website
- Copies template files and customizes them with generated content
- Builds and deploys the website to Surge.sh hosting
- Provides a live, accessible website at the client's subdomain

## Technical Stack

### Backend Framework
- **Django 5.2.3**: Web framework
- **Django REST Framework 3.16.0**: API development
- **SQLite**: Local database for development

### AI & Content Generation
- **Google Gemini AI**: Content generation using structured prompts
- **Custom prompt engineering**: Specialized prompts for each page type
- **JSON-structured responses**: Ensures consistent content formatting

### External Services
- **Supabase**: External database for website content storage
- **Surge.sh**: Website hosting and deployment
- **Token-based authentication**: Secure API access

### Dependencies
```
Django==5.2.3
djangorestframework==3.16.0
django-cors-headers==4.7.0
google-genai==1.20.0
requests==2.32.4
beautifulsoup4==4.13.4
```

## Project Structure

```
premium-websites-automation/
├── premium_websites/          # Django project settings
│   ├── settings.py           # Configuration and installed apps
│   ├── urls.py              # Main URL routing
│   └── wsgi.py              # WSGI application
├── questionnaire/            # Main application logic
│   ├── models.py            # User, questionnaire, and Q&A models
│   ├── views.py             # API endpoints and business logic
│   ├── _questions.py        # 42 predefined questions
│   ├── _prompts_website_generation.py  # AI prompts for each page
│   ├── _util.py             # AI integration utilities
│   └── serializers.py       # API serialization
├── websites_content/         # Website content models
│   └── models.py            # Database models for generated content
├── result/                  # Generated website output directory
├── requirements.txt         # Python dependencies
└── manage.py               # Django management script
```

## Key Features

### 1. Automated Questionnaire System
- 42 comprehensive questions covering all campground aspects
- Progress tracking and validation
- Flexible answer storage system

### 2. AI Content Generation
- **Page-specific prompts**: Each website section has specialized prompts
- **SEO optimization**: Content is generated with search engine optimization in mind
- **Structured output**: AI responses follow strict JSON schemas
- **Content categorization**: Amenities, activities, and features are properly categorized

### 3. Multi-page Website Creation
The system generates content for 7 main pages:
- **Home**: Hero section, amenities overview, nearby attractions
- **About**: Park story, accommodations preview, owner background
- **Accommodations**: Detailed site types and features
- **Activities**: Local attractions and recreational opportunities
- **Amenities**: Comprehensive facility descriptions
- **Reservations**: Pricing structure and booking information
- **Rules & FAQ**: Park policies and common questions

### 4. Automated Deployment
- React application generation
- Automated build process
- Surge.sh deployment
- Live website at custom subdomain

### 5. Data Management
- **Local SQLite**: Development and questionnaire storage
- **Supabase integration**: Production content storage
- **API endpoints**: RESTful API for frontend integration
- **Authentication**: Token-based security

## API Endpoints

### Questionnaire Management
- `GET /questionnaire/premium-website/` - Retrieve questionnaire
- `GET /questionnaire/qanda/` - Get specific question/answer
- `POST /questionnaire/qanda/` - Submit answer to question

### Content Generation
- `GET /questionnaire/website-content-generator/` - Trigger AI content generation and website deployment

### Authentication
- `POST /authentication/` - Obtain API token

## Setup and Installation

### Prerequisites
- Python 3.11+
- Node.js and npm
- Google AI API key
- Supabase account and API keys

### Installation Steps

1. **Clone the repository**
```bash
git clone [repository-url]
cd premium-websites-automation
```

2. **Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
source venv/bin/activate  # On Linux/Mac
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**
- Set up Google AI API key in `questionnaire/_util.py`
- Configure Supabase credentials in `questionnaire/views.py`

5. **Run migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Run development server**
```bash
python manage.py runserver
```

## Usage Workflow

### For Developers
1. Start the Django development server
2. Use the admin interface to manage users and questionnaires
3. Test API endpoints using the browsable API
4. Monitor content generation and deployment process

### For End Users (Campground Owners)
1. Register through the frontend application
2. Complete the 42-question questionnaire
3. Review and submit answers
4. Trigger website generation
5. Receive live website at custom subdomain

## AI Content Generation Process

### 1. Data Collection
- Extract all answered questions from questionnaire
- Format into structured prompt context
- Include campground-specific details (name, location, contact)

### 2. Page-Specific Generation
For each website page:
- Use specialized prompts with specific content requirements
- Request structured JSON responses
- Validate and parse AI-generated content
- Store in appropriate database tables

### 3. Content Organization
- **Categorized amenities**: Essential, activities, special features
- **Structured accommodations**: Site types, features, pricing
- **Organized activities**: Outdoor, family, cultural, staff recommendations
- **Detailed rules**: General, pet policies, facility usage

### 4. Quality Assurance
- JSON validation for all AI responses
- Retry mechanism for failed generations
- Content length and format validation
- SEO optimization checks

## Database Schema

### User Management
- **User**: Extended Django user with campground-specific fields
- **PremiumWebsiteForm**: Links users to their questionnaires
- **QandA**: Stores question-answer pairs with validation status

### Website Content (Supabase)
- **Home, About, Accommodations, Activities, Amenities**: Page-specific content
- **Rules, FAQ**: Policy and help content
- **Contact, Reservations**: Business information and pricing

## Security Features

- **Token-based authentication**: Secure API access
- **CORS configuration**: Controlled cross-origin requests
- **Input validation**: Questionnaire answer validation
- **Environment separation**: Development and production configurations

## Deployment Considerations

### Development
- SQLite database
- Local file storage
- Debug mode enabled
- Local AI model testing

### Production
- PostgreSQL database recommended
- Supabase integration required
- Static file serving configuration
- Production-grade web server (Gunicorn, uWSGI)
- Reverse proxy setup (Nginx)

## Monitoring and Maintenance

### Content Generation Monitoring
- Track AI response success rates
- Monitor website deployment status
- Log failed generations for debugging
- Performance metrics for content creation time

### Database Maintenance
- Regular backup of questionnaire data
- Supabase data synchronization
- User management and cleanup
- Content versioning considerations

## Future Enhancements

### Planned Features
- Multiple template themes
- Custom branding options
- Advanced SEO features
- Analytics integration
- Mobile app support
- Multi-language support

### Technical Improvements
- Caching for improved performance
- Queue system for content generation
- WebSocket for real-time updates
- Enhanced error handling
- Automated testing suite

## Support and Maintenance

### Common Issues
- **AI generation failures**: Check API keys and retry mechanisms
- **Deployment errors**: Verify Surge.sh configuration and file permissions
- **Database connectivity**: Confirm Supabase credentials and network access
- **Questionnaire validation**: Review answer format requirements

### Debugging
- Enable Django debug mode for development
- Check logs for AI generation errors
- Monitor Supabase dashboard for data storage issues
- Verify website deployment through Surge.sh dashboard

---

This premium website automation system streamlines the creation of professional campground websites by combining comprehensive data collection, AI-powered content generation, and automated deployment processes.