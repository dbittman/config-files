#!/bin/zsh

echo "Warning - running this in bash may NOT WORK"

git clone --recursive https://github.com/sorin-ionescu/prezto.git "${ZDOTDIR:-$HOME}/.zprezto"
setopt EXTENDED_GLOB
for rcfile in "${ZDOTDIR:-$HOME}"/.zprezto/runcoms/^README.md(.N); do
	ln -s "$rcfile" "${ZDOTDIR:-$HOME}/.${rcfile:t}"
done

cp prompt_db_setup "${ZDOTDIR:-$HOME}/.zprezto/modules/prompt/functions/"
cp .zshrc "${ZDOTDIR:-$HOME}/.zshrc"

