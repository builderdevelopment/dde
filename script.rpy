label start:

    $ anticheat = persistent.anticheat
    $ chapter = 0
    $ _dismiss_pause = config.developer


    $ s_name = "???"
    $ m_name = "Girl 3"
    $ n_name = "Girl 2"
    $ y_name = "Girl 1"
    $ mo_name = "Mom"

    $ quick_menu = True
    $ style.say_dialogue = style.normal
    $ in_sayori_kill = None
    $ allow_skipping = True
    $ config.allow_skipping = True


    if persistent.playthrough == 0:

        label pb:
            play music m1
            "This is a PUBLIC BETA release. Please note, things are very buggy and some things are subject to change."
            return

        call pb

        $ chapter = 0
        $ act = 1
        call ch0_main

        $ chapter = 1
        call ch1_main

        call poem

        call credits

label credits:
    play music credits
    "Thank you for playing."
    return
