import re
from xkeysnail.transform import *

define_modmap({
    Key.GRAVE: Key.ESC,
    Key.TAB: Key.LEFT_ALT,
    Key.CAPSLOCK: Key.LEFT_CTRL,
    Key.RO: Key.RIGHT_SHIFT,
    Key.BACKSLASH: Key.RIGHT_CTRL,
    Key.ENTER: Key.RIGHT_ALT,
    Key.INSERT: Key.BACKSPACE,

    Key.RIGHT_BRACE: Key.EQUAL,
    Key.PAUSE: Key.EQUAL,

    Key.R: Key.P,
    Key.T: Key.Y,
    Key.Y: Key.F,
    Key.U: Key.G,
})
