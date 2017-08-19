# Fuck you Disyer. Stealing my fucking paypal. GET FUCKED: toontown.ai.HolidayDecorator
from panda3d.core import NodePath, TransformState, TransparencyAttrib, Vec4
from direct.interval.IntervalGlobal import Parallel, Sequence, Func, Wait

class HolidayDecorator:

    def __init__(self):
        self.swapIval = None
        return

    def exit(self):
        if self.swapIval is not None and self.swapIval.isPlaying():
            self.swapIval.finish()
        return

    def decorate(self):
        self.swapIval = self.getSwapVisibleIval()
        if self.swapIval:
            self.swapIval.start()

    def undecorate(self):
        self.swapIval = self.getSwapVisibleIval()
        if self.swapIval:
            self.swapIval.start()

    def getSwapVisibleIval(self, wait = 5.0, tFadeOut = 3.0, tFadeIn = 3.0):
        loader = base.cr.playGame.hood.loader
        npl = render.findAllMatches('**/=DNARoot=holiday_prop;+s')
        p = Parallel()
        for i in xrange(npl.getNumPaths()):
            np = npl.getPath(i)
            np.setTransparency(TransparencyAttrib.MDual, 1)
            if not np.hasTag('DNACode'):
                continue
            dnaCode = np.getTag('DNACode')
            dnaNode = assetStorage.findNode(dnaCode)
            if dnaNode.isEmpty():
                continue
            newNP = dnaNode.copyTo(np.getParent())
            newNP.setTag('DNARoot', 'holiday_prop')
            newNP.setTag('DNACode', dnaCode)
            newNP.setColorScale(1, 1, 1, 0)
            newNP.setTransparency(TransparencyAttrib.MDual, 1)
            if np.hasTag('transformIndex'):
                index = int(np.getTag('transformIndex'))
                transform = loader.holidayPropTransforms.get(index, TransformState.makeIdentity())
                newNP.setTransform(NodePath(), transform)
                newNP.setTag('transformIndex', `index`)
            s = Sequence(Wait(wait), np.colorScaleInterval(tFadeOut, Vec4(1, 1, 1, 0), startColorScale=Vec4(1, 1, 1, 1), blendType='easeInOut'), Func(np.detachNode), Func(np.clearTransparency), newNP.colorScaleInterval(tFadeOut, Vec4(1, 1, 1, 1), startColorScale=Vec4(1, 1, 1, 0), blendType='easeInOut'), Func(newNP.clearTransparency), Func(newNP.clearColorScale))
            p.append(s)

        return p