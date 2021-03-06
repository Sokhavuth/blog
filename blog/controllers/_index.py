from .. import config
from copy import deepcopy
from datetime import datetime
from pytz import timezone
from .. models import Post

def call():
    kdict = deepcopy(config.kdict)
    kdict['datetime'] = datetime.now(timezone('Asia/Phnom_Penh'))
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    kdict['posts'] = queryset
    
    return kdict