from scr.cwFetch import UserKataInfo
from scr.jsonSave import Save
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
    user = UserKataInfo(config.data['user_name'])
    user.get()
    save = Save(user.id_list, "scr/katas.json")
    save.save()
    print(f"[{len(user.id_list)}] katas found")


