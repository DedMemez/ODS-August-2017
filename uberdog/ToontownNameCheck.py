# Fuck you Disyer. Stealing my fucking paypal. GET FUCKED: toontown.uberdog.ToontownNameCheck
from panda3d.core import TextEncoder
from otp.otpbase import OTPLocalizer
from toontown.toon import NPCToons
Blacklist = ['aeolus',
 'ahole',
 'anal',
 'anilingus',
 'anorexia',
 'anorexic',
 'anus',
 'areola',
 'areole',
 'arian',
 'arrse',
 'arse',
 'aryan',
 'ass',
 'azazel',
 'azz',
 'baal',
 'babe',
 'ballbag',
 'balls',
 'bang',
 'barf',
 'bawdy',
 'beaner',
 'beardedclam',
 'beastial',
 'beatch',
 'beater',
 'beaver',
 'beer',
 'beeyotch',
 'bellend',
 'beotch',
 'bestial',
 'biatch',
 'bimbo',
 'bitch',
 'blew',
 'bloody',
 'blow',
 'bod',
 'boink',
 'boiolas',
 'bollock',
 'bollok',
 'bone',
 'bong',
 'boob',
 'booger',
 'bookie',
 'booky',
 'booobs',
 'boooobs',
 'booooobs',
 'booooooobs',
 'bootee',
 'bootie',
 'booty',
 'booze',
 'boozy',
 'bosom',
 'bowel',
 'bra',
 'breast',
 'buceta',
 'bugger',
 'bukkake',
 'bulimia',
 'bulimiic',
 'bum',
 'bung',
 'burp',
 'bush',
 'busty',
 'butt',
 'caca',
 'cahone',
 'cameltoe',
 'carnal',
 'carpetmuncher',
 'cawk',
 'cervix',
 'chieur',
 'chieuse',
 'chinc',
 'chink',
 'chode',
 'cipa',
 'climax',
 'clit',
 'cnut',
 'cocain',
 'cock',
 'coital',
 'cok',
 'commie',
 'condom',
 'connard',
 'conne',
 'coon',
 'corpse',
 'coven',
 'cox',
 'crabs',
 'crack',
 'crap',
 'cuervo',
 'cum',
 'cunilingus',
 'cunillingus',
 'cunnilingus',
 'cunny',
 'cunt',
 'cyalis',
 'cyberfuc',
 'dago',
 'dammit',
 'damn',
 'dick',
 'diddle',
 'dike',
 'dildo',
 'diligaf',
 'dimwit',
 'dingle',
 'dink',
 'dirsa',
 'dlck',
 'doggin',
 'dong',
 'donkeyribber',
 'doofus',
 'doosh',
 'dopey',
 'douche',
 'drunk',
 'duche',
 'dummy',
 'dyke',
 'ejaculate',
 'ejaculating',
 'ejaculation',
 'ejakulate',
 'enculer',
 'enlargement',
 'erect',
 'erotic',
 'essohbee',
 'exotic',
 'extacy',
 'extasy',
 'fack',
 'faerie',
 'faery',
 'fag',
 'faig',
 'fairy',
 'fanny',
 'fanyy',
 'fart',
 'fcuk',
 'feck',
 'felch',
 'fellate',
 'fellatio',
 'feltch',
 'fisted',
 'fisting',
 'fisty',
 'flange',
 'floozy',
 'foad',
 'fondle',
 'foobar',
 'fook',
 'foreskin',
 'frack',
 'freex',
 'frigg',
 'fubar',
 'fuck',
 'fudgepacker',
 'fuk',
 'fux',
 'fvck',
 'fxck',
 'gae',
 'gai',
 'ganja',
 'gay',
 'gey',
 'gfy',
 'ghay',
 'ghey',
 'gigolo',
 'glans',
 'goatse',
 'god',
 'goldenshower',
 'gook',
 'gtfo',
 'handjob',
 'hebe',
 'hell',
 'hemp',
 'heroin',
 'herp',
 'heshe',
 'hijack',
 'hitler',
 'hiv',
 'hoar',
 'hobag',
 'hoer',
 'homey',
 'homo',
 'honky',
 'hooch',
 'hookah',
 'hooker',
 'hoor',
 'hootch',
 'hooter',
 'hore',
 'horniest',
 'horny',
 'hump',
 'hussy',
 'hymen',
 'inbred',
 'incest',
 'injun',
 'jackhole',
 'jackoff',
 'jap',
 'jerk',
 'jism',
 'jiz',
 'junkie',
 'junky',
 'kawk',
 'kike',
 'kill',
 'kinky',
 'kkk',
 'klan',
 'kock',
 'kondum',
 'kooch',
 'kootch',
 'kraut',
 'kum',
 'kunilingus',
 'kyke',
 'labia',
 'lech',
 'leper',
 'lesbians',
 'lesbos',
 'lez',
 'lmao',
 'lmfao',
 'loin',
 'lsd',
 'lube',
 'lul',
 'lust',
 'mams',
 'marijuana',
 'masochist',
 'masterbat',
 'masturbate',
 'masturbating',
 'masturbation',
 'maxi',
 'menses',
 'menstruate',
 'menstruation',
 'merde',
 'meth',
 'mofo',
 'molest',
 'moolie',
 'moron',
 'muff',
 'murder',
 'mutha',
 'muther',
 'nad',
 'naked',
 'napalm',
 'nappy',
 'nazi',
 'negro',
 'nigga',
 'nigger',
 'niggle',
 'nimrod',
 'ninny',
 'nipple',
 'nique',
 'nob',
 'nooky',
 'numbnuts',
 'nutsack',
 'nympho',
 'opiate',
 'opium',
 'oral',
 'organ',
 'orgasim',
 'orgasm',
 'orgies',
 'orgy',
 'ovary',
 'ovum',
 'paddy',
 'pantie',
 'panty',
 'pastie',
 'pasty',
 'pawn',
 'pcp',
 'pecker',
 'pedo',
 'pee',
 'penetrate',
 'penetration',
 'penial',
 'penile',
 'penis',
 'perversion',
 'peyote',
 'phalli',
 'phallus',
 'phuck',
 'phuk',
 'phuq',
 'pillowbiter',
 'pimp',
 'pinko',
 'piss',
 'pms',
 'polack',
 'poop',
 'porn',
 'pot',
 'prick',
 'prig',
 'pron',
 'prude',
 'pube',
 'pubic',
 'pubis',
 'punky',
 'puss',
 'putain',
 'pute',
 'queaf',
 'queef',
 'queer',
 'quicky',
 'quim',
 'racist',
 'racy',
 'rape',
 'rapist',
 'raunch',
 'rectal',
 'rectum',
 'rectus',
 'reefer',
 'reich',
 'revue',
 'rimjaw',
 'rimming',
 'risque',
 'rum',
 'sadism',
 'sadist',
 'salaud',
 'salop',
 'satan',
 'scag',
 'scantily',
 'schizo',
 'schlong',
 'screw',
 'scroat',
 'scrog',
 'scrot',
 'scrud',
 'seaman',
 'seamen',
 'seduce',
 'semen',
 'sex',
 'shag',
 'shamedame',
 'shemale',
 'shit',
 'shiz',
 'sissy',
 'skag',
 'skank',
 'slave',
 'sleaze',
 'sleazy',
 'slut',
 'smegma',
 'smut',
 'snatch',
 'sniper',
 'snuff',
 'sodom',
 'souse',
 'spac',
 'sperm',
 'spic',
 'spik',
 'spooge',
 'spunk',
 'stab',
 'steamy',
 'stfu',
 'stiffy',
 'stoned',
 'strip',
 'stroke',
 'suck',
 'tampon',
 'tard',
 'tawdry',
 'teabagging',
 'teat',
 'teets',
 'teez',
 'terd',
 'teste',
 'testical',
 'testicle',
 'testis',
 'thrust',
 'thug',
 'tinkle',
 'tit',
 'toke',
 'toots',
 'tosser',
 'tramp',
 'trashy',
 'tubgirl',
 'turd',
 'tush',
 'twat',
 'twunt',
 'undies',
 'unwed',
 'urinal',
 'urine',
 'uterus',
 'uzi',
 'vag',
 'valium',
 'viagra',
 'virgin',
 'vixen',
 'vodka',
 'vomit',
 'voyeur',
 'vulgar',
 'vulva',
 'wad',
 'wang',
 'wank',
 'wazoo',
 'wedgie',
 'weed',
 'weenie',
 'weewee',
 'weiner',
 'weirdo',
 'wench',
 'wetback',
 'whitey',
 'whiz',
 'whoring',
 'wigger',
 'willies',
 'willy',
 'womb',
 'woody',
 'wop',
 'wtf',
 'xrated',
 'xxx',
 'yeasty',
 'yobbo',
 'zoophile']

def _sanityName(name):
    return TextEncoder().encodeWtext(name).strip()


def _checkNpcNames(name):
    name = _sanityName(name).lower()
    for npcId in NPCToons.NPCToonDict.keys():
        npcName = NPCToons.NPCToonDict[npcId][1]
        if npcName.lower() == name:
            return OTPLocalizer.NCGeneric


def _checkBlacklist(name):
    name = _sanityName(name).lower()
    for word in name.split(' '):
        for blacklisted in Blacklist:
            if blacklisted in word:
                return OTPLocalizer.NCGeneric


def getExtraChecks():
    return [_checkNpcNames, _checkBlacklist]