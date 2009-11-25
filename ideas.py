from collections import defaultdict
from UserDict import DictMixin
import re

class World(object):
    def __init__(self, defaults=None, filters=None):
        self.store = {}
        self.defaults = defaults or {}
        self.filters = filters or []

    def __len__(self):
        seen = []
        for i in self.store.values():
            if i not in seen:
                seen.append(i)
        return len(seen)

    def __getitem__(self, key):
        return self.store[key]
    
    def __contains__(self, item):
        return item in self.store

    def load(self, source):
        char = Character(source, self.defaults, self.filters)
        for n in char['name']:
            self.store[n] = char


class Character(DictMixin):
    expressions = {}

    def __init__(self, source, defaults=None, filters=None):
        self.filters = filters or []
        self.store = {}
        self.defaults = defaults or {}
        methods = (self._catch_blank, self._catch_name, self._catch_int_stat, self._catch_stat)
        for line in source:
            if line.strip():
                for m in methods:
                    if m(line):
                        break
                else:
                    print line.strip()

    def _catch_blank(self, line):
        return not line.strip()

    def _catch_name(self, line):
        if 'name' not in self.expressions:
            self.expressions['name'] = re.compile("^(?:name\s?)[\s:]*([\w\s]+)$", re.I)
        i = self.expressions['name'].match(line)
        if i:
            self.store.setdefault('name', []).append(i.group(1).strip())
        return i

    def _catch_int_stat(self, line):
        if 'intstat' not in self.expressions:
            self.expressions['intstat'] = re.compile("^[\s\*\#]*([\w\s\(\)]+)\s*:*\s*(\d+)", re.I)
        i = self.expressions['intstat'].match(line)
        if i:
            self[i.group(1)] = int(i.group(2).strip())
        return i

    def _catch_stat(self, line):
        if 'stat' not in self.expressions:
            self.expressions['stat'] = re.compile("^[\s\*\#]*([\w\s\(\)]+)\s*:*\s*([\d\s\w\(\)]+)", re.I)
        i = self.expressions['stat'].match(line)
        if i:
            self[i.group(1)] = i.group(2).strip()
        return i
    
    def __contains__(self, item):
        return item in self.store or item in self.defaults

    def __setitem__(self, key, value):
        self.store[key.strip().lower()] = value

    def __delitem__(self, key):
        del self.store[key]

    def __getitem__(self, key):
        key = key.lower().strip()
        if key in self.store:
            value = self.store[key]
        elif key in self.defaults:
            value = self.defaults[key]
        else:
            return 0
        for f in self.filters:
            value = f(self, value)
        return value
