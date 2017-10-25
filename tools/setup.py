import os


def setup(root_path, args):
    """
    Add/Remove shortcut to autostart

    `python defender.py install` : add script to autostart
    `python defender.py uninstall` : remove script from autostart

    :param args:
    :return:
    """
    home = os.environ["HOME"]
    name = "py.eyes.defender"
    comment = "Helper to control time for rest"
    command = "{0}/defender.py".format(root_path)

    # path to autostart
    dr = home + "/.config/autostart/"
    if not os.path.exists(dr):
        os.makedirs(dr)
    file = dr + name.lower() + ".desktop"

    # set logging
    if len(args) == 3 and args[2] == 'log':
        command += " > " + root_path + "/eyes.log"

    operation = args[1]
    if operation == "install":

        launcher = ["[Desktop Entry]", "Name=", "Comment=", "Exec=",
                    "Type=Application", "Terminal=false", "StartupNotify=false"]
        if not os.path.exists(file):
            with open(file, "wt") as out:
                for l in launcher:
                    l = l + name if l == "Name=" else l
                    l = l + comment if l == "Comment=" else l
                    l = l + command if l == "Exec=" else l
                    out.write(l + "\n")
            print("Eyes.Defender added to autostart.")
        else:
            print("Eyes.Defender exists in autostart.")

    elif operation == "uninstall":

        if os.path.exists(file):
            os.unlink(file)
            print("Eyes.Defender removed from autostart.")
        else:
            print("Eyes.Defender does not exist in autostart.")

    return True
