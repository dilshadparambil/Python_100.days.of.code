import requests

class Post:
    def __init__(self):
        blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
        self.response = requests.get(blog_url)
        self.blogs = self.response.json()


    def get_data(self,post_id):
        for contents in self.blogs:
            if contents["id"]==post_id:
                post_title=contents["title"]
                subtitle=contents["subtitle"]
                body=contents["body"]
                return post_title, subtitle, body

        return None