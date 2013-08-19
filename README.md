

# Unicode characters & codepoints

## JavaScript & Unicode

**When JavaScript was conceived and standardized** in 1994/95, the Unicode standard was still in its infancy.
Early design plans for a Universal Character Set had argumented that 2<sup>16</sup> or even a mere
2<sup>14</sup> codepoints should be more than sufficient to represent all characters in current use—it was
only in 1996 that the Unicode Consortium acknowledged the need for a far bigger number of codepoints, and
hence pushed the highest valid codepoint position from `0xffff` to `0x10ffff`; there are, consequently,
1,114,112 codepoints available in Unicode from version 2.0 onwards. In the vernacular, Unicode codepoints
beyond `0xffff` (the frontier of the Basic Multilingual Plane, BMP) are known as '32bit characters', and
the wilderness out there as 'The Astral Planes'.

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
codepoints in use (as of Unicode&nbsp;6). Understanding the codepoint / character / byte schism is essential
for any programmer wanting to process text.

Now JavaScript *was* fairly advanced for its time in that its text data type—the `String`—was defined in
terms of Unicode characters at a time when the programming community at large was still happily hacking
bytes, and web designers spit out HTML pages using ISO&nbsp;8859-1 (by comparison, Python, which was
conceived in 1991, got a Unicode data type only in 2000, and abolished its 8bit string type in 2008—until
then, most programmers operated on bytes rather than codepoints when manipulating text in that language).

Since JavaScript's `String` data type is character-oriented and Array-like, it is very convenient to, say,
iterate over characters in a text. It is as simple as fetching the length of the string and iterate over
its indexes:

    var chr_count = text.length;
    for ( var idx = 0; idx < chr_count; idx += 1 ) {
      log( text[ idx ] ); }

Where JavaScript is something of **a bit of a failure** is its treatment of those elusive 32bit / astral
codepoints. Sadly, for all its simplicity and correctness in 95% of all practically occurring situations
in day-to-day programming situations, the above code snippets is **not correct**, as it fails to account
for the fact that **in JavaScript, 32bit characters occupy two `String` positions**. We can easily test this:

    var show_codepoints = function( text ) {
        var chr;
        var chr_count = text.length;
        for ( var idx = 0; idx < chr_count; idx += 1 ) {
          chr = text[ idx ];
          log( chr, idx, '0x' + chr.charCodeAt( 0 ).toString( 16 ) ); } };

    var text = '自強不息';
    show_codepoints( text );

gives

    自 0 0x81ea
    強 1 0x5f37
    不 2 0x4e0d
    息 3 0x606f

which is correct, since all codepoints are below `0xffff`. However, should or text inadvertently include
astral entities, the algorithm breaks down in nasty ways:

    var text = '𤕣古文龜';
    show_codepoints( text );

gives

    � 0 0xd851
    � 1 0xdd63
    古 2 0x53e4
    文 3 0x6587
    龜 4 0x9f9c

Like in an X-ray, we see that the string now holds *five* codepoints, in spite of there being only *four*
characters, as in the previous one. The first two codepoints are rendered with the Unicode Replacement
Character (which itself, confusingly, has a codepoint, `0xffd`), as they constitute, each by itself, *no
legal codepoints*, as they must always appear side-by-side. The numbers shown—`0xd851` and `0xdd63`—indicate
that JavaScript *can* deal with those positions, it just cannot print out a suitable glyph for them. In essence,
all codepoints deemed illegal are mapped to `0xfffd` on their way through the output pipeline.

Indeed, when we apply the formula for
Unicode Surrogate Pair conversion to the first two codepoints in the critical text:

    H = 0xd851
    L = 0xdd63
    codepoint = ( H - 0xD800 ) * 0x400 + ( L - 0xDC00 ) + 0x10000

we find that the result `0x24563` does point to 𤕣 (an archaic variant of the modern Chinese character 龜). So
it becomes clear that JavaScript *can* deal with 'astral texts' (rendering it in what has become known as
*mojibake* 文字化け or *krüsel-krüsel*)—provided that programmers do respect surrogates.




## UTF-8 & CESU-8

## A CESU-8-aware library for the representation & transformation of







