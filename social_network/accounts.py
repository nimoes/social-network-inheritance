class User(object):
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        
        self.following = []
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def get_timeline(self):
        allposts = []
        for eachuser in self.following:
            for eachpost in eachuser.posts:
                allposts.append(eachpost)
        
        return sorted(allposts, key=lambda eachpost:eachpost.timestamp)

    def follow(self, other):
        self.following.append(other)