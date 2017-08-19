# Fuck you Disyer. Stealing my fucking paypal. GET FUCKED: toontown.dna.DNASignGraphic
from panda3d.core import LVector4, LVector4f
import DNANode
import DNAUtil

class DNASignGraphic(DNANode.DNANode):
    COMPONENT_CODE = 8

    def __init__(self, name):
        DNANode.DNANode.__init__(self, name)
        self.code = ''
        self.color = LVector4f(1, 1, 1, 1)
        self.width = 0
        self.height = 0
        self.bDefaultColor = True

    def setCode(self, code):
        self.code = code

    def getCode(self):
        return self.code

    def setWidth(self, width):
        self.width = width

    def getWidth(self):
        return self.width

    def setHeight(self, height):
        self.height = height

    def getHeight(self):
        return self.height

    def setColor(self, color):
        self.color = color
        self.bDefaultColor = False

    def getColor(self):
        return self.color

    def makeFromDGI(self, dgi):
        DNANode.DNANode.makeFromDGI(self, dgi)
        self.code = DNAUtil.dgiExtractString8(dgi)
        self.color = DNAUtil.dgiExtractColor(dgi)
        self.width = dgi.getInt16() / 100.0
        self.height = dgi.getInt16() / 100.0
        self.bDefaultColor = dgi.getBool()

    def traverse(self, nodePath, dnaStorage):
        node = assetStorage.findNode(self.code, self.getName())
        node.reparentTo(nodePath, 0)
        node.setScale(self.scale)
        node.setScale(node, self.getParent().scale)
        node.setPosHpr(self.getParent().pos, self.getParent().hpr)
        node.setDepthOffset(10)
        node.setPos(node, 0, -0.1, 0)
        node.setColor(self.color)
        node.flattenStrong()
        for child in self.children:
            child.traverse(node, dnaStorage)