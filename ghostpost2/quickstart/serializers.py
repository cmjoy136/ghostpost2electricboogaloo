from ghostpost2.quickstart.models import *
from rest_framework import serializers

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = [ 'boast_roast', 'upvote', 'downvote', 'content', 'datetime']