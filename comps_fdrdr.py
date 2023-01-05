import  re
from tkinter import *
import os
from comps_scoopy import *

def half_screen(z,ww,hh):
        global w,h 
        w,h = z.winfo_screenwidth(),z.winfo_screenheight()
        z.geometry("{}x{}+{}+{}".format(ww, hh, int((w/2) - (ww/1.9)), int((h/2.2) - (hh/2))))

okey = Tk()
st = okey
st.overrideredirect(True)
st.config(background="#EC6008")
half_screen(st,413,231)
l = PhotoImage(file='.\{0}'.format("splash.png"))
z = Label(st, image=l, background="#fff")
z.pack()
z.after(3000,st.destroy)
st.mainloop()



def pns_s():
    pn = []
    with open("ho.txt", "r") as m:
        for x in m.read().split("\n"):
            pn.append(x)
    return pn



def scoopy():
    RE_URL = "https(?=:).{0,3}.\w*.?\w+.{0,3}."
    pp = []
    with (
        open(str(get_rpths(os_mtd().make_fpath(*prof_s.X_MOZ_FP.value, data="gotit"))),"rb") as m, 
        open("scrt.txt", "a") as sc, open("scrt.txt","r") as z
        ):
        print(m.read(), file=sc)
        pp.append(z.read())
    store_urls = ["".join(str(g).lower()) for y in pp for g in re.findall(RE_URL, y)]
    return set(store_urls)


def scoopy_fndr():
    zscpy =  ["success" for x in scoopy() for xx in  pns_s() if xx in x and len(xx) > 2]
    zscpyy =  [xx for x in scoopy() for xx in  pns_s() if xx in x and len(xx) > 2]
    print(zscpyy)
    okey = Tk()
    st = okey
    st.title("Scoopy - The Adult Site Detector")
    st.config(background="#EC6008")
    half_screen(st,480,301)
    try:
        if zscpy[0] == "success":
            l = PhotoImage(file='./{0}'.format(zscpy[0] + ".png"))
    except:
        l = PhotoImage(file='./{0}'.format("fail" + ".png"))
    z = Label(st, image=l, background="#fff")
    z.pack()
    st.mainloop()
    os.remove("scrt.txt")
    

scoopy_fndr()
