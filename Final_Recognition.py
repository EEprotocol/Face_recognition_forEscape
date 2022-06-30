from importlib.metadata import files
import face_recognition
import matplotlib.pyplot as plt
import glob
import cv2
import shutil
import os
import pickle

#ディレクトリを変える
os.chdir("C:\\Users\\kei31\\python0step\\Final_Weapon_for_Face\\faces_material\\Judge_assesment\\")

with open("name_list.pkl","rb") as f:#復元！
    files=pickle.load(f)
    

#カメラから取り込む場合
os.chdir("C:\\Users\\kei31\\python0step\\Final_Weapon_for_Face\\faces_material\\examine_field\\")
deviceid=0
capture=cv2.VideoCapture(deviceid)
ret,frame=capture.read()
cv2.imwrite("img_from_camera.jpg", frame)
CheckFile=["img_from_camera.jpg"]

"""
##ディレクトリから取り込む場合

os.chdir("C:\\Users\\kei31\\python0step\\Final_Weapon_for_Face\\faces_material\\examine_field")
CheckFile=glob.glob("*")
print(CheckFile[0])
"""


"""
i=int(0)
# 保存されている人物の顔の画像を読み込む。
known_face_imgs = []
for path in files:
    img = face_recognition.load_image_file(path)
    known_face_imgs.append(img)

print(known_face_imgs)##########################################################
"""

# 認証する人物の顔の画像を読み込む。
face_img_to_check = face_recognition.load_image_file("{}".format(CheckFile[0]))

"""
# 顔の画像から顔の領域を検出する。
known_face_locs = []
for img in known_face_imgs:
    loc = face_recognition.face_locations(img, model="hog")
    assert len(loc) == 1, "{}画像から顔の検出に失敗したか、2人以上の顔が検出されました".format(files[i])
    known_face_locs.append(loc)
    i=1+i

print(known_face_locs)############################################################
"""


face_loc_to_check = face_recognition.face_locations(face_img_to_check, model="hog")
if len(face_loc_to_check) != 1:
    print("画像から顔の検出に失敗したか、2人以上の顔が検出されました")
    os.remove("C:\\Users\\kei31\\python0step\\Final_Weapon_for_Face\\faces_material\\examine_field\\{}".format(CheckFile[0]))




#顔の領域を描画する。
def draw_face_locations(img, locations):
    fig, ax = plt.subplots()
    ax.imshow(img)
    ax.set_axis_off()
    for i, (top, right, bottom, left) in enumerate(locations):
        # 長方形を描画する。
        w, h = right - left, bottom - top
        ax.add_patch(plt.Rectangle((left, top), w, h, ec="r", lw=2, fill=None))
    plt.show()
"""
for img, loc in zip(known_face_imgs, known_face_locs):
    draw_face_locations(img, loc)

draw_face_locations(face_img_to_check, face_loc_to_check)
"""

"""
# 顔の領域から特徴量を抽出する。
known_face_encodings = []
for img, loc in zip(known_face_imgs, known_face_locs):
    (encoding,) = face_recognition.face_encodings(img, loc)   
    known_face_encodings.append(encoding) 
"""

(face_encoding_to_check,) = face_recognition.face_encodings(
    face_img_to_check, face_loc_to_check
)
#print(known_face_encodings)######################################################

os.chdir("C:\\Users\\kei31\\python0step\\Final_Weapon_for_Face\\faces_material\\Judge_assesment\\")

#学習済み特徴量データを持ってくる
with open("feature.pkl","rb") as f:#復元！
    known_face_encodings=pickle.load(f)



#閾値を下回ったものにTrueをかえす。
matches = face_recognition.compare_faces(known_face_encodings, face_encoding_to_check,tolerance=0.38)
print(matches)  #################################################################



dists=[]
for enco in known_face_encodings:
    dist = face_recognition.face_distance([enco], face_encoding_to_check)
    dists.append(dist[0])
    print(dist)

pro = face_recognition.face_distance(known_face_encodings, face_encoding_to_check)


print(dists)######################################################################

correspond_man=[]

#判決！！

#１．Trueが一人のとき
if matches.count(True)==1:
    print(matches.index(True))
    print(files[matches.index(True)])
    name=os.path.splitext(os.path.basename(files[matches.index(True)]))[0]
    jgmsg = str("こいつは{}と考えられる。".format(name))
    print()
#2.Trueが一人よりも多いとき
elif matches.count(True)>=1:
    for i, value in enumerate(matches):
        if value==True:
            name=os.path.splitext(os.path.basename(files[i]))[0]
            correspond_man.append(name)
        else:
            continue
    name=os.path.splitext(os.path.basename(files[dists.index(min(dists))]))[0]
    jgmsg = str("{}の{}名が閾値を超えました。このうち最も距離が近いのは{}です。".format(correspond_man,matches.count(True),name))
#3.Trueがいないとき
else:
    name=os.path.splitext(os.path.basename(files[dists.index(min(dists))]))[0]
    jgmsg = str(
        "多分こいつは知らん奴。\n"+"しかしながら現段階のデータで一番似ているのは{}である。".format(name)
    )

print(jgmsg)
    
    

#今回検査した画像を別ファイルに移してしまう
new_path=shutil.move(
    "C:\\Users\\kei31\\python0step\\Final_Weapon_for_Face\\faces_material\\examine_field\\{}".format(CheckFile[0]),
    "C:\\Users\\kei31\\python0step\\Final_Weapon_for_Face\\faces_material\\Judge_assesment\\used_material\\{}"
    .format("{}.jpg".format(name))
)

#________________________________________________________________________________________________

