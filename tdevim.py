#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# File              : tdevim.py
# Author            : Jörg Bakker <jorg@hakker.de>
# Date              : 2020-01-02
# Last Modified Date: 2020-01-02
# Last Modified By  : Jörg Bakker <jorg@hakker.de>
# interaction between vim and terminal

import vim
# import libtmux
import subprocess
import re
import os

errlist = []
currerr = 0
cellstr = "# %%"
bash_cmd = "bash"
# tde_dir = os.path.join(os.environ["HOME"], "/devel/tde")
tde_dir = "/home/jorg/devel/tde"
# init_anaconda = os.path.join(tde_dir, "init_anaconda.sh")
tde_default_shell_cmd = "fish"
# tde_default_shell_cmd = "xonsh"
# tde_ipython2_cmd = "ipython"
# tde_ipython2_init = "init_ipython2.py"
# tde_ipython3_cmd = "ipython3"
# tde_ipython3_init = "init_ipython3.py"
# tde_session = "tde"
# tde_xon = "xon"

###############################################################################
# Vim related utility functions

def vim_close_all_buffers():
    vim.command(":1,$bd")


def vim_save_session_to_file(filename):
    vim.command(":mksession! " + filename)


def vim_load_session_from_file(filename):
    vim.command(":source " + filename)


###############################################################################
# Session interface

# global session related configs
session_dir = os.path.join(os.environ["HOME"], ".tde/sessions")
vim_session_dir = os.path.join(session_dir, "vim")
console_session_dir = os.path.join(session_dir, "console")
default_session_file = os.path.join(session_dir, "default") 

def get_default_session():
    if os.path.exists(default_session_file):
        with open(default_session_file) as f:
            return f.readline().strip()
    return None


# def save_session(session_name=get_default_session()):
def save_session(*argv):
    session_name = get_default_session()
    if len(argv) == 1:
        session_name = argv[0]
    # save vim session
    if session_name and os.path.exists(os.path.join(vim_session_dir, session_name)):
        vim_save_session_to_file(os.path.join(vim_session_dir, session_name))
        with open(default_session_file, "w") as f:
            f.write(session_name)
    # save console session


# def open_session(session_name=get_default_session()):
def open_session(*argv):
    session_name = get_default_session()
    if len(argv) == 1:
        session_name = argv[0]
    if session_name and session_name != get_default_session():
        close_session()
    # load vim session
    if session_name and os.path.exists(os.path.join(vim_session_dir, session_name)):
        vim_load_session_from_file(os.path.join(vim_session_dir, session_name))
        with open(default_session_file, "w") as f:
            f.write(session_name)
    # load console session


def close_session():
    session_name = get_default_session()
    if session_name and os.path.exists(os.path.join(vim_session_dir, session_name)):
        vim_close_all_buffers()
        save_session()
        if os.path.exists(default_session_file):
            os.remove(default_session_file)


###############################################################################
# Console component IPC interface

# def tmux_cmd(cmd):
#     libtmux.Server().cmd(cmd)
#     # libtmux.Server().cmd("source-file " + os.path.join(tde_dir, "tmux.conf"))


# def get_session():
#     pass
#     # server = libtmux.Server()
#     # return server.find_where({"session_name": tde_session})


def get_tde_window():
    pass
    # session = get_session()
    # return session.find_where({"window_name": tde_tde})


def get_console():
    pass
    # tde_window = get_tde_window()
    # if len(tde_window.panes) > 1:
    #     return get_tde_window().panes[1]
    # return None


def open_console(cmd=tde_default_shell_cmd, cwd=None, env=None):
    # close_console()
    # if cmd == "ipython" or cmd == "ipython3":
    #     cmd = tde_ipython3_cmd + " -i " + os.path.join(
    #         tde_dir, tde_ipython3_init)
    # elif cmd == "ipython2":
    #     cmd = tde_ipython2_cmd + " -i " + os.path.join(
    #         tde_dir, tde_ipython2_init)
    if cwd is None:
        cwd = vim.eval("getcwd()")
    # if env == "anaconda":
    #     cmd = "%s -c 'source %s; cd %s; %s'" % (
    #         bash_cmd, init_anaconda, cwd, cmd)
    # get_tde_window().cmd("split-window", "-d", "-h", "-c", cwd, cmd)
    subprocess.run(["i3-msg", "exec kitty -d " + cwd + " " + cmd])
    # subprocess.run(["kitty", "-d", cwd, cmd])


def close_console():
    pass
    # console = get_console()
    # if console is not None:
    #     console.cmd("kill-pane")


