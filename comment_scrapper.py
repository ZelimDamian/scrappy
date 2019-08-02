import json

from inscrawler import InsCrawler
from inscrawler.settings import override_settings


class Settings:
    def __init__(self):
        self.fetch_imgs = False
        self.fetch_comments = True
        self.fetch_likes_plays = False
        self.fetch_likers = False
        self.fetch_mentions = False
        self.fetch_hashtags = False


settings = Settings()

output_filepath = './results.json'
username = 'groznytv'
number = 3
full_posts = True
debug = True

override_settings(settings)

ins_crawler = InsCrawler(has_screen=debug)
results = ins_crawler.get_user_posts(username, number, full_posts)

out = json.dumps(results, ensure_ascii=False)

with open(output_filepath, "w", encoding="utf8") as f:
    f.write(out)
