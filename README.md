# WavGrep

WavGrep searches a folder of your choice for audio files that are similar to an audio file you choose. It works using statistical cross-correlation.

If you have a small audio file (perhaps ripped from a game or a movie, perhaps not the entire source track), you know what composers might have worked on it, you don't know the track title, and you have those composers' discography available, WavGrep can help you search for the matching track.

In addition to finding exact matches, WavGrep can sometimes surface related-but-not-identical tracks. For example, it can sometimes find an acoustic mix of a rock track.

## Installation

First, you'll need to install [CrossLooper](https://github.com/Splendide-Imaginarius/crosslooper) according to its installation instructions.

Once you've done that, to install WavGrep via pip, do this from the `wavgrep` repo directory:

```
pip install --user .
```

## Usage

The following command will search `./library/` for the top 15 most similar tracks to `./sample.ogg`, with start position 5s and length 10s:

```
wavgrep --start 5 --len 10 --count 15 --in-dir ./library ./sample.ogg
```

If you leave off any of the options, the defaults are start position 15s, length 15s, count 10 (use count 0 to show all matches), and the current working directory.

## Related Projects

* [CrossLooper](https://github.com/Splendide-Imaginarius/crosslooper)

## Credits

Copyright 2023 Splendide Imaginarius.

This is not a license requirement, but if you use WavGrep for a project, it would be greatly appreciated if you credit me. Example credits: "Audio was identified with WavGrep by Splendide Imaginarius." Linking back to this Git repository would also be greatly appreciated.

WavGrep is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

WavGrep is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with WavGrep. If not, see [https://www.gnu.org/licenses/](https://www.gnu.org/licenses/).

This project is not derived from any of the various files on GitHub Gist named "wavgrep.py". I didn't notice that those Gists existed until after I had created this project. Those Gists appear to be abandoned and only support Python 2, so I don't think confusion is likely.
