import json, requests, subprocess

from rest_framework.views import APIView

from rest_framework.response import Response

from questionnaire.models import *
from questionnaire.serializers import *
from questionnaire._util import *

from ._prompts_website_generation import *


HEADERS = {
    'apikey': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJtbHJ4ZG5ueGhhd3JobmNidm96Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0OTU1Mjc4NSwiZXhwIjoyMDY1MTI4Nzg1fQ.nxB9n8R4OjPaAdCYc8CooJYfx5OVLxcs_Xs3ZKW295I',
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJtbHJ4ZG5ueGhhd3JobmNidm96Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0OTU1Mjc4NSwiZXhwIjoyMDY1MTI4Nzg1fQ.nxB9n8R4OjPaAdCYc8CooJYfx5OVLxcs_Xs3ZKW295I'
}
BASE_URL = 'https://bmlrxdnnxhawrhncbvoz.supabase.co/rest/v1/'


class PremiumWebsiteView(APIView):
    def get(self, request):
        questionnaire_id = request.query_params.get('fid')

        client = User.objects.get(pk=questionnaire_id)

        questionnaire = client.premiumwebsiteform.qanda_set.all()

        questionnaire_serializer = QandASerializer(questionnaire, many=True)

        return Response(questionnaire_serializer.data)
    

class QandAView(APIView):
    def get(self, request):
        user_id = request.query_params.get('fid')
        type = request.query_params.get('type')

        questionnaire_id = User.objects.get(pk=user_id).premiumwebsiteform.pk
        
        all_qas = PremiumWebsiteForm.objects.get(pk=questionnaire_id).qanda_set.all()
        qa = all_qas.get(type=type)
    
        qa_serializer = QandASerializer(qa)

        data = qa_serializer.data

        if str(qa.type) == str(42):
            for qa_ in all_qas.order_by('pk'):
                if not qa_.checked:
                    data['checked'] = False
                    break

        return Response(data)
    
    def post(self, request):
        questionnaire_id = request.query_params.get('fid')
        type = request.query_params.get('type')

        all_qas = PremiumWebsiteForm.objects.get(pk=questionnaire_id).qanda_set.all()
        qa = all_qas.get(type=type)

        answer = json.loads(request.body)['answer']

        """ add_prompt = f'''<question>{qa.question}</question><answer>{answer}</answer>'''

        result = None

        while result is None or not isinstance(result, bool):
            response = llama3(prompt=add_prompt)

            if response.lower() == "true":
                result = True
            elif response.lower() == "false":
                result = False

        if result:
            qa.answer = answer
            qa.checked = True
            qa.save() """
        
        qa.answer = answer
        qa.checked = True
        qa.save()

        qa_serializer = QandASerializer(qa)

        data = qa_serializer.data

        if str(qa.type) == str(42):
            for qa_ in all_qas.order_by('pk'):
                if not qa_.checked:
                    data['checked'] = False
                    break

        print(data)

        return Response(data)


