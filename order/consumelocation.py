from enum import Enum

class ConsumeLocation(Enum):
    TAKEAWAY = "TAKEAWAY"
    INSHOP = "INSHOP"

    @classmethod
    def Selected(selection):
        return tuple((status_selected.name, status_selected.value) for status_selected in selection)