
### Front matter

The CoffeeNode `CHR` module (short for 'character') is a library for handling characters within NodeJS in a
Unicode-compliant, Astral-Plane-aware fashion. It includes functions to split texts into characters,
iterate over characters, and convert between a number of different character representations.

### Installation

Install as

    npm install coffeenode-chr

Require as, e.g.

    CHR = require 'coffeenode-chr'

# API

## Overview

**analyze        = ( cid\_hint, options ) ->**

The many-tricks-pony of `coffeenode-chr`. It will return an
object describing multiple aspects of the codepoint in question. Examples:

```coffeescript
$ log CHR.analyze 'helo world'

{ chr:    'h',                # The first character of the text.
  csg:    'u',                # CSG 'u', i.e. a Unicode character.
  cid:    104,                # Codepoint: 104 = 0x68.
  fncr:   'u-latn-68',        # The 'friendly NCR'; see 'rsg', below.
  sfncr:  'u-68',             # The 'short friendly NCR'.
  ncr:    '&#x68;',           # HTML-comaptible Numeric Character Reference (NCR).
  xncr:   '&#x68;',           # For codepoints outside of Unicode, this will differ from the NCR.
  rsg:    'u-latn' }          # The 'range sigil', i.e. Unicode block identifier.
````

When using Numerical Character References (NCRs), it is important to choose the right 'mode' (namely, `ncr`
or `xncr`):

```coffeescript
$ log CHR.analyze '&#x24563;' # or use mode: 'plain'

{ chr:    '&',
  csg:    'u',
  cid:    38,
  fncr:   'u-latn-26',
  sfncr:  'u-26',
  ncr:    '&#x26;',
  xncr:   '&#x26;',
  rsg:    'u-latn' }

$ log CHR.analyze '&#x24563;', mode: 'ncr'

{ chr:    '𤕣',
  csg:    'u',
  cid:    148835,
  fncr:   'u-cjk-xb-24563',
  sfncr:  'u-24563',
  ncr:    '&#x24563;',
  xncr:   '&#x24563;',
  rsg:    'u-cjk-xb' }

$ log CHR.analyze '&#x24563;', mode: 'xncr'

{ chr:    '𤕣',
  csg:    'u',
  cid:    148835,
  fncr:   'u-cjk-xb-24563',
  sfncr:  'u-24563',
  ncr:    '&#x24563;',
  xncr:   '&#x24563;',
  rsg:    'u-cjk-xb' }
````

In the above examples, the NCR `&#x24563;` was successfully decoded in modes `ncr` and `xncr`, while in
`plain` mode, `&` counts as the first character of the text.

Two more examples to show how to reference characters outside of Unicode: First let's analyze an 'extended
NCR' using mode `ncr`. The result is that, since `&jzr#x24563;` violates the rules for NCRs, it is not
recognized and treated as an ordinary text (the same way browsers do it). The first character of that text
is an `&` ampersand, so all we get is a desciption of that character in mode `ncr`:

```coffeescript
$ log CHR.analyze '&jzr#xe100;', mode: 'ncr'

{ chr:    '&',
  csg:    'u',
  cid:    38,
  fncr:   'u-latn-26',
  sfncr:  'u-26',
  ncr:    '&#x26;',
  xncr:   '&#x26;',
  rsg:    'u-latn' }
````

When we switch to mode `xncr`,

```coffeescript
$ log CHR.analyze '&jzr#xe100;', mode: 'xncr'

{ chr: '&jzr#xe100;',       # the XNCR has been recognized.
  csg: 'jzr',               # The CSG identifies the Jizura Character Set (JZRCS).
  cid: 57600,               # CID is 57600 = 0xe100
  fncr: 'jzr-cc-e100',      # The FNCR tells us that the codepoint is in the 'cc' block of the JZRCS.
  sfncr: 'jzr-e100',
  ncr: '&#xe100;',          # When rendering to a web page, we must use standard NCRs.
  xncr: '&jzr#xe100;',      # In plain texts, databases and so on, we may wish to use this notation.
  rsg: 'jzr-cc' }
````

**as\_chr         = ( cid\_hint, options ) ->**

**as\_cid         = ( cid\_hint, options ) ->**

**as\_csg         = ( cid\_hint, options ) ->**

**as\_fncr        = ( cid\_hint, options ) ->**

