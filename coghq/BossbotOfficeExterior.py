# Fuck you Disyer. Stealing my fucking paypal. GET FUCKED: toontown.coghq.BossbotOfficeExterior
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
from direct.fsm import State
from toontown.toonbase import ToontownGlobals
from toontown.building import Elevator
import FactoryExterior

class BossbotOfficeExterior(FactoryExterior.FactoryExterior):
    notify = DirectNotifyGlobal.directNotify.newCategory('LawbotOfficeExterior')

    def enterWalk(self, teleportIn = 0):
        FactoryExterior.FactoryExterior.enterWalk(self, teleportIn)
        self.ignore('teleportQuery')
        base.localAvatar.setTeleportAvailable(0)