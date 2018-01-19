if !has('python3') && !has(python)
  echo "No python"
  finish
endif

function! SearchWithFormattedSelection()
  echo "First test!"
endfunc

vmap <silent> AS  :call SearchWithFormattedSelection()<CR>
