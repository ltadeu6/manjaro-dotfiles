# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from typing import List  # noqa: F401
import subprocess
import datetime
import os

from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy

mod = "mod4"
terminal = "kitty"

keys = [
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "Tab", lazy.screen.next_group(), desc="Next Group"),
    Key([mod, "shift"], "Tab", lazy.screen.prev_group(), desc="Next Group"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Fullscreen"),
    Key([mod, "shift"], "f", lazy.window.toggle_floating(), desc="Floating"),
    # Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key(
        [mod, "shift"], "period", lazy.layout.grow_main(), desc="increase layout ratio"
    ),
    Key(
        [mod, "shift"], "comma", lazy.layout.shrink_main(), desc="decrease layout ratio"
    ),
    Key([mod, "shift"], "equal", lazy.layout.grow(), desc="increase pane ratio"),
    Key([mod, "shift"], "minus", lazy.layout.shrink(), desc="decrease pane ratio"),
    Key([mod], "r", lazy.layout.normalize(), desc="reset layout"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    # Key(
    #     [mod, "shift"],
    #     "Return",
    #     lazy.layout.toggle_split(),
    #     desc="Toggle between split and unsplit sides of stack",
    # ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "z", lazy.spawn("zathura"), desc="Zathura"),
    Key(
        ["shift"],
        "Print",
        lazy.spawn("xfce4-screenshooter -fc"),
        desc="Print screen to clipboard",
    ),
    Key(
        ["mod1"],
        "Print",
        lazy.spawn("xfce4-screenshooter -wc"),
        desc="Print Window clipboard",
    ),
    Key(
        [],
        "Print",
        lazy.spawn("xfce4-screenshooter -rc"),
        desc="Print region clipboard",
    ),
    Key(
        ["shift", "control"],
        "Print",
        lazy.spawn("xfce4-screenshooter -f"),
        desc="Print screen",
    ),
    Key(
        ["control", "mod1"],
        "Print",
        lazy.spawn("xfce4-screenshooter -w"),
        desc="Print window",
    ),
    Key(
        ["control"],
        "Print",
        lazy.spawn("xfce4-screenshooter -r"),
        desc="Print region",
    ),
    Key(
        [mod],
        "m",
        lazy.spawn(
            'kitty -o "font_family=Fira Code" -o background_opacity=1 --name "float" -e ncmpcpp'
        ),
        desc="Zathura",
    ),
    Key(
        [mod, "mod1"],
        "Return",
        lazy.spawn('kitty --name "float"'),
        desc="Launch floating terminal",
    ),
    Key(
        [mod],
        "space",
        lazy.spawn("/home/ltadeu6/.config/rofi/bin/launcher_misc"),
        desc="rofi",
    ),
    Key([], "XF86MonBrightnessDown", lazy.spawn("light -U 10"), desc="Lower Brithness"),
    Key([], "XF86MonBrightnessUp", lazy.spawn("light -A 10"), desc="Raise Brithnes"),
    Key(
        [], "XF86AudioMute", lazy.spawn("amixer set Master toggle"), desc="Volume mute"
    ),
    Key(
        [], "XF86AudioRaiseVolume", lazy.spawn("amixer set Master 5%+"), desc="Volume+"
    ),
    Key(
        [], "XF86AudioLowerVolume", lazy.spawn("amixer set Master 5%-"), desc="Volume-"
    ),
    Key([mod], "d", lazy.spawn("emacsclient -c"), desc="emacs"),
    Key([mod, "shift"], "p", lazy.spawn("rofi-pass"), desc="rofi-pass"),
    Key([mod, "shift"], "Return", lazy.spawn("firefox"), desc="browser"),
    # Toggle between different layouts as defined below
    Key([mod, "mod1"], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.restart(), desc="Restart Qtile"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod, "shift"], "n", lazy.spawn("pcmanfm"), desc="file manager"),
    Key(
        [mod, "shift"],
        "space",
        lazy.spawn("/home/ltadeu6/.config/rofi/bin/run_colorful"),
        desc="Spawn a command using a prompt widget",
    ),
]

groups = [
    Group("1", layout="monadtall"),
    Group("2", layout="monadtall"),
    Group("3", layout="monadtall"),
    Group("4", layout="stack"),
    Group("5", layout="monadtall"),
    Group("6", layout="monadtall"),
    Group("7", layout="monadtall"),
    Group("8", layout="monadtall"),
    Group("9", layout="monadtall"),
]

