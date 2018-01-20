if !has('python3') && !has(python)
  echo "No python"
  finish
endif

if !exists('g:format_ack_search_from_selection_ignore_dirs')
  let g:format_ack_search_from_selection_ignore_dirs = []
endif

if !exists('g:format_ack_search_from_selection_filepath')
  let g:format_ack_search_from_selection_filepath = '~/.vim/bundle/format-ack-search-from-selection/plugin/' 
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
 
function! SearchAckWithFormattedSelection(query)
  let g:selectedText = strlen(a:query) > 0 ? a:query : GetSelectedText()
  execute (has('python3') ? 'py3file ' : 'pyfile ') g:format_ack_search_from_selection_filepath . 'format_ack_search_from_selection.py'
endfunc

set 

vmap <silent> AS :call SearchAckWithFormattedSelection('')<CR>
