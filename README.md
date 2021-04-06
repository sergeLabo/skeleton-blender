# skeleton-blender

Visualisation dans le Blender Game Engine de la Détection de squelette avec capteur RealSense et OpenCV

### Capture

La capture est réalisée avec le projet [skeleton-rs](https://github.com/sergeLabo/skeleton-rs)


### Dépendances

* Debian 10 Buster
* python3.7
* oscpy
* numpy
* scipy
* Blender 2.79b

Le venv ne sert que pour tester utils.py et rs_utils.py

### BGE

Quelques briques sont utilisées pour excécuter labomedia_once.py et labomedia_always.py
en tant que modules. Il ne faut pas modifier ces scripts.
Les autres scripts doivent être modifiés dans un EDI externe et enregistrés.

Le jeu ne doit jamais être lancé avec le Embedded Player avec "P", pour ne pas avoir
de soucis avec les threads de oscpy.

Lancer le jeu en terminal dans le dossier du blend:

```
blenderplayer blender_osc.blend
```

### TODO

Faire la version UPBGE 0.3

### Merci à

* [La Labomedia](https://ressources.labomedia.org/)
