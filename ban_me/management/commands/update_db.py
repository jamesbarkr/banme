from django.core.management.base import BaseCommand, CommandError
from ban_me.models import Post
from ban_me import get_posts
import time

class Command(BaseCommand):
    help = 'Updates the SQL db with recent posts from Reddit, ignoring things already in the db'

    def handle(self, *args, **options):
        print("Getting posts, this may take a while.")
        posts = get_posts.get()
        for post in posts:
            if len(Post.objects.filter(title=post)) == 0: # checks if the post already exists
                post_model = Post(title=post) # if it does not, instantiate and save a new model
                post_model.save()
            else:
                continue
        self.stdout.write(self.style.SUCCESS("Posts retrieved and archived")) # return "success" message
