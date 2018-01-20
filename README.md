# format-ack-search-from-selection
A vim plugin to search current selection with Ack

![Gif showing plugin](https://thumbs.gfycat.com/FantasticBoldBillygoat-size_restricted.gif)

## Installation

Use your plugin manager of choice.

- [Vundle](https://github.com/gmarik/vundle)
  - Add `Plugin 'JohanGustafsson91/format-ack-search-from-selection'`
  - Run `:BundleInstall`

__OBS!__ [Ack](https://github.com/mileszs/ack.vim) is required for the plugin to work.

## Basic usage
##### Search from selection
1. Select some text
2. Press `AF` to search

##### Manual search
`:call SearchAckWithFormattedQuery('My search query')` 

## Basic options

#### Set file path to python script
Default is `~/.vim/bundle/format-ack-search-from-selection/plugin/`

```
let g:format_ack_search_from_selection_filepath = 'new/file/path/'
```

#### Set ignore folders

```
 let g:format_ack_search_from_selection_ignore_dirs = ['node_modules', 'dist']
```


#### TODOs

_Please feel free to send a pull request_

- [] Add custom key mapping:w
