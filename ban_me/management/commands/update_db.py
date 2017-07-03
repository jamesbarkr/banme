from django.core.management.base import BaseCommand, CommandError
from ban_me.models import Post
from ban_me import get_posts
import time

class Command(BaseCommand):
    help = 'Updates the SQL db with recent posts from Reddit'

    def handle(self, *args, **options):
        print("Getting posts, this may take a while.")
        posts = get_posts.get()
        for post in posts:
            if len(Post.objects.filter(title=post)) == 0:
                post_model = Post(title=post)
                post_model.save()
            else:
                continue
        self.stdout.write(self.style.SUCCESS("Posts retrieved and archived"))
