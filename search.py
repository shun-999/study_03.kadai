import pandas as pd
import eel

### デスクトップアプリ作成課題
def kimetsu_search(word, file):
    # 検索対象取得
    #df=pd.read_csv("./source.csv")
    df = pd.read_csv(file)
    source=list(df["name"])

    # 検索
    if word in source:
        print("『{}』はあります".format(word))
        eel.view_log_js("「{}」はいます".format(word))
    else:
        print("『{}』はありません".format(word))
        eel.view_log_js("「{}」はいません".format(word))
        # 追加
        #add_flg=input("追加登録しますか？(0:しない 1:する)　＞＞　")
        #if add_flg=="1":
        eel.view_log_js("「{}」を追加します".format(word))
        source.append(word)
    
    # CSV書き込み
    df=pd.DataFrame(source,columns=["name"])
    #df.to_csv("./source.csv",encoding="utf_8-sig")
    df.to_csv(file, encoding="utf_8-sig")
    print(source)
