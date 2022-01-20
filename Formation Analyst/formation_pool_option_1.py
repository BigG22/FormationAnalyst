"'Module that stores the list of formations possible, when using a wide 4 at the back system, with Wide Midfielders.'"

import midfield_combo_checker

cm_only = [
    {'four four two wide': {'CB': 2, 'FB': 2, 'CM': 2, 'WM': 2, 'ST': 2}},
    {'four five one wide': {'CB': 2, 'FB': 2, 'CM': 3, 'WM': 2, 'ST': 1}},
]

dm_only = [
    {'four four two 2dm wide': {'CB': 2, 'FB': 2, 'DM': 2, 'WM': 2, 'ST': 2}},
]

cm_amc = [
    {'four four one one wide': {'CB': 2, 'FB': 2, 'CM': 2, 'WM': 2, 'AMC': 1, 'ST': 1}},
]

dm_amc = [
    {'four four one one 2dm wide': {'CB': 2, 'FB': 2, 'DM': 2, 'WM': 2, 'AMC': 1, 'ST': 1}},
    {'four five one zero 2dm wide': {'CB': 2, 'FB': 2, 'DM': 2, 'WM': 2, 'AMC': 1}}
]

dm_cm = [
    {'four one three two wide': {'CB': 2, 'FB': 2, 'DM': 1, 'CM': 1, 'WM': 2, 'ST': 2}},
    {'four one four one wide': {'CB': 2, 'FB': 2, 'DM': 1, 'CM': 2, 'WM': 2, 'ST': 1}},
    {'four five one 2dm wide': {'CB': 2, 'FB': 2, 'DM': 2, 'CM': 1, 'WM': 2, 'ST': 1}},
]