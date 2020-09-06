from rest_framework import serializers

from post.models import Post



class PostSerializer(serializers.ModelSerializer):
    "Linkleme"
    url = serializers.HyperlinkedIdentityField(
        view_name='post:detail',
        lookup_field='slug',
    )

    username = serializers.SerializerMethodField()

    "Linkleme de slug yerine url yazıcaz ve url'e namespace eklememiz gerekiyor"
    class Meta:
        model = Post
        fields = [
            'username',
            'title',
            'content',
            'image',
            'url',
            'created',
            'modified_by',
        ]
    "Bize yükleyenleri id değil username olarak göstericek"
    def get_username(self,obj):
        return str(obj.user.username)



" Models'den editable=False diyerek de slug ve create'i kapatabilirsin "
class PostUpdateCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'title',
            'content',
            'image',
        ]


