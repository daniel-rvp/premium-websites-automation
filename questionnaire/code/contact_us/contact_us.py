CONTACT_US = """import Layout from "@/components/Layout";
import PageHeader from "@/components/PageHeader";
import SectionDivider from "@/components/SectionDivider";
import ContactForm from "@/components/ContactForm";
import GoogleMap from "@/components/GoogleMap";
import {{ MapPin, Phone, Mail, Clock }} from "lucide-react";
import {{ Link }} from "react-router-dom";
import {{ Card, CardContent }} from "@/components/ui/card";
const Contact = () => {{
  return <Layout>
      <PageHeader title="Contact Us" description="<invitation-to-inquire-with-camp-name />" />
      
      {{/* Contact Information & Form */}}
      <section className="section-container">
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-10">
          {{/* Contact Information */}}
          <div>
            <h2 className="section-title"><form-title /></h2>
            <p className="text-gray-600 mb-8">
              <form-description />
            </p>
            
            <div className="space-y-6">
              <div className="flex items-start">
                <div className="text-rvred mt-1 mr-4">
                  <MapPin size={{24}} />
                </div>
                <div>
                  <h3 className="font-semibold text-lg">Location</h3>
                  <p className="text-gray-600">{address}</p>
                </div>
              </div>
              
              <div className="flex items-start">
                <div className="text-rvred mt-1 mr-4">
                  <Phone size={{24}} />
                </div>
                <div>
                  <h3 className="font-semibold text-lg">Phone</h3>
                  <p className="text-gray-600">{phone}</p>
                  <p className="text-gray-500 text-sm">For general inquiries and reservations</p>
                </div>
              </div>
              
              <div className="flex items-start">
                <div className="text-rvred mt-1 mr-4">
                  <Mail size={{24}} />
                </div>
                <div>
                  <h3 className="font-semibold text-lg">Email</h3>
                  <p className="text-gray-600">{mail}
                </p>
                  <p className="text-gray-500 text-sm"><response-description /></p>
                </div>
              </div>
              
              <div className="flex items-start">
                <div className="text-rvred mt-1 mr-4">
                  <Clock size={{24}} />
                </div>
              </div>
            </div>
          </div>
          
          {{/* Contact Form */}}
          <div>
            <h2 className="section-title">Send Us a Message</h2>
            <ContactForm />
          </div>
        </div>
      </section>
      
      <SectionDivider />
      
      {{/* Map Section */}}
      <section className="section-container">
        <div className="text-center mb-10">
          <h2 className="section-title">Find Us</h2>
          <p className="text-gray-600 max-w-2xl mx-auto">
            <location-description />
          </p>
        </div>
        
        <div className="h-96 w-full">
          <GoogleMap address="{address}" />
        </div>
      </section>
      
      <SectionDivider />
      
      {{/* FAQs Section */}}
      <section className="section-container pb-20">
        <div className="text-center mb-10">
          <h2 className="section-title">Frequently Asked Questions</h2>
          <p className="text-gray-600 max-w-2xl mx-auto">
            Need more info? Here are a few quick answers — or view our full FAQ page.
          </p>
        </div>
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-10">
          <Card className="bg-white shadow-md">
            <CardContent className="pt-6">
              <h3 className="text-lg font-semibold text-rvmaroon mb-2"><question-1 /></h3>
              <p className="text-gray-600"><answer-1 /></p>
            </CardContent>
          </Card>
          
          <Card className="bg-white shadow-md">
            <CardContent className="pt-6">
              <h3 className="text-lg font-semibold text-rvmaroon mb-2"><question-2 /></h3>
              <p className="text-gray-600"><answer-2 /></p>
            </CardContent>
          </Card>
          
          <Card className="bg-white shadow-md">
            <CardContent className="pt-6">
              <h3 className="text-lg font-semibold text-rvmaroon mb-2"><question-3 /></h3>
              <p className="text-gray-600"><answer-3 /></p>
            </CardContent>
          </Card>
          
          <Card className="bg-white shadow-md">
            <CardContent className="pt-6">
              <h3 className="text-lg font-semibold text-rvmaroon mb-2"><question-4 /></h3>
              <p className="text-gray-600"><answer-4 /></p>
            </CardContent>
          </Card>
        </div>
        
        <div className="text-center">
          <Link to="/rules-faqs" className="btn-primary">
            View All FAQs →
          </Link>
        </div>
      </section>
    </Layout>;
}};
export default Contact;"""