# Fuck you Disyer. Stealing my fucking paypal. GET FUCKED: toontown.coghq.DistributedBarrelBase
from panda3d.core import CollideMask, CollisionNode, CollisionSphere, NodePath
from direct.interval.IntervalGlobal import *
from toontown.toonbase.ToontownGlobals import *
from toontown.coghq import BarrelBase
from otp.level import BasicEntities

class DistributedBarrelBase(BasicEntities.DistributedNodePathEntity, BarrelBase.BarrelBase):

    def __init__(self, cr):
        BasicEntities.DistributedNodePathEntity.__init__(self, cr)
        self.grabSoundPath = 'phase_4/audio/sfx/SZ_DD_treasure.ogg'
        self.rejectSoundPath = 'phase_4/audio/sfx/ring_miss.ogg'
        self.rewardPerGrabMax = 0
        self.animTrack = None
        self.barrelScale = 0.5
        self.sphereRadius = 4.2
        self.gagNode = None
        self.barrel = None
        return

    def disable(self):
        BasicEntities.DistributedNodePathEntity.disable(self)
        self.ignoreAll()
        if self.animTrack:
            self.animTrack.pause()
            self.animTrack = None
        return

    def setEntId(self, entId):
        self.entId = entId

    def delete(self):
        BasicEntities.DistributedNodePathEntity.delete(self)
        self.gagNode.removeNode()
        del self.gagNode
        if self.barrel:
            self.barrel.removeNode()
            self.barrel = None
        return

    def announceGenerate(self):
        BasicEntities.DistributedNodePathEntity.announceGenerate(self)
        self.setTag('doId', str(self.getDoId()))
        self.loadModel()
        self.collSphere = CollisionSphere(0, 0, 0, self.sphereRadius)
        self.collSphere.setTangible(0)
        self.collNode = CollisionNode(self.uniqueName('barrelSphere'))
        self.collNode.setIntoCollideMask(WallBitmask)
        self.collNode.addSolid(self.collSphere)
        self.collNodePath = self.barrel.attachNewNode(self.collNode)
        self.collNodePath.hide()
        self.applyLabel()
        self.accept(self.uniqueName('enterbarrelSphere'), self.handleEnterSphere)
        messenger.send('barrel-generated', [self])

    def loadModel(self):
        self.grabSound = loader.loadSfx(self.grabSoundPath)
        self.rejectSound = loader.loadSfx(self.rejectSoundPath)
        self.barrel = loader.loadModel('phase_4/models/cogHQ/gagTank')
        self.barrel.setScale(self.barrelScale)
        self.barrel.reparentTo(self)
        dcsNode = self.barrel.find('**/gagLabelDCS')
        dcsNode.setColor(0.15, 0.15, 0.1)
        self.gagNode = self.barrel.attachNewNode('gagNode')
        self.gagNode.setPosHpr(0.0, -2.62, 4.0, 0, 0, 0)
        self.gagNode.setColorScale(0.7, 0.7, 0.6, 1)

    def handleEnterSphere(self, collEntry = None):
        localAvId = base.localAvatar.getDoId()
        self.d_requestGrab()

    def d_requestGrab(self):
        self.sendUpdate('requestGrab', [])

    def setGrab(self, avId, reward):
        if not avId:
            return
        else:
            self.avId = avId
            if avId == base.localAvatar.doId:
                self.ignore(self.uniqueName('enterbarrelSphere'))
                self.barrel.setColorScale(0.5, 0.5, 0.5, 1)
            if self.animTrack:
                self.animTrack.finish()
                self.animTrack = None
            base.playSfx(self.grabSound)
            self.animTrack = Sequence(LerpScaleInterval(self.barrel, 0.2, 1.1 * self.barrelScale, blendType='easeInOut'), LerpScaleInterval(self.barrel, 0.2, self.barrelScale, blendType='easeInOut'), Func(self.resetBarrel), name=self.uniqueName('animTrack'))
            self.animTrack.start()
            return

    def resetBarrel(self):
        self.barrel.setScale(self.barrelScale)

    def forceDisable(self):
        self.ignore(self.uniqueName('enterbarrelSphere'))
        self.barrel.setColorScale(0.5, 0.5, 0.5, 1)
        base.playSfx(self.rejectSound)