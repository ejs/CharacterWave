import ideas


defaults = {'academics': -3, 'computer': -3, 'init':'dex comp'}


def filter(self, rep, key):
    if key == "defence":
        return min(self['dex'], self['wits'])
    if type(rep) == str:
        print 'str'
        try:
            return sum((self[i] if i in self else int(i)) for i in rep.split())
        except Exception, e:
            print e
            return rep
    else:
        return rep


def test_example_filter():
    assert filter({'dex':2, 'wits':3}, 0, 'defence') == 2
    assert filter({}, 3, 'pie') == 3
    assert filter({'dex':2, 'str':2}, 'dex str', 'speed') == 4
    assert filter({'dex':2, 'str':2}, 'dex str 5', 'speed') == 9
    assert filter({'dex':2, 'str':2}, 'dex str -3', 'speed') == 1


def test_character():
    char = ideas.Character(open('mel.txt'))
    assert len(char['name']) == 3
    assert 'Mel' in char['name']
    assert char['Int'] == 2
    assert char['int'] == 2
    assert char['Dex'] == 3
    assert char['Man'] == 2
    assert char['Academics'] == 1
    assert char['Craft'] == 1
    assert char['attack'] == 'dex firearms pistol'
    assert char['Monky'] == 0


def test_world():
    world = ideas.World()
    world.load(open('mel.txt'))
    assert len(world) == 1
    assert 'Mel' in world
    assert 'Melba Brandon' in world
    assert world['Mel'] is world['Melba Brandon']
    char = world['Mel']
    assert 'Mel' in char['name']
    assert char['Int'] == 2


def test_defaults():
    char = ideas.Character(open('mel.txt'), defaults)
    assert char['int'] == 2
    assert char['computer'] == -3
    assert char['init'] == 'dex comp'


def test_world_defaults():
    world = ideas.World(defaults)
    world.load(open('mel.txt'))
    char = world['Mel']
    assert char['int'] == 2
    assert char['computer'] == -3
    assert char['init'] == 'dex comp'


def test_filter():
    filters = [filter]
    char = ideas.Character(open('mel.txt'), defaults, filters)
    assert char['computer'] == -3
    assert char['int'] == 2
    assert char['attack'] == 6
    assert char['init'] == 6
    assert char['defence'] == 2


def test_world_filters():
    filters = [filter]
    world = ideas.World(defaults, filters)
    world.load(open('mel.txt'))
    char = world['Mel']
    assert char['int'] == 2
    assert char['attack'] == 6
    assert char['computer'] == -3
    assert char['init'] == 6
