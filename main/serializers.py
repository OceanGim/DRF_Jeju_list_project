from rest_framework import serializers
from main.models import Store, Comment


class CommentSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()

    def get_user(self, obj):
        return obj.user.username

    def get_created_at(self, obj):
        created_at = obj.created_at.replace(microsecond=0).isoformat()
        return created_at
    class Meta:
        model = Comment
        exclude = ("store",)

class StoreListSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True, source="comment_set")

    class Meta:
        model = Store
        fields = "__all__"


class CommentCreateSerializer(serializers.ModelSerializer):
        class Meta:
            model = Comment
            fields = ("content",)