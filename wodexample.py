import ideas
import random


def roll(number, again):
    if number < 1:
        once = random.randint(1, 10)
        if once == 1:
            return [1], "botch"
        elif once == 10:
            return [10], 1
        else:
            return [once], "failure"
    result = []
    count = 0
    while count < number:
        once = random.randint(1, 10)
        result.append(once)
        if once < again:
            count += 1
    return result, sum(1 for i in result if i > 7) or "failure"


def filter(self, rep, key):
    if key == "defence":
        return min(self['dex'], self['wits'])
    if type(rep) == str:
        try:
            return sum((self[i] if i in self else int(i)) for i in rep.split())
        except Exception, e:
            return rep
    if rep == 0 and key not in self:
        try:
            return int(key)
        except:
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
    pool = sum(world['mel'][i] for i in a.split())
    sucesses, result = roll(pool, 10)
    print " = [%i = %s = %s]"%(pool, ' '.join("%i"%i for i in sucesses), result)
