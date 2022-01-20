
def midfield_combo_check(dict_object):    
    center_mid = 'CM'
    defensive_mid = 'DM'
    attacking_mid = 'AMC'

    if defensive_mid in dict_object:
        if center_mid in dict_object:
            if attacking_mid in dict_object:
                print("You have all of the positions in midfield.")
                midfield_combo = 'All'
            else:
                print("You have DMs and CMs in your squad.")
                midfield_combo = 'DMs and CMs'
        else:
            if defensive_mid and attacking_mid in dict_object:
                print("You have DMs and AMCs in your squad.")
                midfield_combo = 'DMs and AMCs'
            else:
                print("You only have DMs in your squad.")
                midfield_combo = 'DMs'
    else:
        if center_mid in dict_object:
            if attacking_mid in dict_object:
                print("You have CMs and AMCs in your squad.")
                midfield_combo = 'CMs and AMCs'
            else:
                print("You only have CMs in your squad.")
                midfield_combo = 'CMs'
        else:
            if attacking_mid in dict_object:
                print("You only have AMCs")
                midfield_combo = 'AMCs'
            else:
                print("You do not have a midfield. No sensible recommendation can be made.")
                midfield_combo = 'Nothing'

    return midfield_combo

def even_more_concise(dict_object):
    "'Removes any unpopulated positions from the chart.'"

    if dict_object['WB'] == 0:
        del dict_object['WB']
            
    if dict_object['FB'] == 0:
        del dict_object['FB']

    if dict_object['WM'] == 0:
        del dict_object['WM']

    if dict_object['AW'] == 0:
        del dict_object['AW']

    if dict_object['ST'] == 0:
        del dict_object['ST']

    return dict_object

def dominant_midfield_position(midfield_combo, dict_object):
    "'Checks which midfield position has the most players available to it.'"

    if midfield_combo == 'All':
        if dict_object['CM'] > dict_object['DM']:
            if dict_object['CM'] > dict_object['AMC']:
                position = 'CM'
            elif dict_object['CM'] == dict_object['AMC']:
                position = 'CM and AMC'
        elif dict_object['DM'] > dict_object['CM']:
            if dict_object['DM'] > dict_object['AMC']:
                position = 'DM'
            elif dict_object['DM'] == dict_object['AMC']:
                position = 'DM and AMC'
            else:
                position = 'AMC'
        elif dict_object['CM'] == dict_object['DM']:
            if dict_object['AMC'] > dict_object['CM']:
                position = 'AMC'
            elif dict_object['AMC'] == dict_object['CM']:
                position = 'None'
            elif dict_object['AMC'] < dict_object['CM']:
                    position = 'CM and DM'

    if midfield_combo == 'DMs and CMs':
        if dict_object['DM'] > dict_object['CM']:
            position = 'DM'
        elif dict_object['DM'] < dict_object['CM']:
            position = 'CM'
        elif dict_object['DM'] == dict_object['CM']:
            position = 'Both DM and CM'

    if midfield_combo == 'DMs and AMCs':
        if dict_object['DM'] > dict_object['AMC']:
            position = 'DM'
        elif dict_object['DM'] < dict_object['AMC']:
            position = 'AMC'
        elif dict_object['DM'] == dict_object['AMC']:
            position = 'Both DM and AMC'

    if midfield_combo == 'CMs and AMCs':
        if dict_object['CM'] > dict_object['AMC']:
            position = 'CM'
        elif dict_object['CM'] < dict_object['AMC']:
            position = 'AMC'
        elif dict_object['CM'] == dict_object['AMC']:
            position = 'Both CM and AMC'

    if midfield_combo == 'CMs' or midfield_combo == 'DMs' or midfield_combo == 'AMCs' or midfield_combo == 'Nothing':
        position = f'{midfield_combo}'

    return position