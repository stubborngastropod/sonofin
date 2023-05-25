from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Board, Comment
from accounts.serializers import UserDetailsSerializer

User = get_user_model()

class BoardListSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    author_name = serializers.ReadOnlyField(source='author.username')
    like_user_names = serializers.StringRelatedField(many=True, read_only=True)
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    updated_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Board
        fields = ['id','author_name', 'like_user_names', 'title', 'content', 'created_at', 'updated_at']

# class CommentSerializer(serializers.ModelSerializer):
#     comment_author = UserDetailsSerializer()
#     class Meta:
#         model = Comment
#         fields = '__all__'
#         read_only_fields = ('board',)

# class CommentSerializer(serializers.ModelSerializer):
#     comment_author = serializers.CharField(source='comment_author.username', read_only=True)

#     class Meta:
#         model = Comment
#         fields = '__all__'
#         read_only_fields = ('board',)

#     def create(self, validated_data):
#         # 현재 로그인한 유저를 comment_author로 설정
#         validated_data['comment_author'] = self.context['request'].user
#         return super().create(validated_data)

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('board', 'author')





class BoardSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    # username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Board
        fields = '__all__'
        # read_only_fields = ('user', )