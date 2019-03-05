""" Write a Python program to access and print a URL's content to the console.  """

# getting function and classes which helps in opening URLs
import urllib.request

# get access/open to the url
webUrl = urllib.request.urlopen("https://google.com")

# reading content
content = webUrl.read()

# display content on console
print(content)
