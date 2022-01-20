"'Module that stores the list of formations possible, when using a 3 at the back system.'"

import midfield_combo_checker

dm_cm = [
    {'three one four two wide': {'CB': 3, 'DM': 1, 'CM': 2, 'WM': 2, 'ST': 2}},
]

cm_amc = [
    {'three four one two wide': {'CB': 3, 'CM': 2, 'WM': 2, 'AMC': 1, 'ST': 2}},
    {'three four two one wide': {'CB': 3, 'CM': 2, 'WM': 2, 'AMC': 2, 'ST': 1}}
]

cm_only = [
    {'three four three wide': {'CB': 3, 'CM': 2, 'WM': 2, 'ST': 3}},
    {'three five two wide': {'CB': 3, 'CM': 3, 'WM': 2, 'ST': 2}}
]
