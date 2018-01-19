if !has('python3') && !has(python)
  echo "No python"
  finish
endif

function! GetSelectedText()
    let [line_start, column_start] = getpos("'<")[1:2]
    let [line_end, column_end] = getpos("'>")[1:2]
    let lines = getline(line_start, line_end)
    if len(lines) == 0
        return ''
    endif
    let lines[-1] = lines[-1][: column_end - (&selection == 'inclusive' ? 1 : 2)]
    let lines[0] = lines[0][column_start - 1:]
    return join(lines, "\n")
endfunction
 
function! SearchWithFormattedSelection()
  let g:selectedText = GetSelectedText()
  execute 'pwd'
  "execute (has('python3') ? 'py3file' : 'pyfile') 'format_ack_search_from_selection.py'
endfunc

vmap <silent> AS  :call SearchWithFormattedSelection()<CR>
