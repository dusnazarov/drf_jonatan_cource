from rest_framework import serializers
from .models import Post



# class PostSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(max_length=50)
#     content = serializers.CharField()
#     created = serializers.DateTimeField(read_only=True)


"""
    >>> from posts.models import Post
    >>> from posts.serializers import PostSerializer
    >>> from rest_framework.renderers import JSONRenderer
    
    >>> new_post = Post(title='Learn DRF', content='Basics of DRF')
    >>> new_post.save()
    >>> serializer=PostSerializer(instance=new_post)
    >>> serializer.data
    {'id': 3, 'title': 'Learn DRF', 'content': 'Basics of DRF', 'created': '2023-09-20T10:07:23.591600Z'}
    
    >>> json_data = JSONRenderer().render(serializer.data)
    >>> json_data
    b'{"id":3,"title":"Learn DRF","content":"Basics of DRF","created":"2023-09-20T10:07:23.591600Z"}'
  
    >>> import io
    >>> stream=io.BytesIO(json_data)
    >>> from rest_framework.parsers import JSONParser
    >>> dict_data=JSONParser().parse(stream)
    >>> dict_data
    {'id': 3, 'title': 'Learn DRF', 'content': 'Basics of DRF', 'created': '2023-09-20T10:07:23.591600Z'}


""" 


# //////////////////

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields = ["id", "title", "content", "created"]
    
