oh-my-posh init fish --config $HOME/.poshthemes/gruvbox.omp.json | source
set fish_greeting (set_color "#ffbdd9")"🌟Hewo, have a nice day =w="(set_color normal)
fastfetch
echo -e '\\033[36m☔Weather info:\\033[0m'
python3 ~/.config/fastfetch/weather.py
alias ff fastfetch
alias checkw "python3 .config/fastfetch/weather.py"
if status is-interactive
    # Commands to run in interactive sessions can go here
end

fish_add_path /home/kaaru/.spicetify
