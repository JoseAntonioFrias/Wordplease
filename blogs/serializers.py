from rest_framework import serializers
from blogs.models import Blog
from posts.models import Post


class BlogSerializer(serializers.ModelSerializer):
    owner_author = serializers.SerializerMethodField()
    owner_username = serializers.SerializerMethodField()
    num_posts = serializers.SerializerMethodField()
    blog_url = serializers.SerializerMethodField()
    owner_first_name = serializers.SerializerMethodField()

    def get_owner_author(self, obj):
        return '{0} {1}'.format(obj.owner.first_name, obj.owner.last_name)

    def get_owner_username(self, obj):
        return obj.owner.username

    def get_num_posts(self, obj):
        return Post.objects.all().filter(blog=obj.id).count()

    def get_blog_url(self, obj):
        return "/blogs/" + str(obj.owner.username)

    def get_owner_first_name(self, obj):
        return obj.owner.first_name

    class Meta:
        model = Blog
        fields = ['owner_author', 'owner_username', 'title', 'description', 'blog_url', 'num_posts', 'owner_first_name']
