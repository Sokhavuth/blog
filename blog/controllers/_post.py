from .. import config
from copy import deepcopy
from datetime import datetime
from pytz import timezone
from .. models import Post

def call(slug):
    kdict = deepcopy(config.kdict)
    kdict['datetime'] = datetime.now(timezone('Asia/Phnom_Penh'))
    queryset = Post.objects.filter(slug=slug)
    kdict['post'] = queryset

    return kdict