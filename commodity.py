# The idea is that each commodity
# will have an accessibility default, 0 if not
# Technologies will just be transforms on the commodity
# types. So a technology will add a hashmap or improve an existing one
# potentially requiring more steps in the chain but providing higher quality
# or higher accessibility (which is roughly the speed of harvest)


commodity_types = {
    'food': {
        'type': 'necessity',
        'quality': 20,
        'accessibility': 30,
        'dependencies': {
            'workers': ['farmer'],
            'tools': []
        }
    },
    'regular clothing': {
        'type': 'necessity',
        'quality': 50,
        'accessibility': 20,
        'dependencies': {
            'workers': [],
            'tools': []
        }
    },
    'fancy clothing': {
        'type': 'luxury',
        'quality': 70,
        'accessibility': 80,
        'dependencies': {
            'workers': [],
            'tools': []
        }
    }
}
