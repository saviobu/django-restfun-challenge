from enum import Enum

class OrderStatus(Enum):
    WAITING = "WAITING"
    READY = "READY"
    CANCELED = "CANCELED"

    @classmethod
    def Selected(selection):
        return tuple((status_selected.name, status_selected.value) for status_selected in selection)