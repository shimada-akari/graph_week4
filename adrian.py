import os
import pandas as pd
import bisect 

def load_nicknames_data():#nicknameを返す
    path = "./sns/nicknames.txt"
    nicknames = []

    nicknames_data = open(path, "r")

    # 行ごとにすべて読み込んでリストデータにする
    all_lines = nicknames_data.readlines()

    for line in all_lines: 
        line = line.replace('\n','') #改行文字削除
        id, person_name = line.split('\t') #idとnicknameで分ける
        # id = int(id)
        # nicknames.append([id, person_name])
        nicknames.append(person_name)

    # ファイルをクローズする
    nicknames_data.close()

    return nicknames

def sort(list, ele): #connectedのlistに要素を順番を保ちながら挿入（昇順）
    insert_position = bisect.bisect_left(list, ele)
    list.insert(insert_position, ele)
    return list




def load_links_data():

    path = "./sns/links.txt"
    links_table = []

    links_data = open(path, "r")

    # 行ごとにすべて読み込んでリストデータにする
    all_lines = links_data.readlines()

    table_append_index = -1
    for line in all_lines: 
        line = line.replace('\n','') #改行文字削除
#         print(line)
        from_id, to_id = map(lambda x:int(x), line.split('\t')) #from_idとto_idで分ける（どちらもint型）
        
        if from_id == table_append_index:
#             links_table[from_id].append(to_id)
            links_table[from_id] = sort(links_table[from_id], to_id)

     

        else:
            if table_append_index >= 0:
                links_table[table_append_index].sort()

            while(len(links_table) < from_id):
                links_table.append([])
                table_append_index += 1

            links_table.append([to_id])
            table_append_index += 1

    # ファイルをクローズする
    links_data.close()

    return links_table




def check_person(from_id, to_id, links_table, color_list):
    connected_people = links_table[from_id]

    # index = bisect.bisect_left(connected_people, to_id) #to_id index以下の要素のうち、最も大きい要素のindexが返ってくる
    
    # if index < len(connected_people) and connected_people[index] == to_id:
    #     print("yes")
    # else:
    #     print("no")
    if color_list[from_id] == color_list[to_id]:
        print("yes")
    else:
        print("no")

def search_id(nickname, id_nicknames):
    index = bisect.bisect_left(id_nicknames, nickname)
    return index

def search_connection(id, links_table, color_list, color_value):
    stack = []
    stack.append(id)

    color_list[id] = color_value

    # count = 0 #for check
    while (len(stack) != 0):
        direct_linked_person = stack.pop(0)
        # print(stack, direct_linked_person, color_list[direct_linked_person]) #for check

        for person in links_table[direct_linked_person]:
            if color_list[person] == -1: #未訪問
                # print(linked_person)
                color_list[person] = color_value
                stack.append(person)

        # count += 1
        # if count >= 10:
        #     break

    return color_list

def assign_color():
    color_list = [-1]* len(links_table)
    color_value = 1
    for id in range(len(links_table)):
        if(color_list[id] == -1): #まだ訪問していない
            color_list = search_connection(id, links_table, color_list, color_value)
            color_value += 1
    return color_list


id_nicknames  =  load_nicknames_data() #id_nicknames : idのindexにnicknameが入っている, nicknamesのabc順
links_table = load_links_data() #人数分の配列の中につながっている人のindexが入っている

color_list = assign_color()


while(True):
    from_nickname, to_nickname = map(lambda x:x, input("from -> to : ").split())
    
    from_id = search_id(from_nickname, id_nicknames)
    to_id = search_id(to_nickname, id_nicknames)

    # print(from_id, to_id)
    check_person(from_id, to_id, links_table, color_list)

# print(links_table)
# print(links)
# print(nicknames[1])
# check_person(from_id, to_id)