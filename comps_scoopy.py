import os, enum
from enum import unique
from types import MappingProxyType



@unique
class prof_s(enum.Enum):
    X_MOZ_FP = ["Mozilla", "Firefox", "Profiles\\"]


class os_mtd():

    __slots__ = ["operatingsystem"]

    def __init__(self):
        self.operatingsystem = os
    
   
    def make_fpath(self, *args, data) -> str:
        forward_slashpath = "".join(("\%s" % x for x in args))
        full_paths =  os.environ.get("APPDATA", "notget")
        pathsgets = full_paths + forward_slashpath if full_paths != "notget" else "notokey"
        pathgets = {"path": pathsgets, "gotit": 'N' if pathsgets == "notokey" else 'Y'}
        return pathgets[data]

    def close_paths(self):
        self.operatingsystem.close()



def get_rpths(pths):
    match pths:
        case "Y":
            try:
                mydata, l = {''}, os_mtd()
                for x, _, _ in os.walk(l.make_fpath(*prof_s.X_MOZ_FP.value, data="path")):
                    mydata.add(str(x.split("storage")[0]))
                for x in range(0, len(mydata) - 1): mydata.pop()
                get_dt = list(str(mydata).split("\\"))
                gdata = "".join([x for x in get_dt[get_dt.index("Profiles") + 1:get_dt.index("Profiles") + 1 + 2]  if len(x) != 0 ])
                return MappingProxyType(l.make_fpath(*prof_s.X_MOZ_FP.value, data="path")  + gdata + "\places.sqlite")
            except: 
                return ""
        case "N":
            return "can't fetch the path..."
        case "_":
            return "///"