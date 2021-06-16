from inspect import getmembers, isfunction

from Webpanel import Webpanel
print(getmembers(Webpanel, isfunction))
