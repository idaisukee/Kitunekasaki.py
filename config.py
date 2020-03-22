import re
from xkeysnail.transform import *

define_modmap({
    Key.GRAVE: Key.ESC,
    Key.TAB: Key.LEFT_ALT,
    Key.CAPSLOCK: Key.LEFT_CTRL,
    Key.LEFT_CTRL: Key.LEFT_META,
    Key.RIGHT_CTRL: Key.RIGHT_META,
    Key.RO: Key.RIGHT_SHIFT,
    Key.BACKSLASH: Key.RIGHT_CTRL,
    Key.ENTER: Key.RIGHT_ALT,
    Key.PAUSE: Key.EQUAL,
    Key.SCROLLLOCK: Key.ENTER
})

define_keymap(re.compile("Firefox|Google-chrome"), {
    # Ctrl+Alt+j/k to switch next/previous tab
    K("M-z"): K("C-w"),
    K("M-x"): K("C-page_up"),
    K("M-c"): K("C-page_down"),
    K("M-v"): K("C-t"),
    K("M-s"): K("C-o"),
}, "Firefox and Chrome")

define_keymap(lambda wm_class: wm_class not in ("Emacs", "URxvt"), {
    # Cursor
    K("C-h"): with_mark(K("left")),
    K("C-j"): with_mark(K("down")),
    K("C-k"): with_mark(K("up")),
    K("C-l"): with_mark(K("right")),
    K("C-Shift-h"): with_mark(K("C-left")),
    K("C-Shift-l"): with_mark(K("C-right")),
    K("C-a"): with_mark(K("home")),
    K("C-s"): with_mark(K("page_down")),
    K("C-d"): with_mark(K("page_up")),
    K("C-f"): with_mark(K("end")),
    K("C-Shift-s"): with_mark(K("C-end")),
    K("C-Shift-d"): with_mark(K("C-home")),
    K("C-g"): K("tab"),
    # Edit
    K("C-o"): [K("delete"), set_mark(False)],
    K("C-Shift-o"): [K("C-delete"), set_mark(False)],
    K("C-n"): with_mark(K("backspace")),
    K("C-Shift-n"): with_mark(K("C-backspace")),
    K("C-v"): [K("Shift-end"), K("C-x"), set_mark(False)],
    # Newline
    K("C-m"): K("enter"),
    # Copy
    K("C-w"): [K("C-c"), set_mark(False)],
    K("C-e"): [K("C-x"), set_mark(False)],
    K("C-r"): [K("C-v"), set_mark(False)],
    # Undo
    K("C-right_brace"): [K("C-z"), set_mark(False)],
    # Mark
    K("C-space"): set_mark(True),
    # Search
    K("C-semicolon"): K("F3"),
    # Cancel
    K("C-u"): [K("esc"), set_mark(False)],
    # Escape
    K("C-q"): escape_next_key,


}, "Emacs-like keys")

