#
# Executes commands at the start of an interactive session.
#
# Authors:
#   Sorin Ionescu <sorin.ionescu@gmail.com>
#
[[ -z "$PS1" ]] && return
# Source Prezto.
if [[ -s "${ZDOTDIR:-$HOME}/.zprezto/init.zsh" ]]; then
	source "${ZDOTDIR:-$HOME}/.zprezto/init.zsh"
fi

# Customize to your needs...
prompt db

alias ssrv='ssh danny@192.168.2.200'
alias pssrv='ssh danny@dbittman.mooo.com'

autoload edit-command-line
zle -N edit-command-line
bindkey '^Xe' edit-command-line

alias sut='ssh dbittman@unix.ic.ucsc.edu'

export GCC_COLORS="error=01;31:warning=01;35:note=01;36:caret=01;32:locus=01:quote=01"
export TERM=xterm-256color
[ -n "$TMUX" ] && export TERM=screen-256color
zle -N fancy-ctrl-z
bindkey '^Z' fancy-ctrl-z
fancy-ctrl-z () {
	if [[ $#BUFFER -eq 0 ]]; then
		bg
		zle redisplay
	else
		zle push-input
	fi
}

TZ="America/Los_Angeles"

alias wtf='dmesg'

export PAGER='less'
export EDITOR='vim'
setopt appendhistory autocd extendedglob notify
function extract() {
  local remove_archive
  local success
  local file_name
  local extract_dir

  if (( $# == 0 )); then
    echo "Usage: extract [-option] [file ...]"
    echo
    echo Options:
    echo "    -r, --remove    Remove archive."
    echo
    echo "Report bugs to <sorin.ionescu@gmail.com>."
  fi

  remove_archive=1
  if [[ "$1" == "-r" ]] || [[ "$1" == "--remove" ]]; then
    remove_archive=0 
    shift
  fi

  while (( $# > 0 )); do
    if [[ ! -f "$1" ]]; then
      echo "extract: '$1' is not a valid file" 1>&2
      shift
      continue
    fi

    success=0
    file_name="$( basename "$1" )"
    extract_dir="$( echo "$file_name" | sed "s/\.${1##*.}//g" )"
    case "$1" in
      (*.tar.gz|*.tgz) tar xzf "$1" ;;
      (*.tar.bz2|*.tbz|*.tbz2) tar xjf "$1" ;;
      (*.tar.xz|*.txz) tar --xz --help &> /dev/null \
        && tar --xz -xf "$1" \
        || xzcat "$1" | tar xf - ;;
      (*.tar.zma|*.tlz) tar --lzma --help &> /dev/null \
        && tar --lzma -xf "$1" \
        || lzcat "$1" | tar xf - ;;
      (*.tar) tar xf "$1" ;;
      (*.gz) gunzip "$1" ;;
      (*.bz2) bunzip2 "$1" ;;
      (*.xz) unxz "$1" ;;
      (*.lzma) unlzma "$1" ;;
      (*.Z) uncompress "$1" ;;
      (*.zip) unzip "$1" -d $extract_dir ;;
      (*.rar) unrar e -ad "$1" ;;
      (*.7z) 7za x "$1" ;;
      (*.deb)
        mkdir -p "$extract_dir/control"
        mkdir -p "$extract_dir/data"
        cd "$extract_dir"; ar vx "../${1}" > /dev/null
        cd control; tar xzf ../control.tar.gz
        cd ../data; tar xzf ../data.tar.gz
        cd ..; rm *.tar.gz debian-binary
        cd ..
      ;;
      (*) 
        echo "extract: '$1' cannot be extracted" 1>&2
        success=1 
      ;; 
    esac

    (( success = $success > 0 ? $success : $? ))
    (( $success == 0 )) && (( $remove_archive == 0 )) && rm "$1"
    shift
  done
}

alias x=extract

