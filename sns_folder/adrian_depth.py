#深さ優先探索


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
        id, next_id_name = line.split('\t') #idとnicknameで分ける
        nicknames.append(next_id_name)

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
    
    all_lines = links_data.readlines() # 行ごとにすべて読み込んでリストデータにする

    table_append_index = -1
    for line in all_lines: 
        line = line.replace('\n','') #改行文字削除

        from_id, to_id = map(lambda x:int(x), line.split('\t')) #from_idとto_idで分ける（どちらもint型）
        
        if from_id == table_append_index:

            links_table[from_id] = sort(links_table[from_id], to_id)

        else:

            while(len(links_table) < from_id): #誰もフォローしていない人がいた場合、その人用の空リストを追加する
                links_table.append([])
                table_append_index += 1

            links_table.append([to_id])
            table_append_index += 1
    
    links_data.close() # ファイルをクローズする

    return links_table


def search_id(nickname, id_nicknames):
    index = bisect.bisect_left(id_nicknames, nickname)
    if id_nicknames[index] == nickname:
        return index
    else:
        print("There is no people whose name is {}.".format(nickname))
        exit()


def search_connection(from_id, to_id, links_table, people_number):
    
    visited_list = [-1] * people_number #-1ならunvisited, 1なら探索修了   
    stack = []

    stack.append(from_id)

    while (len(stack) != 0): #stackに何も無くなったら探索終了　to_idは無し
        
        next_id = stack.pop(-1)

        if next_id == to_id:
            return "yes" #探索終了
         
        elif visited_list[next_id] == -1:
            visited_list[next_id] += 1 
            
            for neighbor in links_table[next_id]:
                stack.append(neighbor)

    return "no"


def check_link(from_id, to_id, links_table, id_nicknames): 
    people_number = len(id_nicknames)

    flag = search_connection(from_id, to_id, links_table, people_number)

    print(flag) 
        

def run_test():

    #テスト1
    id_nicknames = ["aaron", "adrian", "alan", "alex"]
    links_table = [[1], [], [0, 3], [1, 2]]
    

    check_link(0, 1, links_table, id_nicknames) #yes 0,1
    check_link(0, 2, links_table, id_nicknames) #no
    check_link(0, 3, links_table, id_nicknames) #no

    check_link(1, 0, links_table, id_nicknames) #no
    check_link(1, 2, links_table, id_nicknames) #no
    check_link(1, 3, links_table, id_nicknames) #no

    check_link(2, 0, links_table, id_nicknames) #yes 2, 0
    check_link(2, 1, links_table, id_nicknames) #yes 2, 3, 1
    check_link(2, 3, links_table, id_nicknames) #yes 2, 3

    check_link(3, 0, links_table, id_nicknames) #yes 3, 2, 0
    check_link(3, 1, links_table, id_nicknames) #yes 3, 1
    check_link(3, 2, links_table, id_nicknames) #yes 3, 2

    #テスト2
    id_nicknames = ["aaron", "adrian"]
    links_table = [[], []]
  
    check_link(0, 1, links_table, id_nicknames) #no

    #テスト3
    id_nicknames = ["aaron", "adrian"]
    links_table = [[1], []]

    check_link(0, 1, links_table, id_nicknames) #yes 0,1
    check_link(1, 0, links_table, id_nicknames) #no

    #テスト4
    id_nicknames = ["aaron", "adrian", "alan", "alex"]
    links_table = [[1], [2], [3], [0]]

    check_link(0, 1, links_table, id_nicknames) #yes 
    check_link(0, 2, links_table, id_nicknames) #yes
    check_link(0, 3, links_table, id_nicknames) #yes
    check_link(1, 0, links_table, id_nicknames) #yes 
    check_link(1, 2, links_table, id_nicknames) #yes 
    check_link(1, 3, links_table, id_nicknames) #yes 

def main():

    id_nicknames  =  load_nicknames_data() #id_nicknames : idのindexにnicknameが入っている, nicknamesのabc順
    links_table = load_links_data() #人数分の配列の中につながっている人のindexが入っている

    people_number = len(id_nicknames)
    

    while(True):
        from_nickname, to_nickname = map(lambda x:x, input("from -> to : ").split())
        
        from_id = search_id(from_nickname, id_nicknames)
        to_id = search_id(to_nickname, id_nicknames)

        # print(from_id, to_id)
        check_link(from_id, to_id, links_table, id_nicknames)



if __name__ == "__main__":
    run_test() #テスト実行
    main()
