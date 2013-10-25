
"""Apply these patches to the PyXPCOM Mercurial repository (default branch)."""

def applicable(config):
    return config.mozVer >= 24.0 and config.mozVer <= 24.99 and \
           config.patch_target == "pyxpcom"

def patch_args(config):
    # patch $topsrcdir/extensions/python
    return ['-p1']

