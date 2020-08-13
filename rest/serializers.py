from .models import *
from rest_framework import serializers

class PersonSerializer(serializers.ModelSerializer):     #http://127.0.0.1:8000/api/rest/
    class Meta:
        model=Person
        fields='__all__'


class StateReadSerializer(serializers.ModelSerializer):   #http://127.0.0.1:8000/api/rest/state/
    class Meta:
        model=State
        fields=['id','country','name','description','population','GDP']
        #read_only_fields=('country',)


class CountrySerializer(serializers.ModelSerializer):      #http://127.0.0.1:8000/api/viewset/rest/
    state_country=StateReadSerializer(many=True)

    class Meta:
        model=Country
        fields=['id','name','description','population','GDP','state_country']

    def create(self, validated_data):
        state_data = validated_data.pop('state_data')
        country = Country.objects.create(**validated_data)
        for state_data in state_data:
            State.objects.create(country=Country, **state_data)
        return Country

    def update(self, instance, validated_data):
        state_data = validated_data.pop('state_country')
        states = (instance.state_country).all()
        states = list(states)
        instance.name = validated_data.get('first_name', instance.name)
        instance.description = validated_data.get('last_name', instance.description)
        instance.population = validated_data.get('instrument', instance.population)
        instance.GDP = validated_data.get('instrument', instance.GDP)
        instance.save()

        for state_data in state_data:
            state = states.pop(0)
            state.name = state_data.get('name', state.name)
            state.description = state_data.get('description', state.description)
            state.population = state_data.get('population', state.population)
            state.GDP = state_data.get('GDP', state.GDP)
            state.save()
        return instance

class CitySerializer(serializers.Serializer):
    class Meta:
        model=City
        fields=['id','name','description','population','GDP']

class TownSerializer(serializers.Serializer):
    class Meta:
        model=Town
        fields=['id','name','description','population','GDP','Pincode']
