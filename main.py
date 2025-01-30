from scr.save import Save
from scr.chalanges import UserKataInfo, KataInfo
from cli.command import commands
import yaml



if __name__ == "__main__":
    
    with open("settings.yaml", "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)  

    commands.run_all()
    # u = UserKataInfo(data.get('user_name'))
    # u.get()
    # s = Save(u.id_list, 'katas.json')
    # s.save()