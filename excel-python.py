import pandas as pd #Excelのブックを操作するライブラリ

#Excelに出力するデータを格納するリスト
item_list = []
item_no = input("商品番号を入力してください。終了は-1:")

while(int(item_no) != -1):
    item_name = input("商品名を入力してください:")
    item_price = input("価格を入力してください:")
    item_sales = input("売上額を入力してください:")
    #入力したデータをリスト形式で追加
    item_list.append([item_no, item_name, item_price, item_sales])

    item_no = input("商品番号を入力してください。終了は-1:")

#データリストに見出し（列名）を付ける
df = pd.DataFrame(item_list, columns = ['商品番号', '商品名', '価格', '売上額'])

#1行目：Excelファイルを書き出すための準備
#2行目：実際にExcelファイルを書き出す
#※withブロックにすることでExcelファイルに書き込み終了後、Excelファイルを閉じてくれる。
with pd.ExcelWriter("sample.xlsx") as writer:
    df.to_excel(writer, index = False)
