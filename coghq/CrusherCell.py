# Fuck you Disyer. Stealing my fucking paypal. GET FUCKED: toontown.coghq.CrusherCell
import ActiveCell
from direct.directnotify import DirectNotifyGlobal

class CrusherCell(ActiveCell.ActiveCell):
    notify = DirectNotifyGlobal.directNotify.newCategory('CrusherCell')

    def __init__(self, cr):
        ActiveCell.ActiveCell.__init__(self, cr)