# def open_desktop(cmd=tde_default_shell_cmd):
#     pass
#     # session = get_session()
#     # # cmd = "/home/jorg/.local/bin/xonsh"
#     # # session.cmd("new-window", "-d", "-n", tde_con, "-c",
#     # #                      vim.eval("getcwd()"), cmd)
#     # # window = session.find_where({"window_name": tde_con})
#     # window = session.new_window(window_name=cmd[:3],
#     #                             start_directory=vim.eval("getcwd()"),
#     #                             attach=False,
#     #                             window_shell=cmd)
#     # window.cmd("split-window", "-d", "-h", "-c", vim.eval("getcwd()"), cmd)


# def close_desktop(cmd=tde_default_shell_cmd):
#     pass
#     # session = get_session()
#     # window = session.find_where({"window_name": cmd[:3]})
#     # window.kill_window()


def close_all_windows():
    save_session()
    close_console()
    # session = get_session()
    # for w in session.windows:
    #     if w.name != tde_tde:
    #         w.kill_window()


def send_to_console(string):
    pass
    # console = get_console()
    # # bracketed_string = "\x1b[200~" + string + "\x1b[201~"
    # # terminal.send_keys(bracketed_string, enter=True)
    # libtmux.Server().cmd("set-buffer", "-b", "tdebuf", string)
    # console.cmd("paste-buffer", "-pdr", "-b", "tdebuf")
    # if string[-1] == "\n":
    #     console.send_keys("", enter=True)


###############################################################################
# pasting text from editor to console

def get_selected_lines():
    buf = vim.current.buffer
    start = buf.mark("<")  # begin of the selection
    end = buf.mark(">")  # end of the selection
    return "\n".join(unindent(buf[start[0]-1:end[0]])) + "\n"


def get_selection():
    buf = vim.current.buffer
    start_line, start_col = buf.mark("<")  # begin of the selection
    end_line, end_col = buf.mark(">")  # end of the selection
    sel = []
    for lidx in range(start_line-1, end_line):
        line = ""
        if lidx == start_line-1:
            if lidx == end_line-1:
                line = buf[lidx][start_col:end_col+1]
            else:
                line = buf[lidx][start_col:]
        elif lidx == end_line-1:
            line = buf[lidx][:end_col+1]
        else:
            line = buf[lidx]
        sel.append(line)
    lines = "\n".join(unindent(sel))
    if lidx < end_line-1 or (
        lidx == end_line-1 and end_col >= len(buf[lidx])-1):
        lines += "\n"
    return lines


def unindent(lines):
    spaces = re.compile(r"(\s*)")
    positions = [spaces.match(l).span(0)[1] for l in lines]
    min_pos = min(positions)
    return [l[min_pos:] for l in lines]


def run_line():
    send_to_console(vim.current.line.lstrip() + "\n")


def run_selected_lines():
    send_to_console(get_selected_lines())


def run_selection():
    send_to_console(get_selection())


def run_file():
    # NOTE: this is ipython specific
    # TODO: should also implement running the whole buffer, not only the file
    #       (but can always do that by selecting the whole buffer and run
    #       the selection)
    send_to_console("%run " + vim.current.buffer.name + "\n")


def run_cell():
    # find current line number
    row, col = vim.current.window.cursor
    # search upwards for cell string at beginning of line
    start = row
    for lno in range(row, 0, -1):
        if vim.current.buffer[lno - 1].startswith(cellstr) or lno == 1:
            start = lno
            break
    # search downwards
    end = row
    for lno in range(row, len(vim.current.buffer) + 1):
        if vim.current.buffer[lno - 1].startswith(cellstr) or \
                lno == len(vim.current.buffer):
            end = lno
            break
    # return current.buffer[start, end]
    print(start, end)
    cell = "\n".join(vim.current.buffer[start - 1:end]) + "\n"
    send_to_console(cell)


###############################################################################
# cell movement commands

def goto_prev_cell():
    row, col = vim.current.window.cursor
    found_count = 0
    for lno in range(row, 0, -1):
        if lno == 1:
            vim.current.window.cursor = lno, 0
        elif vim.current.buffer[lno - 1].startswith(cellstr):
            found_count += 1
            if found_count == 2:
                vim.current.window.cursor = lno + 1, 0
                return


def goto_next_cell():
    row, col = vim.current.window.cursor
    end = row
    for lno in range(row, len(vim.current.buffer) + 1):
        if vim.current.buffer[lno - 1].startswith(cellstr):
            end = lno
            if end == len(vim.current.buffer):
                return
            vim.current.window.cursor = end + 1, 0
            return


###############################################################################
# handling error list that has been sent from the console

def goto_error(errno=0):
    global errlist
    # can we open a file with the python interface?
    vim.command("e %s" % errlist[int(errno)][0])
    vim.current.window.cursor = (errlist[int(errno)][1], 0)


def goto_next_error():
    global currerr
    goto_error(currerr)
    currerr += 1
