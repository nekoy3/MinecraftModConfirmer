# coding: utf_8
import os
import re

def main():
    #1，2引数を取得
    args = os.sys.argv
    if 2 > len(args) < 3:
        print("引数が不適切です。バージョンの指定、対話式確認をするかのフラグを指定してください。")
        return
    version = args[1].split(".")[0] + "." + args[1].split(".")[1]

    try:
        is_interactive = True if args[2] == "true" else False
    except IndexError:
        is_interactive = False
    
    file_list = read_file_list()
    file_list = remove_mcversion(file_list, version)

def read_file_list():
    file_list = []
    for file in os.listdir("./mods"):
        file_list.append(file)
    return file_list

def remove_mcversion(f_list, v):
    for i in range(len(f_list)):
        f_list[i].replace("-" + v, "").replace(r"\[(.+)\]", "")
        print(f_list[i])
    return f_list

#importで実行した際にimportしただけでmain()が実行される事を防ぐためのおまじない
#__name__はファイル名(これならmodconfirmer.pyなので、import modconfirmerとした時modconfirmerとなるが
#pythonコマンドでスクリプトを実行した場合は__name__には文字列"__main__"が代入されるため、if文でmain関数を実行する、という動きをする）
#__main__はpythonコマンドで実行した際に実行される
if __name__ == "__main__":
    main()