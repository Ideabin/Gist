# Gist 

This is a fork of the original plugin by [Condemil](https://github.com/condemil/Gist). See differences to know what has been changed. 

## Installation

Go to the "Packages" directory (`Preferences` / `Browse Packages…`). Then clone this repository:

    git clone git://github.com/ideabin/Gist

Consult the [original readme](https://github.com/condemil/Gist/blob/master/README.md) for any other stuff.

## Differences from the original version

#### Markdown gists now support Jekyll style YAML frontmatter

```
---
id: {gist_id}
desc: {gist_description}
---

Contents of the gist.
```

I save all my idea files in a directory, so this allows sublime to detect the gist when the file is loaded again.

#### `Ctrl + K` `Ctrl + N` A silly new command to create a new idea (just creates a new tab with a starting template.)

## Todo

* Multiple files?
* Update Gist Description
* Update Gist
