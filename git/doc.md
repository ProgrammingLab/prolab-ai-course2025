# Gitの環境構築をしよう！  
[GitとGitHubの環境構築](https://zenn.dev/zarathustra/books/79762a7f46d3b4/viewer/bc7a89)からサイトの手順を踏んで環境構築をしよう。  
  
## Gitのコマンドを使ってみよう。  
### 1. このリポジトリを自分の環境に落としてみよう。
(1) 保存したい好きなディレクトリに移動しする
```sh
cd (好きなディレクトリのパス)
```
(2) AI講習リポジトリを`git clone`コマンドで自分の環境に落として、**リポジトリのフォルダに移動する。**
```sh
git clone git@github.com:ProgrammingLab/prolab-ai-course2025.git
cd prolab-ai-course2025
```
(3) ブランチを作成する。(コマンドにあるブランチ名は例)  
```sh
git branch workbranch-ootoro
```
これは`workbranch-ootoro`が作成されただけで、現在のブランチはmainのまま。  
(4) ブランチを確認する。
```sh
git branch
```
実行結果  
```
* main
  workbranch-ootoro
```
(5) ブランチを移動する。
```sh
git switch workbranch-ootoro
```
`git branch`で現在のブランチを確認してみてください。

ここまでで、全員出来たかの確認をします。  
  
### 2. `git pull`をやってみる。 
※講師はここで./git/confirm.mdの内容を変更してpushまでやる。  
(1) ブランチをmainに変更  
```sh
git switch main
```
(2) リモートリポジトリ(origin)のmainブランチから変更を反映する。
```sh
git pull origin main
```
./git/confirm.mdを確認してみてください。**変更が反映されている**はずです。  
(3) ブランチをworkbranch-ootoro(あなたが作成したブランチ)に変更  
```sh
git switch workbranch-ootoro
```
./git/confirm.mdを確認してみてください。**変更が反映されていない**はずです。  
(4) `git merge`でmainの変更を反映させる。
```sh
git merge main
```
./git/confirm.mdを確認してみてください。**変更が反映されている**です。  

### 3. 次回以降のGitの利用
習うより慣れよの精神で毎回最初にGitのコマンドを打ってもらいます。  
**毎回このリポジトリに新しいフォルダを追加するので、それを自分のパソコンに`git pull`で反映してください。**  
手順は[2. git pullをやってみる。](#2-git-pullをやってみる)と同じようにすればできます。 

### 4. 補足
今回、詳しく紹介していないコマンドがたくさんあります。…が、それをいきなり説明してもパンクするだけなのでここでは必要最低限のものしか紹介していません。  
部内ハッカソンを本格的に始動する時には改めて共同開発のためのGitの使い方を簡単に紹介するつもりではありますが、そんなの待ってられねぇ！って人は[サル先生のGit入門](https://backlog.com/ja/git-tutorial/)から独学してみてください。