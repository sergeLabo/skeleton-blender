
from time import time
import json

from oscpy.server import OSCThreadServer

from bge import logic as gl
from scripts.utils import get_all_objects, add_object, read_json
from scripts.utils import JOINTS, PAIRS_COCO, PAIRS_MPI
from scripts.rs_utils import Filtre, get_points
from scripts.sound import EasyAudio


def default_handler(*args):
    print("default_handler", args)


def on_points(*args):
    # J'ôte le body
    body = args[-1]
    args = args[:-1]

    gl.points = get_points(args)
    gl.new = 1
    # Durée en frame depuis la dernière réception
    gl.tempo = gl.frame_number - gl.receive_at
    gl.receive_at = gl.frame_number


def on_note(i):
    print("Play note", i)
    if gl.notes:
        gl.notes[str(i)].play()


def osc_server_init():
    gl.server = OSCThreadServer()
    gl.server.listen('0.0.0.0', port=8003, default=True)
    # Les callbacks du serveur
    gl.server.default_handler = default_handler
    gl.server.bind(b'/points', on_points)
    gl.server.bind(b'/note', on_note)

def get_notes():
    """ gl.music["BlueScorpion"].set_volume(0.2)
        gl.motorSound[i] = EasyAudio(["son_moteur"], "//samples/")
        gl.motorSound[0]["son_moteur"].repeat()
        EasyAudio(self, soundList, path, buffered=True)
    """
    soundList = []
    for i in range(36):
        soundList.append(str(i))
    gl.notes = EasyAudio(soundList, "//samples/")


def main():
    print("Lancement de once.py ...")

    gl.all_obj = get_all_objects()
    gl.cube = gl.all_obj["Cube"]
    gl.metarig = gl.all_obj["metarig"]
    gl.person = gl.all_obj["person"]

    gl.spheres = []
    # 18 est le  body au centre de 11 et 12
    # 19 est le centre des yeux pour la tête
    for i in ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09",
                "10", "11", "12", "13", "14", "15", "16", "17", "18", "19"]:
        gl.spheres.append(gl.all_obj[i])

    # AA sur Text
    for obj_name, obj in gl.all_obj.items():
        if "Text" in obj_name:
            obj.resolution = 64

    gl.t = time()
    gl.fps = 0
    gl.server = None
    gl.points = None
    gl.frame_number = 0
    gl.nums = 2022
    gl.new = 0
    gl.receive_at = 0
    gl.tempo = 0
    gl.body_visible = 1
    gl.person.visible = 0

    gl.debug = 1  # 1=avec fichier enregistré
    if gl.debug:
        b = './scripts/json/cap_2021_04_11_15_14.json'
        gl.data = read_json(b)
        print("Nombre de frame big =", len(gl.data))
    else:
        gl.notes = None
        osc_server_init()
    gl.every = 5

    # Le filtre Savonarol Wakowski de scipy
    gl.mode = "MPI"  # ou "COCO"
    if gl.mode == "MPI":
        gl.nombre = 15
        gl.pairs = PAIRS_MPI
    elif gl.mode == "COCO":
        gl.nombre = 18
        gl.pairs = PAIRS_COCO
    gl.filtre = Filtre(gl.nombre, 50)

    # Placement et échelle dans la scène
    gl.scale = 1
    gl.up_down = 1.5
    gl.left_right = 0.2
    gl.av_ar = -2.5

    # audio
    get_notes()
