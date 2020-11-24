import fpm_tablut_player.configs as CONFIGS

from fpm_tablut_player.libraries.game_state import GameState

###


class GameMove:
    fromCell: str
    toCell: str
    turn: str

    def __init__(self):
        self.fromCell = None
        self.toCell = None
        self.turn = str(CONFIGS.APP_ROLE)

    def __computeMoveForGoingFromStartToEnd(self, start: GameState, end: GameState) -> (str, str):
        # TODO: missing code.
        # ...
        fromCell = "d1"
        toCell = "d2"
        return (fromCell, toCell)

    ###

    def fromStartToEnd(self, start: GameState, end: GameState):
        (fromCell, toCell) = self.__computeMoveForGoingFromStartToEnd(start, end)
        self.fromCell = fromCell
        self.toCell = toCell

        return self

    def export(self):
        return {
            "from": self.fromCell,
            "to": self.toCell,
            "turn": self.turn
        }
