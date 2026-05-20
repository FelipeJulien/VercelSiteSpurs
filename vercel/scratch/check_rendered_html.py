import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from html.parser import HTMLParser
from django.test import Client
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'spurs_site.settings')
django.setup()

class HTMLTagChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.errors = []
        
    def handle_starttag(self, tag, attrs):
        # List of self-closing HTML5 tags
        if tag in ['img', 'input', 'br', 'hr', 'meta', 'link', 'col', 'source', 'embed', 'param']:
            return
        self.stack.append((tag, self.getpos()))
        
    def handle_endtag(self, tag):
        if tag in ['img', 'input', 'br', 'hr', 'meta', 'link', 'col', 'source', 'embed', 'param']:
            return
        if not self.stack:
            self.errors.append(f"Unexpected closing tag </{tag}> at line {self.getpos()[0]}, col {self.getpos()[1]}")
            return
        
        last_tag, last_pos = self.stack.pop()
        if last_tag != tag:
            self.errors.append(f"Mismatched closing tag </{tag}> at line {self.getpos()[0]} (expected </{last_tag}> which was opened at line {last_pos[0]})")
            # Push back to keep stack aligned if possible, or just log
            self.stack.append((last_tag, last_pos))

# Get rendered home page
c = Client()
r = c.get('/', HTTP_HOST='127.0.0.1')
html_content = r.content.decode('utf-8')

checker = HTMLTagChecker()
checker.feed(html_content)

print("--- HTML VALIDATION RESULTS ---")
if checker.errors:
    for err in checker.errors:
        print(err)
else:
    print("No tag mismatches found in rendered HTML!")

if checker.stack:
    print("\nTags left open at the end of the document:")
    for tag, pos in checker.stack:
        print(f"<{tag}> opened at line {pos[0]}, col {pos[1]}")
else:
    print("\nNo tags left open!")