define_keymap(None, {
    K("r"): K("p"),
    K("t"): K("y"),
    K("y"): K("f"),
    K("u"): K("g"),
    K("i"): K("c"),
    K("o"): K("r"),
    K("p"): K("l"),
    K("s"): K("o"),
    K("d"): K("e"),
    K("f"): K("u"),
    K("g"): K("i"),
    K("h"): K("d"),
    K("j"): K("h"),
    K("k"): K("t"),
    K("l"): K("n"),
    K("x"): K("q"),
    K("c"): K("j"),
    K("v"): K("k"),
    K("b"): K("x"),
    K("n"): K("b"),
    K("w"): K("comma"),
    K("e"): K("dot"),
    K("comma"): K("w"),
    K("dot"): K("v"),
    K("slash"): K("z"),
    K("semicolon"): K("s"),
    K("minus"): K("right_brace"),
    K("equal"): K("backslash"),
    K("left_brace"): K("slash"),
    K("insert"): K("backspace"),
    K("Shift-r"): K("Shift-p"),
    K("Shift-t"): K("Shift-y"),
    K("Shift-y"): K("Shift-f"),
    K("Shift-u"): K("Shift-g"),
    K("Shift-i"): K("Shift-c"),
    K("Shift-o"): K("Shift-r"),
    K("Shift-p"): K("Shift-l"),
    K("Shift-s"): K("Shift-o"),
    K("Shift-d"): K("Shift-e"),
    K("Shift-f"): K("Shift-u"),
    K("Shift-g"): K("Shift-i"),
    K("Shift-h"): K("Shift-d"),
    K("Shift-j"): K("Shift-h"),
    K("Shift-k"): K("Shift-t"),
    K("Shift-l"): K("Shift-n"),
    K("Shift-x"): K("Shift-q"),
    K("Shift-c"): K("Shift-j"),
    K("Shift-v"): K("Shift-k"),
    K("Shift-b"): K("Shift-x"),
    K("Shift-n"): K("Shift-b"),
    K("Shift-w"): K("Shift-comma"),
    K("Shift-e"): K("Shift-dot"),
    K("Shift-comma"): K("Shift-w"),
    K("Shift-dot"): K("Shift-v"),
    K("Shift-slash"): K("Shift-z"),
    K("Shift-semicolon"): K("Shift-s"),
    K("Shift-minus"): K("Shift-right_brace"),
    K("Shift-equal"): K("Shift-backslash"),
    K("Shift-left_brace"): K("Shift-slash"),
    K("Shift-insert"): K("Shift-backspace"),
    K("C-r"): K("C-p"),
    K("C-t"): K("C-y"),
    K("C-y"): K("C-f"),
    K("C-u"): K("C-g"),
    K("C-i"): K("C-c"),
    K("C-o"): K("C-r"),
    K("C-p"): K("C-l"),
    K("C-s"): K("C-o"),
    K("C-d"): K("C-e"),
    K("C-f"): K("C-u"),
    K("C-g"): K("C-i"),
    K("C-h"): K("C-d"),
    K("C-j"): K("C-h"),
    K("C-k"): K("C-t"),
    K("C-l"): K("C-n"),
    K("C-x"): K("C-q"),
    K("C-c"): K("C-j"),
    K("C-v"): K("C-k"),
    K("C-b"): K("C-x"),
    K("C-n"): K("C-b"),
    K("C-w"): K("C-comma"),
    K("C-e"): K("C-dot"),
    K("C-comma"): K("C-w"),
    K("C-dot"): K("C-v"),
    K("C-slash"): K("C-z"),
    K("C-semicolon"): K("C-s"),
    K("C-minus"): K("C-right_brace"),
    K("C-equal"): K("C-backslash"),
    K("C-left_brace"): K("C-slash"),
    K("C-insert"): K("C-backspace"),
    K("M-r"): K("M-p"),
    K("M-t"): K("M-y"),
    K("M-y"): K("M-f"),
    K("M-u"): K("M-g"),
    K("M-i"): K("M-c"),
    K("M-o"): K("M-r"),
    K("M-p"): K("M-l"),
    K("M-s"): K("M-o"),
    K("M-d"): K("M-e"),
    K("M-f"): K("M-u"),
    K("M-g"): K("M-i"),
    K("M-h"): K("M-d"),
    K("M-j"): K("M-h"),
    K("M-k"): K("M-t"),
    K("M-l"): K("M-n"),
    K("M-x"): K("M-q"),
    K("M-c"): K("M-j"),
    K("M-v"): K("M-k"),
    K("M-b"): K("M-x"),
    K("M-n"): K("M-b"),
    K("M-w"): K("M-comma"),
    K("M-e"): K("M-dot"),
    K("M-comma"): K("M-w"),
    K("M-dot"): K("M-v"),
    K("M-slash"): K("M-z"),
    K("M-semicolon"): K("M-s"),
    K("M-minus"): K("M-right_brace"),
    K("M-equal"): K("M-backslash"),
    K("M-left_brace"): K("M-slash"),
    K("M-insert"): K("M-backspace"),
    K("Win-r"): K("Win-p"),
    K("Win-t"): K("Win-y"),
    K("Win-y"): K("Win-f"),
    K("Win-u"): K("Win-g"),
    K("Win-i"): K("Win-c"),
    K("Win-o"): K("Win-r"),
    K("Win-p"): K("Win-l"),
    K("Win-s"): K("Win-o"),
    K("Win-d"): K("Win-e"),
    K("Win-f"): K("Win-u"),
    K("Win-g"): K("Win-i"),
    K("Win-h"): K("Win-d"),
    K("Win-j"): K("Win-h"),
    K("Win-k"): K("Win-t"),
    K("Win-l"): K("Win-n"),
    K("Win-x"): K("Win-q"),
    K("Win-c"): K("Win-j"),
    K("Win-v"): K("Win-k"),
    K("Win-b"): K("Win-x"),
    K("Win-n"): K("Win-b"),
    K("Win-w"): K("Win-comma"),
    K("Win-e"): K("Win-dot"),
    K("Win-comma"): K("Win-w"),
    K("Win-dot"): K("Win-v"),
    K("Win-slash"): K("Win-z"),
    K("Win-semicolon"): K("Win-s"),
    K("Win-minus"): K("Win-right_brace"),
    K("Win-equal"): K("Win-backslash"),
    K("Win-left_brace"): K("Win-slash"),
    K("Win-insert"): K("Win-backspace"),
    K("Shift-C-r"): K("Shift-C-p"),
    K("Shift-C-t"): K("Shift-C-y"),
    K("Shift-C-y"): K("Shift-C-f"),
    K("Shift-C-u"): K("Shift-C-g"),
    K("Shift-C-i"): K("Shift-C-c"),
    K("Shift-C-o"): K("Shift-C-r"),
    K("Shift-C-p"): K("Shift-C-l"),
    K("Shift-C-s"): K("Shift-C-o"),
    K("Shift-C-d"): K("Shift-C-e"),
    K("Shift-C-f"): K("Shift-C-u"),
    K("Shift-C-g"): K("Shift-C-i"),
    K("Shift-C-h"): K("Shift-C-d"),
    K("Shift-C-j"): K("Shift-C-h"),
    K("Shift-C-k"): K("Shift-C-t"),
    K("Shift-C-l"): K("Shift-C-n"),
    K("Shift-C-x"): K("Shift-C-q"),
    K("Shift-C-c"): K("Shift-C-j"),
    K("Shift-C-v"): K("Shift-C-k"),
    K("Shift-C-b"): K("Shift-C-x"),
    K("Shift-C-n"): K("Shift-C-b"),
    K("Shift-C-w"): K("Shift-C-comma"),
    K("Shift-C-e"): K("Shift-C-dot"),
    K("Shift-C-comma"): K("Shift-C-w"),
    K("Shift-C-dot"): K("Shift-C-v"),
    K("Shift-C-slash"): K("Shift-C-z"),
    K("Shift-C-semicolon"): K("Shift-C-s"),
    K("Shift-C-minus"): K("Shift-C-right_brace"),
    K("Shift-C-equal"): K("Shift-C-backslash"),
    K("Shift-C-left_brace"): K("Shift-C-slash"),
    K("Shift-C-insert"): K("Shift-C-backspace"),
    K("Shift-M-r"): K("Shift-M-p"),
    K("Shift-M-t"): K("Shift-M-y"),
    K("Shift-M-y"): K("Shift-M-f"),
    K("Shift-M-u"): K("Shift-M-g"),
    K("Shift-M-i"): K("Shift-M-c"),
    K("Shift-M-o"): K("Shift-M-r"),
    K("Shift-M-p"): K("Shift-M-l"),
    K("Shift-M-s"): K("Shift-M-o"),
    K("Shift-M-d"): K("Shift-M-e"),
    K("Shift-M-f"): K("Shift-M-u"),
    K("Shift-M-g"): K("Shift-M-i"),
    K("Shift-M-h"): K("Shift-M-d"),
    K("Shift-M-j"): K("Shift-M-h"),
    K("Shift-M-k"): K("Shift-M-t"),
    K("Shift-M-l"): K("Shift-M-n"),
    K("Shift-M-x"): K("Shift-M-q"),
    K("Shift-M-c"): K("Shift-M-j"),
    K("Shift-M-v"): K("Shift-M-k"),
    K("Shift-M-b"): K("Shift-M-x"),
    K("Shift-M-n"): K("Shift-M-b"),
    K("Shift-M-w"): K("Shift-M-comma"),
    K("Shift-M-e"): K("Shift-M-dot"),
    K("Shift-M-comma"): K("Shift-M-w"),
    K("Shift-M-dot"): K("Shift-M-v"),
    K("Shift-M-slash"): K("Shift-M-z"),
    K("Shift-M-semicolon"): K("Shift-M-s"),
    K("Shift-M-minus"): K("Shift-M-right_brace"),
    K("Shift-M-equal"): K("Shift-M-backslash"),
    K("Shift-M-left_brace"): K("Shift-M-slash"),
    K("Shift-M-insert"): K("Shift-M-backspace"),
    K("Shift-Win-r"): K("Shift-Win-p"),
    K("Shift-Win-t"): K("Shift-Win-y"),
    K("Shift-Win-y"): K("Shift-Win-f"),
    K("Shift-Win-u"): K("Shift-Win-g"),
    K("Shift-Win-i"): K("Shift-Win-c"),
    K("Shift-Win-o"): K("Shift-Win-r"),
    K("Shift-Win-p"): K("Shift-Win-l"),
    K("Shift-Win-s"): K("Shift-Win-o"),
    K("Shift-Win-d"): K("Shift-Win-e"),
    K("Shift-Win-f"): K("Shift-Win-u"),
    K("Shift-Win-g"): K("Shift-Win-i"),
    K("Shift-Win-h"): K("Shift-Win-d"),
    K("Shift-Win-j"): K("Shift-Win-h"),
    K("Shift-Win-k"): K("Shift-Win-t"),
    K("Shift-Win-l"): K("Shift-Win-n"),
    K("Shift-Win-x"): K("Shift-Win-q"),
    K("Shift-Win-c"): K("Shift-Win-j"),
    K("Shift-Win-v"): K("Shift-Win-k"),
    K("Shift-Win-b"): K("Shift-Win-x"),
    K("Shift-Win-n"): K("Shift-Win-b"),
    K("Shift-Win-w"): K("Shift-Win-comma"),
    K("Shift-Win-e"): K("Shift-Win-dot"),
    K("Shift-Win-comma"): K("Shift-Win-w"),
    K("Shift-Win-dot"): K("Shift-Win-v"),
    K("Shift-Win-slash"): K("Shift-Win-z"),
    K("Shift-Win-semicolon"): K("Shift-Win-s"),
    K("Shift-Win-minus"): K("Shift-Win-right_brace"),
    K("Shift-Win-equal"): K("Shift-Win-backslash"),
    K("Shift-Win-left_brace"): K("Shift-Win-slash"),
    K("Shift-Win-insert"): K("Shift-Win-backspace"),
    K("C-M-r"): K("C-M-p"),
    K("C-M-t"): K("C-M-y"),
    K("C-M-y"): K("C-M-f"),
    K("C-M-u"): K("C-M-g"),
    K("C-M-i"): K("C-M-c"),
    K("C-M-o"): K("C-M-r"),
    K("C-M-p"): K("C-M-l"),
    K("C-M-s"): K("C-M-o"),
    K("C-M-d"): K("C-M-e"),
    K("C-M-f"): K("C-M-u"),
    K("C-M-g"): K("C-M-i"),
    K("C-M-h"): K("C-M-d"),
    K("C-M-j"): K("C-M-h"),
    K("C-M-k"): K("C-M-t"),
    K("C-M-l"): K("C-M-n"),
    K("C-M-x"): K("C-M-q"),
    K("C-M-c"): K("C-M-j"),
    K("C-M-v"): K("C-M-k"),
    K("C-M-b"): K("C-M-x"),
    K("C-M-n"): K("C-M-b"),
    K("C-M-w"): K("C-M-comma"),
    K("C-M-e"): K("C-M-dot"),
    K("C-M-comma"): K("C-M-w"),
    K("C-M-dot"): K("C-M-v"),
    K("C-M-slash"): K("C-M-z"),
    K("C-M-semicolon"): K("C-M-s"),
    K("C-M-minus"): K("C-M-right_brace"),
    K("C-M-equal"): K("C-M-backslash"),
    K("C-M-left_brace"): K("C-M-slash"),
    K("C-M-insert"): K("C-M-backspace"),
    K("C-Win-r"): K("C-p"),
    K("C-Win-t"): K("C-y"),
    K("C-Win-y"): K("C-f"),
    K("C-Win-u"): K("C-g"),
    K("C-Win-i"): K("C-c"),
    K("C-Win-o"): K("C-r"),
    K("C-Win-p"): K("C-l"),
    K("C-Win-s"): K("C-o"),
    K("C-Win-d"): K("C-e"),
    K("C-Win-f"): K("C-u"),
    K("C-Win-g"): K("C-i"),
    K("C-Win-h"): K("C-d"),
    K("C-Win-j"): K("C-h"),
    K("C-Win-k"): K("C-t"),
    K("C-Win-l"): K("C-n"),
    K("C-Win-x"): K("C-q"),
    K("C-Win-c"): K("C-j"),
    K("C-Win-v"): K("C-k"),
    K("C-Win-b"): K("C-x"),
    K("C-Win-n"): K("C-b"),
    K("C-Win-w"): K("C-comma"),
    K("C-Win-e"): K("C-dot"),
    K("C-Win-comma"): K("C-w"),
    K("C-Win-dot"): K("C-v"),
    K("C-Win-slash"): K("C-z"),
    K("C-Win-semicolon"): K("C-s"),
    K("C-Win-minus"): K("C-right_brace"),
    K("C-Win-equal"): K("C-backslash"),
    K("C-Win-left_brace"): K("C-slash"),
    K("C-Win-insert"): K("C-backspace"),
    K("M-Win-r"): K("M-Win-p"),
    K("M-Win-t"): K("M-Win-y"),
    K("M-Win-y"): K("M-Win-f"),
    K("M-Win-u"): K("M-Win-g"),
    K("M-Win-i"): K("M-Win-c"),
    K("M-Win-o"): K("M-Win-r"),
    K("M-Win-p"): K("M-Win-l"),
    K("M-Win-s"): K("M-Win-o"),
    K("M-Win-d"): K("M-Win-e"),
    K("M-Win-f"): K("M-Win-u"),
    K("M-Win-g"): K("M-Win-i"),
    K("M-Win-h"): K("M-Win-d"),
    K("M-Win-j"): K("M-Win-h"),
    K("M-Win-k"): K("M-Win-t"),
    K("M-Win-l"): K("M-Win-n"),
    K("M-Win-x"): K("M-Win-q"),
    K("M-Win-c"): K("M-Win-j"),
    K("M-Win-v"): K("M-Win-k"),
    K("M-Win-b"): K("M-Win-x"),
    K("M-Win-n"): K("M-Win-b"),
    K("M-Win-w"): K("M-Win-comma"),
    K("M-Win-e"): K("M-Win-dot"),
    K("M-Win-comma"): K("M-Win-w"),
    K("M-Win-dot"): K("M-Win-v"),
    K("M-Win-slash"): K("M-Win-z"),
    K("M-Win-semicolon"): K("M-Win-s"),
    K("M-Win-minus"): K("M-Win-right_brace"),
    K("M-Win-equal"): K("M-Win-backslash"),
    K("M-Win-left_brace"): K("M-Win-slash"),
    K("M-Win-insert"): K("M-Win-backspace"),
    K("Shift-C-M-r"): K("Shift-C-M-p"),
    K("Shift-C-M-t"): K("Shift-C-M-y"),
    K("Shift-C-M-y"): K("Shift-C-M-f"),
    K("Shift-C-M-u"): K("Shift-C-M-g"),
    K("Shift-C-M-i"): K("Shift-C-M-c"),
    K("Shift-C-M-o"): K("Shift-C-M-r"),
    K("Shift-C-M-p"): K("Shift-C-M-l"),
    K("Shift-C-M-s"): K("Shift-C-M-o"),
    K("Shift-C-M-d"): K("Shift-C-M-e"),
    K("Shift-C-M-f"): K("Shift-C-M-u"),
    K("Shift-C-M-g"): K("Shift-C-M-i"),
    K("Shift-C-M-h"): K("Shift-C-M-d"),
    K("Shift-C-M-j"): K("Shift-C-M-h"),
    K("Shift-C-M-k"): K("Shift-C-M-t"),
    K("Shift-C-M-l"): K("Shift-C-M-n"),
    K("Shift-C-M-x"): K("Shift-C-M-q"),
    K("Shift-C-M-c"): K("Shift-C-M-j"),
    K("Shift-C-M-v"): K("Shift-C-M-k"),
    K("Shift-C-M-b"): K("Shift-C-M-x"),
    K("Shift-C-M-n"): K("Shift-C-M-b"),
    K("Shift-C-M-w"): K("Shift-C-M-comma"),
    K("Shift-C-M-e"): K("Shift-C-M-dot"),
    K("Shift-C-M-comma"): K("Shift-C-M-w"),
    K("Shift-C-M-dot"): K("Shift-C-M-v"),
    K("Shift-C-M-slash"): K("Shift-C-M-z"),
    K("Shift-C-M-semicolon"): K("Shift-C-M-s"),
    K("Shift-C-M-minus"): K("Shift-C-M-right_brace"),
    K("Shift-C-M-equal"): K("Shift-C-M-backslash"),
    K("Shift-C-M-left_brace"): K("Shift-C-M-slash"),
    K("Shift-C-M-insert"): K("Shift-C-M-backspace"),
    K("Shift-C-Win-r"): K("Shift-C-p"),
    K("Shift-C-Win-t"): K("Shift-C-y"),
    K("Shift-C-Win-y"): K("Shift-C-f"),
    K("Shift-C-Win-u"): K("Shift-C-g"),
    K("Shift-C-Win-i"): K("Shift-C-c"),
    K("Shift-C-Win-o"): K("Shift-C-r"),
    K("Shift-C-Win-p"): K("Shift-C-l"),
    K("Shift-C-Win-s"): K("Shift-C-o"),
    K("Shift-C-Win-d"): K("Shift-C-e"),
    K("Shift-C-Win-f"): K("Shift-C-u"),
    K("Shift-C-Win-g"): K("Shift-C-i"),
    K("Shift-C-Win-h"): K("Shift-C-d"),
    K("Shift-C-Win-j"): K("Shift-C-h"),
    K("Shift-C-Win-k"): K("Shift-C-t"),
    K("Shift-C-Win-l"): K("Shift-C-n"),
    K("Shift-C-Win-x"): K("Shift-C-q"),
    K("Shift-C-Win-c"): K("Shift-C-j"),
    K("Shift-C-Win-v"): K("Shift-C-k"),
    K("Shift-C-Win-b"): K("Shift-C-x"),
    K("Shift-C-Win-n"): K("Shift-C-b"),
    K("Shift-C-Win-w"): K("Shift-C-comma"),
    K("Shift-C-Win-e"): K("Shift-C-dot"),
    K("Shift-C-Win-comma"): K("Shift-C-w"),
    K("Shift-C-Win-dot"): K("Shift-C-v"),
    K("Shift-C-Win-slash"): K("Shift-C-z"),
    K("Shift-C-Win-semicolon"): K("Shift-C-s"),
    K("Shift-C-Win-minus"): K("Shift-C-right_brace"),
    K("Shift-C-Win-equal"): K("Shift-C-backslash"),
    K("Shift-C-Win-left_brace"): K("Shift-C-slash"),
    K("Shift-C-Win-insert"): K("Shift-C-backspace"),
    K("Shift-M-Win-r"): K("Shift-M-Win-p"),
    K("Shift-M-Win-t"): K("Shift-M-Win-y"),
    K("Shift-M-Win-y"): K("Shift-M-Win-f"),
    K("Shift-M-Win-u"): K("Shift-M-Win-g"),
    K("Shift-M-Win-i"): K("Shift-M-Win-c"),
    K("Shift-M-Win-o"): K("Shift-M-Win-r"),
    K("Shift-M-Win-p"): K("Shift-M-Win-l"),
    K("Shift-M-Win-s"): K("Shift-M-Win-o"),
    K("Shift-M-Win-d"): K("Shift-M-Win-e"),
    K("Shift-M-Win-f"): K("Shift-M-Win-u"),
    K("Shift-M-Win-g"): K("Shift-M-Win-i"),
    K("Shift-M-Win-h"): K("Shift-M-Win-d"),
    K("Shift-M-Win-j"): K("Shift-M-Win-h"),
    K("Shift-M-Win-k"): K("Shift-M-Win-t"),
    K("Shift-M-Win-l"): K("Shift-M-Win-n"),
    K("Shift-M-Win-x"): K("Shift-M-Win-q"),
    K("Shift-M-Win-c"): K("Shift-M-Win-j"),
    K("Shift-M-Win-v"): K("Shift-M-Win-k"),
    K("Shift-M-Win-b"): K("Shift-M-Win-x"),
    K("Shift-M-Win-n"): K("Shift-M-Win-b"),
    K("Shift-M-Win-w"): K("Shift-M-Win-comma"),
    K("Shift-M-Win-e"): K("Shift-M-Win-dot"),
    K("Shift-M-Win-comma"): K("Shift-M-Win-w"),
    K("Shift-M-Win-dot"): K("Shift-M-Win-v"),
    K("Shift-M-Win-slash"): K("Shift-M-Win-z"),
    K("Shift-M-Win-semicolon"): K("Shift-M-Win-s"),
    K("Shift-M-Win-minus"): K("Shift-M-Win-right_brace"),
    K("Shift-M-Win-equal"): K("Shift-M-Win-backslash"),
    K("Shift-M-Win-left_brace"): K("Shift-M-Win-slash"),
    K("Shift-M-Win-insert"): K("Shift-M-Win-backspace"),
    K("C-M-Win-r"): K("C-M-Win-p"),
    K("C-M-Win-t"): K("C-M-Win-y"),
    K("C-M-Win-y"): K("C-M-Win-f"),
    K("C-M-Win-u"): K("C-M-Win-g"),
    K("C-M-Win-i"): K("C-M-Win-c"),
    K("C-M-Win-o"): K("C-M-Win-r"),
    K("C-M-Win-p"): K("C-M-Win-l"),
    K("C-M-Win-s"): K("C-M-Win-o"),
    K("C-M-Win-d"): K("C-M-Win-e"),
    K("C-M-Win-f"): K("C-M-Win-u"),
    K("C-M-Win-g"): K("C-M-Win-i"),
    K("C-M-Win-h"): K("C-M-Win-d"),
    K("C-M-Win-j"): K("C-M-Win-h"),
    K("C-M-Win-k"): K("C-M-Win-t"),
    K("C-M-Win-l"): K("C-M-Win-n"),
    K("C-M-Win-x"): K("C-M-Win-q"),
    K("C-M-Win-c"): K("C-M-Win-j"),
    K("C-M-Win-v"): K("C-M-Win-k"),
    K("C-M-Win-b"): K("C-M-Win-x"),
    K("C-M-Win-n"): K("C-M-Win-b"),
    K("C-M-Win-w"): K("C-M-Win-comma"),
    K("C-M-Win-e"): K("C-M-Win-dot"),
    K("C-M-Win-comma"): K("C-M-Win-w"),
    K("C-M-Win-dot"): K("C-M-Win-v"),
    K("C-M-Win-slash"): K("C-M-Win-z"),
    K("C-M-Win-semicolon"): K("C-M-Win-s"),
    K("C-M-Win-minus"): K("C-M-Win-right_brace"),
    K("C-M-Win-equal"): K("C-M-Win-backslash"),
    K("C-M-Win-left_brace"): K("C-M-Win-slash"),
    K("C-M-Win-insert"): K("C-M-Win-backspace"),
    K("q"): K("Shift-key_7"),
    K("Shift-q"): K("Shift-key_2"),
    K("z"): K("semicolon"),
    K("Shift-z"): K("apostrophe"),
    K("Shift-key_2"): K("left_brace"),
    K("Shift-key_6"): K("equal"),
    K("Shift-key_7"): K("Shift-key_6"),
    K("Shift-key_8"): K("Shift-apostrophe"),
    K("Shift-key_9"): K("Shift-key_8"),
    K("Shift-key_0"): K("Shift-key_9"),
    K("minus"): K("right_brace"),
    K("backspace"): K("Shift-left_brace"),
    K("Shift-backspace"): K("Shift-equal"),
    K("apostrophe"): K("minus"),
    K("Shift-apostrophe"): K("Shift-ro"),
    K("right_brace"): K("Shift-minus"),
    K("Shift-right_brace"): K("Shift-semicolon"),
    K("C-q"): K("C-Shift-key_7"),
    K("C-Shift-q"): K("C-Shift-key_2"),
    K("C-z"): K("C-semicolon"),
    K("C-Shift-z"): K("C-apostrophe"),
    K("C-Shift-key_2"): K("C-left_brace"),
    K("C-Shift-key_6"): K("C-equal"),
    K("C-Shift-key_7"): K("C-Shift-key_6"),
    K("C-Shift-key_8"): K("C-Shift-apostrophe"),
    K("C-Shift-key_9"): K("C-Shift-key_8"),
    K("C-Shift-key_0"): K("C-Shift-key_9"),
    K("C-minus"): K("C-right_brace"),
    K("C-backspace"): K("C-Shift-left_brace"),
    K("C-Shift-backspace"): K("C-Shift-equal"),
    K("C-apostrophe"): K("C-minus"),
    K("C-Shift-apostrophe"): K("C-Shift-ro"),
    K("C-right_brace"): K("C-Shift-minus"),
    K("C-Shift-right_brace"): K("C-Shift-semicolon"),
    K("M-q"): K("M-Shift-key_7"),
    K("M-Shift-q"): K("M-Shift-key_2"),
    K("M-z"): K("M-semicolon"),
    K("M-Shift-z"): K("M-apostrophe"),
    K("M-Shift-key_2"): K("M-left_brace"),
    K("M-Shift-key_6"): K("M-equal"),
    K("M-Shift-key_7"): K("M-Shift-key_6"),
    K("M-Shift-key_8"): K("M-Shift-apostrophe"),
    K("M-Shift-key_9"): K("M-Shift-key_8"),
    K("M-Shift-key_0"): K("M-Shift-key_9"),
    K("M-minus"): K("M-right_brace"),
    K("M-backspace"): K("M-Shift-left_brace"),
    K("M-Shift-backspace"): K("M-Shift-equal"),
    K("M-apostrophe"): K("M-minus"),
    K("M-Shift-apostrophe"): K("M-Shift-ro"),
    K("M-right_brace"): K("M-Shift-minus"),
    K("M-Shift-right_brace"): K("M-Shift-semicolon"),
    K("Win-q"): K("Win-Shift-key_7"),
    K("Win-Shift-q"): K("Win-Shift-key_2"),
    K("Win-z"): K("Win-semicolon"),
    K("Win-Shift-z"): K("Win-apostrophe"),
    K("Win-Shift-key_2"): K("Win-left_brace"),
    K("Win-Shift-key_6"): K("Win-equal"),
    K("Win-Shift-key_7"): K("Win-Shift-key_6"),
    K("Win-Shift-key_8"): K("Win-Shift-apostrophe"),
    K("Win-Shift-key_9"): K("Win-Shift-key_8"),
    K("Win-Shift-key_0"): K("Win-Shift-key_9"),
    K("Win-minus"): K("Win-right_brace"),
    K("Win-backspace"): K("Win-Shift-left_brace"),
    K("Win-Shift-backspace"): K("Win-Shift-equal"),
    K("Win-apostrophe"): K("Win-minus"),
    K("Win-Shift-apostrophe"): K("Win-Shift-ro"),
    K("Win-right_brace"): K("Win-Shift-minus"),
    K("Win-Shift-right_brace"): K("Win-Shift-semicolon"),
    K("C-M-q"): K("C-M-Shift-key_7"),
    K("C-M-Shift-q"): K("C-M-Shift-key_2"),
    K("C-M-z"): K("C-M-semicolon"),
    K("C-M-Shift-z"): K("C-M-apostrophe"),
    K("C-M-Shift-key_2"): K("C-M-left_brace"),
    K("C-M-Shift-key_6"): K("C-M-equal"),
    K("C-M-Shift-key_7"): K("C-M-Shift-key_6"),
    K("C-M-Shift-key_8"): K("C-M-Shift-apostrophe"),
    K("C-M-Shift-key_9"): K("C-M-Shift-key_8"),
    K("C-M-Shift-key_0"): K("C-M-Shift-key_9"),
    K("C-M-minus"): K("C-M-right_brace"),
    K("C-M-backspace"): K("C-M-Shift-left_brace"),
    K("C-M-Shift-backspace"): K("C-M-Shift-equal"),
    K("C-M-apostrophe"): K("C-M-minus"),
    K("C-M-Shift-apostrophe"): K("C-M-Shift-ro"),
    K("C-M-right_brace"): K("C-M-Shift-minus"),
    K("C-M-Shift-right_brace"): K("C-M-Shift-semicolon"),
    K("C-Win-q"): K("C-Shift-key_7"),
    K("C-Win-Shift-q"): K("C-Shift-key_2"),
    K("C-Win-z"): K("C-semicolon"),
    K("C-Win-Shift-z"): K("C-apostrophe"),
    K("C-Win-Shift-key_2"): K("C-left_brace"),
    K("C-Win-Shift-key_6"): K("C-equal"),
    K("C-Win-Shift-key_7"): K("C-Shift-key_6"),
    K("C-Win-Shift-key_8"): K("C-Shift-apostrophe"),
    K("C-Win-Shift-key_9"): K("C-Shift-key_8"),
    K("C-Win-Shift-key_0"): K("C-Shift-key_9"),
    K("C-Win-minus"): K("C-right_brace"),
    K("C-Win-backspace"): K("C-Shift-left_brace"),
    K("C-Win-Shift-backspace"): K("C-Shift-equal"),
    K("C-Win-apostrophe"): K("C-minus"),
    K("C-Win-Shift-apostrophe"): K("C-Shift-ro"),
    K("C-Win-right_brace"): K("C-Shift-minus"),
    K("C-Win-Shift-right_brace"): K("C-Shift-semicolon"),
    K("M-Win-q"): K("M-Win-Shift-key_7"),
    K("M-Win-Shift-q"): K("M-Win-Shift-key_2"),
    K("M-Win-z"): K("M-Win-semicolon"),
    K("M-Win-Shift-z"): K("M-Win-apostrophe"),
    K("M-Win-Shift-key_2"): K("M-Win-left_brace"),
    K("M-Win-Shift-key_6"): K("M-Win-equal"),
    K("M-Win-Shift-key_7"): K("M-Win-Shift-key_6"),
    K("M-Win-Shift-key_8"): K("M-Win-Shift-apostrophe"),
    K("M-Win-Shift-key_9"): K("M-Win-Shift-key_8"),
    K("M-Win-Shift-key_0"): K("M-Win-Shift-key_9"),
    K("M-Win-minus"): K("M-Win-right_brace"),
    K("M-Win-backspace"): K("M-Win-Shift-left_brace"),
    K("M-Win-Shift-backspace"): K("M-Win-Shift-equal"),
    K("M-Win-apostrophe"): K("M-Win-minus"),
    K("M-Win-Shift-apostrophe"): K("M-Win-Shift-ro"),
    K("M-Win-right_brace"): K("M-Win-Shift-minus"),
    K("M-Win-Shift-right_brace"): K("M-Win-Shift-semicolon"),
    K("C-M-Win-q"): K("C-M-Win-Shift-key_7"),
    K("C-M-Win-Shift-q"): K("C-M-Win-Shift-key_2"),
    K("C-M-Win-z"): K("C-M-Win-semicolon"),
    K("C-M-Win-Shift-z"): K("C-M-Win-apostrophe"),
    K("C-M-Win-Shift-key_2"): K("C-M-Win-left_brace"),
    K("C-M-Win-Shift-key_6"): K("C-M-Win-equal"),
    K("C-M-Win-Shift-key_7"): K("C-M-Win-Shift-key_6"),
    K("C-M-Win-Shift-key_8"): K("C-M-Win-Shift-apostrophe"),
    K("C-M-Win-Shift-key_9"): K("C-M-Win-Shift-key_8"),
    K("C-M-Win-Shift-key_0"): K("C-M-Win-Shift-key_9"),
    K("C-M-Win-minus"): K("C-M-Win-right_brace"),
    K("C-M-Win-backspace"): K("C-M-Win-Shift-left_brace"),
    K("C-M-Win-Shift-backspace"): K("C-M-Win-Shift-equal"),
    K("C-M-Win-apostrophe"): K("C-M-Win-minus"),
    K("C-M-Win-Shift-apostrophe"): K("C-M-Win-Shift-ro"),
    K("C-M-Win-right_brace"): K("C-M-Win-Shift-minus"),
    K("C-M-Win-Shift-right_brace"): K("C-M-Win-Shift-semicolon")
}, "Global")
