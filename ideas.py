from collections import defaultdict
import re


expressions = {}
expressions['name'] = re.compile("^(?:name\s?:?)\s*([\w\s]*)$", re.I)
expressions['stat'] = re.compile("^[\s\*\#]*([\w]+)[\s\:]+(\d+)", re.I)


def load(source):
    character = defaultdict(int)
    for line in source:
        i = expressions['name'].match(line)
        if i:
            if 'name' in character:
                character['name'].append(i.group(1).strip())
            else:
                character['name'] = [i.group(1).strip()]
            continue
        i = expressions['stat'].match(line)
        print i
        if i:
            character[i.group(1).strip()] = int(i.group(2).strip())
    return character

