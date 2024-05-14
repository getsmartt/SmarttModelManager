import gc
import pprint
# Construct a graph cycle
a = 23764723

# Collecting now keeps the objects as uncollectable,
# but not garbage.
print()
print('Collecting...')
n = gc.collect()
print('Unreachable objects:', n)
print('Remaining Garbage:', end=' ')
pprint.pprint(gc.garbage)

# Ignore references from local variables in this module, global
# variables, and from the garbage collector's bookkeeping.
REFERRERS_TO_IGNORE = []


def find_referring_graphs(obj):
    print('Looking for references to {!r}'.format(obj))
    referrers = (r for r in gc.get_referrers(obj)
                 if r not in REFERRERS_TO_IGNORE)
    for ref in referrers:
        if isinstance(ref, dict):
            print("is dict") # An instance or other namespace dictionary
            for parent in find_referring_graphs(ref):
                yield parent


# Look for objects that refer to the objects in the graph.
print()
print('Clearing referrers:')

for ref in find_referring_graphs(a):
    print('Found referrer:', ref)
    ref.set_next(None)
    del ref  # remove reference so the node can be deleted
 # remove reference so the node can be deleted

# Clear references held by gc.garbage
print()
print('Clearing gc.garbage:')
del gc.garbage[:]

# Everything should have been freed this time
print()
print('Collecting...')
n = gc.collect()
print('Unreachable objects:', n)
print('Remaining Garbage:', end=' ')
pprint.pprint(gc.garbage)
