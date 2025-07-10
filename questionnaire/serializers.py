from rest_framework import serializers

from questionnaire.models import QandA, PremiumWebsiteForm


class PremiumWebsiteFormSerializer(serializers.Serializer):
    questionnaire = serializers.SerializerMethodField()

    def get_questionnaire(self, obj):
        obj.qanda_set.all()


    class Meta:
        model = PremiumWebsiteForm
        fields = ['camp', 'questionnaire']


class QandASerializer(serializers.ModelSerializer):
    class Meta:
        model = QandA
        fields = ['type', 'question', 'answer', 'checked', 'questionnaire']
