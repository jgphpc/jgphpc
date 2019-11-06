" Get neovim from https://github.com/neovim/neovim/wiki/Installing-Neovim
"
" Get plugin manager from https://github.com/Shougo/dein.vim#unixlinux-or-mac-os-x
"   wget https://raw.githubusercontent.com/Shougo/dein.vim/master/bin/installer.sh
"   . ./installer.sh ~/.config/nvim/bundle
"   ln -s ~/jgphpc.git/nvim/init.vim ~/.config/nvim/init.vim
"
"

"{{{dein Scripts-----------------------------
if &compatible
  set nocompatible               " Be iMproved
endif

" Required:
set runtimepath+=$HOME/.config/nvim/bundle/repos/github.com/Shougo/dein.vim

" Required:
if dein#load_state('$HOME/.config/nvim/bundle')
  call dein#begin('$HOME/.config/nvim/bundle')

  " Let dein manage dein
  " Required:
  call dein#add('$HOME/.config/nvim/bundle/repos/github.com/Shougo/dein.vim')

  " --- JG plugins:
  " Add or remove your plugins here like this:
  "call dein#add('Shougo/neosnippet.vim')
  "call dein#add('Shougo/neosnippet-snippets')
  " call dein#add('github_username'/'project_name')
  call dein#add('majutsushi/tagbar')
  " --- JG plugins:

  " Required:
  call dein#end()
  call dein#save_state()
endif

" Required:
filetype plugin indent on
syntax enable

" If you want to install not installed plugins on startup.
if dein#check_install()
  call dein#install()
endif

"End dein Scripts-------------------------
"}}}

