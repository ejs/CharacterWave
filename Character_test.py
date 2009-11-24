import ideas


def test_load():
    char = ideas.load(open('mel.txt'))
    print char
    assert len(char['name']) == 3
    assert 'Mel' in char['name']
    assert char['Int'] == 2
    assert char['Dex'] == 3
    assert char['Man'] == 2
    assert char['Academics'] == 1
    assert char['Craft'] == 1
    assert char['Monky'] == 0
