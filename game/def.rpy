define config.developer = False

# Anims
init:
    python:
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.675,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)

#Transf
transform dizzy(m, t, subpixel=True):
    subpixel subpixel
    parallel:
        xoffset 0
        ease 0.675 * t xoffset 10 * m
        ease 0.675 * t xoffset 5 * m
        ease 0.675 * t xoffset -5 * m
        ease 0.675 * t xoffset -3 * m
        ease 0.675 * t xoffset -10 * m
        ease 0.675 * t xoffset 0
        ease 0.675 * t xoffset 5 * m
        ease 0.675 * t xoffset 0
        repeat
    parallel:
        yoffset 0
        ease 1.0 * t yoffset 5 * m
        ease 2.0 * t yoffset -5 * m
        easein 1.0 * t yoffset 0
        repeat
# ep3
image ep3_1:
    truecenter
    "images/a_ep3/1.png"
image ep3_2:
    truecenter
    "images/a_ep3/2.png"
image ep3_3:
    truecenter
    "images/a_ep3/3.png"
image ep3_4:
    truecenter
    "images/a_ep3/4.png"
image ep3_5:
    truecenter
    "images/a_ep3/5.png"
image ep3_6:
    truecenter
    "images/a_ep3/6.png"
image ep3_7:
    truecenter
    "images/a_ep3/7.png"
image ep3_8:
    truecenter
    "images/a_ep3/8.png"
image ep3_9:
    truecenter
    "images/a_ep3/9.png"
image ep3_10:
    truecenter
    "images/a_ep3/10.png"
image ep3_11:
    truecenter
    "images/a_ep3/11.png"
image ep3_12:
    truecenter
    "images/a_ep3/12.png"
image ep3_13:
    truecenter
    "images/a_ep3/13.png"
image ep3_14:
    truecenter
    "images/a_ep3/14.png"
image ep3_15:
    truecenter
    "images/a_ep3/15.png"
image ep3_16:
    truecenter
    "images/a_ep3/16.png"
image ep3_17:
    truecenter
    "images/a_ep3/17.png"
image ep3_18:
    truecenter
    "images/a_ep3/18.png"
image ep3_19:
    truecenter
    "images/a_ep3/19.png"
image ep3_20:
    truecenter
    "images/a_ep3/20.png"
image ep3_21:
    truecenter
    "images/a_ep3/21.png"
image ep3_22:
    truecenter
    "images/a_ep3/22.png"
image ep3_23:
    truecenter
    "images/a_ep3/23.png"
image ep3_24:
    truecenter
    "images/a_ep3/24.png"
image ep3_25:
    truecenter
    "images/a_ep3/25.png"
image ep3_26:
    truecenter
    "images/a_ep3/26.png"
image ep3_27:
    truecenter
    "images/a_ep3/27.png"
image ep3_28:
    truecenter
    "images/a_ep3/28.png"
image ep3_29:
    truecenter
    "images/a_ep3/29.png"
image ep3_30:
    truecenter
    "images/a_ep3/30.png"
image ep3_31:
    truecenter
    "images/a_ep3/31.png"
image ep3_32:
    truecenter
    "images/a_ep3/32.png"
image ep3_33:
    truecenter
    "images/a_ep3/33.png"
image ep3_34:
    truecenter
    "images/a_ep3/34.png"
image ep3_35:
    truecenter
    "images/a_ep3/35.png"
image ep3_36:
    truecenter
    "images/a_ep3/36.png"
image ep3_37:
    truecenter
    "images/a_ep3/37.png"
image ep3_38:
    truecenter
    "images/a_ep3/38.png"
image ep3_39:
    truecenter
    "images/a_ep3/39.png"
image ep3_40:
    truecenter
    "images/a_ep3/40.png"
image ep3_41:
    truecenter
    "images/a_ep3/41.png"
image ep3_42:
    truecenter
    "images/a_ep3/42.png"
image ep3_43:
    truecenter
    "images/a_ep3/43.png"
image ep3_44:
    truecenter
    "images/a_ep3/44.png"
image ep3_45:
    truecenter
    "images/a_ep3/45.png"
image ep3_46:
    truecenter
    "images/a_ep3/46.png"
