# stats.rpy
# Keeps track of and displays the stats for the DSE.
#
# To change styles, add a style block for the element you want
# preceded by "dse_stats_" down below

init -100 python:

    dse_stats = [ ]

    class __Stat(object):

        def __init__(self, name, var, default, max):
            self.name = name
            self.var = var
            self.default = default
            self.max = max

    def __init_stats():
        for s in dse_stats:
            setattr(store, s.var, s.default)

    config.start_callbacks.append(__init_stats)
    
    def register_stat(name, var, default, max):
        dse_stats.append(__Stat(name, var, default, max))

    def normalize_stats():
        for s in dse_stats:

            v = getattr(store, s.var)

            if v > s.max:
                v = s.max
            if v < 0:
                v = 0

            setattr(store, s.var, v)

    # Whenever a python statement is executed, we will ensure our stats
    # stay within range.
    config.python_callbacks.append(normalize_stats)
                  
                  
    # Function to save skills for New Game +, up to SKILL_SAVED_MAX,
    # if they are greater than what has already been saved.
    def save_skill(current_saved_value, new_skill_value):
        if (new_skill_value <= SKILL_SAVED_MAX):
            if (not current_saved_value):
                return new_skill_value
            else:
                if (current_saved_value < new_skill_value):
                    return new_skill_value
                else:
                    return current_saved_value
        else:
            return SKILL_SAVED_MAX
        
    def highest_stat():
        normalize_stats()
        
        highest_stat = 0
        highest_stat_name = ""

        for curr_stat in dse_stats:
            stat_value = getattr(store, curr_stat.var)
            if (stat_value >= highest_stat):
                highest_stat_name = curr_stat.name
                highest_stat = stat_value
        return highest_stat_name


# Here you can change the style of any elements in the Stats screen you want.
# As an example, here is a style defined for the label text to make sure it is not bold.
style dse_stats_label_text:
    bold False

screen display_stats(name=True, bar=True, value=True, max=True):
    $ dse_stat_length = len(dse_stats)
    frame:
        style_group "dse_stats"        
        yalign 0.0
        xalign 0.5

        vbox:
            yalign 0.0
            xalign 0.5
            label "Statistics" xalign 0.5

            grid 3 dse_stat_length:
                xalign 0.5
                yalign 0.5
                spacing 5
                
                for s in dse_stats:
                    $ v = getattr(store, s.var)

                    if name:
                        label s.name
                    
                    if bar:
                        bar value v range s.max xmaximum 150 xalign 0.0
                        
                    if value and max:
                        label ("%d/%d" % (v, s.max)) xalign 1.0
                    elif value:
                        label ("%d" % (v,)) xalign 1.0
                    elif max:
                        label ("%d" % (max,)) xalign 1.0
