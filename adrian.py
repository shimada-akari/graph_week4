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
    links = []

    links_data = open(path, "r")

    # 行ごとにすべて読み込んでリストデータにする
    all_lines = links_data.readlines()

    for line in all_lines: 
        line = line.replace('\n','') #改行文字削除
        from_id, to_id = map(lambda x:int(x), line.split('\t')) #from_idとto_idで分ける（どちらもint型）
        links.append([from_id, to_id])

    # ファイルをクローズする
    links_data.close()

    return links

def make_link_data(links):
    people_number = links[-1][0] + 1
    link_table = [[] for _ in range(people_number)]

    links_index = 0

    for i in range(people_number):
        
        while (links_index < len(links)) and (links[links_index][0] == i):
            link_table[i].append(links[links_index][1])
            links_index += 1
    

    return link_table


def check_person(from_person, to_person):
    pass




nicknames  =  load_nicknames_data()
links = load_links_data() 
link_table = make_link_data(links) #人数分の配列の中につながっている人のindexが入っている


# print(link_table)
# print(links)
# print(nicknames[1])
# check_person(from_person, to_person)