Note that Vim also supports terminal feature now: https://www.vim.org/vim-8.1-released.php.

======
Conque
======

Conque is a Vim plugin which allows you to run interactive programs, such as
bash on linux or powershell.exe on Windows, inside a Vim buffer. In other words
it is a terminal emulator which uses a Vim buffer to display the program
output.

Usage
=====

Type `:ConqueTerm <command>` to run your command in vim, for example::

    :ConqueTerm bash
    :ConqueTermSplit mysql -h localhost -u joe -p sock_collection
    :ConqueTermTab Powershell.exe
    :ConqueTermVSplit C:\Python27\python.exe


History
=======

This project is an unofficial clone of the original Conque plugin  by Nico Raffo (nicoraffo at gmail.com), located at https://code.google.com/archive/p/conque/ (previously at http://code.google.com/p/conque/).

The last release on Google Code is version 2.3 (on 2011-09-02).
If you'd like to contribute, open an issue (or even better, a pull request!).  Thanks!


License: MIT License