class WebsiteContentGenerator(APIView):
    def get(self, request):
        questionnaire_id = request.query_params.get('fid')

        camp = User.objects.get(pk=(PremiumWebsiteForm.objects.get(pk=questionnaire_id).pk))

        supabase_client_url = f'https://bmlrxdnnxhawrhncbvoz.supabase.co/rest/v1/clients?id=eq.{camp.pk}'
        client_supabase_response = requests.get(
            url=supabase_client_url,
            headers=HEADERS
        )

        data = json.loads(client_supabase_response.content.decode('utf-8'))[0]
        client_id = data['id']

        qa = PremiumWebsiteForm.objects.get(pk=questionnaire_id)

        qandas = qa.qanda_set.all()

        relevant_info = draft_knowledge(qandas=qandas)
        
        for key, value in PROMPT_PAGES.items():
            print(key)
            data = None
            i = 0

            while not data:
                full_prompt = PROMPT.format(
                    client=camp.name,
                    address=camp.address,
                    state=camp.state,
                    relevant_info= relevant_info,
                    page_specific=value
                )

                response = gemini(
                    prompt=full_prompt,

                )

                try:
                    data = json.loads(response)
                except Exception as e:
                    print(e)
                    print((type(response)))
                    print(response)
                    i+=1

                if i > 9:
                    break

            if not data:
                print('ALERTA')

            if key == 'about':
                url = BASE_URL + key
                about_accommodation_url = BASE_URL + 'about_accommodation'
                about_amenity_url = BASE_URL + 'about_amenity'
                
                about_accommodation_data = data['accomodations']
                about_amenity_data = data['amenities']

                del data['accomodations']
                del data['amenities']
                data['client_id'] = client_id

                response_url = requests.post(
                    url=url,
                    headers=HEADERS,
                    data=data
                )

                if response_url.status_code != 201:
                    print('error about response_url')
                    return Response({'error': 'error about response_url'})

                supabase_url = url + f'?client_id=eq.{client_id}'
                client_supabase_response = requests.get(
                    url=supabase_url,
                    headers=HEADERS
                )

                data = json.loads(client_supabase_response.content.decode('utf-8'))[0]
                about_id = data['id']

                for about_accommodation in about_accommodation_data:
                    about_accommodation['about_id'] = about_id
                    response_about_accomodation = requests.post(
                        url=about_accommodation_url,
                        headers=HEADERS,
                        data=about_accommodation
                    )

                    if response_about_accomodation.status_code != 201:
                        print('error response_about_accomodation')
                        return Response({'error': 'error response_about_accomodation'})

                for about_amenity in about_amenity_data:
                    about_amenity['about_id'] = about_id
                    response_about_amenities = requests.post(
                        url=about_amenity_url,
                        headers=HEADERS,
                        data=about_amenity
                    )

                    if response_about_amenities.status_code != 201:
                        print(response_about_amenities.content)
                        print('error response_about_amenities')
                        return Response({'error': 'error response_about_amenities'})
                
            if key == 'accommodations':
                url = BASE_URL + key
                accommodations_site_url = BASE_URL + 'accommodations_site'

                accommodations_site_data = data['accommodations_list']

                del data['accommodations_list']
                data['client_id'] = client_id

                response_url = requests.post(
                    url=url,
                    headers=HEADERS,
                    data=data
                )

                if response_url.status_code != 201:
                    print('error accommodations response_url')
                    return Response({'error': 'error accommodations response_url'})

                supabase_url = url + f'?client_id=eq.{client_id}'
                client_supabase_response = requests.get(
                    url=supabase_url,
                    headers=HEADERS
                )

                data = json.loads(client_supabase_response.content.decode('utf-8'))[0]
                accommodations_id = data['id']


                for accomodation in accommodations_site_data:
                    accomodation['accommodation_id'] = accommodations_id
                    response_accommodations_list = requests.post(
                        url=accommodations_site_url,
                        headers=HEADERS,
                        data=accomodation
                    )

                    if response_accommodations_list.status_code != 201:
                        print('error response_accommodations_list')
                        return Response({'error': 'error response_accommodations_list'})

            if key == 'activities':
                url = BASE_URL + key
                activities_activity_url = BASE_URL + 'activities_activity'

                activities_activity_data = data['activities']

                del data['activities']
                data['client_id'] = client_id

                response_url = requests.post(
                    url=url,
                    headers=HEADERS,
                    data=data
                )

                if response_url.status_code != 201:
                    print('error activities response_url')
                    return Response({'error': 'error activities response_url'})

                supabase_url = url + f'?client_id=eq.{client_id}'
                client_supabase_response = requests.get(
                    url=supabase_url,
                    headers=HEADERS
                )

                data = json.loads(client_supabase_response.content.decode('utf-8'))[0]
                activities_id = data['id']

                for activity_activities in activities_activity_data:
                    activity_activities['activities_id'] = activities_id

                    response_activities = requests.post(
                        url=activities_activity_url,
                        headers=HEADERS,
                        data=activity_activities
                    )

                    if response_activities.status_code != 201:
                        print('error response_activities')
                        return Response({'error': 'error response_activities'})

            if key == 'amenities':
                url = BASE_URL + key
                amenities_activities_url = BASE_URL + 'amenities_activities'
                amenities_essential_url = BASE_URL + 'amenities_essential'
                amenities_special_url = BASE_URL + 'amenities_special'

                amenities = data['amenities']
                del data['amenities']
                data['client_id'] = client_id

                response_url = requests.post(url=url,
                    headers=HEADERS,
                    data=data
                )

                if response_url.status_code != 201:
                    print('error amenities response_url')
                    return Response({'error': 'error amenities response_url'})

                supabase_url = url + f'?client_id=eq.{client_id}'
                client_supabase_response = requests.get(
                    url=supabase_url,
                    headers=HEADERS
                )

                data = json.loads(client_supabase_response.content.decode('utf-8'))[0]
                amenities_id = data['id']

                activities = []
                essentials = []
                specials = []

                for amenity in amenities:
                    if str(amenity['category']) == str(1):
                        del amenity['category']
                        amenity['amenities_id'] = amenities_id
                        activities.append(amenity)
                        continue

                    if str(amenity['category']) == str(0):
                        del amenity['category']
                        amenity['amenities_id'] = amenities_id
                        essentials.append(amenity)
                        continue
                    
                    if str(amenity['category']) == str(2):
                        del amenity['category']
                        amenity['amenities_id'] = amenities_id
                        specials.append(amenity)
                        continue

                for activity in activities:
                    response_activities_ = requests.post(
                        url=amenities_activities_url,
                        headers=HEADERS,
                        data=activity
                    )

                    if response_activities_.status_code != 201:
                        print('error response_activities_')
                        return Response({'error': 'error response_activities_'})

                for essential in essentials:
                    response_essential = requests.post(
                        url=amenities_essential_url,
                        headers=HEADERS,
                        data=essential
                    )

                    if response_essential.status_code != 201:
                        print('error response_essential')
                        return Response({'error': 'error response_essential'})

                for special in specials:
                    response_special = requests.post(
                        url=amenities_special_url,
                        headers=HEADERS,
                        data=special
                    )

                    if response_special.status_code != 201:
                        print('error response_special')
                        return Response({'error': 'error response_special'})
            
            if key == 'contact_us':
                url = BASE_URL + key
                data['client_id'] = client_id

                response_url = requests.post(url=url,
                    headers=HEADERS,
                    data=data
                )

            if key == 'home':
                url = BASE_URL + key
                home_activity_url = BASE_URL + 'home_activity'
                home_amenity_url = BASE_URL + 'home_amenity'
                home_atraction_url = BASE_URL + 'home_attraction'
                home_hero_amenity_url = BASE_URL + 'home_hero_amenity'

                home_activities = data['activities']
                home_amenities = data['amenities']
                home_attractions = data['attractions']
                home_hero_amenity = data['hero_amenity_list']

                del data['activities']
                del data['amenities']
                del data['attractions']
                del data['hero_amenity_list']
                data['client_id'] = client_id

                response_url = requests.post(
                    url=url,
                    headers=HEADERS,
                    data=data
                )

                if response_url.status_code != 201:
                    print('error home response_url')
                    return Response({'error': 'error home response_url'})

                supabase_url = url + f'?client_id=eq.{client_id}'
                client_supabase_response = requests.get(
                    url=supabase_url,
                    headers=HEADERS
                )

                data = json.loads(client_supabase_response.content.decode('utf-8'))[0]
                home_id = data['id']

                for activity_ in home_activities:
                    activity_['home_id'] = home_id
                    response_activity = requests.post(
                        url=home_activity_url,
                        headers=HEADERS,
                        data=activity_
                    )

                    if response_activity.status_code != 201:
                        print('error response_activity')
                        return Response({'error': 'error response_activity'})

                for amenity_ in home_amenities:
                    amenity_['home_id'] = home_id
                    response_amenity = requests.post(
                        url=home_amenity_url,
                        headers=HEADERS,
                        data=amenity_
                    )

                    if response_amenity.status_code != 201:
                        print('error response_amenity')
                        return Response({'error': 'error response_amenity'})

                for attraction_ in home_attractions:
                    attraction_['home_id'] = home_id
                    response_attraction = requests.post(
                        url=home_atraction_url,
                        headers=HEADERS,
                        data=attraction_
                    )

                    if response_attraction.status_code != 201:
                        print('error response_attraction')
                        return Response({'error': 'error response_attraction'})

                for hero_amenity in home_hero_amenity:
                    hero_amenity['home_id'] = home_id
                    response_hero_amenity = requests.post(
                        url=home_hero_amenity_url,
                        headers=HEADERS,
                        data=hero_amenity
                    )

                    if response_hero_amenity.status_code != 201:
                        print('error response_hero_amenity')
                        return Response({'error': 'error response_hero_amenity'})

            if key == 'reservations':
                url = BASE_URL + key
                reservations_accommodation_url = BASE_URL + 'reservations_accommodation'

                accommodations = data['accommodations']
                del data['accommodations']
                data['client_id'] = client_id

                response_url = requests.post(
                    url=url,
                    headers=HEADERS,
                    data=data
                )

                if response_url.status_code != 201:
                    print('error reservations response_url')
                    return Response({'error': 'error reservations response_url'})

                supabase_url = url + f'?client_id=eq.{client_id}'
                client_supabase_response = requests.get(
                    url=supabase_url,
                    headers=HEADERS
                )

                data = json.loads(client_supabase_response.content.decode('utf-8'))[0]
                accomodations_id = data['id']

                for accommodation in accommodations:
                    accommodation['reservations_id'] = accomodations_id
                    response_accommodation = requests.post(
                    url=reservations_accommodation_url,
                    headers=HEADERS,
                    data=accommodation
                    )
                    if response_accommodation.status_code != 201:
                        print('error response_accommodation')
                        return Response({'error': 'error response_accommodation'})
            
            if key == 'rules':
                rules_url = BASE_URL + key
                faqs_url = BASE_URL + 'faqs'

                rules = data['rules']
                rules['client_id'] = client_id

                faqs = data['faqs']
                faqs['client_id'] = client_id

                for rule in rules:
                    rule_response = requests.post(
                    url=rules_url,
                    headers=HEADERS,
                    data=rule
                    )
                    if rule_response.status_code != 201:
                        print('error rule_response')
                        return Response({'error': 'error rule_response'})
                
                for faq in faqs:
                    faq['question'] = faq['type']
                    del faq['type']

                    faq_response = requests.post(
                    url=faqs_url,
                    headers=HEADERS,
                    data=faq
                    )
                    if faq_response.status_code != 201:
                        print('error faq_response')
                        return Response({'error': 'error faq_response'})

        name = camp.name
        #! change in deployment """
        new_project_location = f'/home/admon/premium-websites-automation/result/'
        subprocess.call([f'mkdir {name}'], cwd=new_project_location, shell=True)
        subprocess.call([f'cp -R ./lone-ranger-lodge-web/* ./{name}/'], cwd=new_project_location, shell=True)

        handle_ract_app_directory = f'/Users/daniel/Documents/RoverPass/premium-websites/premium_websites/result/{name}/'
        subprocess.call(['rm -rf package.json'], cwd=handle_ract_app_directory, shell=True)
        subprocess.call(['rm -rf node_modules'], cwd=handle_ract_app_directory, shell=True)
        subprocess.call(['npm cache clean --force'], shell=True)
        subprocess.call(['npm install'], cwd=handle_ract_app_directory, shell=True)
        subprocess.call(['npm run build'], cwd=handle_ract_app_directory, shell=True)
        subprocess.call([f'surge /home/admon/premium-websites-automation/result/{name}/dist/ {camp.domain}'], cwd=handle_ract_app_directory, shell=True)

        #! change in deployment
        #'/Users/daniel/Documents/RoverPass/premium-websites/premium_websites/result/'
        #os.system(f'rm -r {name}/')

        return Response({'res': 'done'})