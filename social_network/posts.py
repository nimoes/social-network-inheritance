from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        if not timestamp:
            timestamp = datetime.now()
        self.timestamp = timestamp.strftime('%A, %b %d, %Y')

        self.user = None
        
    def set_user(self, user):
        self.user = user


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super(TextPost, self).__init__(text, timestamp)
        
    def __str__(self):
        return '@{} {}: "{}"\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.timestamp)


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        return '@{} {}: "{}"\n\t{}\n\t{}'.format(self.user.first_name, self.user.last_name, self.text, self.image_url, self.timestamp)


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return '@{} Checked In: "{}"\n\t{}, {}\n\t{}'.format(self.user.first_name, self.text, self.latitude, self.longitude, self.timestamp)