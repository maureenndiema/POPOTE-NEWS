class Articles:
  '''
  Articles class to define Article objects
  '''

  def __init__(self, author, title, imageurl, publishedAt, url):
    self.author = author
    self.title = title
    self.imageurl =imageurl
    self.publishedAt = publishedAt
    self.url = url

class Breaking:
  '''
  Articles class to define Article objects
  '''
  def __init__(self, title, imageurl, url):
    self.title = title
    self.imageurl =imageurl
    self.url = url

class Keyword:
  '''
  Articles class to define Article objects
  '''

  def __init__(self, author, title, imageurl, publishedAt, url):
    self.author = author
    self.title = title
    self.imageurl =imageurl
    self.publishedAt = publishedAt
    self.url = url
