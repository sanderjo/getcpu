import os, platform, subprocess, re


def getcpu():
    # find the CPU name (which needs a different method per OS), and return it
    # emptry string if none found

    try:
        if platform.system() == "Windows":
            # creationflags=0x08000000 means "no pop-up windows"
            return subprocess.check_output("wmic cpu get name".split(),creationflags=0x08000000 ).strip().split("\n")[1]

        elif platform.system() == "Darwin":
            return subprocess.check_output(['sysctl', "-n", "machdep.cpu.brand_string"]).strip()

        elif platform.system() == "Linux":
            for myline in open("/proc/cpuinfo"):
                if myline.startswith(('model name')):
                    # Typical line:
                    # model name      : Intel(R) Xeon(R) CPU           E5335  @ 2.00GHz
                    return myline.split(":", 1)[1]	# get everything after the first ":"

    except:
        # An exception could happen due to a subprocess call
        pass

    # we couldn't determine the processor name, due to
    # an exception, or
    # not Windows, nor Darwin, nor Linux, so possibly BSD, SUN, ...
    return None


print getcpu()
