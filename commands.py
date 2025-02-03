from scr.katas.cwFetch import UserKataInfo, KataInfo
from scr.katas.jsonSave import Save
from scr.cw_version_control.menager import MainFolder
from cli.command import CLI
from config import ConfigManager

cli = CLI()
config = ConfigManager('settings.yaml')

@cli.command(check_args=True)
def changeuser(name: str):
    """
    Sets the username for the current user in the system.
    """    
    
    config.open()
    config.data["user_name"] = name
    config.save()

@cli.command(check_args=True)
def changedir(path: str):
    """
    Sets the main folder path in the system.
    """
    
    config.open()
    config.data["main_directory"] = path
    config.save()

@cli.command(check_args=False)
def getkatas():
    """Saves all User katas id"""
    config.open()
    user_name = config.data.get('user_name')    
    user = UserKataInfo(user_name)
    
    user.get()
    save = Save(user.id_list, "scr/katas/katas.json")
    save.save()
    print(f"[{len(user.id_list)}] katas found")

@cli.command(check_args=False)
def setenv():
    """Creates main folder for katas with folders for each lvl of difficulty"""
    config.open()
    main_directory = config.data.get('main_directory')
    m = MainFolder(main_directory)
    m.create()

@cli.command(check_args=False)
def update():
    save = Save(path='scr/katas/katas.json')
    katas = save.load()

    katas_list = []
    for kata in katas:
        k = KataInfo(kata)
        k.get()
        katas_list.append(k.data)
    
    config.open()
    main_directory = config.data.get('main_directory')
    m = MainFolder(main_directory)
    m.add_katas(katas_list)
