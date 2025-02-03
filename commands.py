import os

from scr.katas.cwFetch import UserKataInfo, KataInfo
from scr.katas.jsonSave import Save
from scr.cw_version_control.menager import MainFolder
from scr.git import git_commands
from cli.command import CLI
from config import ConfigManager

cli = CLI()
config = ConfigManager('settings.yaml')
data = config.open()

git_manager = git_commands.GIT(os.path.join(data.get('main_directory'), data.get('main_folder')))

@cli.command(check_args=True)
def set_user(name: str):
    """
    Sets the username for the system.
    """
    config.open()
    config.data["user_name"] = name
    config.save()

@cli.command(check_args=True)
def set_dir(path: str):
    """
    Sets the main working directory.
    """
    config.open()
    config.data["main_directory"] = path
    config.save()

@cli.command(check_args=False)
def fetch_katas():
    """Fetches and saves all user kata IDs."""
    config.open()
    user_name = config.data.get('user_name')    
    user = UserKataInfo(user_name)
    
    user.get()
    save = Save(user.id_list, "scr/katas/katas.json")
    save.save()
    print(f"[{len(user.id_list)}] katas found")

@cli.command(check_args=False)
def setup_env():
    """Creates the main folder structure for katas."""
    main_directory = data.get('main_directory')
    manager = MainFolder(main_directory, data.get('main_folder'))
    manager.create()

@cli.command(check_args=False)
def update_katas():
    """Updates kata details and organizes them in the main folder."""
    save = Save(path='scr/katas/katas.json')
    katas = save.load()

    katas_list = []
    for kata in katas:
        kata_info = KataInfo(kata)
        kata_info.get()
        katas_list.append(kata_info.data)
    
    main_directory = data.get('main_directory')
    manager = MainFolder(main_directory, data.get('main_folder'))
    manager.add_katas(katas_list)

@cli.command(check_args=False)
def git_sync():
    """Initializes, commits, pulls, and pushes changes to the repository."""
    git_manager.init_repo()
    git_manager.add()
    commit_message = data.get('commit_msg_base')
    git_manager.commit(commit_message)
    git_manager.pull()
    git_manager.push()
    branch = data.get('main_branch')
    print(git_manager.status())
    print(git_manager.log())
