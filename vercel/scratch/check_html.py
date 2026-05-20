import re

def check_tags(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove Django template tags
    content_clean = re.sub(r'{%.*?%}', '', content)
    content_clean = re.sub(r'{{.*?}}', '', content_clean)
    content_clean = re.sub(r'{#.*?#}', '', content_clean, flags=re.DOTALL)
    
    stack = []
    # Match HTML tags
    tag_regex = re.compile(r'<(/?[a-zA-Z0-9:-]+)(?:\s+[^>]*)?>')
    
    for match in tag_regex.finditer(content_clean):
        tag = match.group(0)
        tag_name = match.group(1)
        
        # Skip self-closing tags
        if tag_name.lower() in ['img', 'input', 'br', 'hr', 'meta', 'link', 'col']:
            continue
            
        if tag_name.startswith('/'):
            name = tag_name[1:]
            if not stack:
                print(f"Error: Closed tag {tag_name} but stack was empty. Match: {tag}")
            else:
                last = stack.pop()
                if last != name:
                    print(f"Error: Closed tag {name} but expected {last}. Current Stack: {stack + [last]}. Match: {tag}")
        else:
            stack.append(tag_name)
            
    if stack:
        print(f"Error: Tags left open in stack at the end: {stack}")
    else:
        print("All tags matched perfectly!")

check_tags('templates/components/header.html')
