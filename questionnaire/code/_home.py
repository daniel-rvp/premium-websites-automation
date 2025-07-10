HOME = """
import React from 'react';
import {{ Link }} from "react-router-dom";
import Layout from "@/components/Layout";
import SectionDivider from "@/components/SectionDivider";
import {{ Button }} from "@/components/ui/button";
import {{ Card, CardContent }} from "@/components/ui/card";
import {{ Waves, House, Activity, Power, Building, Home as HomeIcon, Utensils, MapPin, Calendar, Trees, Car, Wifi, Music, IceCream }} from "lucide-react";
import {{ Carousel, CarouselContent, CarouselItem, CarouselNext, CarouselPrevious }} from "@/components/ui/carousel";
import {{ HoverCard, HoverCardContent, HoverCardTrigger }} from "@/components/ui/hover-card";
import {{ useIsMobile }} from "@/hooks/use-mobile";
import {{ useContent }} from "@/hooks/use-content";

const Home = () => {{
  const isMobile = useIsMobile();

  // Original data to use as fallback
  const originalGalleryImages = [{{
    src: "{path1_original_gallery}",
    alt: "pic-1"
  }}, {{
    src: "{path2_original_gallery}",
    alt: "pic-2"
  }}, {{
    src: "{path3_original_gallery}",
    alt: "pic-3"
  }}, {{
    src: "{path4_original_gallery}",
    alt: "pic-4"
  }}, {{
    src: "{path5_original_gallery}",
    alt: "pic-5"
  }}, {{
    src: "{path6_original_gallery}",
    alt: "pic-6"
  }}];

  const originalFeaturedAmenities = [{{
    title: "<amenity-1-title/>",
    description: "<amenity-1-description/>",
    image: "{path_ammenity_1}",
    icon: <Waves size={{{{24}}}} />
  }}, {{
    title: "<amenity-2-title/>",
    description: "<amenity-2-description/>",
    image: "{path_ammenity_2}",
    icon: <Power size={{{{24}}}} />
  }}, {{
    title: "<amenity-3-title/>",
    description: "<amenity-3-description/>",
    image: "{path_ammenity_3}",
    icon: <Building size={{{{24}}}} />
  }}, {{
    title: "<amenity-4-title/>",
    description: "<amenity-4-description/>",
    image: "{path_ammenity_4}",
    icon: <House size={{{{24}}}} />
  }}, {{
    title: "<amenity-5-title/>",
    description: "<amenity-5-description/>",
    image: "{path_ammenity_5}",
    icon: <Utensils size={{{{24}}}} />
  }}, {{
    title: "<amenity-6-title/>",
    description: "<amenity-6-description/>",
    image: "{path_ammenity_6}",
    icon: <HomeIcon size={{{{24}}}} />
  }}];

  const originalThingsToDo = [{{
    activity: "<thing-to-do-1-title/>",
    icon: <Waves size={{{{24}}}} className="text-rvblue" />
  }}, {{
    activity: "<thing-to-do-2-title/>",
    icon: <Activity size={{{{24}}}} className="text-rvblue" />
  }}, {{
    activity: "<thing-to-do-3-title/>",
    icon: <House size={{{{24}}}} className="text-rvblue" />
  }}, {{
    activity: "<thing-to-do-4-title/>",
    icon: <Music size={{{{24}}}} className="text-rvblue" />
  }}, {{
    activity: "<thing-to-do-5-title/>",
    icon: <Utensils size={{{{24}}}} className="text-rvblue" />
  }}, {{
    activity: "<thing-to-do-6-title/>",
    icon: <IceCream size={{{{24}}}} className="text-rvblue" />
  }}, {{
    activity: "<thing-to-do-7-title/>",
    icon: <Car size={{{{24}}}} className="text-rvblue" />
  }}];

  const originalLocalAttractions = [{{
    name: "<local-attraction-1-name/>",
    description: "<local-attraction-1-description/>",
    distance: "<local-attraction-1-distance/>",
    icon: <Trees size={{{{20}}}} />
  }}, {{
    name: "<local-attraction-2-name/>",
    description: "<local-attraction-2-description/>",
    distance: "<local-attraction-2-distance/>",
    icon: <Waves size={{{{20}}}} />
  }}, {{
    name: "<local-attraction-3-name/>",
    description: "<local-attraction-3-description/>",
    distance: "<local-attraction-3-distance/>",
    icon: <MapPin size={{{{20}}}} />
  }}, {{
    name: "<local-attraction-4-name/>",
    description: "<local-attraction-4-description/>",
    distance: "<local-attraction-4-distance/>",
    icon: <Building size={{{{20}}}} />
  }}, {{
    name: "<local-attraction-5-name/>",
    description: "<local-attraction-5-description/>",
    distance: "<local-attraction-5-distance/>",
    icon: <HomeIcon size={{{{20}}}} />
  }}, {{
    name: "<local-attraction-6-name/>",
    description: "<local-attraction-6-description/>",
    distance: "<local-attraction-6-distance/>",
    icon: <Utensils size={{{{20}}}} />
  }}];

  // Fetch content from the database with fallback to original data
  const {{ content: homeContent, isLoading }} = useContent({{
    page: 'home',
    fallbackData: {{}}
  }});

  // Prepare the content with fallback to original data
  
  // Hero section content
  const heroContent = homeContent.hero || {{}};
  const heroHeadline = heroContent.headline || "<hero-banner-phrase-headline/>";
  const heroSubtitle = heroContent.subtitle || "<hero-banner-phrase-subtitle/>"";
  const heroImage = heroContent.image_url || "{paht_hero_banner_image}";
  const heroCta = heroContent.cta_text || "Book Your Stay Now!";
  
  // Parse features list from string if it exists
  const heroFeatures = heroContent.features 
    ? heroContent.features.split(',').map(item => item.trim())
    : [
        "<feature-1/>",
        "<feature-2/>",
        "<feature-3/>",
        "<feature-4/>",
        "<feature-5/>",
        "<feature-6/>",
        "<feature-7/>",
        "<feature-8/>",
      ];

  // Welcome section content
  const welcomeContent = homeContent.welcome || {{}};
  const welcomeTitle = welcomeContent.title || "<welcome-title/>";
  const welcomeDescription = welcomeContent.description || 
    "<welcome-description";
  const welcomeImage = welcomeContent.image_url || "{path_welcome}";
  const welcomeCta = welcomeContent.cta_text || "Book Now";

  // Gallery section content
  const galleryContent = homeContent.gallery || {{}};
  const galleryTitle = galleryContent.title || "<gallery-title/>";
  const galleryDescription = galleryContent.description || 
    "<gallery-description";
  
  // Create gallery images from content or fall back to original
  const galleryImages = originalGalleryImages.map((original, index) => {{
    const imageNumber = index + 1;
    return {{
      src: galleryContent[`image${{imageNumber}}_url`] || original.src,
      alt: galleryContent[`image${{imageNumber}}_alt`] || original.alt
    }};
  }});

  // Things to do section content
  const thingsToDoContent = homeContent.thingsToDo || {{}};
  const thingsToDoTitle = thingsToDoContent.title || "Things to Do";
  const thingsToDoDescription = thingsToDoContent.description || 
    "<things-to-do-description/>";
  const thingsToDoImage = thingsToDoContent.image_url || "{path_things_to_do}";
  
  // Create things to do list from content or fall back to original
  const thingsToDo = originalThingsToDo.map((original, index) => {{
    return {{
      activity: thingsToDoContent[`activity${{index+1}}`] || original.activity,
      icon: original.icon // Keep the original icon
    }};
  }});

  // Featured Amenities content
  const amenitiesContent = homeContent.featuredAmenities || {{}};
  const amenitiesTitle = amenitiesContent.title || "What Awaits You";
  const amenitiesDescription = amenitiesContent.description || 
    "<amenities-description/>";
  
  // Create amenities list from content or fall back to original
  const featuredAmenities = originalFeaturedAmenities.map((original, index) => {{
    const amenityNumber = index + 1;
    return {{
      title: amenitiesContent[`amenity${{amenityNumber}}_title`] || original.title,
      description: amenitiesContent[`amenity${{amenityNumber}}_description`] || original.description,
      image: amenitiesContent[`amenity${{amenityNumber}}_image`] || original.image,
      icon: original.icon // Keep the original icon
    }};
  }});

  // Rules section content
  const rulesContent = homeContent.rules || {{}};
  const rulesTitle = rulesContent.title || "<rules-title/>";
  const rulesDescription = rulesContent.description || 
    "<rules-description/>";
  const rulesImage = rulesContent.image_url || "{path_rules}";
  
  // Rules items with fallbacks
  const ruleItems = [
    {{
      title: rulesContent.rule1_title || "<rule-1-title/>",
      text: rulesContent.rule1_text || "<rule-1-description/>",
    }},
    {{
      title: rulesContent.rule2_title || "<rule-2-title/>",
      text: rulesContent.rule2_text || "<rule-2-description/>",
    }},
    {{
      title: rulesContent.rule3_title || "<rule-3-title/>",
      text: rulesContent.rule3_text || "<rule-3-description/>",
    }},
    {{
      title: rulesContent.rule4_title || "<rule-4-title/>",
      text: rulesContent.rule4_text || "<rule-4-description/>",
    }},
    {{
      title: rulesContent.rule5_title || "<rule-5-title/>",
      text: rulesContent.rule5_text || "<rule-5-description/>",
    }}
  ];

  // CTA section content
  const ctaContent = homeContent.cta || {{}};
  const ctaTitle = ctaContent.title || "<cta-title/>";
  const ctaDescription = ctaContent.description || 
    "<cta-description/>";
  const ctaButtonText = ctaContent.button_text || "Book Your Getaway";

  // Attractions section content
  const attractionsContent = homeContent.attractions || {{}};
  const attractionsTitle = attractionsContent.title || "<attractions-title/>";
  const attractionsDescription = attractionsContent.description || 
    "<attractions-descrption/>";
  
  // Create attractions list from content or fall back to original
  const localAttractions = originalLocalAttractions.map((original, index) => {{
    const attractionNumber = index + 1;
    return {{
      name: attractionsContent[`attraction${{attractionNumber}}_name`] || original.name,
      description: attractionsContent[`attraction${{attractionNumber}}_description`] || original.description,
      distance: attractionsContent[`attraction${{attractionNumber}}_distance`] || original.distance,
      icon: original.icon // Keep the original icon
    }};
  }});

  return (
    <Layout>
      {{/* Hero Banner Section - Fixed for mobile */}}
      <section className="relative min-h-[600px] flex items-center py-16 md:py-0 h-[85vh] overflow-hidden">
        <div className="absolute inset-0 z-0">
          <img src={{heroImage}} alt="Lone Ranger RV Park" className="w-full h-full object-cover" />
          <div className="absolute inset-0 bg-black/50"></div>
        </div>
        
        <div className="relative z-10 section-container text-white flex flex-col justify-center h-full pb-16">
          <h1 className="text-4xl md:text-5xl lg:text-7xl font-display mb-4 animate-fade-in pt-12 md:pt-0">
            {{heroHeadline}}
          </h1>
          <h2 className="text-xl md:text-2xl lg:text-3xl text-rvyellow mb-8 animate-fade-in" style={{{{
          animationDelay: "0.2s"
        }}}}>
            {{heroSubtitle}}
          </h2>
          
          <div className="bg-white/10 backdrop-blur-sm p-4 md:p-6 rounded-lg max-w-2xl mb-8 animate-fade-in" style={{{{
          animationDelay: "0.4s"
        }}}}>
            <ul className="grid grid-cols-2 md:grid-cols-4 gap-3 md:gap-4 text-base md:text-lg">
              {{heroFeatures.map((feature, index) => (
                <li key={{index}}>{{feature}}</li>
              ))}}
            </ul>
          </div>
          
          <div className="mb-8 md:mb-0">
            <Link to="/reservations" className="btn-primary text-base md:text-lg px-6 md:px-8 py-3 md:py-4 animate-fade-in" style={{{{
            animationDelay: "0.6s"
          }}}}>
            {{heroCta}}
          </Link>
        </div>
      </div>
    </section>

      {{/* Section 1 - Welcome */}}
      <section className="section-container py-16 md:py-24">
        <div className="flex flex-col md:flex-row gap-12 items-center">
          <div className="md:w-1/2">
            <h2 className="section-title text-4xl mb-6">{{welcomeTitle}}</h2>
            <p className="text-xl text-gray-700 mb-8">
              {{welcomeDescription}}
            </p>
            
            <Link to="/reservations" className="btn-primary">
              {{welcomeCta}}
            </Link>
          </div>
          <div className="md:w-1/2 rounded-lg overflow-hidden shadow-2xl">
            <img alt="Lone Ranger RV Park at sunset" className="w-full h-full object-cover transition-transform duration-500 hover:scale-105" src={{welcomeImage}} />
          </div>
        </div>
      </section>

      <SectionDivider />

      {{/* Section 2 - Photo Gallery */}}
      <section className="section-container py-16 bg-gray-50">
        <h2 className="section-title text-4xl text-center mb-10">{{galleryTitle}}</h2>
        <p className="text-xl text-gray-600 text-center max-w-3xl mx-auto mb-12">
          {{galleryDescription}}
        </p>
        
        <Carousel className="w-full max-w-5xl mx-auto">
          <CarouselContent>
            {{galleryImages.map((image, index) => (
              <CarouselItem key={{index}} className="md:basis-1/2 lg:basis-1/3">
                <div className="p-1">
                  <div className="overflow-hidden rounded-lg shadow-md hover:shadow-xl transition-shadow duration-300">
                    <img src={{image.src}} alt={{image.alt}} className="w-full h-64 object-cover transition-transform duration-500 hover:scale-105" />
                  </div>
                  <p className="text-center mt-2 text-sm text-gray-600">{{image.alt}}</p>
                </div>
              </CarouselItem>
            ))}}
          </CarouselContent>
          <div className="flex justify-center mt-4">
            <CarouselPrevious className="relative static left-0 right-auto translate-y-0 mr-2" />
            <CarouselNext className="relative static left-auto right-0 translate-y-0" />
          </div>
        </Carousel>
      </section>

      <SectionDivider />

      {{/* Section 3 - Things To Do */}}
      <section className="section-container py-16">
        <div className="flex flex-col md:flex-row gap-12 items-center">
          <div className="md:w-1/2 rounded-lg overflow-hidden shadow-2xl">
            <img alt="Activities at Lone Ranger RV Park" className="w-full h-full object-cover" src={{thingsToDoImage}} />
          </div>
          <div className="md:w-1/2">
            <h2 className="section-title text-4xl mb-6">{{thingsToDoTitle}}</h2>
            <p className="text-lg text-gray-700 mb-6">
              {{thingsToDoDescription}}
            </p>
            
            <ul className="space-y-3 text-lg">
              {{thingsToDo.map((activity, index) => (
                <li key={{index}} className="flex items-start">
                  <span className="inline-block bg-rvyellow text-rvmaroon rounded-full w-6 h-6 flex items-center justify-center mr-3 mt-1 font-bold">{{index + 1}}</span>
                  <span>{{activity.activity}}</span>
                </li>
              ))}}
            </ul>
          </div>
        </div>
      </section>

      <SectionDivider />

      {{/* Section 4 - What Awaits You */}}
      <section className="section-container py-16 bg-gray-50">
        <h2 className="section-title text-4xl text-center mb-3">{{amenitiesTitle}}</h2>
        <p className="text-xl text-gray-600 text-center max-w-3xl mx-auto mb-12">
          {{amenitiesDescription}}
        </p>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
          {{featuredAmenities.map((amenity, index) => (
            <Card key={{index}} className="overflow-hidden hover:shadow-lg transition-shadow duration-300">
              <div className="h-48 overflow-hidden">
                <img src={{amenity.image}} alt={{amenity.title}} className="w-full h-full object-cover transition-transform duration-500 hover:scale-105" />
              </div>
              <CardContent className="p-6">
                <h3 className="text-xl font-display mb-2 text-rvmaroon">{{amenity.title}}</h3>
                <p className="text-gray-600">{{amenity.description}}</p>
              </CardContent>
            </Card>
          ))}}
        </div>
      </section>

      <SectionDivider />

      {{/* Section 5 - RV Rules & Regulations */}}
      <section className="section-container py-16">
        <div className="flex flex-col md:flex-row gap-12">
          <div className="md:w-1/2">
            <h2 className="section-title text-4xl mb-6">{{rulesTitle}}</h2>
            <p className="text-lg text-gray-700 mb-6">
              {{rulesDescription}}
            </p>
            
            <ul className="space-y-4 text-lg">
              {{ruleItems.map((rule, index) => (
                <li key={{index}} className="flex items-start">
                  <Calendar className="text-rvred mr-3 mt-1 flex-shrink-0" size={{{{20}}}} />
                  <div>
                    <span className="font-semibold">{{rule.title}}</span> {{rule.text}}
                  </div>
                </li>
              ))}}
            </ul>
            
            <Link to="/rules-faqs" className="btn-secondary mt-8 inline-block">
              View All Rules & FAQs
            </Link>
          </div>
          <div className="md:w-1/2 rounded-lg overflow-hidden shadow-2xl">
            <img alt="RV campsite at Lone Ranger RV Park" className="w-full h-full object-cover" src={{rulesImage}} />
          </div>
        </div>
      </section>

      <SectionDivider />

      {{/* Section 6 - Rest CTA Section */}}
      <section className="py-20 bg-rvmaroon text-white">
        <div className="section-container text-center">
          <h2 className="text-4xl md:text-5xl font-display mb-8">{{ctaTitle}}</h2>
          <p className="text-xl max-w-3xl mx-auto mb-10">
            {{ctaDescription}}
          </p>
          <Link to="/reservations" className="btn-primary bg-rvyellow text-rvmaroon hover:bg-rvyellow/90 text-lg px-8 py-4">
            {{ctaButtonText}}
          </Link>
        </div>
      </section>

      {{/* Section 7 - Local Attractions */}}
      <section className="section-container py-16">
        <h2 className="section-title text-4xl text-center mb-3">{{attractionsTitle}}</h2>
        <p className="text-xl text-gray-600 text-center max-w-3xl mx-auto mb-12">
          {{attractionsDescription}}
        </p>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {{localAttractions.map((attraction, index) => (
            <div key={{index}} className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow duration-300 border border-gray-100 h-full">
              <div className="flex justify-between items-start mb-2">
                <h3 className="text-xl font-display text-rvmaroon flex-grow pr-2">{{attraction.name}}</h3>
                <span className="bg-gray-100 text-gray-700 px-2 py-1 rounded text-sm font-medium flex items-center whitespace-nowrap">
                  <MapPin size={{{{14}}}} className="mr-1" />
                  {{attraction.distance}}
                </span>
              </div>
              <p className="text-gray-600">{{attraction.description}}</p>
            </div>
          ))}}
        </div>
        
        <div className="text-center mt-10">
          <Link to="/activities" className="btn-secondary">
            Discover More Attractions
          </Link>
        </div>
      </section>
    </Layout>
  );
}};

export default Home;

"""