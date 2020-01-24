#!/usr/bin/env python3

import sys

from softwarebude import intro
from softwarebude.game import Game

if __name__ == "__main__":
    try:
        player_name = intro.play()
        Game(player_name).play()
    except KeyboardInterrupt:
        sys.exit(0)
