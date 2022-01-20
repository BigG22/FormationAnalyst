"'Module that stores the list of formations possible, when using a wide 4 at the back system, with Attacking Wingers.'"

import midfield_combo_checker

dm_amc = [
    {'four two three one dm_am wide': {'CB': 2, 'FB': 2, 'DM': 2, 'AMC': 1, 'AW': 2, 'ST': 1}},
    {'four_two_four_zero_wide': {'CB': 2, 'FB': 2, 'DM': 2, 'AMC': 2, 'AW': 2}}
]

cm_amc = [
    {'four two three one wide': {'CB': 2, 'FB': 2, 'CM': 2, 'AMC': 1, 'AW': 2, 'ST': 1}},
]

cm_only = [
    {'four two four wide': {'CB': 2, 'FB': 2, 'CM': 2, 'AW': 2, 'ST': 2}},
]

dm_cm = [
    {'four three three wide': {'CB': 2, 'FB': 2, 'DM': 1, 'CM': 2, 'AW': 2, 'ST': 1}}
]