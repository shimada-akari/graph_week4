#ダイクストラ隣接リスト版

def load_stations(path): #path = "./transit/stations.txt"
    
    stations_data = open(path, "r")

    all_lines = stations_data.readlines()
    station_id_dic = {}
    id_station_list = []

    for line in all_lines:
        line = line.replace("\n", "")
        id, station = line.split("\t")
        id = int(id)
        station_id_dic[station] = id
        while(len(id_station_list) < id):
            id_station_list.append("")
        id_station_list.append(station)

    return station_id_dic, id_station_list


def search_id(station_id_dic, station):
    if station in station_id_dic:
        return station_id_dic[station]

    else:
        print("There is no station whose name is {}.".format(station))
        return None


def add_linked_id(from_id, to_id, min, edges_list):
    # print(from_id, to_id, min)
    if edges_list[from_id] == None: #edges_listにto_idを追加するのが初めての駅
        edges_list[from_id] = [[to_id, min]]
    else:
        edges_list[from_id].append([to_id, min])   

    return edges_list


def load_edges(path, STATIONS_NUMBER): #path = "./transit/edges.txt"
    
    edges_list = [None] * STATIONS_NUMBER

    edges_data = open(path, "r")

    all_lines = edges_data.readlines()
    

    for line in all_lines:
        line = line.replace("\n", "")
       
        from_id, to_id, min= map(lambda x:int(x), line.split("\t")) 

        edges_list = add_linked_id(from_id, to_id, min, edges_list)
        edges_list = add_linked_id(to_id, from_id, min, edges_list)    
    
    return edges_list

def find_min_node(min_minutes, color_list):
    min_min = INF #min_min = minimum minutes 最小時間を記録
    min_node = -1
    for i in range(STATIONS_NUMBER):
        if (min_minutes[i] != INF) and (color_list[i] != DONE): #min_minutes[i] != INF 
            if min_minutes[i] < min_min: #min_minutesの中で最小の値を探す
                min_node = i
                min_min = min_minutes[i]

    return min_node

def culculate_minites(min_node, edges_list, min_minutes, color_list, parents):
    for node_info in edges_list[min_node]:
        linked_node = node_info[0]
        linked_node_min = node_info[1]
        
        if (color_list[linked_node] != DONE) and (min_minutes[linked_node] > min_minutes[min_node] + linked_node_min):
            min_minutes[linked_node] = min_minutes[min_node] + linked_node_min
            color_list[linked_node] = DOING
            parents[linked_node] = min_node

    return min_minutes, color_list
        
def print_and_make_route(stack, id_station_list): #ルートの表示とルートリストの作成(assert用)
    route = []

    print("route : ", end = "")

    while(stack):
        id = stack.pop(-1)
        route.append(id)

        print(id_station_list[id], "(", id, ")", end = "   ")
        
    print("")

    return route
    
def make_stack(from_id, to_id, parents): #routeのstackを作る
    next_id = to_id #routeを遡る
    stack = []
    stack.append(next_id)

    while(next_id != from_id):
        stack.append(parents[next_id])
        next_id = parents[next_id]

    return stack

def dijkstra(edges_list, id_station_list, from_id, to_id):

    min_minutes = [INF]*STATIONS_NUMBER
    parents = [-1]*STATIONS_NUMBER
    color_list = [UNDO]*STATIONS_NUMBER

    min_minutes[from_id] = 0
    
    while(True):

        min_node = find_min_node(min_minutes, color_list) #探索完了ノード以外のノードの中で、min_minutesの値が最も小さいノードを見つける

        if (min_node == -1) or (min_node == to_id): #全部　探索済み or to_nodeに行き着いた
            break
        
        color_list[min_node] = DONE
        min_minutes, color_list = culculate_minites(min_node, edges_list, min_minutes, color_list, parents) #min_nodeに隣接するノードについて最小値を計算


    stack = make_stack(from_id, to_id, parents)

    print("minimum time : ", min_minutes[to_id])
    
    route = print_and_make_route(stack, id_station_list)

    return min_minutes[to_id], route


