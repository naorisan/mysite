############################################################
# 2-11
# 複数のシートの情報を1つのシートにまとめる
############################################################
#-----------------------------------------------------------
#ライブリの読込
#-----------------------------------------------------------
import pandas as pd #pandasをインポート
import openpyxl #エクセルのブックを操作するライブラリの読み込み

#指定したブックのすべてのシートを読み込み
df = pd.read_excel("sample2.xlsx",sheet_name=None)
dataList = [] #集計表へ書き出すデータを保存するリスト
sheetsList = list(df.keys())

#シートループ
for sheet in df:
    #行ループ
    for index,rows in df[sheet].iterrows():
        work = [] #作業用リスト
        #列ループ
        for row in rows:
            work.append(row)
        dataList.append(work)

#列名をリストで取得
columns = list(df[sheetsList[0]].columns)
df["統合表"] = pd.DataFrame(dataList,columns=columns)#集計表に全店舗の売上データを追加

#シートごとにエクセルブックに書き出し 2020/12/01 engine="openpyxl"を追加
with pd.ExcelWriter("sample2.xlsx",engine="openpyxl",date_format='YYYY/MM/DD',datetime_format='YYYY/MM/DD',mode = "a") as writer:
    df["統合表"].to_excel(writer,sheet_name="統合表",index=False)
