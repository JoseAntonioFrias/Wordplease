from rest_framework import serializers
from posts.models import Post


class PostListSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()

    def get_author(self, obj):
        return '{0} {1}'.format(obj.owner.first_name, obj.owner.last_name)

    class Meta:
        model = Post
        fields = ['author', 'title', 'summary', 'image', 'pub_date']


class PostSerializer(PostListSerializer):

    class Meta(PostListSerializer.Meta):
        fields = '__all__'
        read_only_fields = ['id', 'owner']
