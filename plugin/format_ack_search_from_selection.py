import re
import sys
import vim

def getSearchOutputString( formattedQuery ):
  return ("Ack " +  "\"" + formattedQuery + "\"" + " -i")

def espaceCharactersInString( string ):
  return re.escape(string)

def getIgnoreDirString( ignoreDir ):
  if len(ignoreDir) is 0:
    return ""
  else:
    return " --ignore-dir=" + " --ignore-dir=".join(map(str, ignoreDir))

# Get values from VIM script
selectedText = vim.eval('g:selectedText')
ignoreDirs = vim.eval('g:format_ack_search_from_selection_ignore_dirs')

if selectedText:
  escapedString = espaceCharactersInString(selectedText)
  vim.command(getSearchOutputString(escapedString) + getIgnoreDirString(ignoreDirs))
else:
  print("format-ack-search-from-selection: No selected text")

