import sys
import webbrowser

URL = 'https://automatetheboringstuff.com/2e/chapter'

if len(sys.argv) > 1:
    chapter = sys.argv[1]
else:
    chapter = '1'

webbrowser.open(URL + chapter)