**as\_ncr         = ( cid\_hint, options ) ->**

**as\_range\_name  = ( cid\_hint, options ) ->**

**as\_rsg         = ( cid\_hint, options ) ->**

**as\_sfncr       = ( cid\_hint, options ) ->**

**as\_xncr        = ( cid\_hint, options ) ->**

**chrs\_of = ( text, mode ) ->**

**cid\_from\_chr = ( chr, mode ) ->**

**cid\_from\_fncr = ( ) ->**

**cid\_from\_ncr = ( ) ->**

**cid\_from\_xncr = ( ) ->**

**csg\_cid\_from\_chr = ( chr, mode ) ->**

**validate\_is\_cid = ( x ) ->**

**validate\_is\_csg = ( x ) ->**


\_analyze = ( csg, cid ) ->
\_as\_fncr = ( csg, cid ) ->
\_as\_range\_name = ( csg, cid ) ->
\_as\_rsg = ( csg, cid ) ->
\_as\_sfncr = ( csg, cid ) ->
\_as\_xncr = ( csg, cid ) ->
\_chr\_csg\_cid\_from\_chr = ( chr, mode ) ->
\_csg\_cid\_from\_hint = ( cid\_hint, options ) ->
\_names\_and\_ranges\_by\_csg = unicode\_blocks\_data[ 'names-and-ranges-by-csg' ]
\_unicode\_chr\_from\_cid = ( cid ) ->

\_csg\_matcher
\_first\_chr\_matcher\_ncr
\_first\_chr\_matcher\_plain
\_first\_chr\_matcher\_xncr
\_ncr\_csg\_cid\_matcher
\_ncr\_matcher
\_ncr\_splitter
\_nonsurrogate\_matcher
\_plain\_splitter
\_surrogate\_matcher
\_xncr\_csg\_cid\_matcher
\_xncr\_matcher
\_xncr\_splitter


# Background

## Unicode characters & codepoints

### JavaScript & Unicode

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
codepoints (for a number of reasons—some good, some bad, some historically justified, some mistaken).
Further, **only 256 Unicode codepoints are representable within a 'byte'—a scant 0.256% of the ≈100,000
codepoints in use** (as of Unicode&nbsp;6). **Understanding the codepoint / character / byte schism is essential
for any programmer wanting to process text**.

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
Character (which itself—confusingly—has a codepoint, `0xffd`; in essence, all codepoints deemed illegal are
mapped to `0xfffd` at some point on their way through the output pipeline), as they are *no legal
codepoints* when occurring without a suitable partner.

> The astute reader will notice a conundrum here: we've just proven that the character `𤕣` is stored as two
> codepoints in JavaScript, rather than one. Still, we managed to get it from an UTF-8 encoded sourcefile
> through the runtime and back out onto the console correctly—shouldn't JavaScript's treatment have
> destroyed the character by splitting it up? The answer is: Yes, that should have happened, and it is
> indeed what did happen in NodeJS versions prior to 7.7 (i believe), and also in earlier versions of
> Chrome. Fortunately, there has been fixed by making it so that input and output routines perform
> 'ensurrogating' and 'desurrogating' on the character streams, with the effect that Joe the Programmer has
> one problem less now.

However, the numbers shown (`0xd851` and `0xdd63`) indicate that JavaScript *can* deal with those positions,
it just cannot print out a suitable glyph for them. Indeed, when we apply the formula for Unicode Surrogate
Pair conversion to the first two codepoints in the critical text:

    H = 0xd851
    L = 0xdd63
    codepoint = ( H - 0xD800 ) * 0x400 + ( L - 0xDC00 ) + 0x10000

we find that the result `0x24563` does point to 𤕣 (an archaic variant of the modern Chinese character 龜). So
it becomes clear that JavaScript *can* deal with 'astral texts' (rendering it in what has become known as
*mojibake* 文字化け or *krüsel-krüsel*)—provided that programmers do respect surrogates.

This leaves code wranglers with a truly confusing and sometimes frustrating situation: First, we had to
swallow that **a byte is not a character** (anyone who spent their time between 2000 and 2010 trying to
'make everything work' in Python versions that had *both* an 8bit `str` type *and* a 16bit `Unicode` type
will know what i'm talking about). Next, we have to swallow that (in Java, in JavaScript, and in some
versions of Python, depending on compilation flags) even **a single character may or may not be a single
codepoint**; instead, **characters with codepoints above `0xffff` are represented as two 'Code Units'**, one
more term to learn here.

