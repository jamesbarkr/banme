from django.core.management.base import BaseCommand, CommandError
from ban_me.models import Post
from ban_me.get_posts import get
import time

class Command(BaseCommand):
    help = 'Updates the SQL db with recent posts from Reddit'

    def handle(self, *args, **options):
        print("Getting posts, this may take a while.")
        posts = get()
        self.stdout.write(self.style.SUCCESS("Posts retrieved"))
