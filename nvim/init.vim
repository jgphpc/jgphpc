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

"{{{ --- JG plugins:
  " Add or remove your plugins here like this:
  "call dein#add('Shougo/neosnippet.vim')
  "call dein#add('Shougo/neosnippet-snippets')
  " call dein#add('github_username'/'project_name')
  call dein#add('majutsushi/tagbar') " TODO: nnoremap <silent> <C-K><C-T> :TagbarToggle<CR>
  call dein#add('Shougo/defx.nvim')

  " https://github.com/Shougo/deoplete.nvim/blob/master/doc/deoplete.txt
  call dein#add('roxma/vim-hug-neovim-rpc')
  call dein#add('Shougo/deoplete.nvim')
  let g:deoplete#enable_at_startup = 1
  " pip3 install --user pynvim
  " :UpdateRemotePlugins

  call dein#add('nvie/vim-flake8') " F7 https://github.com/nvie/vim-flake8#usage
  call dein#add('rking/ag.vim')
  " call dein#add('fholgado/minibufexpl.vim')
  call dein#add('sakhnik/nvim-gdb')
  " call dein#add('Vimjas/vim-python-pep8-indent')
  " call dein#add('hynek/vim-python-pep8-indent')
  call dein#add('tell-k/vim-autopep8')
"}}}

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

"{{{ --- general:
set guicursor=      " cursor shape
set ignorecase      " ignore case when searching
set ruler           " show cursor line at the bottom of the terminal
" set rulerformat=%30(%=\:b%n%y%m%r%w\ %l,%c%V\ %P%) " A ruler on steroids
" set showmatch     " show bracket matches
set showmode        " display current mode in the status line
set nu
let &colorcolumn=join(range(80,80),",")
set expandtab       " insert spaces instead of tab
set shiftwidth=4    " use indents of 4 spaces
set tabstop=4
set bs=2            " Backspace
"}}}

"{{{ --- folding:
set foldmethod=marker
set foldcolumn=0
"setlocal foldnestmax=1
nnoremap <Space> za
vnoremap <Space> za
set foldenable         " Auto fold code
" Code folding options
nmap <leader>f0 :set foldlevel=0<CR>
nmap <leader>f1 :set foldlevel=1<CR>
nmap <leader>f2 :set foldlevel=2<CR>
nmap <leader>f3 :set foldlevel=3<CR>
nmap <leader>f4 :set foldlevel=4<CR>
nmap <leader>f5 :set foldlevel=5<CR>
nmap <leader>f6 :set foldlevel=6<CR>
nmap <leader>f7 :set foldlevel=7<CR>
nmap <leader>f8 :set foldlevel=8<CR>
nmap <leader>f9 :set foldlevel=9<CR>
"}}}

"{{{ --- hpc:
let fortran_free_source=1
"}}}

"{{{ --- python:
let g:pydoc_cmd='pydoc'
let python_highlight_all = 1
"}}}

"{{{ --- :
au BufNewFile,BufRead *.md set ft=sh
au BufRead,BufNewFile *.m  set filetype=octave
au BufRead,BufNewFile .oct set filetype=octave 
au BufNewFile,BufRead *.eb set ft=sh
au BufNewFile,BufRead *.log set ft=sh
au BufNewFile,BufRead *.c set ft=c
au BufNewFile,BufRead *.dox set ft=cpp.doxygen 
au BufNewFile,BufRead *.CUF set ft=cuda
au BufNewFile,BufRead *.cuf set ft=fortran
au BufNewFile,BufRead *.nml set ft=fortran
au BufNewFile,BufRead *.F03 set ft=fortran
au BufNewFile,BufRead *.swn set ft=tcsh
au BufRead,BufNewFile *.ncl set filetype=fortran
au BufNewFile,BufRead *.pc set ft=sh
"}}}

"{{{ --- :
"}}}

"{{{ --- :
"}}}

