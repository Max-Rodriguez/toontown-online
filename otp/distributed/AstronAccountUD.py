from direct.directnotify import DirectNotifyGlobal
from direct.distributed.DistributedObjectUD import DistributedObjectUD


class AstronAccountUD(DistributedObjectUD):
    notify = DirectNotifyGlobal.directNotify.newCategory('AstronAccountUD')
