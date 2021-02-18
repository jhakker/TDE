" File              : tde.vim
" Author            : Jörg Bakker <jorg@hakker.de>
" Date              : 2020-01-02
" Last Modified Date: 2020-01-02
" Last Modified By  : Jörg Bakker <jorg@hakker.de>

" source the python module with tde functions for vim
let tde_path = fnamemodify(resolve(expand('<sfile>:p')), ':h')
let tde_vim_pyscript_path = tde_path . "/tdevim.py"
execute "py3file" tde_vim_pyscript_path

" unmap F1 key, currently the tmux prefix key
" nnoremap <F1> <nop>

" map some tde python functions to keys
" nnoremap , : py3 run_line()<CR>
" vnoremap , : py3 run_selection()<CR>
nnoremap <F5> : py3 run_line()<CR>
vnoremap <F5> : py3 run_selection()<CR>

" function! TmuxCmdFunc(cmd)
"     py3 tmux_cmd(vim.eval("a:cmd"))
" endfunction
" command! -nargs=1 TmuxCmd call TmuxCmdFunc(<f-args>)

" let s:tmux_conf_source_cmd = "source-file " . tde_path . "/tmux.conf"
" execute "TmuxCmd" s:tmux_conf_source_cmd

function! RunFileFunc()
    py3 run_file()
endfunction
command! RunFile call RunFileFunc()

function! RunSelectionFunc()
    py3 run_selection()
endfunction
command! RunSelection call RunSelectionFunc()

function! RunCellFunc()
    py3 run_cell()
endfunction
command! RunCell call RunCellFunc()

function! CellPrevFunc()
    py3 goto_prev_cell()
endfunction
command! CellPrev call CellPrevFunc()

function! CellNextFunc()
    py3 goto_next_cell()
endfunction
command! CellNext call CellNextFunc()

function! ErrorFunc(errno)
    py3 goto_error(vim.eval("a:errno"))
endfunction
command! -nargs=1 Error call ErrorFunc(<f-args>)

function! VimExitFunc()
    py3 exit_vim()
endfunction
command! Exit call VimExitFunc()

function! SessionCloseFunc()
    py3 close_session()
endfunction
command! SessionClose call SessionCloseFunc()

function! SessionOpenFunc(...)
    if a:0 == 0
        py3 open_session()
    elseif a:0 == 1
        py3 open_session(vim.eval("a:1"))
    endif
endfunction
command! -nargs=* SessionOpen call SessionOpenFunc(<f-args>)

function! SessionSaveFunc(...)
    if a:0 == 0
        py3 save_session()
    elseif a:0 == 1
        py3 save_session(vim.eval("a:1"))
    endif
endfunction
command! -nargs=* SessionSave call SessionSaveFunc(<f-args>)

SessionOpen

" function! ConsoleCloseFunc()
"     py3 close_console()
" endfunction
" command! ConsoleClose call ConsoleCloseFunc()

" function! ConsoleOpenFunc(...)
"     if a:0 == 0
"         py3 open_console()
"     elseif a:0 == 1
"         py3 open_console(vim.eval("a:1"))
"     elseif a:0 == 2
"         py3 open_console(vim.eval("a:1"), vim.eval("a:2"))
"     elseif a:0 == 3
"         py3 open_console(vim.eval("a:1"), vim.eval("a:2"), vim.eval("a:3"))
"     endif
" endfunction
" command! -nargs=* ConsoleOpen call ConsoleOpenFunc(<f-args>)

" function! CloseAllWindowsFunc()
"     py3 close_all_windows()
" endfunction
" command! CloseAllWindows call CloseAllWindowsFunc()

" function! DesktopOpenFunc(...)
"     if a:0 == 0
"         py3 open_desktop()
"     elseif a:0 == 1
"         py3 open_desktop(vim.eval("a:1"))
"     endif
" endfunction
" command! -nargs=* DesktopOpen call DesktopOpenFunc(<f-args>)

" function! DesktopCloseFunc(...)
"     if a:0 == 0
"         py3 close_desktop()
"     elseif a:0 == 1
"         py3 close_desktop(vim.eval("a:1"))
"     endif
" endfunction
" command! -nargs=* DesktopClose call DesktopCloseFunc(<f-args>)

" augroup tde
"     " autocmd VimLeavePre * !CloseAllWindows
"     autocmd VimLeavePre * call CloseAllWindowsFunc()
" augroup END


" function! ErrorSetOutputTmux()
"     cexpr system('tmux capture-pane -p -S- -t tde:tde.2')
" endfunction


