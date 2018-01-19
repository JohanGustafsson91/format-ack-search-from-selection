import re
import sys
import vim

def getSearchOutputString( formattedQuery ):
  return ("Ack " +  "\"" + formattedQuery + "\"" + " -i")

def espaceCharactersInString( string ):
  return re.escape(string)

# Check if a variable exists
selectedText = vim.eval('g:selectedText')

if selectedText:
  escapedString = espaceCharactersInString(selectedText)
  vim.command(getSearchOutputString(escapedString))
else:
  print("format-ack-search-from-selection: No selected text")

