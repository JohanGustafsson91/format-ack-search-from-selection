import re
import vim


def get_search_output(formated_query):
    return ("Ack " + "\"" + formated_query + "\"" + " -i")


def escape_chars_in_string(string):
    return re.escape(string)


def get_ignore_dir_string(ignore_dir):
    return "" if not len(ignore_dir) else\
            " --ignore-dir=" + " --ignore-dir=".join(map(str, ignore_dir))


def search_with_ack(selected_text, ignore_dirs):
    escaped_string = escape_chars_in_string(selected_text)
    vim.command(
        get_search_output(escaped_string) + get_ignore_dir_string(ignore_dirs)
    )


def print_err_msg():
    print("format-ack-search-from-selection: No selected text")


# Get values from VIM script
selected_text = vim.eval('g:selected_text')
ignore_dirs = vim.eval('g:format_ack_search_from_selection_ignore_dirs')

if selected_text:
    search_with_ack(selected_text, ignore_dirs)
else:
    print_err_msg()
