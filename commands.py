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

