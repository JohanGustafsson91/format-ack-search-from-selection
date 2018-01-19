# format-ack-search-from-selection
A vim plugin to search current selection with Ack

<div style='position:relative;padding-bottom:54%'><iframe src='https://gfycat.com/ifr/FantasticBoldBillygoat' frameborder='0' scrolling='no' width='100%' height='100%' style='position:absolute;top:0;left:0' allowfullscreen></iframe></div>

## Installation

Use your plugin manager of choice.

- [Vundle](https://github.com/gmarik/vundle)
  - Add `Plugin 'JohanGustafsson91/format-ack-search-from-selection'`
  - Run `:BundleInstall`

__OBS!__ [Ack](https://github.com/mileszs/ack.vim) is required for the plugin to work.

## Basic usage
1. Select some text
2. Press `AF` to search

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

- Add explanation
- Add GIF
- Add custom key mapping
