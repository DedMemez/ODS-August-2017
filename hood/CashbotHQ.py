# Fuck you Disyer. Stealing my fucking paypal. GET FUCKED: toontown.hood.CashbotHQ
from panda3d.core import Lens
from toontown.coghq.CashbotCogHQLoader import CashbotCogHQLoader
from toontown.toonbase import ToontownGlobals, TTLocalizer
from toontown.hood.CogHood import CogHood
from toontown.hood import ZoneUtil

class CashbotHQ(CogHood):
    notify = directNotify.newCategory('CashbotHQ')
    ID = ToontownGlobals.CashbotHQ
    LOADER_CLASS = CashbotCogHQLoader
    SKY_FILE = 'phase_3.5/models/props/TT_sky'

    def enter(self, requestStatus):
        CogHood.enter(self, requestStatus)
        base.localAvatar.setCameraFov(ToontownGlobals.CogHQCameraFov)
        base.camLens.setNearFar(ToontownGlobals.CashbotHQCameraNear, ToontownGlobals.CashbotHQCameraFar)

    def spawnTitleText(self, zoneId, floorNum = None):
        if ZoneUtil.isMintInteriorZone(zoneId):
            text = '%s\n%s' % (ToontownGlobals.StreetNames[zoneId][-1], TTLocalizer.MintFloorTitle % (floorNum + 1))
            self.doSpawnTitleText(text)
            return
        CogHood.spawnTitleText(self, zoneId)