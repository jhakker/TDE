#!/usr/bin/env python3

import subprocess
import os
# import sys

terminal_emu_cmd = "kitty"
editor_cmd = "vim"
tde_src_dir = os.path.join(os.environ["HOME"], "devel/tde")
tde_vim_script = "tde.vim"

subprocess.run([
    terminal_emu_cmd,
    editor_cmd,
    "-S",
    os.path.join(tde_src_dir, tde_vim_script)
    ],
    cwd = tde_src_dir
    )
