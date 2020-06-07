import os
import pandas as pd


def load_nicknames_data():#nicknameを返す
    path = "./sns/nicknames.txt"
    nicknames = []

    nicknames_data = open(path, "r")

    # 行ごとにすべて読み込んでリストデータにする
    all_lines = nicknames_data.readlines()

    for line in all_lines: 
        line = line.replace('\n','') #改行文字削除
        id, person_name = line.split('\t') #idとnicknameで分ける
        id = int(id)
        nicknames.append([id, person_name])

    # ファイルをクローズする
    nicknames_data.close()

    return nicknames

def load_links_data():

    path = "./sns/links.txt"
    links_table = []

    links_data = open(path, "r")

    # 行ごとにすべて読み込んでリストデータにする
    all_lines = links_data.readlines()

    table_append_index = -1
    for line in all_lines: 
        line = line.replace('\n','') #改行文字削除
        from_id, to_id = map(lambda x:int(x), line.split('\t')) #from_idとto_idで分ける（どちらもint型）
        
        if from_id == table_append_index:
            links_table[from_id].append(to_id)
            # insert_sort(links_table[from_id], to_id)

        # elif table_append_index == -1: #[[to_id]]の形を作る
        #     table_append_index += 1
        #     links_table.append([to_id])


        else:
            if table_append_index > 0:
                links_table[table_append_index].sort()

            while(len(links_table) < from_id):
                links_table.append([])
                table_append_index += 1

            links_table.append([to_id])
            table_append_index += 1

    # ファイルをクローズする
    links_data.close()

    return links_table




def check_person(from_person, to_person, links_table):
    connected_people = links_table[from_person]






nicknames  =  load_nicknames_data()
links_table = load_links_data() #人数分の配列の中につながっている人のindexが入っている

print(links_table)
# print(links)
# print(nicknames[1])
# check_person(from_person, to_person)