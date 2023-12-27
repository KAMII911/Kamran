import os,platform
os.system("git pull")
a=platform.architecture()[0]
if "64" in a:
    import soh
    KAMII.run()
elif "32" in a:
    import soh32
    KAMI32.run()