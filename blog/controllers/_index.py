from .. import config
from copy import deepcopy
from datetime import datetime
from pytz import timezone


def call():
    kdict = deepcopy(config.kdict)
    kdict['datetime'] = datetime.now(timezone('Asia/Phnom_Penh'))
    
    return kdict