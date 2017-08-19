# Fuck you Disyer. Stealing my fucking paypal. GET FUCKED: toontown.toon.ToonAvatarPanel
from panda3d.core import TextNode, Vec4
from direct.gui.DirectGui import *
from direct.showbase import DirectObject
import ToonHead
import LaffMeter
from otp.avatar import Avatar
from direct.distributed import DistributedObject
from direct.directnotify import DirectNotifyGlobal
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import TTLocalizer
from toontown.friends import ToontownFriendSecret
import ToonAvatarDetailPanel
import AvatarPanelBase
from toontown.toontowngui import TTDialog
from otp.otpbase import OTPGlobals

class ToonAvatarPanel(AvatarPanelBase.AvatarPanelBase):
    notify = DirectNotifyGlobal.directNotify.newCategory('ToonAvatarPanel')

    def __init__(self, avatar):
        from toontown.friends import FriendsListPanel
        if base.cr.doId2do.get(avatar.getDoId()):
            avatar = base.cr.doId2do.get(avatar.getDoId())
        AvatarPanelBase.AvatarPanelBase.__init__(self, avatar, FriendsListPanel=FriendsListPanel)
        self.notify.debug('Opening toon panel, avId=%d' % self.avId)
        self.laffMeter = None
        wantsLaffMeter = hasattr(avatar, 'hp')
        if not hasattr(avatar, 'style'):
            self.notify.warning("Avatar has no 'style'. Abort initialization.")
            AvatarPanelBase.AvatarPanelBase.cleanup(self)
            return
        else:
            base.localAvatar.obscureFriendsListButton(1)
            self.petButton = None
            self.castDialog = None
            self.frame = DirectFrame(base.a2dTopRight, image=Preloaded['detailPanel'], relief=None, pos=(-0.22, 0, -0.47))
            self.disabledImageColor = Vec4(1, 1, 1, 0.4)
            self.text0Color = Vec4(1, 1, 1, 1)
            self.text1Color = Vec4(0.5, 1, 0.5, 1)
            self.text2Color = Vec4(1, 1, 0.5, 1)
            self.text3Color = Vec4(0.6, 0.6, 0.6, 1)
            self.head = self.frame.attachNewNode('head')
            self.head.setPos(0.02, 0, 0.31)
            self.headModel = ToonHead.ToonHead()
            self.headModel.setupHead(avatar.style, forGui=1)
            self.headModel.fitAndCenterHead(0.175, forGui=1)
            self.headModel.reparentTo(self.head)
            self.headModel.startBlink()
            self.headModel.startLookAround()
            self.healthText = DirectLabel(parent=self.frame, text='', pos=(0.06, 0, 0.2), text_pos=(0, 0), text_scale=0.05)
            self.healthText.hide()
            self.nameLabel = DirectLabel(parent=self.frame, pos=(0.0125, 0, 0.4), relief=None, text=self.avName, text_font=avatar.getFont(), text_fg=Vec4(0, 0, 0, 1), text_pos=(0, 0), text_scale=0.042, text_wordwrap=7.5, text_shadow=(1, 1, 1, 1))
            self.closeButton = DirectButton(parent=self.frame, image=Preloaded['closeButton'], relief=None, pos=(0.157644, 0, -0.379167), command=self.__handleClose)
            self.friendButton = DirectButton(parent=self.frame, image=Preloaded['detailFriends'], image3_color=self.disabledImageColor, image_scale=0.9, relief=None, text=TTLocalizer.AvatarPanelFriends, text_scale=0.06, pos=(-0.103, 0, 0.133), text0_fg=self.text0Color, text1_fg=self.text1Color, text2_fg=self.text2Color, text3_fg=self.text3Color, text_pos=(0.06, -0.02), text_align=TextNode.ALeft, command=self.__handleFriend)
            self.goToButton = DirectButton(parent=self.frame, image=Preloaded['detailGo'], image3_color=self.disabledImageColor, image_scale=0.9, relief=None, pos=(-0.103, 0, 0.045), text=TTLocalizer.AvatarPanelGoTo, text0_fg=self.text0Color, text1_fg=self.text1Color, text2_fg=self.text2Color, text3_fg=self.text3Color, text_scale=0.06, text_pos=(0.06, -0.015), text_align=TextNode.ALeft, command=self.__handleGoto)
            self.whisperButton = DirectButton(parent=self.frame, image=Preloaded['detailWhisper'], image3_color=self.disabledImageColor, image_scale=0.9, relief=None, pos=(-0.103, 0, -0.0375), text=TTLocalizer.AvatarPanelWhisper, text0_fg=self.text0Color, text1_fg=self.text1Color, text2_fg=self.text2Color, text3_fg=self.text3Color, text_scale=TTLocalizer.TAPwhisperButton, text_pos=(0.06, -0.0125), text_align=TextNode.ALeft, command=self.__handleWhisper)
            self.trueFriendsButton = DirectButton(parent=self.frame, image=Preloaded['detailTrueFriends'], image3_color=self.disabledImageColor, image_scale=0.9, relief=None, pos=(-0.103, 0, -0.13), text=TTLocalizer.AvatarPanelTrueFriends, text0_fg=self.text0Color, text1_fg=self.text1Color, text2_fg=self.text2Color, text3_fg=self.text3Color, text_scale=TTLocalizer.TAPtruefriendsButton, text_pos=(0.055, -0.01), text_align=TextNode.ALeft, command=self.__handleTrueFriends)
            ignoreStr, ignoreCmd, ignoreScale = self.getIgnoreButtonInfo()
            self.ignoreButton = DirectButton(parent=self.frame, image=Preloaded['detailIgnore'], image3_color=self.disabledImageColor, image_scale=0.9, relief=None, pos=(-0.103697, 0, -0.21), text=ignoreStr, text0_fg=self.text0Color, text1_fg=self.text1Color, text2_fg=self.text2Color, text3_fg=self.text3Color, text_scale=ignoreScale, text_pos=(0.06, -0.015), text_align=TextNode.ALeft, command=ignoreCmd)
            self.reportButton = DirectButton(parent=self.frame, image=Preloaded['detailReport'], image3_color=self.disabledImageColor, image_scale=0.65, relief=None, pos=(-0.103, 0, -0.29738), text=TTLocalizer.AvatarPanelReport, text0_fg=self.text0Color, text1_fg=self.text1Color, text2_fg=self.text2Color, text3_fg=self.text3Color, text_scale=0.06, text_pos=(0.06, -0.015), text_align=TextNode.ALeft, command=self.handleReport)
            if base.localAvatar.isIgnored(self.avId):
                self.friendButton['state'] = DGG.DISABLED
                self.goToButton['state'] = DGG.DISABLED
                self.whisperButton['state'] = DGG.DISABLED
                self.trueFriendsButton['state'] = DGG.DISABLED
            if not base.localAvatar.isTeleportAllowed():
                self.goToButton['state'] = DGG.DISABLED
            self.detailButton = DirectButton(parent=self.frame, image=Preloaded['detailDetail'], relief=None, text=('',
             TTLocalizer.AvatarPanelDetail,
             TTLocalizer.AvatarPanelDetail,
             ''), text_fg=self.text2Color, text_shadow=(0, 0, 0, 1), text_scale=0.055, text_pos=(-0.075, -0.01), text_align=TextNode.ARight, pos=(-0.133773, 0, -0.395), command=self.__handleDetails)
            self.__makeBoardingGui()
            self.__makePetGui(avatar)
            self.__checkGroupStatus()
            if wantsLaffMeter:
                self.__makeLaffMeter(avatar)
                self.__updateHp(avatar.hp, avatar.maxHp)
                self.healthText.show()
                self.laffMeter.show()
            menuX = -0.05
            menuScale = 0.064
            if self.avGenerateName:
                self.accept(self.avGenerateName, self.__handleGenerateAvatar)
            if self.avHpChangeName:
                self.accept(self.avHpChangeName, self.__updateHp)
            self.accept('updateStaffPanel', self.__makePetGui)
            self.accept('updateLaffMeter', self.__updateLaffMeter)
            self.accept('updateGroupStatus', self.__checkGroupStatus)
            self.frame.show()
            messenger.send('avPanelDone')
            return

    def disableAll(self):
        self.detailButton['state'] = DGG.DISABLED
        self.reportButton['state'] = DGG.DISABLED
        self.ignoreButton['state'] = DGG.DISABLED
        self.goToButton['state'] = DGG.DISABLED
        self.trueFriendsButton['state'] = DGG.DISABLED
        self.whisperButton['state'] = DGG.DISABLED
        self.petButton['state'] = DGG.DISABLED
        self.friendButton['state'] = DGG.DISABLED
        self.closeButton['state'] = DGG.DISABLED
        self.groupButton['state'] = DGG.DISABLED
        self.boardingInfoButton['state'] = DGG.DISABLED

    def cleanup(self):
        if not hasattr(self, 'frame') or self.frame == None:
            return
        else:
            self.notify.debug('Clean up toon panel, avId=%d' % self.avId)
            if self.frame:
                self.frame.destroy()
                del self.frame
            self.frame = None
            ToonAvatarDetailPanel.unloadAvatarDetail()
            if self.groupButton:
                self.groupButton.destroy()
                del self.groupButton
            self.groupButton = None
            if self.boardingInfoButton:
                self.boardingInfoButton.destroy()
                del self.boardingInfoButton
            self.boardingInfoButton = None
            if self.boardingInfoText:
                self.boardingInfoText.destroy()
                del self.boardingInfoText
            self.boardingInfoText = None
            if self.groupFrame:
                self.groupFrame.destroy()
                del self.groupFrame
            self.groupFrame = None
            self.head.removeNode()
            del self.head
            self.headModel.stopBlink()
            self.headModel.stopLookAroundNow()
            self.headModel.delete()
            del self.headModel
            base.localAvatar.obscureFriendsListButton(-1)
            self.laffMeter = None
            self.ignoreAll()
            if hasattr(self.avatar, 'bFake') and self.avatar.bFake:
                self.avatar.delete()
            base.setCellsAvailable([base.rightCells[0]], 1)
            self.cleanupCastDialog()
            AvatarPanelBase.AvatarPanelBase.cleanup(self)
            return

    def __handleGoto(self):
        if base.localAvatar.isTeleportAllowed():
            base.localAvatar.chatMgr.noWhisper()
            messenger.send('gotoAvatar', [self.avId, self.avName, self.avDisableName])

    def __handleToPet(self):
        toonAvatar = self.avatar
        if base.cr.doId2do.get(toonAvatar.getDoId()):
            toonAvatar = base.cr.doId2do.get(toonAvatar.getDoId())
        petAvatar = base.cr.doId2do.get(toonAvatar.getPetId())
        self.disableAll()
        from toontown.pets import PetDetail
        PetDetail.PetDetail(toonAvatar.getPetId(), self.__petDetailsLoaded)

    def __petDetailsLoaded(self, avatar):
        self.cleanup()
        if avatar:
            self.notify.debug("Looking at someone's pet. pet doId = %s" % avatar.doId)
            messenger.send('clickedNametag', [avatar])

    def __handleWhisper(self):
        base.localAvatar.chatMgr.whisperTo(self.avName, self.avId)

    def __handleTrueFriends(self):
        base.localAvatar.chatMgr.noWhisper()
        ToontownFriendSecret.showFriendSecret()

    def __handleFriend(self):
        base.localAvatar.chatMgr.noWhisper()
        messenger.send('friendAvatar', [self.avId, self.avName, self.avDisableName])

    def __handleDetails(self):
        base.localAvatar.chatMgr.noWhisper()
        messenger.send('avatarDetails', [self.avId, self.avName])

    def __handleDisableAvatar(self):
        if not base.cr.isFriend(self.avId):
            self.cleanup()
            AvatarPanelBase.currentAvatarPanel = None
        else:
            self.healthText.hide()
            if self.laffMeter != None:
                self.laffMeter.stop()
                self.laffMeter.destroy()
                self.laffMeter = None
        return

    def __handleGenerateAvatar(self, avatar):
        newAvatar = base.cr.doId2do.get(self.avatar.doId)
        if newAvatar:
            self.avatar = newAvatar
        self.__makePetGui()
        self.__updateLaffMeter(avatar, avatar.hp, avatar.maxHp)
        self.__checkGroupStatus()

    def __updateLaffMeter(self, avatar, hp, maxHp):
        if self.laffMeter == None:
            self.__makeLaffMeter(avatar)
        self.__updateHp(avatar.hp, avatar.maxHp)
        self.laffMeter.show()
        self.healthText.show()
        return

    def __makeLaffMeter(self, avatar):
        self.laffMeter = LaffMeter.LaffMeter(avatar.style, avatar.hp, avatar.maxHp)
        self.laffMeter.reparentTo(self.frame)
        self.laffMeter.setPos(-0.1, 0, 0.24)
        self.laffMeter.setScale(0.03)

    def __updateHp(self, hp, maxHp, quietly = 0):
        if self.laffMeter != None and hp != None and maxHp != None:
            self.laffMeter.adjustFace(hp, maxHp)
            self.healthText['text'] = '%d / %d' % (hp, maxHp)
        return

    def __handleClose(self):
        self.cleanup()
        AvatarPanelBase.currentAvatarPanel = None
        if self.friendsListShown:
            self.FriendsListPanel.showFriendsList()
        return

    def getAvId(self):
        if hasattr(self, 'avatar'):
            if self.avatar:
                return self.avatar.doId

    def isHidden(self):
        if not hasattr(self, 'frame') or not self.frame:
            return 1
        return self.frame.isHidden()

    def getType(self):
        return 'toon'

    def handleInvite(self):
        if localAvatar.boardingParty.isInviteePanelUp():
            localAvatar.boardingParty.showMe(TTLocalizer.BoardingPendingInvite, pos=(0, 0, 0))
        else:
            self.groupButton['state'] = DGG.DISABLED
            localAvatar.boardingParty.requestInvite(self.avId)

    def handleKick(self):
        if not base.cr.playGame.getPlace().getState() == 'elevator':
            self.confirmKickOutDialog = TTDialog.TTDialog(style=TTDialog.YesNo, text=TTLocalizer.BoardingKickOutConfirm % self.avName, command=self.__confirmKickOutCallback)
            self.confirmKickOutDialog.show()

    def __confirmKickOutCallback(self, value):
        if self.confirmKickOutDialog:
            self.confirmKickOutDialog.destroy()
        self.confirmKickOutDialog = None
        if value > 0:
            if self.groupButton:
                self.groupButton['state'] = DGG.DISABLED
            localAvatar.boardingParty.requestKick(self.avId)
        return

    def __checkGroupStatus(self):
        self.groupFrame.hide()
        if hasattr(self, 'avatar'):
            if self.avatar and hasattr(self.avatar, 'getZoneId') and localAvatar.getZoneId() == self.avatar.getZoneId():
                if localAvatar.boardingParty:
                    if self.avId in localAvatar.boardingParty.getGroupMemberList(localAvatar.doId):
                        if localAvatar.boardingParty.getGroupLeader(localAvatar.doId) == localAvatar.doId:
                            self.groupButton['text'] = ('', TTLocalizer.AvatarPanelGroupMemberKick, TTLocalizer.AvatarPanelGroupMemberKick)
                            self.groupButton['image'] = Preloaded['kickButton']
                            self.groupButton['command'] = self.handleKick
                            self.groupButton['state'] = DGG.NORMAL
                        else:
                            self.groupButton['text'] = ('', TTLocalizer.AvatarPanelGroupMember, TTLocalizer.AvatarPanelGroupMember)
                            self.groupButton['command'] = None
                            self.groupButton['image'] = Preloaded['inviteDisabledButton']
                            self.groupButton['image_color'] = Vec4(1, 1, 1, 0.4)
                            self.groupButton['state'] = DGG.NORMAL
                    else:
                        g1 = localAvatar.boardingParty.countInGroup(self.avId)
                        g2 = localAvatar.boardingParty.countInGroup(localAvatar.doId)
                        if g1 + g2 > localAvatar.boardingParty.maxSize:
                            self.groupButton['text'] = ('', TTLocalizer.AvatarPanelGroupMember, TTLocalizer.AvatarPanelGroupMember)
                            self.groupButton['command'] = None
                            self.groupButton['image'] = Preloaded['inviteDisabledButton']
                            self.groupButton['image_color'] = Vec4(1, 1, 1, 0.4)
                        else:
                            if g1 > 0 and g2 > 0:
                                self.groupButton['text'] = ('', TTLocalizer.AvatarPanelGroupInvite, '%s %d' % (TTLocalizer.AvatarPanelGroupMerge, g1 + g2))
                                self.groupFrame['text'] = TTLocalizer.BoardingPartyTitleMerge
                            else:
                                self.groupButton['text'] = ('', TTLocalizer.AvatarPanelGroupInvite, TTLocalizer.AvatarPanelGroupInvite)
                                self.groupFrame['text'] = TTLocalizer.BoardingPartyTitle
                            self.groupButton['command'] = self.handleInvite
                            self.groupButton['image'] = Preloaded['inviteButton']
                        self.groupButton['state'] = DGG.NORMAL
                    if config.GetBool('want-boarding-groups', 1):
                        base.setCellsAvailable([base.rightCells[0]], 0)
                        self.groupFrame.show()
        return

    def handleReadInfo(self, task = None):
        self.boardingInfoButton['state'] = DGG.DISABLED
        if self.boardingInfoText:
            self.boardingInfoText.destroy()
        self.boardingInfoText = TTDialog.TTDialog(style=TTDialog.Acknowledge, text=TTLocalizer.BoardingPartyInform % localAvatar.boardingParty.maxSize, command=self.handleCloseInfo)

    def handleCloseInfo(self, *extraArgs):
        self.boardingInfoButton['state'] = DGG.NORMAL
        if self.boardingInfoText:
            self.boardingInfoText.destroy()
            del self.boardingInfoText
        self.boardingInfoText = None
        return

    def __makePetGui(self, avatar = None):
        if not avatar:
            avatar = self.avatar
        if self.petButton:
            self.petButton.removeNode()
        if self.avatar.isAdmin() and self.avatar.getStaffPanel().isEnabled():
            self.petButton = DirectButton(parent=self.frame, image=Preloaded['purpleHelpButton'], relief=None, pos=(0.02, -0.2, -0.385), text=('',
             TTLocalizer.AvatarPanelCast,
             TTLocalizer.AvatarPanelCast,
             ''), text_fg=self.text2Color, scale=0.8, text_shadow=(0, 0, 0, 1), text_scale=0.07, text_pos=(0, -0.125), text_align=TextNode.ACenter, command=self.__handleCastDialog)
            return
        else:
            self.petButton = DirectButton(parent=self.frame, image=Preloaded['detailPet'], geom=Preloaded['petIcon'], geom3_color=self.disabledImageColor, relief=None, pos=(0.22, -0.2, -0.475), text=('',
             TTLocalizer.AvatarPanelPet,
             TTLocalizer.AvatarPanelPet,
             ''), text_fg=self.text2Color, text_shadow=(0, 0, 0, 1), text_scale=0.325, text_pos=(-1.3, 0.05), scale=0.15, text_align=TextNode.ACenter, command=self.__handleToPet)
            if not (base.wantPets and avatar.hasPet()):
                self.petButton['state'] = DGG.DISABLED
                self.petButton.hide()
            return

    def __handleCastDialog(self):
        if self.castDialog:
            return
        base.cr.playGame.getPlace().setState('stopped')
        self.castDialog = self.avatar.getStaffPanel().getGui(self.avatar.getAdminAccess(), self.__cleanupCastDialogAndWalk)

    def cleanupCastDialog(self):
        if self.castDialog:
            self.castDialog.destroy()
            self.castDialog = None
        return

    def __cleanupCastDialogAndWalk(self):
        self.cleanupCastDialog()
        base.cr.playGame.getPlace().fsm.request('walk')

    def __makeBoardingGui(self):
        self.confirmKickOutDialog = None
        self.groupFrame = DirectFrame(parent=self.frame, relief=None, image=Preloaded['boardingBg'], image_scale=(0.5, 1, 0.5), textMayChange=1, text=TTLocalizer.BoardingPartyTitle, text_wordwrap=16, text_scale=TTLocalizer.TAPgroupFrame, text_pos=(0.01, 0.08), pos=(0, 0, -0.61))
        self.groupButton = DirectButton(parent=self.groupFrame, image=Preloaded['inviteButton'], image3_color=self.disabledImageColor, image_scale=0.85, relief=None, text=('', TTLocalizer.AvatarPanelGroupInvite, TTLocalizer.AvatarPanelGroupInvite), text0_fg=self.text0Color, text1_fg=self.text1Color, text2_fg=self.text2Color, text3_fg=self.text3Color, text_scale=TTLocalizer.TAPgroupButton, text_pos=(-0.0, -0.1), text_align=TextNode.ACenter, command=self.handleInvite, pos=(0.01013, 0, -0.05464))
        self.boardingInfoButton = DirectButton(parent=self.groupFrame, relief=None, text_pos=(-0.05, 0.05), text_scale=0.06, text_align=TextNode.ALeft, text_fg=Vec4(1, 1, 1, 1), text_shadow=Vec4(0, 0, 0, 1), image=Preloaded['purpleHelpButton'], image_scale=(0.5, 1, 0.5), image3_color=self.disabledImageColor, scale=1.05, command=self.handleReadInfo, pos=(0.1829, 0, 0.02405))
        self.boardingInfoText = None
        return