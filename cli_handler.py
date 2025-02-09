import os

from core.kata_data.kata_fetcher import UserKataInfo, KataInfo
from core.kata_data.json_storage import Save
from core.version_control.folder_manager import MainFolder
from core.errors.errors import CustomError
from core.git_tools.git_manager import GIT
from command_interface.command import CLI
from config_manager import ConfigManager

cli = CLI()
config = ConfigManager('settings.yaml')
data = config.open()


@cli.command(check_args=True)
def set_user(name: str):
    """
    Sets the username for the system.
    """
    config.open()
    config.data["username"] = name
    config.save()

@cli.command(check_args=True)
def set_dir(path: str):
    """
    Sets the main working directory.
    """
    config.open()
    config.data["root_directory"] = path
    config.save()

@cli.command(check_args=False)
def fetch_katas():
    """Fetches and saves all user kata IDs."""
    config.open()
    user_name = config.data.get('username')    
    if user_name is not None:
        user = UserKataInfo(user_name)
        
        user.get()
        save = Save(user.id_list, "core/kata_data/kata_data.json")
        save.save()
        print(f"[{len(user.id_list)}] katas found")
    else:
        CustomError('UnassignedError', 'Variable <user> has no assigned value. Use <set_user> command.')

@cli.command(check_args=False)
def setup_env():
    """Creates the main folder structure for katas."""
    main_directory = data.get('root_directory')
    main_folder = data.get('workspace_folder')
    if main_directory is not None:
        manager = MainFolder(main_directory, main_folder)
        manager.create()
    else:
        CustomError('UnassignedError', 'Variable <directory> has no assigned value. Use <set_dir> command.')

@cli.command(check_args=False)
def update_katas():
    """Updates kata details and organizes them in the main folder."""
    save = Save(path='scr/katas/katas.json')
    katas = save.load()
    print(katas)
    if katas:
            katas_list = []
            for kata in katas:
                kata_info = KataInfo(kata)
                kata_info.get()
                katas_list.append(kata_info.data)
            
            main_directory = data.get('root_directory')
            if main_directory is not None:
                manager = MainFolder(main_directory, data.get('workspace_folder'))
                manager.add_katas(katas_list)
            else:
                CustomError('UnassignedError', 'Variable <directory> has no assigned value. Use <set_dir> command.')
    else:
        CustomError('UnassignedError', 'JSON file is empty. Use <fetch_katas> command.')

@cli.command(check_args=False)
def git_sync():
    """Initializes, commits, pulls, and pushes changes to the repository."""
    dir = data.get('root_directory')
    workspace = data.get('workspace_folder')
    
    if dir is not None:
        git_manager = GIT(os.path.join(dir, workspace))
        git_manager.init_repo()
        git_manager.add()
        commit_message = data.get('commit_prefix')
        git_manager.commit(commit_message)
        branch = data.get('default_branch')
        git_manager.pull(branch)
        git_manager.push(branch)  
        print(git_manager.status(branch))
        print(git_manager.log(branch))

    else:
        CustomError('UnassignedError', 'Variable <directory> has no assigned value. Use <set_dir> command.')