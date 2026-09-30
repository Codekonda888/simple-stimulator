from ursina import *

app = Ursina()
Entity.default_shader = None
window.color = color.white
window.title = 'Mensch Simulator'

camera.position = (0, 2, -15)
camera.rotation_x = 0

boden = Entity(
    model='plane',
    scale=(20, 1, 20),
    color=color.pink,
    position=(0, 0, 0),
    unlit=True
)

mensch_root = Entity(position=(0, 0, 0))

koerper = Entity(
    parent=mensch_root,
    model='quad',
    color=color.red,
    scale=(0.6, 1.2, 0.4),
    position=(0, 2, 0),
    unlit=True
)

kopf = Entity(
    parent=mensch_root,
    model='sphere',
    color=color.rgb(255, 218, 185),
    scale=(0.4, 0.4, 0.4),
    position=(0, 2.9, 0.1),
    unlit=True
)

bein_links = Entity(
    parent=mensch_root,
    model=Cylinder(),
    color=color.rgb(47, 79, 79),
    scale=(0.15, 0.8, 0.15),
    position=(-0.2, 0.6, 0),
    unlit=True
)

bein_rechts = Entity(
    parent=mensch_root,
    model=Cylinder(),
    color=color.rgb(47, 79, 79),
    scale=(0.15, 0.8, 0.15),
    position=(0.2, 0.6, 0),
    unlit=True
)

arm_links = Entity(
    parent=mensch_root,
    model='quad',
    color=color.rgb(255, 218, 185),
    scale=(0.8, 0.15, 0.1),
    position=(-0.7, 2.4, 0.1),
    unlit=True
)

arm_rechts = Entity(
    parent=mensch_root,
    model='quad',
    color=color.rgb(255, 218, 185),
    scale=(0.8, 0.15, 0.1),
    position=(0.7, 2.4, 0.1),
    unlit=True
)

groesse_slider = Slider(
    min=1.0, max=2.2, default=1.7,
    color=color.blue,
    text='Größe (m)',
    y=-0.35, x=-0.6,
    dynamic=True
)

gewicht_slider = Slider(
    min=40, max=150, default=75,
    color=color.blue,
    text='Gewicht (kg)',
    y=-0.42, x=-0.6,
    dynamic=True
)

def update():
    mensch_root.scale_y = groesse_slider.value / 1.7
    breite = gewicht_slider.value / 75.0
    koerper.scale_x = 0.6 * breite
    koerper.scale_z = 0.4 * breite
    kopf.scale_x = 0.4 * (1.0 + (breite - 1.0) * 0.3)
    kopf.scale_z = 0.4 * (1.0 + (breite - 1.0) * 0.3)
    arm_links.position_x = -0.3 * breite - 0.4
    arm_rechts.position_x = 0.3 * breite + 0.4

app.run()
