import ideas


def filter(self, rep, key):
    if key == "defence":
        return min(self['dex'], self['wits'])
    if type(rep) == str:
        try:
            return sum((self[i] if i in self else int(i)) for i in rep.split())
        except Exception, e:
            return rep
    else:
        return rep


if __name__ == '__main__':
    import sys

    defaults = ideas.Character(open('changeling_defaults'))
    world = ideas.World(defaults, [filter])
    world.load(open('mel.txt'))
    a = sys.argv[1]
    for section in a.split():
        print "%s(%i)"%(section, world['mel'][section]),
    print " = [%i]"%sum(world['mel'][i] for i in a.split())
