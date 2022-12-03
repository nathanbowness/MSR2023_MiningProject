#+STARTUP: showall indent

* Fakeymacs

Fakeymacs は、Windows の操作を Emacs のキーバインドで行えるようにするための
Keyhac の設定です。

Keyhac for Windows ver 1.82 以上のバージョンでご利用ください。

- https://sites.google.com/site/craftware/keyhac-ja

manual は次のリンクを参照してください。

1. [[fakeymacs_manuals/configuration_parameters.org][Configuration parameters]]
1. [[fakeymacs_manuals/key_bindings.org][Key bindings]]
1. [[fakeymacs_manuals/extensions.org][Extensions]]
1. [[fakeymacs_manuals/functions.org][Functions]]

次のページにも関連の情報があります。

- [[https://www49.atwiki.jp/ntemacs/pages/25.html][Windows の操作を Emacs のキーバインドで行うための設定 （Keyhac版）]]

** 本設定のキーバインドがサポートする機能

本設定のキーバインドでは、次の機能をサポートしています。

- Emacs標準キーバインド
- Emacs日本語入力モード [1]
- other_window（一番最近までフォーカスがあったウィンドウに移動する機能）
- shell_command（コマンドコンソールを起動する機能）
- アクティブウィンドウの切り替え [2]
- アクティブウィンドウのディスプレイ間移動
- デュアルディスプレイにそれぞれ表示されているウィンドウの入れ替え
- ウィンドウの最大化、リストア
- ウィンドウの最小化、リストア
- 仮想デスクトップの切り替え
- クリップボードリスト
- ランチャーリスト
- 拡張機能（Extensions）で実現している機能

また、関連して次の機能もサポートしています。

- 日本語キーボード設定されている OS で英語キーボードを使うための機能
- IME の状態をテキスト カーソル インジケーターの色で表現する機能

[1] IME が ON の時に文字（英数字か、スペースを除く特殊文字）を入力すると起動するモードです。
（モードに入ると、▲のマークが表示されます。） Emacs日本語入力モードになると Emacsキーバインド
として利用できるキーが限定され、その他のキーは Windows にそのまま渡されるようになるため、
IME のショートカットキーが利用できるようになります。
また、このモードでは IME のショートカットを置き換える機能もサポートしており、初期値では
「ことえり」のキーバインドを利用できるようにしています。

[2] A-Esc キーの動作とは異なり、仮想デスクトップを跨ぎ、最小化されていないウィンドウを順に
切り替える機能を提供します。作業するウィンドウのみを表示するようにしておけば、その表示している
ウィンドウ間を容易に行き来することが可能となります。ウィンドウの最小化の機能、other_window
の機能と併せて利用すると、より有用な機能になると思います。

** 使い方

*** 1) キーボード配列の調整を行う

Aキーの左横が Caps Lock のキーボードを使っている場合は、右 Control キーに置き換える
ことをお勧めします。

Caps Lock のキーの置き換えは Keyhac ではできませんので、KeySwap や Change Key という
ツールで対応ください。Caps Lock の変更だけであれば、KeySwap の利用をお勧めします。

- http://pasokatu.com/8460

変更後、Windows の再ログインを行ってください。

*** 2) Keyhac をインストールする

次のサイトから Keyhac をインストールしてください。

- https://sites.google.com/site/craftware/keyhac-ja

起動時に dll load エラーが発生する場合は、「Microsoft Visual C++ 再頒布可能パッケージ」を
インストールする必要があります。上記のサイトにリンクしてあるものは少し古いバージョンですので、
次のサイトから最新の「Visual Studio 2015、2017、2019、および2022の Microsoft Visual C++
再頒布可能パッケージ」をダウンロードし、インストールしてください。

- https://docs.microsoft.com/ja-JP/cpp/windows/latest-supported-vc-redist?view=msvc-170

※ Windows OS が x64版 でも、「Microsoft Visual C++ 再頒布可能パッケージ」は x86版 を
インストールする必要があります。

※ dll load エラーが発生しない場合でも、「Microsoft Visual C++ 再頒布可能パッケージ」の
最新版をインストールすることは意味のあることかもしれません。

※ 上記でインストールされる C:\Windows\SysWOW64\msvcp140.dll を keyhac.exe と同じフォルダに
置けば、再頒布可能パッケージをインストールしていない PC でも Keyhac を動かすことができる
ようになります。

*** 3) Keyhac を自動起動するようにする

Win+R で開く画面に shell:startup と入力して Startup フォルダを開き、インストールした Keyhac
フォルダ配下にある keyhac.exe のショートカットを Startup フォルダに配置してください。

*** 4) Fakeymacs をダウンロードする

本サイトの Code のボタン（緑色のボタン）から、Download ZIP を選択し、Fakeymacs 一式を
ダウンロードしてください。（可能であれば、Git を使ってダウンロードすることをお勧めします。
Git を使うと、今後の Fakeymacs のバージョンアップに容易に対応できます。）

