import requests
url = "https://moralfoundations.org/wp-content/uploads/files/downloads/moral%20foundations%20dictionary.dic"
def read_dicts():
    r = requests.get(url)
    content = r.text 
    lines = content.split('\n')
    groups = {}
    codes = {}
    reading_groups = False

    for line in lines:
        line_ = ' '.join(line.split())
        if not line_: continue
        if line_.startswith('%'):
            reading_groups = not reading_groups
        else:
            line__ = line.split()
            if reading_groups:
                groups[line__[0]] = line__[1]
            else:
                codes[line__[0]] = ','.join(line__[1:])
    return (groups, codes)
