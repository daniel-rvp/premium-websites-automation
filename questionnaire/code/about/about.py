ABOUT = """import React, {{ useEffect }} from 'react';
import Layout from "@/components/Layout";
import SectionDivider from "@/components/SectionDivider";
import {{ useContent }} from "@/hooks/use-content";
import {{ toast }} from "@/hooks/use-toast";
import {{ getIconByName, defaultAmenities, defaultAccommodations }} from "@/utils/iconMapping";
import HeaderSection from "@/components/about/HeaderSection";
import TexasCharmSection from "@/components/about/TexasCharmSection";
import AccommodationsSection from "@/components/about/AccommodationsSection";
import CTASection from "@/components/about/CTASection";

interface AmenityItem {{
  name: string;
  icon: React.ReactElement;
}}

const About = () => {{
  // Get content data from database with fallback to original data
  const {{ content: aboutContent, isLoading, error, refresh }} = useContent({{
    page: "about",
    fallbackData: {{}}
  }});

  // If there's an error loading content, show a toast and try to refresh
  useEffect(() => {{
    if (error) {{
      console.error("Error loading content:", error);
      toast({{
        title: "Content loading issue",
        description: "Some content may not display correctly. Trying to reload.",
        variant: "destructive",
      }});
      
      // Try to refresh the content after a short delay
      const timer = setTimeout(() => {{
        refresh();
      }}, 3000);
      
      return () => clearTimeout(timer);
    }}
  }}, [error, refresh]);

  // Prepare content data with fallbacks
  const headerTitle = aboutContent?.header?.title || "<about-header-title/>";
  const headerDescription = aboutContent?.header?.description || "<about-header-description/>";
  const headerImageUrl = aboutContent?.header?.imageUrl || "{header_image_path}";

  const stateCharmTitle = aboutContent?.texas_charm?.title || "<location-charm-header-title/>";
  const stateCharmDescription = aboutContent?.texas_charm?.description || "<location-charm-header-title/>";

  // Parse amenities from JSON if available
  let amenities: AmenityItem[] = defaultAmenities;
  try {{
    if (aboutContent?.texas_charm?.amenities) {{
      let parsedAmenities;
      
      // Handle both string and already parsed object
      if (typeof aboutContent.texas_charm.amenities === 'string') {{
        parsedAmenities = JSON.parse(aboutContent.texas_charm.amenities);
      }} else {{
        parsedAmenities = aboutContent.texas_charm.amenities;
      }}
      
      if (Array.isArray(parsedAmenities) && parsedAmenities.length > 0) {{
        amenities = parsedAmenities.map((item) => {{
          // Map the icon name string to the actual icon component
          const iconName = item.icon || "Waves";
          return {{
            name: item.name || "",
            icon: getIconByName(iconName)
          }};
        }});
      }}
    }}
  }} catch (error) {{
    console.error("Error parsing amenities:", error);
  }}

  const accommodationsTitle = aboutContent?.accommodations?.title || "Find Your Perfect Stay";
  const accommodationsDescription = aboutContent?.accommodations?.description || 
    "Choose from a variety of accommodations designed to suit your travel style";
  const accommodationsButtonText = aboutContent?.accommodations?.buttonText || "Book Your Stay Now";
  const accommodationsButtonLink = aboutContent?.accommodations?.buttonLink || "/reservations";

  // Parse accommodation items from JSON if available
  let accommodations = defaultAccommodations;
  try {{
    if (aboutContent?.accommodations?.items) {{
      let parsedItems;
      
      // Handle both string and already parsed object
      if (typeof aboutContent.accommodations.items === 'string') {{
        parsedItems = JSON.parse(aboutContent.accommodations.items);
      }} else {{
        parsedItems = aboutContent.accommodations.items;
      }}
      
      if (Array.isArray(parsedItems) && parsedItems.length > 0) {{
        accommodations = parsedItems;
      }}
    }}
  }} catch (error) {{
    console.error("Error parsing accommodation items:", error);
  }}

  const ctaTitle = aboutContent?.cta?.title || "<about-cta-title-content/>";
  const ctaDescription = aboutContent?.cta?.description || 
    "<about-cta-description-content/>";
  const ctaButtonText = aboutContent?.cta?.buttonText || "Contact Us";
  const ctaButtonLink = aboutContent?.cta?.buttonLink || "/contact";
  const ctaButtonLinkType = aboutContent?.cta?.buttonLinkType || "internal";

  return (
    <Layout>
      <HeaderSection
        title={{headerTitle}}
        description={{headerDescription}}
        imageUrl={{headerImageUrl}}
      />
      
      <SectionDivider />
      
      <TexasCharmSection
        title={{stateCharmTitle}}
        description={{stateCharmDescription}}
        amenities={{amenities}}
      />
      
      <SectionDivider />
      
      <AccommodationsSection
        title={{aboutContent?.accommodations?.title || "Find Your Perfect Stay"}}
        description={{aboutContent?.accommodations?.description || 
          "Choose from a variety of accommodations designed to suit your travel style"}}
        buttonText={{aboutContent?.accommodations?.buttonText || "Book Your Stay Now"}}
        buttonLink={{aboutContent?.accommodations?.buttonLink || "/reservations"}}
        accommodations={{accommodations}}
      />
      
      <CTASection
        title={{ctaTitle}}
        description={{ctaDescription}}
        buttonText={{ctaButtonText}}
        buttonLink={{ctaButtonLink}}
        buttonLinkType={{ctaButtonLinkType as "internal" | "external"}}
      />
    </Layout>
  );
}};

export default About;"""