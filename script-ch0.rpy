label ch0_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

    s "[player], wait up!"
    "I hear a familliar voice supposedly running towards me."
    "I can't exactly remember who that voice belongs to.."
    show sayori 1p at t11 zorder 2
    s "Haaahhh...haaahhh..."
    "Oh, it's Sayori. A childhood friend."
    $ s_name = "Sayori"
    s 1a "Thanks for stopping."
    mc "No problem."
    "It's been a while since I talked with Sayori. Might as well catch up."
    mc "So, how are you?"
    s "Good, how are you?"
    mc "Fine."
    "There's an awkward silence."
    s 1b "Have you looked at any clubs yet?"
    mc "Yes, I have."
    s "Oooh! Which ones?"
    mc "It's a suprise..."
    s 1n "Ooh! A suprise!"
    "The suprise is that I'm joining the Literature Club sometime this week."
    "Sayori likes suprises, as long as they aren't too scary."
    "We arrive at the school and I say goodbye to Sayori until the end of the school day."
    stop music fadeout 2.0
    scene bg corridor
    with dissolve_scene_full
    play music t2
    play sound mod_sfx_1
    "As class finishes, I hear a familliar voice."
    show sayori 1a at t11 zorder 2
    s "[player]?"
    mc "Sayori?"
    mc "Don't you have a club?"
    s "Yeah, but they aren't meeting today."
    mc "Oh."
    mc "Why are you here?"
    s 1c "I want to ask you something."
    mc "Okay.."
    "I say with a confused expression on my face."
    s 1b "Will you walk home with me?"
    mc "Sure."
    s 1q "Yay!"
    s 1a "Let's go!"
    "Sayori practically drags me out of the classroom while humming a tune."
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2
    "As we approach our houses we wave to each other."
    stop music fadeout 2.0
    scene bg mod_6a
    with dissolve_scene_full
    play music t8
    "As I enter my home, I'm greeted by my mother who is in the living room watching TV."
    mo "Welcome home, [player]! Who were you waving to?"
    mc "Just Sayori."
    mo "Oh! It's been a while since I've seen her, is she doing well?"
    mc "Yeah, I think."
    mo "That's great to hear, I'll have dinner ready around 5:30."
    mc "Okay."
    "I make my way to my bedroom."
    stop music fadeout 2.0
    scene bg bedroom
    with dissolve_scene_full
    play music t8
    "I sit down at my desk and tun on my computer."
    "I then decided to just watch some videos online."
    return
