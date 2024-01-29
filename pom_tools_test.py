import pom_tools as pom

def t_odd_poms_should_be_work():
    actual = pom.translate_reps_to_break_or_work(5)
    assert actual == "Work"

def t_every_8th_pom_should_be_a_long_break():
    actual = pom.translate_reps_to_break_or_work(8)
    assert actual == "Long Break"

def t_even_poms_execpt_8th_should_be_breaks():
    actual = pom.translate_reps_to_break_or_work(16)
    assert actual == "Long Break"
    actual = pom.translate_reps_to_break_or_work(12)
    assert actual == "Break"

def t_305_seconds_should_be_5_05():
    actual = pom.convert_seconds_to_time_string(305)
    expected = "5:05"
    assert actual == expected

def t_5_seconds_should_be_0_05():
    actual = pom.convert_seconds_to_time_string(5)
    expected = "0:05"
    assert actual == expected

def t_3_poms_should_be_2_checks():
    actual = pom.get_check_marks(3)
    expected = "✔✔"
    assert actual == expected