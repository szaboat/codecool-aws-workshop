import requests
import json
from django.template.response import TemplateResponse
from django.core.cache import cache

def home(request):

    posts = cache.get('posts')
    if not posts:
        response = requests.get('https://jsonplaceholder.typicode.com/posts')
        posts = json.loads(response.content)
        cache.set('posts', posts, 30)

    return TemplateResponse(request, 'posts.html', context={'posts': posts})