image ep3_47:
    truecenter
    "images/a_ep3/47.png"
image ep3_48:
    truecenter
    "images/a_ep3/48.png"
image ep3_49:
    truecenter
    "images/a_ep3/49.png"
image ep3_50:
    truecenter
    "images/a_ep3/50.png"
image ep3_51:
    truecenter
    "images/a_ep3/51.png"
image ep3_52:
    truecenter
    "images/a_ep3/52.png"
image ep3_53:
    truecenter
    "images/a_ep3/53.png"
image ep3_54:
    truecenter
    "images/a_ep3/54.png"
image ep3_55:
    truecenter
    "images/a_ep3/55.png"
image ep3_56:
    truecenter
    "images/a_ep3/56.png"
image ep3_57:
    truecenter
    "images/a_ep3/57.png"
image ep3_58:
    truecenter
    "images/a_ep3/58.png"
image ep3_59:
    truecenter
    "images/a_ep3/59.png"
image ep3_60:
    truecenter
    "images/a_ep3/60.png"
image ep3_61:
    truecenter
    "images/a_ep3/61.png"
image ep3_62:
    truecenter
    "images/a_ep3/62.png"
image ep3_63:
    truecenter
    "images/a_ep3/63.png"
image ep3_64:
    truecenter
    "images/a_ep3/64.png"
image ep3_65:
    truecenter
    "images/a_ep3/65.png"
image ep3_66:
    zoom 0.675
    truecenter
    "images/a_ep3/66.png"
image ep3_67:
    zoom 0.675
    truecenter
    "images/a_ep3/67.png"
image ep3_68:
    zoom 0.675
    truecenter
    "images/a_ep3/68.png"
image ep3_69:
    zoom 0.675
    truecenter
    "images/a_ep3/69.png"
image ep3_70:
    zoom 0.675
    truecenter
    "images/a_ep3/70.png"
image ep3_71:
    zoom 0.675
    truecenter
    "images/a_ep3/71.png"
image ep3_72:
    zoom 0.675
    truecenter
    "images/a_ep3/72.png"
image ep3_73:
    zoom 0.675
    truecenter
    "images/a_ep3/73.png"
image ep3_74:
    zoom 0.675
    truecenter
    "images/a_ep3/74.png"
image ep3_75:
    zoom 0.675
    truecenter
    "images/a_ep3/75.png"
image ep3_76:
    zoom 0.675
    truecenter
    "images/a_ep3/76.png"
image ep3_77:
    zoom 0.675
    truecenter
    "images/a_ep3/77.png"
image ep3_78:
    zoom 0.675
    truecenter
    "images/a_ep3/78.png"
image ep3_79:
    truecenter
    "images/a_ep3/79.png"
image ep3_80:
    truecenter
    "images/a_ep3/80.png"
image ep3_81:
    truecenter
    "images/a_ep3/81.png"
image ep3_82:
    truecenter
    "images/a_ep3/82.png"
image ep3_83:
    truecenter
    "images/a_ep3/83.png"
image ep3_84:
    truecenter
    "images/a_ep3/84.png"
image ep3_85:
    truecenter
    "images/a_ep3/85.png"
image ep3_86:
    truecenter
    "images/a_ep3/86.png"
image ep3_87:
    truecenter
    "images/a_ep3/87.png"
image ep3_88:
    truecenter
    "images/a_ep3/88.png"
image ep3_89:
    truecenter
    "images/a_ep3/89.png"
image ep3_90:
    truecenter
    "images/a_ep3/90.png"
image ep3_91:
    truecenter
    "images/a_ep3/91.png"
image ep3_92:
    truecenter
    "images/a_ep3/92.png"
image ep3_93:
    zoom 0.675
    truecenter
    "images/a_ep3/93.png"
image ep3_94:
    truecenter
    "images/a_ep3/94.png"
image ep3_95:
    truecenter
    "images/a_ep3/95.png"
image ep3_96:
    truecenter
    "images/a_ep3/96.png"
image ep3_97:
    truecenter
    "images/a_ep3/97.png"
image ep3_98:
    truecenter
    "images/a_ep3/98.png"
