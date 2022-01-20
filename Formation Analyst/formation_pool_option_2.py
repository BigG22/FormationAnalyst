"'Module that stores the list of formations possible, when using a narrow 4 at the back system.'"

import midfield_combo_checker

dm_cm_amc = [
    {'four four two diamond narrow': {'CB': 2, 'FB': 2, 'DM': 1, 'CM': 2, 'AMC': 1, 'ST': 2}},
    {'four one three one one': {'CB': 2, 'FB': 2, 'DM': 1, 'CM': 3, 'AMC': 1, 'ST': 1}}
]

dm_cm = [
    {'four one three two narrow': {'CB': 2, 'FB': 2, 'DM': 1, 'CM': 3, 'ST': 2}},
    {'four two two two dm narrow': {'CB': 2, 'FB': 2, 'DM': 2, 'CM': 2, 'ST': 2}},
    {'four three three dm narrow': {'CB': 2, 'FB': 2, 'DM': 1, 'CM': 2, 'ST': 3}}
]

dm_amc = [
    {'four two two two dm_am narrow': {'CB': 2, 'FB': 2, 'DM': 2, 'AMC': 2, 'ST': 2}},
    {'four two three one dm_am narrow': {'CB': 2, 'FB': 2, 'DM': 2, 'AMC': 3, 'ST': 1}},
    {'four three one two narrow': {'CB': 2, 'FB': 2, 'DM': 3, 'AMC': 1, 'ST':2}},
    {'four three two one narrow': {'CB': 2, 'FB': 2, 'DM': 3, 'AMC': 2, 'ST': 1}},
    {'four three three am narrow': {'CB': 2, 'FB': 2, 'DM': 1, 'AMC': 2, 'ST': 3}}
]

cm_amc = [
    {'four two three one narrow': {'CB': 2, 'FB': 2, 'CM': 2, 'AMC': 3, 'ST': 1}}
]