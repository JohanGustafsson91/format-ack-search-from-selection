import re
import vim


def getSearchOutputString(formattedQuery):
    return ("Ack " + "\"" + formattedQuery + "\"" + " -i")


def espaceCharactersInString(string):
    return re.escape(string)


def getIgnoreDirString(ignoreDir):
    return "" if not len(ignoreDir) else\
            " --ignore-dir=" + " --ignore-dir=".join(map(str, ignoreDir))


def searchWithAck(selectedText, ignoreDirs):
    escapedString = espaceCharactersInString(selectedText)
    vim.command(
        getSearchOutputString(escapedString) + getIgnoreDirString(ignoreDirs)
    )


def printErrorMessage():
    print("format-ack-search-from-selection: No selected text")


# Get values from VIM script
selectedText = vim.eval('g:selectedText')
ignoreDirs = vim.eval('g:format_ack_search_from_selection_ignore_dirs')

if selectedText:
    searchWithAck(selectedText, ignoreDirs)
else:
    printErrorMessage()
