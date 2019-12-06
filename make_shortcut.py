import sys
from pyshortcuts import make_shortcut


icon_name = "Make_Logo"
if sys.argv[0] is not None:
    icon_name = sys.argv[0]

make_shortcut('file.py', name=icon_name, desktop=True)