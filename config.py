import re
from xkeysnail.transform import *

define_keymap(re.compile("Firefox|Google-chrome"), {
    # Ctrl+Alt+j/k to switch next/previous tab
    K("M-j"): K("C-TAB"),
    K("M-q"): K("C-Shift-TAB"),
}, "Firefox and Chrome")

define_modmap({
    Key.CAPSLOCK: Key.LEFT_CTRL,
})

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
    K("Shift-r"): K("Shift-p"),
    K("T"): K("Y"),
    K("Y"): K("F"),
    K("U"): K("G"),
    K("I"): K("C"),
    K("O"): K("R"),
    K("P"): K("L"),
    K("S"): K("O"),
    K("D"): K("E"),
    K("F"): K("U"),
    K("G"): K("I"),
    K("H"): K("D"),
    K("J"): K("H"),
    K("K"): K("T"),
    K("L"): K("N"),
    K("X"): K("Q"),
    K("C"): K("J"),
    K("V"): K("K"),
    K("B"): K("X"),
    K("N"): K("B"),

    K("q"): K("Shift-key_7"),
    K("Shift-q"): K("Shift-key_2"),
    K("w"): K("comma"),
    K("Shift-w"): K("Shift-comma"),
    K("e"): K("dot"),
    K("Shift-e"): K("Shift-dot"),
    K("z"): K("semicolon"),
    K("Shift-z"): K("apostrophe"),

    K("comma"): K("w"),
    K("Shift-comma"): K("Shift-w"),
    K("dot"): K("v"),
    K("Shift-dot"): K("Shift-v"),
    K("slash"): K("z"),
    K("Shift-slash"): K("Shift-z"),
    K("semicolon"): K("s"),
    K("Shift-semicolon"): K("Shift-s")

}, "Global")
