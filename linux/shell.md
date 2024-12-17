<div id="toc" />
## Table of content
1. [Chapter 1](#chapter-1)

<div id="chapter-1" />
## Chapter 1 ([toc](#toc))

### Lesson 1: basic operation

1. Moving cursor with `up`, `down`, `left`, `right`
2. Starting vim with `vim file-name.ext`
3. Exiting vim with:
    - `ESC` :`q!` to discard all changes
    - `ESC` :`wq` to save all changes
4. Deleting any character with `ESC` `x`

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

### Lesson 3: the change operator

1. Putting the previous deleted text to the cursor with `p`.
2. Replacing the character at the cursor with x with `rx` (x is the typed character).
3. Changing the word (removing then inserting) to the end of the word with `ce`
4. Changing the word to the end of the line with `cc`, `c$`
5. Changing can also work with the format `operator [number] motion`