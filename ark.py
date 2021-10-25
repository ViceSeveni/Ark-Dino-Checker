import webbrowser
import sys

class dino():
    def __init__(self, dino):
        self.dino = dino
        
    def wiki(self):
        url ='https://ark.fandom.com/wiki/' + self.dino
        webbrowser.open(url)

def dex():
    if len(sys.argv) > 1:
        request = sys.argv[1]
        
    if len(sys.argv) < 2:
        request = input('Enter a Dino: ')
        
    entry = dino(request)
    try:
        entry.wiki()
    except:
        print('Something went wrong, try again!')
    
if __name__ == "__main__":
    dex()
