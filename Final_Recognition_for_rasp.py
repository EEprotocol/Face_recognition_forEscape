from base64 import encode
import face_recognition
import matplotlib.pyplot as plt
import cv2
import shutil
import os
import pickle
import time
import serial
import tqdm
import numpy as np
import subprocess
import numpy as np
import threading

deviceid=0
capture=cv2.VideoCapture(deviceid)
print("Open Port")

ser =serial.Serial("/dev/ttyACM0", 9600)
    
try:
    """
    time.sleep(3)
    print("YUKI.N> このメッセージが表示されたということは、そこにはあなた、わたし、涼宮ハルヒ、朝比奈みくる、古泉一樹が存在しているはずである。")
    time.sleep(2)
    print("\nYUKI.N> それが鍵。あなたは解答を見つけ出した。")
    time.sleep(2)
    print("\nYUKI.N> これは緊急脱出プログラムである。起動させる場合はエンターキーを、そうでない場合はそれ以外のキーを選択せよ。起動させた場合、あなたは時空修正の機会を得る。ただし成功は保証できない。また帰還の保証もできない。")
    time.sleep(2)
    print("\nYUKI.N> このプログラムが起動するのは一度きりである。実行ののち、消去される。非実行が選択された場合は起動せずに消去される。Ready?")
    stat=input("\n>>>")
    
    if stat=="":
    """
    i=int(0)
    for i in range(3,0,-1):
        print(i)
        time.sleep(1)
        
    while True:
        print("System> パスワードを入力してください。忘れた場合は\"HELP\"と入力してください。")
        Pass = input("Password>>>")
        if Pass == "HELP":
            break
        elif Pass == "GeBaYaShi":
            print("OPEN")
            ser.write("1".encode())
            die()
            break
        else:
            print("System> パスワードが違います。もう一度入力してください。")

    #第一問
    print("\nHakase.N> 今から脱出を望むあなた方には3つの質問に答えてもらう。")
    time.sleep(2.5)
    print("\nHakase.N> 謎博士の初めて買ったCDのアーティストは誰？(キーボードで入力してください）")
    while True:        
            Ans=input(">>>")
            if Ans=="あいみょん":
                print("Hakase.N> 正解。")
                break
            else :
                print("Hakase.N> 答えが違う、もう一度。")

    #第二問
    print("\nHakase.N> 謎博士の母親の旧姓は？ひらがなで答えよ。(キーボードで入力してください）")
    while True:        
            Ans=input(">>>")
            if Ans=="長宗我部" or "ちょうそかべ":
                print("Hakase.N> 正解。次が最後。")
                break
            else :
                print("Hakase.N> 答えが違う、もう一度。")
    #第三問
    print("\nHakase.N> 謎博士が初めて映画館で観た映画は？")
    while True:        
            Ans=input(">>>")
            if Ans==("アルマゲドン" or "Armageddon"):
                print("Hakase.N> 正解。")
                break
            else :
                print("Hakase.N> 答えが違う、もう一度。")
    
    time.sleep(0.5)
    
    print("System> 最後に顔認証システムによる照合を行います。")
    time.sleep(0.8)
    print("\nSystem> システム準備中")

    
    #ローディング画面
    for i in tqdm.tqdm(range(int(100))):
                np.pi*np.pi
                time.sleep(0.01)
    

    """    
    else:
        print("プログラムは消去された。さようなら、Sleeping Beauty。")
        for i in range(5,0,-1):
            print(i)
            time.sleep(1)
    """    
except KeyboardInterrupt:
    print("緊急停止")




ser.write("0".encode())

#ディレクトリを変える
os.chdir("//home//pi//Kondo//Judge_basement")

print("学習データ復元中")
with open("Name_list.pkl","rb") as f:#復元！
    files=pickle.load(f)
for i in tqdm.tqdm(range(int(100))):
                    np.pi*np.pi
                    time.sleep(0.01)


#カメラから取り込む場合
os.chdir("//home//pi//Kondo//examine_field")
print("カメラ準備中")

for i in tqdm.tqdm(range(int(100))):
                    np.pi*np.pi
                    time.sleep(0.01)
while True:
    while True:
        ser.write("3".encode())
        print("System> 撮影、認証をを行うには、pを押してください")
        #ビデオ再生部（p押下で抜ける）
        while True:
            ret,frame=capture.read()
            cv2.imshow("PRESS \"p\" to identify!", frame)   
            if cv2.waitKey(1) & 0xFF == ord("p"):
                break

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
            print("画像から顔の検出に失敗したか、2人以上の顔が検出されました。もう一度撮り直してください")
            #os.remove("C//home//pi//Kondo//examine_field//{}".format(CheckFile[0]))
        else:
            break


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
    try:
        (face_encoding_to_check,) = face_recognition.face_encodings(
            face_img_to_check, face_loc_to_check
        )
    except ValueError:
        print("System> 検証に失敗。もう一度行ってください")
    #print(known_face_encodings)######################################################

    os.chdir("//home//pi//Kondo//Judge_basement")

    #学習済み特徴量データを持ってくる
    with open("feature.pkl","rb") as f:#復元！
        known_face_encodings=pickle.load(f)



    #閾値を下回ったものにTrueをかえす。
    matches = face_recognition.compare_faces(known_face_encodings, face_encoding_to_check,tolerance=0.385)
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
        command="1"
        ser.write(command.encode())
        break
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
        command="1"
        ser.write(command.encode())
        break
    #3.Trueがいないとき
    else:
        name=os.path.splitext(os.path.basename(files[dists.index(min(dists))]))[0]
        jgmsg = str(
            "多分こいつは知らん奴。\n"+"しかしながら現段階のデータで一番似ているのは{}である。".format(name)
        )
        print("一致する人物がいません。やり直してください。")
        command="2"
        ser.write(command.encode())

print(jgmsg)
    
for i in range(5,0,-1):
    print(i)
    time.sleep(1)

    

#今回検査した画像を別ファイルに移してしまう
new_path=shutil.move(
    "//home//pi//Kondo//examine_field//{}".format(CheckFile[0]),
    "//home//pi//Kondo//Judge_basement//result//{}"
    .format("{}.jpg".format(name))
)

print("Close Port")
#ser.close()

#________________________________________________________________________________________________

