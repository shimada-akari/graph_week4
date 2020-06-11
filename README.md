# graph_week4

## sns_folder 　　　　 snsデータを使った解析

### adrian_depth.py ：　深さ優先探索で from -> to　へのパスがあるのかを判定する

### adrian_width.py ：　幅優先探索でfrom -> to　へのパスがあるのか、ある場合は最小の経路（idと名前）を表示する。

'''
from -> to : carolyn bruce
from : 11 to : 10 no 

from -> to : bruce adrian
from : 10 to : 1 yes
3
10 bruce, 5 barry, 8 brent, 1 adrian, 

from -> to : edwin bruce
from : 23 to : 10 yes
15
23 edwin, 12 cecil, 27 francis, 38 janice, 50 kevin, 4 austin, 19 debra, 29 gene, 7 brenda, 28 frederick, 37 jamie, 9 brett, 22 duane, 24 emma, 0 aaron, 10 bruce, 
'''

### check_non_connected.py　：　入力された人に、友達を辿ってもたどり着けない人がいるのかを調べる。たどり着けない人がいる場合、その人の名前とidを表示する。

'''
from : bruce
betty ( 6 )    carolyn ( 11 )    lawrence ( 52 )    
from : cynthi 
There is no people whose name is cynthi.
from : cynthia
betty ( 6 )    carolyn ( 11 )    lawrence ( 52 )    
from : carolyn
aaron ( 0 )    adrian ( 1 )    alan ( 2 )    alexander ( 3 )    austin ( 4 )    barry ( 5 )    betty ( 6 )    brenda ( 7 )    brent ( 8 )    brett ( 9 )    bruce ( 10 )    cecil ( 12 )    cheryl ( 13 )    cody ( 14 )    cynthia ( 15 )    daniel ( 16 )    danielle ( 17 )    darryl ( 18 )    debra ( 19 )    dennis ( 20 )    diane ( 21 )    duane ( 22 )    edwin ( 23 )    emma ( 24 )    eugene ( 25 )    frances ( 26 )    francis ( 27 )    frederick ( 28 )    gene ( 29 )    helen ( 30 )    herman ( 31 )    howard ( 32 )    hugh ( 33 )    jack ( 34 )    jacqueline ( 35 )    jaime ( 36 )    jamie ( 37 )    janice ( 38 )    jared ( 39 )    jay ( 40 )    jeremy ( 41 )    jerry ( 42 )    jimmie ( 43 )    joan ( 44 )    joel ( 45 )    johnnie ( 46 )    jon ( 47 )    judith ( 48 )    kathleen ( 49 )    kevin ( 50 )
'''


## transit_folder　　　　　staionのデータを使った解析

### transit.py　：　現在地の駅名と目的地の駅名の入力を受け取って、現在地の駅から幅優先探索をする。目的地の駅を見つけた時点で探索を終了し、そこに至るまでの経路（駅名と駅id）を表示する。

'''
from : 東中野
to : 東銀座
minimum time :  21
route : 東中野 ( 37 )   大久保 ( 38 )   新宿 ( 7 )   新宿三丁目 ( 87 )   新宿御苑前 ( 88 )   四谷三丁目 ( 89 )   四ツ谷 ( 41 )   永田町 ( 155 )   桜田門 ( 156 )   有楽町 ( 24 )   新橋 ( 25 )   東銀座 ( 103 )   
'''