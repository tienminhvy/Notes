<div id="toc" />
## Table of content
1. [Chapter 1](#chapter-1)
    - [Lesson 1: basic operation](#c1-lesson1)
    - [Lesson 2: the delete operator](#c1-lesson2)
    - [Lesson 3: the change operator](#c1-lesson3)
    - Lesson 4
        - [Lesson 4-1: cursor location and file status](#c1-lesson4-1)
        - [Lesson 4-2: the search command](#c1-lesson4-2)
        - [Lesson 4-3: cursor location and file status](#c1-lesson4-3)
    - [Lesson 5](#c1-lesson5)
    - [Lesson 6](#c1-lesson6)

<div id="chapter-1" />
## Chapter 1 ([toc](#toc))

<div id="c1-lesson1" />
### Lesson 1: basic operation

1. Moving cursor with `up`, `down`, `left`, `right`
2. Starting vim with `vim file-name.ext`
3. Exiting vim with:
    - `ESC` :`q!` to discard all changes
    - `ESC` :`wq` to save all changes
4. Deleting any character with `ESC` `x`

<div id="c1-lesson2" />
### Lesson 2: the delete operator

1. Deleting from the cursor to the next word type: `dw`
2. Deleting from the cursor to the end of the word type: `de`
3. Deleting from the cursor to the end of a line type: `d$`
4. Deleting a whole line: `dd`

5. Repeating a motion: `operator [number] motion`. Where
    - operator: For what to do. Ex: `d` for delete
    - number: Optional count to repeat a motion
    - motion: moves over the text to operate on. Ex: `w` (word), `e` (end of word), `$` (end of line), etc
6. Moving to the start on the line: `0`
7. Undoing actions:
    - `u` for previous actions.
    - capital u `U` for all the changes on a line.
    - `CTRL-R` for undo the undos (redo)

<div id="c1-lesson3" />
### Lesson 3: the change operator

1. Putting the previous deleted text to the cursor with `p`.
2. Replacing the character at the cursor with x with `rx` (x is the typed character).
3. Changing the word (removing then inserting) to the end of the word with `ce`
4. Changing the word to the end of the line with `cc`, `c$`
5. Changing can also work with the format `operator [number] motion`

<div id="c1-lesson4-1" />
### Lesson 4.1: cursor location and file status
1. Press `CTRL-G` to show the location of the file editing.
2. Press `G` (capital g) to go to the bottom of the file.
3. Type `gg` to go to the top of the file.
4. Type number of the line and `G` to go to that line. For ex: `5G`

<div id="c1-lesson4-2" />
### Lesson 4.2: The search command
Type / followed by the pharse in order to search for it
1. Press `enter` to search.
2. Type `n` in order to search again forward, `N` for backward direction.
3. When wrapscan is turned on, if the search reaches the end of the file it will continue at the start.
4. `CTRL-O` to go back where you came from, `CTRL-I` goes forward.
5. Matching parentheses search by move the cursor to (, ), {, }, [, ] then type %.

<div id="c1-lesson4-3" />
### Lesson 4.3: The substitute command

1. Type `:s/old/new/g` to substitute 'new' for 'old'.
2. `s/thee/the` will only changes the first occurence.
3. Adding the `g` flag means to substitute globally in the line, change all occurrences of "thee" in the line.
4. To change every occurrence of a character string between two lines,
    - type `:#,#s/old/new/g` where #,# are the line numbers of the range of lines
      where the substitution is to be done.
    - Type `:%s/old/new/g` to change every occurrence in the whole file.
    - Type `:%s/old/new/gc` to find every occurrence in the whole file,
      with a prompt whether to substitute or not.

### Lesson 4: Summary

1.  -   `CTRL-G` displays your location in the file and the file status.
    -   `G` moves to the end of the file.
    -   number `G` moves to that line number.
    -   `gg` moves to the first line.

2.  -   Typing `/` followed by a phrase searches FORWARD for the phrase.
    -   Typing `?` followed by a phrase searches BACKWARD for the phrase.
    -   After a search type `n` to find the next occurrence in the same direction
        or `N` to search in the opposite direction.
    -   `CTRL-O` takes you back to older positions, `CTRL-I` to newer positions.

3.  Typing `%` while the cursor is on a (,),[,],{, or } goes to its match.

4.  -   To substitute new for the first old in a line type `:s/old/new`
    -   To substitute new for all 'old's on a line type `:s/old/new/g`
    -   To substitute phrases between two line #'s type `:#,#s/old/new/g`
    -   To substitute all occurrences in the file type `:%s/old/new/g`
    -   To ask for confirmation each time add 'c' `:%s/old/new/gc`

### Lesson 5:

1.  :!command executes an external command.
    - Some useful examples are:
        - :!ls - shows a directory listing.
        - :!rm FILENAME - removes file FILENAME.
2.  :w FILENAME writes the current Vim file to disk with name FILENAME.
3.  v motion :w FILENAME saves the Visually selected lines in file FILENAME.
4.  :r FILENAME retrieves disk file FILENAME and puts it below the cursor position.
5.  :r !dir reads the output of the dir command and puts it below the cursor position.
