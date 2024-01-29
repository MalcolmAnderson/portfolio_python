import tkinter as tk
import pom_tools as pom


import mba_logging as log
logger = log.logger_factory()
# log.logging.getLogger().setLevel(log.logging.DEBUG)
logger.info("pomodoro started")

# TODO Add a sound file to signify the end of a period
# TODO find a sound file for "TAKE A BREAK !!!" for end of a Work Period
# TODO find a sound file for "BACK TO WORK !!!" for end of a Break
# TODO find a sound file for "TAKE A LOOOOONG BREAK !!!" for end of a 4th Work Period


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
PRODUCTION = False # var is not actually used, but is a reminder for
# how to change from testing to production
if False:
    MIN_BREAK = 5 # 5 for prod, .1 for testing (6 seconds)
    MIN_LONG_BREAK = 20 # 20 for prod, .3 for testing (18 seconds)
    MIN_WORK = 25 # 25 for prod, .2 for testing (12 seconds)
else:
    MIN_BREAK = .1 # 5 for prod, .1 for testing (6 seconds)
    MIN_LONG_BREAK = .3 # 20 for prod, .3 for testing (18 seconds)
    MIN_WORK = .2 # 25 for prod, .2 for testing (12 seconds)

button_font = (FONT_NAME, 24, "bold")
title_font = (FONT_NAME, 64, "bold")
check_mark_font = (FONT_NAME, 64, "bold")
label_x_pad = 20
label_y_pad = 20
reps = 0
timer = None

# items that have to be declared in a global manner to work with the __main__ setup
# window = tk.Tk() # window needs to be initialized
# canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_function():
    logger.info("reset button clicked")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="0:00")
    lb_title.config(text = "Timer")
    global reps
    reps = 0
    lb_check_marks.config(text = "")
        
# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_function():
    # TODO return value from translater maybe should be an enum
    logger.info(f"start button clicked")
    global reps
    reps += 1
    pom_type = pom.translate_reps_to_break_or_work(reps)
    if pom_type == "Work": 
        lb_title.config(text="WORK ", fg=GREEN)
        count = MIN_WORK * 60
    else:
        if pom_type == "Long Break":
            count = MIN_LONG_BREAK * 60
            lb_title.config(text="BREAK", fg=RED)
        else:
            count = MIN_BREAK * 60
            lb_title.config(text="BREAK", fg=PINK)
    logger.info(f"pom number: {reps}, pom type: {pom_type}, pom seconds: {count}")
    count_down(count)
    

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count = int(count)
    time_text = pom.convert_seconds_to_time_string(count)
    canvas.itemconfig(timer_text, text=time_text)
    logger.debug(time_text, reps)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        lb_title.config(text = "Timer", fg=GREEN)
        if reps % 2 == 1: 
            pom_text = pom.get_check_marks(reps)
            lb_check_marks.config(text = pom_text)
        

# ---------------------------- UI SETUP ------------------------------- #

#def main():
window = tk.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="pom_tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="0:00", fill="white")
canvas.itemconfig(timer_text, font=(FONT_NAME, 35, "bold"))
canvas.grid(column=2, row=2)


lb_title = tk.Label(text="Timer", font=title_font, 
                    padx = label_x_pad, pady=label_y_pad, 
                    bg=YELLOW, fg=GREEN )
lb_title.grid(column=2, row=1)

lb_check_marks = tk.Label(text="", font=check_mark_font, 
                            padx = label_x_pad , pady=label_y_pad, 
                            bg=YELLOW, fg=GREEN )
lb_check_marks.grid(column=2, row=4)

bn_start = tk.Button(text="Start", command=start_function)
                            #highlightthickness=0 )
bn_start.grid(column=1, row=3)

bn_reset = tk.Button(text="Reset", command=reset_function)
                            #highlightthickness=0, bg=YELLOW )
bn_reset.grid(column=3, row=3)


window.mainloop()

logger.info("pomodoro ended")



# def main():
#     pass


#if __name__ == "__main__":
#     logger.info("pomodoro started")
#     logger.debug("testing debug and level changes")
#     main()
#     logger.info("pomodoro ended")