image ep3_99:
    truecenter
    "images/a_ep3/99.png"
image ep3_100:
    truecenter
    "images/a_ep3/100.png"
image ep3_101:
    truecenter
    "images/a_ep3/101.png"
image ep3_102:
    truecenter
    "images/a_ep3/102.png"
image ep3_103:
    truecenter
    "images/a_ep3/103.png"
image ep3_104:
    truecenter
    "images/a_ep3/104.png"
image ep3_105:
    truecenter
    "images/a_ep3/105.png"
image ep3_106:
    truecenter
    "images/a_ep3/106.png"
image ep3_107:
    truecenter
    "images/a_ep3/107.png"
image ep3_108:
    zoom 0.675
    truecenter
    "images/a_ep3/108.png"
image ep3_109:
    zoom 0.675
    truecenter
    "images/a_ep3/109.png"
image ep3_110:
    truecenter
    "images/a_ep3/110.png"
image ep3_111:
    truecenter
    "images/a_ep3/111.png"
image ep3_112:
    truecenter
    "images/a_ep3/112.png"
image ep3_113:
    truecenter
    "images/a_ep3/113.png"
image ep3_114:
    truecenter
    "images/a_ep3/114.png"
image ep3_115:
    truecenter
    "images/a_ep3/115.png"
image ep3_116:
    truecenter
    "images/a_ep3/116.png"
image ep3_117:
    truecenter
    "images/a_ep3/117.png"
image ep3_118:
    truecenter
    "images/a_ep3/118.png"
image ep3_119:
    truecenter
    "images/a_ep3/119.png"
image ep3_120:
    truecenter
    "images/a_ep3/120.png"
image ep3_121:
    truecenter
    "images/a_ep3/121.png"
image ep3_122:
    truecenter
    "images/a_ep3/122.png"
image ep3_123:
    truecenter
    "images/a_ep3/123.png"
image ep3_124:
    truecenter
    "images/a_ep3/124.png"
image ep3_125:
    truecenter
    "images/a_ep3/125.png"
image ep3_126:
    truecenter
    "images/a_ep3/126.png"
image ep3_127:
    truecenter
    "images/a_ep3/127.png"
image ep3_128:
    truecenter
    "images/a_ep3/128.png"
image ep3_129:
    truecenter
    "images/a_ep3/129.png"
image ep3_130:
    truecenter
    "images/a_ep3/130.png"
image ep3_131:
    truecenter
    "images/a_ep3/131.png"
image ep3_132:
    truecenter
    "images/a_ep3/132.png"
image ep3_133:
    truecenter
    "images/a_ep3/133.png"
image ep3_134:
    truecenter
    "images/a_ep3/134.png"
image ep3_135:
    truecenter
    "images/a_ep3/135.png"
image ep3_136:
    truecenter
    "images/a_ep3/136.png"
image ep3_137:
    truecenter
    "images/a_ep3/137.png"
image ep3_138:
    truecenter
    "images/a_ep3/138.png"
image ep3_139:
    truecenter
    "images/a_ep3/139.png"
image ep3_140:
    truecenter
    "images/a_ep3/140.png"
image ep3_141:
    truecenter
    "images/a_ep3/141.png"
image ep3_142:
    truecenter
    "images/a_ep3/142.png"
image ep3_143:
    truecenter
    "images/a_ep3/143.png"
image ep3_144:
    truecenter
    "images/a_ep3/144.png"
image ep3_145:
    truecenter
    "images/a_ep3/145.png"
image ep3_146:
    truecenter
    "images/a_ep3/146.png"
image ep3_147:
    truecenter
    "images/a_ep3/147.png"
image ep3_148:
    truecenter
    "images/a_ep3/148.png"
image ep3_149:
    truecenter
    "images/a_ep3/149.png"
image ep3_150:
    truecenter
    "images/a_ep3/150.png"
image ep3_151:
    truecenter
    "images/a_ep3/151.png"
image ep3_152:
    truecenter
    "images/a_ep3/152.png"
image ep3_153:
    truecenter
    "images/a_ep3/153.png"
image ep3_154:
    truecenter
    "images/a_ep3/154.png"
