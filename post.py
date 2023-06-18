import requests


class Post:
    def __init__(self):
        self.url = "https://api.npoint.io/c790b4d5cab58020d391"
        self.response = requests.get(self.url)
        
        self.posts = self.response.json()
        
    def get_posts(self):
        return self.posts
    
    def get_a_post(self, post_id):
        for post in self.posts:
            if post["id"] == post_id:
                return post
        