*** 5) 必要なファイルを Keyhac のフォルダに複写する

ダウンロードした Fakeymacs の ZIPファイルから、必要なファイルを Keyhac のフォルダに複写
します。次の中から必要なファイルを複写してください。（フォルダ配下にあるファイルは、
フォルダ階層を維持して複写するようにしてください。）

|------------------------+---------------------------------------------------------------------------------------------|
| Filename               | Description                                                                                 |
|------------------------+---------------------------------------------------------------------------------------------|
| config.py              | Fakeymacs の本体です。このファイルは必ず必要です。                                          |
| _config_personal.py    | 個人設定ファイルです。config_personal.py という名称に変更することで機能するようになります。 |
| fakeymacs_extensions/* | 機能拡張ファイルです。config_personal.py の中で有効／無効を切り替えることができます。       |
|------------------------+---------------------------------------------------------------------------------------------|

*** 6) コンフィグレーションパラメータをカスタマイズする

config.py の内容をみて、変更したいコンフィグレーションパラメータをカスタマイズします。
カスタマイズする際は、_config_personal.py ファイルを config_personal.py という名称に変更し、
このファイルの中で設定を修正するようにしてください。

次は、修正する必要性が高いと思われるコンフィグレーションパラメータです。

|-------------------------+----------------------------------------------------------------------|
| Configuration Parameter | Description                                                          |
|-------------------------+----------------------------------------------------------------------|
| ime                     | 利用している IME を指定する                                          |
| not_emacs_target        | Emacs のキーバインドに“したくない”アプリケーションソフトを指定する |
| ime_target              | IME の切り替え“のみをしたい”アプリケーションソフトを指定する       |
| side_of_ctrl_key        | 左右どちらの Ctrlキーを使うかを指定する                              |
| use_esc_as_meta         | Escキーを Metaキーとして使うかどうかを指定する                       |
| use_emacs_ime_mode      | Emacs日本語入力モードを使うかどうかを指定する                        |
| toggle_input_method_key | IME をトグルで切り替えるキーを指定する                               |
| set_input_method_key    | IME を切り替えるキーの組み合わせ（disable、enable の順）を指定する   |
|-------------------------+----------------------------------------------------------------------|

※ 1) で Caps Lock に右 Control キーを割り当てた場合には、side_of_ctrl_key を "R" に
変更する必要があります。この場合、左 Control キーは従来どおり Windows ショートカット用
のキーとして利用できます。

*** 7) 拡張機能の設定を行う

config_personal.py には、Fakeymacs の拡張機能を有効化／無効化するための設定も含まれています。
（初期設定では、vscode_key Extension のみ有効にしています。）

次のページを参照して、使いたい拡張機能があればその設定を行ってください。
（拡張機能を有効化する場合には、if 0: を if 1: にしてください。
また、必要であれば、コンフィグレーションパラメータの設定も行ってください。）

- https://github.com/smzht/fakeymacs/blob/master/fakeymacs_manuals/extensions.org

VSCode を利用する場合には、次の vscode_key Extension 用のコンフィグレーションパラメータの設定は
確認してください。

|-------------------------------------+------------------------------------------------------------------------------------------------------------------|
| Configuration Parameter             | Description                                                                                                      |
|-------------------------------------+------------------------------------------------------------------------------------------------------------------|
| vscode_target                       | VSCode 用のキーバインドを利用するアプリケーションソフトを指定する                                                |
| use_direct_input_in_vscode_terminal | VSCode の Terminal内 で ４つのキー（Ctrl+k、Ctrl+r、Ctrl+s、Ctrl+y）のダイレクト入力機能を使うかどうかを指定する |
|-------------------------------------+------------------------------------------------------------------------------------------------------------------|

*** 8) テキスト カーソル インジケーターの設定を行う

IME の状態をテキスト カーソル インジケーターの色で表現する機能を利用する場合、次のページを参考とし、
テキスト カーソル インジケーターを有効にしてください。

-  https://faq.nec-lavie.jp/qasearch/1007/app/servlet/relatedqa?QID=022081

また、config_personal.py 内の use_ime_status_cursor_color 変数を True にしてください。

※ テキスト カーソル インジケーターは次の issue で報告されているとおり、VSCode で正常に動作しません。

- https://github.com/microsoft/vscode/issues/109151

Backlog として扱われているようですので、改善については気長に待ちたいと思います。

*** 9) SylphyHorn の設定を行う

アクティブウィンドウを仮想デスクトップ間で移動する機能を利用する場合、次のページから  SylphyHornPlus
をインストールしてください。（SylphyHornPlus は、Microsoft Store からインストール可能な SylphyHorn
の Fork で、Windows 11 の対応など、改良が加えられたものとなっています。）

- https://github.com/hwtnb/SylphyHornPlusWin11/releases

また、操作のためのキー設定を config_personal.py 内で window_movement_key_for_desktops 変数に対し、
行ってください。（変数の設定方法は、config.py を参考としてください。）

※ SylphyHorn の仮想デスクトップ切り替え時に表示される通知機能は、テキスト カーソル インジケーター
と相性が悪いようです（インジケーターが消えてしまいます）。SylphyHorn とテキスト カーソル インジケーター
の機能を同時に利用する場合には、SylphyHorn の通知機能を OFF にし、代わりに「デスクトップの番号を
タスクトレイに表示する」機能を利用するようにしてください。

*** 10) keyhac.exe を起動する

keyhac.exe を起動すると、タスクバー（＾アイコンの中）に Keyhac のアイコンが表示されます。
必要に応じて、通知領域に表示するようにしてください。
このアイコンを左クリックするとコンソールが表示され、右クリックすると機能の一覧が表示されます。

** 個人設定ファイル（config_personal.py）

_config_personal.py というファイルを config_personal.py というファイル名にすることで個人設定ファイル
として機能します。本ファイルの設定には [ ] で括られたセクション名が定義されており、その単位で config.py
の中に設定が取り込まれ、exec 関数により実行されます。

config.py のコンフィグレーションパラメータ等の設定を変更したい内容は、config_personal.py に記載して
管理することで、config.py のバージョンアップに容易に対応できるようになります。

何のセクションがどこで読み込まれるかについては、config.py ファイル内の exec 関数をコールしている
ところを検索して確認してください。

** クロージャについて

Fakeymacs では、Python のクロージャの機能を多用しています。次のページを読むと、クロージャの理解が
深まり、Fakeymacs の設定も読みやすくなると思います。

- https://www.lifewithpython.com/2014/09/python-use-closures.html

** VSCode の機能強化について

VSCode については、次の２つの拡張機能により、機能強化を図っています。

|-------------------+---------------------------------------|
| Extension name    | Description                           |
|-------------------+---------------------------------------|
| [[/fakeymacs_extensions/vscode_key][vscode_key]]        | VSCode 用のキーの設定を行う           |
| [[/fakeymacs_extensions/vscode_extensions][vscode_extensions]] | VSCode Extension 用のキーの設定を行う |
|-------------------+---------------------------------------|

VSCode の Emacs Keymap Extension と比較した本機能の特徴は、次のページの *<2021/02/23 追記>*
の箇所に記載しています。参考としてください。

- https://w.atwiki.jp/ntemacs/pages/25.html

** 留意事項

● Microsoft Excel や Word などの Office系アプリを使ってコピー＆ペーストをした際、「Ctrl」と表示
される「貼り付けオプション」ボタンが表示される場合があります。
この「貼り付けオプション」ボタンは、fc.side_of_ctrl_key 変数で指定している側の Ctrl キーではオープン
しないように対策していますので、「貼り付けオプション」ボタンを操作する場合は、fc.side_of_ctrl_key
変数で指定している側でない Ctrl キーを単押しするか、マウスを使って操作するようにしてください。
また、「貼り付けオプション」ボタンが不要な場合には、次のページの記載に従い、ボタンを表示しない設定
としてご利用ください。

- https://www.koikikukan.com/archives/2020/02/02-235555.php

● Keyhac のクリップボードリスト画面で migemo 検索を可能とするためには、辞書ファイルを登録する必要
があります。次のページに分かりやすく説明がされていますので、参考としてください。
（dictフォルダの中をすべてコピーするのではなく、dict/utf-8 の中のファイルをコピーするところが
ポイントです。また、migemo 検索するには、検索文字列の一文字目を大文字で指定する必要があります。）

- http://blog.livedoor.jp/ryman_trainee/archives/1042315792.html

● Logicool のマウス で SetPoint アプリによりキーストロークの割当を行った場合、Keyhac のフックを
OFF にしてから割当をしないと正常に動作しませんでした。他のキーストロークを設定するソフトの場合
にも同様の問題が発生する可能性があると思いますので、ご留意ください。

● Windows 11 にしたら、Keyhac のコンソールに「Time stamp inversion happened.」と表示される頻度が
高くなりました。これは、レジストリ HKEY_CURRENT_USER\Control Panel\Desktop\LowLevelHooksTimeout を
DWORD 形式で作成し、そこに ms の値（10進数で 3000、5000 などの数値）を設定して再起動することで、
ある程度の回避ができるようです。ただし、この設定により生ずる影響は分かっていませんので、試す場合は
各自の責任でお願いします。

- https://apollo440.hatenablog.com/entries/2010/12/21
- https://nazochu.blogspot.com/2011/08/windows7.html
- https://blogs.msdn.microsoft.com/alejacma/2010/10/14/global-hooks-getting-lost-on-windows-7/
- https://jinblog.at.webry.info/201103/article_9.html
- https://jinblog.at.webry.info/201103/article_10.html
