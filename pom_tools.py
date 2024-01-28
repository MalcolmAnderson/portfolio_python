def translate_reps_to_break_or_work(reps):
    if reps % 2 == 1:
        return "Work"
    else:
        return "Long Break"