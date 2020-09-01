import subprocess
import pystray
from PIL import Image

state = 0


def set_state(v):
    def inner(icon, item):
        global state
        state = v

    return inner


def get_state(v):
    def inner(item):
        return state == v

    return inner


def button_press(i):
    if i == 0:
        set_time('15')
    elif i == 1:
        set_time('10')
    elif i == 2:
        set_time('180')
    else:
        set_time('0xffffffff')
    print(i)
    return set_state(i)


def stop_app():
    # set_time(15)
    app.stop()


def set_time(t, p='ac'):
    subprocess.call(f"powercfg -change -monitor-timeout-{p} {t}")
    # print(f"powercfg -change -monitor-timeout-{p} {t}")
    # 0xffffffff option for never


app = pystray.Icon(
    name="Sleep Toggle",
    title="Sleep Toggle",
    icon=Image.open("sleep.jpg"),
    # "Sleep Icon" by Army Medicine is licensed under CC BY 2.0
    menu=pystray.Menu(
        pystray.MenuItem(
            text="Sleep Toggle",
            action=None,
        ),
        pystray.MenuItem(
            text="Set to 10 minutes",
            # action=lambda: button_press(1),
            action=lambda: set_time(10),
            checked=get_state(1),
            radio=True
        ),
        pystray.MenuItem(
            text="Set to 3 hours",
            # action=button_press(2),
            action=lambda: set_time(180),
            checked=get_state(2),
            radio=True
        ),
        pystray.MenuItem(
            text="Set to forever",
            # action=button_press(3),
            action=lambda: set_time('0xffffffff'),
            checked=get_state(3),
            radio=True
        ),
        pystray.MenuItem(
            text='Quit',
            action=lambda: stop_app(),
            checked=None
        )
    )
)

app.run()

