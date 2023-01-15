# Util to store Github Repos User 
class Repos():
    def __init__(self,repos_data) -> None:
        self.name = repos_data['name']
        self.desc = repos_data['description']
        self.language = repos_data['language']
        self.url = repos_data['html_url']

# Util to store Github User 
class Profile():
    def __init__(self,user_data) -> None:
        self.name = user_data['name']
        self.bio = user_data['bio']
        self.url = user_data['html_url']
        self.img_url = user_data['avatar_url']
        self.company = user_data['company']
        self.location = user_data['location']
        self.twitter = user_data['twitter_username']
        self.public_repos = user_data['public_repos']