def test(actual_min, actual_stack, edges_list, id_station_list, from_id, to_id):
    
    result_min, result_stack = dijkstra(edges_list, id_station_list, from_id, to_id)
    assert(result_min == actual_min)
    assert(actual_stack == result_stack)


def run_test():
    global STATIONS_NUMBER

    #test 1
    station_id_dic, id_station_list = load_stations("./transit/test_stations1.txt") #stations.txtの内容を返す。[[id, station_name], [], [], ...]
    STATIONS_NUMBER = len(station_id_dic)
    edges_list = load_edges("./transit/test_edges1.txt", STATIONS_NUMBER) #edges.txtの内容を返す。[[from_id, to_id, minits], [], [], ...]

    #本当はinputで入力された駅名のみidをゲットする
    OSAKI_id = search_id(station_id_dic, "大崎")
    GOTANDA_id = search_id(station_id_dic, "五反田")
    HARAJUKU_id = search_id(station_id_dic, "原宿")
    MEGURO_id = search_id(station_id_dic, "目黒")
    EBISU_id = search_id(station_id_dic, "恵比寿")

    
    test(0, [0], edges_list, id_station_list, OSAKI_id, OSAKI_id) 
    test(2, [0, 1], edges_list, id_station_list, OSAKI_id, GOTANDA_id) 
    test(4, [0, 1, 2], edges_list, id_station_list, OSAKI_id, MEGURO_id) 
    test(7, [0, 1, 2, 3], edges_list, id_station_list, OSAKI_id, EBISU_id) 
    test(2, [1, 0],edges_list, id_station_list, GOTANDA_id, OSAKI_id) 
    test(0, [1], edges_list, id_station_list, GOTANDA_id, GOTANDA_id) 
    test(2, [1, 2], edges_list, id_station_list, 1, 2) 
    test(5, [1, 2, 3], edges_list, id_station_list, 1, 3) 
    test(4, [2, 1, 0],edges_list, id_station_list, 2, 0) 
    test(2, [2, 1], edges_list, id_station_list, 2, 1) 
    test(0, [2], edges_list, id_station_list, 2, 2) 
    test(3, [2, 3], edges_list, id_station_list, 2, 3) 
    test(7, [3, 2, 1, 0],edges_list, id_station_list, 3, 0) 
    test(5, [3, 2, 1], edges_list, id_station_list, 3, 1) 
    test(3, [3, 2], edges_list, id_station_list, 3, 2) 
    test(0, [3], edges_list, id_station_list, 3, 3) 


    #test 2
    station_id_dic, id_station_list = load_stations("./transit/test_stations2.txt") #stations.txtの内容を返す。[[id, station_name], [], [], ...]
    STATIONS_NUMBER = len(station_id_dic)
    edges_list = load_edges("./transit/test_edges2.txt", STATIONS_NUMBER) #edges.txtの内容を返す。[[from_id, to_id, minits], [], [], ...] 
    test(2, [0, 1], edges_list, id_station_list, 0, 1) 
    test(2, [0, 3, 2], edges_list, id_station_list, 0, 2) 
    test(1, [0, 3], edges_list, id_station_list, 0, 3)    
    test(3, [0, 3, 2, 4], edges_list, id_station_list, 0, 4)  

def main():
    global STATIONS_NUMBER
    station_id_dic, id_station_list = load_stations("./transit/stations.txt") #stations.txtの内容を返す。[[id, station_name], [], [], ...]
    STATIONS_NUMBER = len(station_id_dic)

    edges_list = load_edges("./transit/edges.txt", STATIONS_NUMBER) #edges.txtの内容を返す。[[from_id, to_id, minits], [], [], ...]
    
    # print(station_id_dic)
    # print(edges_list)
    while(True):
        from_station = input("from : ")
        to_station = input("to : ")

        from_id = search_id(station_id_dic, from_station)
        to_id = search_id(station_id_dic, to_station)

        if from_id == None or to_id == None: #入力不正
            continue

        dijkstra(edges_list, id_station_list, from_id, to_id)


if __name__ == "__main__":
    INF = 100000000
    DONE = 2 #探索完了
    DOING = 1 #訪問済み、未探索
    UNDO = 0 #未訪問

    run_test()
    main()

