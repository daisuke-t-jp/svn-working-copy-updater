# svn-working-copy-updater

## はじめに

登録した SVN ワーキングコピーに対して udpate / checkout を実行できる Python スクリプトです。  
  
このスクリプトを使用することで、個々のワーキングコピーに対してそれぞれ操作をすることなく、  
一括で複数の SVN ワーキングコピーの内容を最新に保つことができます。


## 実行環境

- Python 3


## 使用方法

### 準備 - リポジトリの登録

[config.py](https://github.com/daisuke-t-jp/svn-working-copy-updater/blob/master/config.py) に SVN リポジトリを登録します。  
ファイルにはあらかじめ、サンプルのリポジトリがコメントされています。

```py
    array = [
    {
        KEY_URL : 'http://svn.apache.org/repos/asf/httpd/httpd/trunk/',
        KEY_NAME: 'httpd',
    },
    # 以下、さらにリポジトリを追加する...
    ]
```

リポジトリ情報は Dictionary の Array で表現されています。  
個々のリポジトリは以下の形式で登録します。

- `KEY_URL` リポジトリ URL。
- `KEY_NAME` リポジトリの名前。この名前は、スクリプトで作られるワーキングコピーのディレクトリ名に使用されます。


### スクリプト実行

スクリプトの引数にワーキングコピーのルートのパスを指定して実行します。

```sh
$ python3 svn-working-copy-updater.py <working_copy_root> 

repo http://svn.apache.org/repos/asf/httpd/httpd/trunk/
Checked out revision 1872111.

repo https://svn.apache.org/repos/asf/subversion/trunk/
Checked out revision 1872111.

repo https://svn.apache.org/repos/asf/kafka/trunk/
A    trunk/core
A    trunk/core/src
A    trunk/core/src/test
...
```

対象のリポジトリがワーキングコピーのルート以下に展開されます。  
  
この時、すでに対象のワーキングコピーがあれば `svn update` が実行されます。  
まだワーキングコピー自体がない場合は `svn checkout` が実行されます。
