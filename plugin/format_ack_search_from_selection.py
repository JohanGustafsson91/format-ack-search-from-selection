import re
import sys
import vim

def getSearchOutputString( formattedQuery ):
  return ("Ack " +  "\"" + formattedQuery + "\"" + " -i")

def espaceCharactersInString( string ):
  return re.escape(string)

def getIgnoreDirString( ignoreDir ):
  return "" if len(ignoreDirs) is 0 else " --ignore-dir=" + " --ignore-dir=".join(map(str, ignoreDir))

def searchWithAck( selectedText ):
  escapedString = espaceCharactersInString(selectedText)
  vim.command(getSearchOutputString(escapedString) + getIgnoreDirString(ignoreDirs))

def printErrorMessage():
  print("format-ack-search-from-selection: No selected text")

# Get values from VIM script
selectedText = vim.eval('g:selectedText')
ignoreDirs = vim.eval('g:format_ack_search_from_selection_ignore_dirs')

return searchWithAck(selectedText) if selectedText else printErrorMessage()
