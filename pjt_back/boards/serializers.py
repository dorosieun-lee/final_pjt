from .models import MMBoard, MMComment, LBoard, LComment
from rest_framework import serializers
from django.contrib.auth import get_user_model
from accounts.models import DetailUser

User = get_user_model()

class UsernameSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class MMBoardListSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.detailuser.nickname', read_only=True)

    class Meta:
        model = MMBoard
        fields = ('id', 'title', 'content', 'nickname', 'created_at')


class MMCommentSerializer(serializers.ModelSerializer):
    nickname = serializers.CharField(source='user.detailuser.nickname', read_only=True)
    user = UsernameSerializer(read_only=True)

    class Meta:
        model = MMComment
        fields = '__all__'
        read_only_fields = ('board', 'user')


class MMBoardSerializer(serializers.ModelSerializer):
    mm_comment = MMCommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='mm_comment.count', read_only=True)
    nickname = serializers.CharField(source='user.detailuser.nickname', read_only=True)
    user = UsernameSerializer(read_only=True)
    
    class Meta:
        model = MMBoard
        fields = '__all__'
        read_only_fields = ('user',)


# class DetailUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DetailUser
#         fields = ('address', )

class LBoardListSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source='user.detailuser.address', read_only=True)

    class Meta:
        model = LBoard
        fields = ('id', 'title', 'content', 'address', 'created_at')


class LCommentSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source='user.detailuser.address', read_only=True)
    user = UsernameSerializer(read_only=True)

    class Meta:
        model = LComment
        fields = '__all__'
        read_only_fields = ('board', 'user')


class LBoardSerializer(serializers.ModelSerializer):
    local_comment = LCommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='local_comment.count', read_only=True)
    address = serializers.CharField(source='user.detailuser.address', read_only=True)
    user = UsernameSerializer(read_only=True)
    
    class Meta:
        model = LBoard
        fields = '__all__'
        read_only_fields = ('user',)