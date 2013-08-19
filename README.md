

# Unicode characters & codepoints

## JavaScript & Unicode — Introducing CESU-8

When JavaScript was conceived and standardized in 1994/95, the Unicode standard was still in its infancy.
Early design plans for a Universal Character Set had argumented that 2¹⁶ or even only 2¹⁴ codepoints should
be more than sufficient to represent all characters in current use—it was only in 1996 that the Unicode
Consortium acknowledged the need for a far bigger number of codepoints, and hence pushed the highest valid
codepoint position from `0xffff` to `0x10ffff`; there are, consequently, 1,114,112 codepoints available in
Unicode from version 2.0 onwards.

In order to remain backwards compatible to those applications which had been implemented under the premise
that each Unicode codepoint would be representable within 16 bits, a 'Surrogate Character' mechanism was
introduced alongside with the extension of the character set. To understand Surrogate Characters, imagine
the same had happened to ASCII—an 8bit character set that leaves all codepoints with the 8ᵗʰ bit set
undefined. We could go and make those 128 codepoints surrogate characters, stipulating that the 64
codepoints in the range  `0x80`...`0xbf` shall serve as 'High (or Leading) Surrogates', those in the range
`0xc0`...`0xff` as 'High (or Trailing) Surrogates', and that High and Low Surrogates shall always appear as
pairs. In essence, then, every pair `HL` then represents a number written out in a positional system with
the base 64, that is, we can project it onto codepoints beyond `0xff` (255) by saying that a surrogate pair
`HL` is a way to access codepoint `( H — 0x80 ) * 64 + ( L — 0xc0 ) + 255`—allowing to express around 4000
additional codepoints within an 8bit character set!


2³²


## UTF

## A CESU-8-aware library for the representation & transformation of