<!--
## UTF-8 & CESU-8

UTF-8 (an abbreviation for 'Unified Character Set Transformation Format, 8-bit') was invented in 1992 to
solve the problem of transmitting and storing Unicode texts using the available octet-(byte-)based file and
wire formats of the time. It has since become the undisputed standard encoding for web pages, URLs, and
text files.

Since codepoints are represented as positive integers, and octets (bytes) can be used to represent numbers
between zero and 255, the problem that UTF-8 attempts to solve boils down to representing 'big' integers
(those greater than 255) as series of octets.

I won't go into detail here—there's a good (Wikipedia)[http://en.wikipedia.org/wiki/UTF-8] article
on how UTF-8 mangles bits. The one important thing to understand when it comes to JavaScript and UTF-8
is that


 -->

# Character Representations

It is often necessary to convert between different character representations. For example, the character `強`
may be represented as `&#x5f37;` in HTML—this can help when the source text must be edited in a
Unicode-unfriendly environment. Likewise, the Unicode Consortium identifies codepoints using the `U+`
notation, e.g. `U+5F37;`.

## Numeric Character Representation (NCR)

The Numeric(al) Character Representation (NCR) format was invented to represent 'difficult' characters in
SGML, a markup format designed in 1960s which became the ancestor of both XML and HTML. An NCR consists of
an ampersand&nbsp;`&` followed by a hash&nbsp;`#`, followed by the numerical codepoint identifier (CID,
otherwise known as simple 'a codepoint') of the character in question, and closed with a semicolon&nbsp;`;`.
The CID may be written out in decimal or hexadecimal, upper- or lowercase, and with optional leading zeros.
If written in hexadecimal, an `x` must be placed between the hash&nbsp;`#` and the CID: thus, `ਵ`, named
GURMUKHI LETTER VA, may be represented as `&#x0A35;`, `&#xA35;`, `&#x0a35;`, `&#2613;`, `&#02613;`. (The
flexibility of these rules and the plethora of possible variants is somewhat of a hallmark of earlier
computing standards; other examples for this phenomenon are email- and IP-addresses.)

## Unicode Character Representation (UCR)

The Unicode Consortium's Character Representation (UCR) format is used by the Unicode Consortium in its
publications. It consists of an uppercase&nbsp;`U`, followed by a plus sign&nbsp;`+`, followed by the CID of
the character in question. The CID is invariably written out in uppercase hexadecimal; it is padded with
zeros when shorter than four digits; otherwise, it consists of five or six digits as needed. For example,
`ਵ` is represented as `U+0A35`.

## Proprietary Formats

When having to reference and identify characters, i personally like to write out the codepoint in a fashion
that is both somewhat less 'formal' than NCRs and somewhat more readable, flexible and informative than
UCRs; i call this format FNCR for Friendly Numeric Characer Representation. It is mainly intended for use
in publications such as character references, where a notice should be made for the reader how to decode
the constituent parts of the notation.

The general format of an FNCR is as follows: first, the character set is indicated by a short string of
letters, `u` being reserved for Unicode; this part is called the Character Set siGil (CSG). Then, the
relevant subset or block of the position of the codepoint in the character set is identified by a so-called
Range SiGil (RSG). Last, the CID is written out in lowercase hexadecimal. The parts of the FNCR are joined
by hyphens `-`. Here are a few examples:

    ਵ      u-guru-a35      # guru:  (ISO code for) 'Gurmukhi'
    強     u-cjk-5f37      # cjk:   Unicode block 'CJK Unified Ideographs'
    𤕣     u-cjkxb-24563   # cjkxb: Unicode block 'CJK Ideograph Extension B'
    €      u-cur-20ac      # cur:   Unicode block 'Currency Symbols'

RSGs are important for big character sets such as Unicode, where tens of thousands of characters are
distributed over hundred of blocks—it is easy to loose orientation. Since FNCRs include a character set
sigil, codepoints from multiple character sets may be identified; for example, here we use `l9` to stand for
Latin-9, otherwise known as ISO 8859-15, and `w1252` for Windows Codepage 1252:

    €      u-cur-20ac
         = l9-a4
         = w1252-80

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX





