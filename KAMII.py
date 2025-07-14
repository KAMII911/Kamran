import os,platform
os.system("git pull")
a=platform.architecture()[0]
if "64" in a:
    import file
    file.run()
elif "32" in a:
    import file32
    file32.run()
