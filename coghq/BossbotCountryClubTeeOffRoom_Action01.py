# Fuck you Disyer. Stealing my fucking paypal. GET FUCKED: toontown.coghq.BossbotCountryClubTeeOffRoom_Action01
from panda3d.core import Point3, Vec3, Vec4
from toontown.coghq.SpecImports import *
GlobalEntities = {1000: {'type': 'levelMgr',
        'name': 'LevelMgr',
        'comment': '',
        'parentEntId': 0,
        'cogLevel': 0,
        'farPlaneDistance': 1500,
        'modelFilename': 'phase_12/models/bossbotHQ/BossbotTeeOffRoom',
        'wantDoors': 1},
 0: {'type': 'zone',
     'name': 'UberZone',
     'comment': '',
     'parentEntId': 0,
     'scale': 1,
     'description': '',
     'visibility': []},
 110100: {'type': 'door',
          'name': 'TeeOffExitDoor',
          'comment': '',
          'parentEntId': 110001,
          'pos': Point3(0, 0, 0),
          'hpr': Point3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'color': Vec4(1, 1, 1, 1),
          'isLock0Unlocked': 1,
          'isLock1Unlocked': 0,
          'isLock2Unlocked': 1,
          'isLock3Unlocked': 1,
          'isOpen': 0,
          'isOpenEvent': 0,
          'isVisBlocker': 0,
          'secondsOpen': 1,
          'unlock0Event': 0,
          'unlock1Event': 110102,
          'unlock2Event': 0,
          'unlock3Event': 0},
 110102: {'type': 'moleField',
          'name': '<unnamed>',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(-38.6164, -26.2922, 0),
          'hpr': Vec3(0, 0, 0),
          'scale': Vec3(1, 1, 1),
          'numSquaresX': 6,
          'numSquaresY': 6,
          'spacingX': 10.0,
          'spacingY': 10.0,
          'timeToPlay': 60,
          'molesBase': 4,
          'molesPerPlayer': 2},
 10002: {'type': 'nodepath',
         'name': 'props',
         'comment': '',
         'parentEntId': 0,
         'pos': Point3(0, 0, 0),
         'hpr': Vec3(0, 0, 0),
         'scale': 1},
 110001: {'type': 'nodepath',
          'name': 'doorParent',
          'comment': '',
          'parentEntId': 0,
          'pos': Point3(60.2682, 0.55914, 0),
          'hpr': Vec3(270, 0, 0),
          'scale': Vec3(1, 1, 1)}}
Scenario0 = {}
levelSpec = {'globalEntities': GlobalEntities,
 'scenarios': [Scenario0]}