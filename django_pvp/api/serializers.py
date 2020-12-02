from rest_framework import serializers


class TournamentSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
    name = serializers.CharField(max_length=2000)
    description = serializers.CharField(max_length=2000)
    created = serializers.DateTimeField()
    start_date = serializers.DateTimeField()
    participants = serializers.IntegerField()


class TournamentListSerializer(serializers.Serializer):
    total_amount = serializers.IntegerField(default=0)
    tournaments = TournamentSerializer(many=True)
