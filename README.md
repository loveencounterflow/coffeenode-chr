

# Unicode characters & codepoints

## JavaScript & Unicode

**When JavaScript was conceived and standardized** in 1994/95, the Unicode standard was still in its infancy.
Early design plans for a Universal Character Set had argumented that 2<sup>16</sup> or even a mere
2<sup>14</sup> codepoints should be more than sufficient to represent all characters in current use—it was
only in 1996 that the Unicode Consortium acknowledged the need for a far bigger number of codepoints, and
hence pushed the highest valid codepoint position from `0xffff` to `0x10ffff`; there are, consequently,
1,114,112 codepoints available in Unicode from version 2.0 onwards.

**In order to remain backwards compatible** to those applications which had been implemented under the
premise that each Unicode codepoint would be representable within 16 bits, a **'Surrogate Character'**
mechanism was introduced alongside with the extension of the character set. To understand Surrogate
Characters, imagine the same had happened to ASCII—an 8bit character set that leaves all codepoints using
the 8<sup>th</sup> bit undefined. We could go and make those 128 codepoints surrogate characters,
stipulating that the 64 codepoints in the range  `0x80`...`0xbf` shall serve as 'High (or Leading)
Surrogates', those in the range `0xc0`...`0xff` as 'Low (or Trailing) Surrogates', and that High and Low
Surrogates shall always appear as pairs. In essence, then, every aurrogate pair `HL` then represents a
number written out in a positional system with the base 64, that is, we can project it onto codepoints
beyond `0xff` (255) by saying that a surrogate pair `HL` is a way to access codepoint `( H — 0x80 ) * 64 + (
L — 0xc0 ) + 255`, allowing us to express around 4000 additional codepoints in the range `0x100`...`0x10fe`
from within the confines of an 8bit character set!

Of course, such a move would have **broken a lot of assumptions**, such as the Olde Saw that 'a character is
a codepoint, a codepoint is a byte', a truism in all early encoding schemes. In Unicode, a 'character' (a
unit of writing) is distinct from a 'glyph' (the graphical appearance of a character), and while each
'glyph' is mapped to a 'codepoint', many virtually indistinguishable glyphs may be mapped to disparate
codepoints (for a number of reasons—some good, some bad, some historically justified, some mistakenly).
Further, only 256 Unicode codepoints are representable within a 'byte'—a scant 0.256% of the ≈100,000
codepoints in use as of Unicode 6. Understanding the codepoint / character / byte schism is essential for
any programmer wanting to process text.

Now JavaScript *was* fairly advanced for its time in that its text data type—the `String`—was defined in
terms of Unicode characters at a time when the programming community at large was still happily hacking
bytes, and web designers spit out HTML pages using ISO&nbsp;8859-1 (by comparison, Python, which was
conceived in 1991, got a Unicode data type only in 2000, and abolished its 8bit string type in 2008—until
then, most programmers operated on bytes rather than codepoints when manipulating text in that language).

2<sup>32</sup>


## UTF-8 & CESU-8

## A CESU-8-aware library for the representation & transformation of







