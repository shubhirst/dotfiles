#HOME=/home/ec2-user/
PROFILE_PATH="$HOME"/.profile
if [ -f "$PROFILE_PATH" ]; then
	source $PROFILE_PATH
fi

BASH_DOTFILES_PATH="$HOME"/dotfiles/bash
for DOTFILE in `find $BASH_DOTFILES_PATH`
do
    [ -f "$DOTFILE" ] && source "$DOTFILE"
done

