"'Module that stores the list of formations possible, when using a narrow 5 at the back system, with Wingbacks.'"

import midfield_combo_checker

dm_cm = [
    {'five one three one': {'CB': 3, 'WB': 2, 'DM': 1, 'CM': 3, 'ST': 1}},
    {'five two two one dm': {'CB': 3, 'WB': 2, 'DM': 2, 'CM': 2, 'ST': 1}},
    {'five three two dm wb': {'CB': 3, 'WB': 2, 'DM': 1, 'CM': 2, 'ST': 2}},
]

dm_cm_amc = [
    {'five four one wb': {'CB': 3, 'WB': 2, 'DM': 1, 'CM': 2, 'AMC': 1, 'ST': 1}}
]

cm_amc = [
    {'five two one two': {'CB': 3, 'WB': 2, 'CM': 2, 'AMC': 1, 'ST': 2}},
    {'five two two one wb': {'CB': 3, 'WB': 2, 'CM': 2, 'AMC': 2, 'ST': 1}}
]

dm_amc = [
    {'five two two one am': {'CB': 3, 'WB': 2, 'DM': 2, 'AMC': 2, 'ST': 1}}
]
