


if __name__ == "__main__":
    from scr.save import Save
    from scr.chalanges import UserKataInfo, KataInfo
    u = UserKataInfo('NelexstarMain')
    u.get()
    s = Save(u.id_list, 'katas.json')
    s.save()