image ep3_155:
    truecenter
    "images/a_ep3/155.png"
image ep3_156:
    truecenter
    "images/a_ep3/156.png"
image ep3_157:
    truecenter
    "images/a_ep3/157.png"
image ep3_158:
    truecenter
    "images/a_ep3/158.png"
image ep3_159:
    truecenter
    "images/a_ep3/159.png"
image ep3_160:
    truecenter
    "images/a_ep3/160.png"
image ep3_161:
    truecenter
    "images/a_ep3/161.png"
image ep3_162:
    truecenter
    "images/a_ep3/162.png"
image ep3_163:
    truecenter
    "images/a_ep3/163.png"
image ep3_164:
    zoom 0.675
    truecenter
    "images/a_ep3/164.png"
image ep3_165:
    zoom 0.675
    truecenter
    "images/a_ep3/165.png"
image ep3_166:
    truecenter
    "images/a_ep3/166.png"
image ep3_167:
    truecenter
    "images/a_ep3/167.png"
image ep3_168:
    truecenter
    "images/a_ep3/168.png"
image ep3_169:
    truecenter
    "images/a_ep3/169.png"
image ep3_170:
    zoom 0.675
    truecenter
    "images/a_ep3/170.png"
image ep3_171:
    zoom 0.675
    truecenter
    "images/a_ep3/171.png"

#ep3 edit
image ep3_e_1:
    truecenter
    "images/a_ep3/1_edit.png"

image ep3_e_2:
    truecenter
    "images/a_ep3/84_edit_1.png"

image ep3_e_3:
    truecenter
    "images/a_ep3/84_edit_2.png"

image ep3_e_4:
    truecenter
    "images/a_ep3/84_edit_3.png"

image ep3_130_extra:
    truecenter
    "images/a_ep3/130-extra.png"

image ep3_147_extra:
    truecenter
    "images/a_ep3/147-extra.png"

# Scenes
image endDDLC:
    truecenter
    "images/endDDLC.png"
image black = "#000"
image white = "#ffffff"
image noise:
    truecenter
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    xzoom -1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    yzoom -1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    xzoom 1
    "images/bg/noise1.jpg"
    pause 0.1
    "images/bg/noise2.jpg"
    pause 0.1
    "images/bg/noise3.jpg"
    pause 0.1
    "images/bg/noise4.jpg"
    pause 0.1
    yzoom 1
    repeat

# Chars
define aoba = Character("Aoba", color="#b19cd9")
define aoffy = Character("Aoffy", color="#ffff00")
define apple = Character("Apple", color="#8db600")
define angel = Character("Angel", color="#add8e6")
define simon = Character("Simon", color="#f47fff")
define unknown = Character("???")

# Python Scripts
init python:
    def delete_character(name):
        import os
        try: os.remove(config.basedir + "/characters/" + name + ".chr")
        except: pass
    def restore_all_characters():
        try: renpy.file("../characters/aoba.chr")
        except: open(config.basedir + "/characters/aoba.chr", "wb").write(renpy.file("aoba.chr").read())
        try: renpy.file("../characters/angel.chr")
        except: open(config.basedir + "/characters/angel.chr", "wb").write(renpy.file("angel.chr").read())
        try: renpy.file("../characters/akinya.chr")
        except: open(config.basedir + "/characters/akinya.chr", "wb").write(renpy.file("akinya.chr").read())
        try: renpy.file("../characters/aoffy.chr")
        except: open(config.basedir + "/characters/aoffy.chr", "wb").write(renpy.file("aoffy.chr").read())
        try: renpy.file("../characters/apple.chr")
        except: open(config.basedir + "/characters/apple.chr", "wb").write(renpy.file("apple.chr").read())
        try: renpy.file("../characters/cashier.chr")
        except: open(config.basedir + "/characters/cashier.chr", "wb").write(renpy.file("cashier.chr").read())
        try: renpy.file("../characters/jerry.chr")
        except: open(config.basedir + "/characters/jerry.chr", "wb").write(renpy.file("jerry.chr").read())
        try: renpy.file("../characters/simon.chr")
        except: open(config.basedir + "/characters/simon.chr", "wb").write(renpy.file("simon.chr").read())