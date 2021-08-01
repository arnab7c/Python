def CheerLeader():
    """
    :return:
    """
    word = input ( "Give me a word >>> " )
    level = int ( input ( "What is the enthusiasm level [1 to 10] ? " ) )

    for char in word:
        if char.lower () in [ 'a', 'e', 'i', 'o', 'u', 'f', 'h', 'l', 'm', 'n', 'r', 's', 'x' ]:
            prelude = "Give me an "
        else:
            prelude = "Give me a "
        print ( prelude + char.upper () + " ??? " + char.upper () + " !!!" )

    print ( "and, What's the spell ??? " )

    for x in range ( level ):
        print ( "!!! " + word.upper () + " !!!" )


CheerLeader ()