for i in groups:
    keys.extend(
        [
            # mod1 + letter of group = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + letter of group = switch to & move focused window to group
            Key(
                [mod, "mod1"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod1 + shift + letter of group = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )
# group_names = [
#     ("WWW", {"layout": "tile"}),
#     ("DEV", {"layout": "tile"}),
#     ("SYS", {"layout": "tile"}),
#     ("DOC", {"layout": "tile"}),
#     ("VBOX", {"layout": "tile"}),
#     ("CHAT", {"layout": "tile"}),
#     ("MUS", {"layout": "tile"}),
#     ("VID", {"layout": "tile"}),
# ]

# groups = [Group(name, **kwargs) for name, kwargs in group_names]

# for i, (name, kwargs) in enumerate(group_names, 1):
#     keys.append(
#         Key([mod], str(i), lazy.group[name].toscreen())
#     )  # Switch to another group
#     keys.append(
#         Key([mod, "shift"], str(i), lazy.window.togroup(name))
#     )  # Send current window to another group


colors = []
cache = "/home/ltadeu6/.cache/wal/colors"


def load_colors(cache):
    with open(cache, "r") as file:
        for i in range(8):
            colors.append(file.readline().strip())
    colors.append("#ffffff")
    lazy.reload()


load_colors(cache)


layout_theme = {
    "border_focus": colors[2],
    "border_normal": colors[0],
}


layouts = [
    # layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    layout.MonadTall(
        border_focus=colors[2],
        border_normal=colors[0],
        ratio=0.7,
        min_ratio=0.5,
        max_ratio=0.7,
        single_border_width=0,
        margin=0,
        change_ratio=0.05,
        border_width=1,
        new_client_position="top",
    ),
    # layout.Columns(fair=True),
    # layout.Matrix(),
    # layout.Slice(),
    # layout.MonadWide(),
    # layout.Tile(**layout_theme, ratio=0.7),
    # layout.RatioTile(**layout_theme, fancy=True),
    layout.Stack(num_stacks=1, margin=[100, 201, 100, 201], border_width=0),
    # layout.Max(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


widget_defaults = dict(
    font="sans",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

screens = [
    Screen(
        top=bar.Gap(size=26),
        # bottom=bar.Bar(
        #     [
        #         widget.CurrentLayoutIcon(),
        #         widget.GroupBox(),
        #         # widget.Prompt(),
        #         widget.WindowName(),
        #         widget.Chord(
        #             chords_colors={
        #                 "launch": ("#ff0000", "#ffffff"),
        #             },
        #             name_transform=lambda name: name.upper(),
        #         ),
        #         # widget.TextBox("default config", name="default"),
        #         # widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
        #         widget.Battery(format="{percent:2.0%}"),
        #         widget.Backlight(
        #             backlight_name="intel_backlight",
        #             change_command="light -S {0}",
        #             step=3,
        #         ),
        #         widget.Systray(),
        #         widget.Clock(format="%Y-%m-%d %a %I:%M %p"),
        #         widget.QuickExit(),
        #     ],
        #     24,
        # ),
    ),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = False
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        # *layout.Floating.default_float_rules,
        # Match(wm_type='utility'),
        Match(wm_type="notification"),
        Match(wm_type="notification"),
        Match(wm_type="toolbar"),
        Match(wm_type="splash"),
        Match(wm_type="dialog"),
        Match(wm_class="file_progress"),
        Match(wm_class="float"),
        Match(wm_class="confirm"),
        Match(wm_class="dialog"),
        Match(wm_class="download"),
        Match(wm_class="error"),
        Match(wm_class="notification"),
        Match(wm_class="splash"),
        Match(wm_class="toolbar"),
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="guake"),  # guake
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ],
    **layout_theme,
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False


@hook.subscribe.startup
def start():

    script = os.path.expanduser("~/.config/qtile/start.sh")
    subprocess.call([script])


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser("~")
    subprocess.call([home + "/.config/qtile/start_once.sh"])

    time = datetime.datetime.now().hour
    if (time < 17) and (time > 6):
        subprocess.call(["set_light_theme"])
    else:
        subprocess.call(["set_dark_theme"])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
