import pom_tools as pom

def t_odd_poms_should_be_work():
    actual = pom.translate_reps_to_break_or_work(5)
    assert actual == "Work"

def t_every_8th_pom_should_be_a_long_break():
    pass

def test_even_poms_execpt_8th_should_be_breaks():
    pass