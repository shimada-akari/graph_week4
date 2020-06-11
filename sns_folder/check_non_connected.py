#幅優先探索
#たどり着けない人っているのでしょうか

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
        # id = int(id)
        # nicknames.append([id, next_id_name])
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

    # 行ごとにすべて読み込んでリストデータにする
    all_lines = links_data.readlines()

    table_append_index = -1
    for line in all_lines: 
        line = line.replace('\n','') #改行文字削除

        from_id, to_id = map(lambda x:int(x), line.split('\t')) #from_idとto_idで分ける（どちらもint型）
        
        if from_id == table_append_index:

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


def search_id(nickname, id_nicknames):
    index = bisect.bisect_left(id_nicknames, nickname)

    if index < len(id_nicknames) and id_nicknames[index] == nickname:
        return index
    else:
        print("There is no people whose name is {}.".format(nickname))
        return None

def search_connection(from_id, links_table, people_number):
    visited_list = [0]*people_number #未訪問なら0
    queue = []
    queue.append(from_id)
    nodes_counter = [0]*people_number
    route_list = [[i] for i in range(people_number)]
  
    for i in range(people_number):
        if visited_list[i] != 0: #訪問済みノード
            continue

        while(len(queue) != 0):
            # print(queue)
            next_id = queue.pop(0)

            if visited_list[next_id] == 0: #queueから取り出した要素が未訪問
                visited_list[next_id] += 1
            

                for neighbor in links_table[next_id]:
                    queue.append(neighbor)
                    nodes_counter[neighbor] = nodes_counter[next_id] + 1
            
                    route_list[neighbor] = route_list[next_id].copy() #静的確保
                    # print("before", route_list[next_id], route_list[neighbor])
                    route_list[neighbor].append(neighbor)
                    # print(route_list, next_id, neighbor)

        
    not_connected = []
    for i in range(people_number):
        if visited_list[i] == 0: #未訪問ノード
            not_connected.append(i)
      
  
    return not_connected



def check_link(from_id, links_table, id_nicknames):
    people_number = len(id_nicknames)

    return search_connection(from_id, links_table, people_number)

    



def run_test():

    #テスト1
    id_nicknames = ["aaron", "adrian", "alan", "alex"]
    links_table = [[1], [], [0, 3], [1, 2]]
    
    assert([2, 3] == check_link(0, links_table, id_nicknames))
    assert([0, 2, 3] ==  check_link(1, links_table, id_nicknames))
    assert([] ==  check_link(2, links_table, id_nicknames))
    assert([] ==  check_link(3, links_table, id_nicknames))   
   

    #テスト2
    id_nicknames = ["aaron", "adrian", "alan", "alex"]
    links_table = [[], [], [], []]
  
    assert([1, 2, 3] == check_link(0, links_table, id_nicknames))
    assert([0, 2, 3] == check_link(1, links_table, id_nicknames))   
    assert([0, 1, 3] == check_link(2, links_table, id_nicknames))
    assert([0, 1, 2] == check_link(3, links_table, id_nicknames)) 

    #テスト3
    id_nicknames = ["aaron", "adrian"]
    links_table = [[1], []]

    assert([] == check_link(0, links_table, id_nicknames))
    assert([0] == check_link(1, links_table, id_nicknames))   

    #テスト4
    id_nicknames = ["aaron", "adrian", "alan", "alex"]
    links_table = [[1], [2], [3], [0]]

    assert([] == check_link(0, links_table, id_nicknames))
    assert([] == check_link(1, links_table, id_nicknames))
    assert([] == check_link(2, links_table, id_nicknames))
    assert([] == check_link(3, links_table, id_nicknames)) 

    #テスト5
    id_nicknames = ["aaron"]
    links_table = [[]]

    assert([] == check_link(0, links_table, id_nicknames))

    #テスト6
    id_nicknames = ["aaron", "adrian", "alan", "alex"]
    links_table = [[], [0, 2, 3], [], []]

    assert([1, 2, 3] == check_link(0, links_table, id_nicknames))
    assert([] == check_link(1, links_table, id_nicknames))
    assert([0, 1, 3] == check_link(2, links_table, id_nicknames))
    assert([0, 1, 2] == check_link(3, links_table, id_nicknames))     

    #テスト7
    id_nicknames = ["aaron", "adrian", "alan", "alex"]
    links_table = [[], [0], [0], [0]]

    assert([1, 2, 3] == check_link(0, links_table, id_nicknames))
    assert([2, 3] == check_link(1, links_table, id_nicknames))
    assert([1, 3] == check_link(2, links_table, id_nicknames))
    assert([1, 2] == check_link(3, links_table, id_nicknames))     

def main():

    id_nicknames  =  load_nicknames_data() #id_nicknames : idのindexにnicknameが入っている, nicknamesのabc順
    links_table = load_links_data() #人数分の配列の中につながっている人のindexが入っている

    people_number = len(id_nicknames)

    while(True):
        from_nickname = input("from : ")
        
        from_id = search_id(from_nickname, id_nicknames)

        if from_id == None:
            continue
       
        non_connected = check_link(from_id, links_table, id_nicknames)

        if len(non_connected) != 0:
            
            print(" ".join(map(lambda x:str(x), non_connected)))
        else:
            print("All connected.")

if __name__ == "__main__":
    run_test()
    main()