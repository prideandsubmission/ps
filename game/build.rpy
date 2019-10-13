init python:
    # Declare two archives.
    build.archive("scripts", "all")
    build.archive("images", "all")

    # Put script files into the scripts archive.
    build.classify("game/**.rpyc", "scripts")
    build.classify("game/**.rpa",None)

    # Put images into the images archive.
    build.classify("game/**.jpg", "images")
    build.classify("game/**.png", "images")