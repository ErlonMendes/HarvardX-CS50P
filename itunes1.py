# https://itunes.apple.com/search?entity=song&limit=1&term=weeser
# Um arquivo 1.txt será baixado em Downloads
import requests
import sys

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())
