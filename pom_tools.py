TWO_DIGIT_FORMAT_CODE = '%02d'
CHECK_MARK = "✔"


def translate_reps_to_break_or_work(reps):
    # odd reps are work poms
    # even reps are break poms
    # every 4th break is a long break
    if reps % 2 == 1:
        return "Work"
    else: # by definition, reps % 2 == 0 must be true for the else
        if reps % 8 == 0:
            return "Long Break"
        else: 
            return "Break"

def convert_seconds_to_time_string(seconds):
    minutes_string = str(seconds // 60)
    seconds_string = TWO_DIGIT_FORMAT_CODE % (seconds % 60)
    return minutes_string + ":" + seconds_string

def get_check_marks(reps):
    poms = (reps + 1) // 2
    pom_str = ""
    for i in range(poms):
        pom_str += CHECK_MARK
    return pom_str
