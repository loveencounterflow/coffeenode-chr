#
# -*- coding: utf-8 -*-


############################################################################################################
from _xxrange import xxrange as                                         _xxrange
from _xxrange import urange as                                          _urange




############################################################################################################
class UMX_data_000:

  #---------------------------------------------------------------------------------------------------------
  chr_by_namedcref = {
    '&quot;':          '\u0022',  # quotation mark (= APL quote)
    '&amp;':           '\u0026',  # ampersand
    '&apos;':          '\u0027',  # apostrophe (= apostrophe-quote); see below
    '&lt;':            '\u003c',  # less-than sign
    '&gt;':            '\u003e',  # greater-than sign
    '&nbsp;':          '\u00a0',  # no-break space (= non-breaking space)
    '&iexcl;':         '\u00a1',  # inverted exclamation mark
    '&cent;':          '\u00a2',  # cent sign
    '&pound;':         '\u00a3',  # pound sign
    '&curren;':        '\u00a4',  # currency sign
    '&yen;':           '\u00a5',  # yen sign (= yuan sign)
    '&brvbar;':        '\u00a6',  # broken bar (= broken vertical bar)
    '&sect;':          '\u00a7',  # section sign
    '&uml;':           '\u00a8',  # diaeresis (= spacing diaeresis); see German umlaut
    '&copy;':          '\u00a9',  # copyright sign
    '&ordf;':          '\u00aa',  # feminine ordinal indicator
    '&laquo;':         '\u00ab',  # left-pointing double angle quotation mark (= left pointing guillemet)
    '&not;':           '\u00ac',  # not sign
    '&shy;':           '\u00ad',  # soft hyphen (= discretionary hyphen)
    '&reg;':           '\u00ae',  # registered sign ( = registered trade mark sign)
    '&macr;':          '\u00af',  # macron (= spacing macron = overline = APL overbar)
    '&deg;':           '\u00b0',  # degree sign
    '&plusmn;':        '\u00b1',  # plus-minus sign (= plus-or-minus sign)
    '&sup2;':          '\u00b2',  # superscript two (= superscript digit two = squared)
    '&sup3;':          '\u00b3',  # superscript three (= superscript digit three = cubed)
    '&acute;':         '\u00b4',  # acute accent (= spacing acute)
    '&micro;':         '\u00b5',  # micro sign
    '&para;':          '\u00b6',  # pilcrow sign ( = paragraph sign)
    '&middot;':        '\u00b7',  # middle dot (= Georgian comma = Greek middle dot)
    '&cedil;':         '\u00b8',  # cedilla (= spacing cedilla)
    '&sup1;':          '\u00b9',  # superscript one (= superscript digit one)
    '&ordm;':          '\u00ba',  # masculine ordinal indicator
    '&raquo;':         '\u00bb',  # right-pointing double angle quotation mark (= right pointing guillemet)
    '&frac14;':        '\u00bc',  # vulgar fraction one quarter (= fraction one quarter)
    '&frac12;':        '\u00bd',  # vulgar fraction one half (= fraction one half)
    '&frac34;':        '\u00be',  # vulgar fraction three quarters (= fraction three quarters)
    '&iquest;':        '\u00bf',  # inverted question mark (= turned question mark)
    '&Agrave;':        '\u00c0',  # Latin capital letter A with grave (= Latin capital letter A grave)
    '&Aacute;':        '\u00c1',  # Latin capital letter A with acute
    '&Acirc;':         '\u00c2',  # Latin capital letter A with circumflex
    '&Atilde;':        '\u00c3',  # Latin capital letter A with tilde
    '&Auml;':          '\u00c4',  # Latin capital letter A with diaeresis
    '&Aring;':         '\u00c5',  # Latin capital letter A with ring above (= Latin capital letter A ring)
    '&AElig;':         '\u00c6',  # Latin capital letter AE (= Latin capital ligature AE)
    '&Ccedil;':        '\u00c7',  # Latin capital letter C with cedilla
    '&Egrave;':        '\u00c8',  # Latin capital letter E with grave
    '&Eacute;':        '\u00c9',  # Latin capital letter E with acute
    '&Ecirc;':         '\u00ca',  # Latin capital letter E with circumflex
    '&Euml;':          '\u00cb',  # Latin capital letter E with diaeresis
    '&Igrave;':        '\u00cc',  # Latin capital letter I with grave
    '&Iacute;':        '\u00cd',  # Latin capital letter I with acute
    '&Icirc;':         '\u00ce',  # Latin capital letter I with circumflex
    '&Iuml;':          '\u00cf',  # Latin capital letter I with diaeresis
    '&ETH;':           '\u00d0',  # Latin capital letter ETH
    '&Ntilde;':        '\u00d1',  # Latin capital letter N with tilde
    '&Ograve;':        '\u00d2',  # Latin capital letter O with grave
    '&Oacute;':        '\u00d3',  # Latin capital letter O with acute
    '&Ocirc;':         '\u00d4',  # Latin capital letter O with circumflex
    '&Otilde;':        '\u00d5',  # Latin capital letter O with tilde
    '&Ouml;':          '\u00d6',  # Latin capital letter O with diaeresis
    '&times;':         '\u00d7',  # multiplication sign
    '&Oslash;':        '\u00d8',  # Latin capital letter O with stroke (= Latin capital letter O slash)
    '&Ugrave;':        '\u00d9',  # Latin capital letter U with grave
    '&Uacute;':        '\u00da',  # Latin capital letter U with acute
    '&Ucirc;':         '\u00db',  # Latin capital letter U with circumflex
    '&Uuml;':          '\u00dc',  # Latin capital letter U with diaeresis
    '&Yacute;':        '\u00dd',  # Latin capital letter Y with acute
    '&THORN;':         '\u00de',  # Latin capital letter THORN
    '&szlig;':         '\u00df',  # Latin small letter sharp s (= ess-zed); see German Eszett
    '&agrave;':        '\u00e0',  # Latin small letter a with grave
    '&aacute;':        '\u00e1',  # Latin small letter a with acute
    '&acirc;':         '\u00e2',  # Latin small letter a with circumflex
    '&atilde;':        '\u00e3',  # Latin small letter a with tilde
    '&auml;':          '\u00e4',  # Latin small letter a with diaeresis
    '&aring;':         '\u00e5',  # Latin small letter a with ring above
    '&aelig;':         '\u00e6',  # Latin small letter ae (= Latin small ligature ae)
    '&ccedil;':        '\u00e7',  # Latin small letter c with cedilla
    '&egrave;':        '\u00e8',  # Latin small letter e with grave
    '&eacute;':        '\u00e9',  # Latin small letter e with acute
    '&ecirc;':         '\u00ea',  # Latin small letter e with circumflex
    '&euml;':          '\u00eb',  # Latin small letter e with diaeresis
    '&igrave;':        '\u00ec',  # Latin small letter i with grave
    '&iacute;':        '\u00ed',  # Latin small letter i with acute
    '&icirc;':         '\u00ee',  # Latin small letter i with circumflex
    '&iuml;':          '\u00ef',  # Latin small letter i with diaeresis
    '&eth;':           '\u00f0',  # Latin small letter eth
    '&ntilde;':        '\u00f1',  # Latin small letter n with tilde
    '&ograve;':        '\u00f2',  # Latin small letter o with grave
    '&oacute;':        '\u00f3',  # Latin small letter o with acute
    '&ocirc;':         '\u00f4',  # Latin small letter o with circumflex
    '&otilde;':        '\u00f5',  # Latin small letter o with tilde
    '&ouml;':          '\u00f6',  # Latin small letter o with diaeresis
    '&divide;':        '\u00f7',  # division sign
    '&oslash;':        '\u00f8',  # Latin small letter o with stroke (= Latin small letter o slash)
    '&ugrave;':        '\u00f9',  # Latin small letter u with grave
    '&uacute;':        '\u00fa',  # Latin small letter u with acute
    '&ucirc;':         '\u00fb',  # Latin small letter u with circumflex
    '&uuml;':          '\u00fc',  # Latin small letter u with diaeresis
    '&yacute;':        '\u00fd',  # Latin small letter y with acute
    '&thorn;':         '\u00fe',  # Latin small letter thorn
    '&yuml;':          '\u00ff',  # Latin small letter y with diaeresis
    '&OElig;':         '\u0152',  # Latin capital ligature oe
    '&oelig;':         '\u0153',  # Latin small ligature oe
    '&Scaron;':        '\u0160',  # Latin capital letter s with caron
    '&scaron;':        '\u0161',  # Latin small letter s with caron
    '&Yuml;':          '\u0178',  # Latin capital letter y with diaeresis
    '&fnof;':          '\u0192',  # Latin small letter f with hook (= function = florin)
    '&circ;':          '\u02c6',  # modifier letter circumflex accent
    '&tilde;':         '\u02dc',  # small tilde
    '&Alpha;':         '\u0391',  # Greek capital letter Alpha
    '&Beta;':          '\u0392',  # Greek capital letter Beta
    '&Gamma;':         '\u0393',  # Greek capital letter Gamma
    '&Delta;':         '\u0394',  # Greek capital letter Delta
    '&Epsilon;':       '\u0395',  # Greek capital letter Epsilon
    '&Zeta;':          '\u0396',  # Greek capital letter Zeta
    '&Eta;':           '\u0397',  # Greek capital letter Eta
    '&Theta;':         '\u0398',  # Greek capital letter Theta
    '&Iota;':          '\u0399',  # Greek capital letter Iota
    '&Kappa;':         '\u039a',  # Greek capital letter Kappa
    '&Lambda;':        '\u039b',  # Greek capital letter Lambda
    '&Mu;':            '\u039c',  # Greek capital letter Mu
    '&Nu;':            '\u039d',  # Greek capital letter Nu
    '&Xi;':            '\u039e',  # Greek capital letter Xi
    '&Omicron;':       '\u039f',  # Greek capital letter Omicron
    '&Pi;':            '\u03a0',  # Greek capital letter Pi
    '&Rho;':           '\u03a1',  # Greek capital letter Rho
    '&Sigma;':         '\u03a3',  # Greek capital letter Sigma
    '&Tau;':           '\u03a4',  # Greek capital letter Tau
    '&Upsilon;':       '\u03a5',  # Greek capital letter Upsilon
    '&Phi;':           '\u03a6',  # Greek capital letter Phi
    '&Chi;':           '\u03a7',  # Greek capital letter Chi
    '&Psi;':           '\u03a8',  # Greek capital letter Psi
    '&Omega;':         '\u03a9',  # Greek capital letter Omega
    '&alpha;':         '\u03b1',  # Greek small letter alpha
    '&beta;':          '\u03b2',  # Greek small letter beta
    '&gamma;':         '\u03b3',  # Greek small letter gamma
    '&delta;':         '\u03b4',  # Greek small letter delta
    '&epsilon;':       '\u03b5',  # Greek small letter epsilon
    '&zeta;':          '\u03b6',  # Greek small letter zeta
    '&eta;':           '\u03b7',  # Greek small letter eta
    '&theta;':         '\u03b8',  # Greek small letter theta
    '&iota;':          '\u03b9',  # Greek small letter iota
    '&kappa;':         '\u03ba',  # Greek small letter kappa
    '&lambda;':        '\u03bb',  # Greek small letter lambda
    '&mu;':            '\u03bc',  # Greek small letter mu
    '&nu;':            '\u03bd',  # Greek small letter nu
    '&xi;':            '\u03be',  # Greek small letter xi
    '&omicron;':       '\u03bf',  # Greek small letter omicron
    '&pi;':            '\u03c0',  # Greek small letter pi
    '&rho;':           '\u03c1',  # Greek small letter rho
    '&sigmaf;':        '\u03c2',  # Greek small letter final sigma
    '&sigma;':         '\u03c3',  # Greek small letter sigma
    '&tau;':           '\u03c4',  # Greek small letter tau
    '&upsilon;':       '\u03c5',  # Greek small letter upsilon
    '&phi;':           '\u03c6',  # Greek small letter phi
    '&chi;':           '\u03c7',  # Greek small letter chi
    '&psi;':           '\u03c8',  # Greek small letter psi
    '&omega;':         '\u03c9',  # Greek small letter omega
    '&thetasym;':      '\u03d1',  # Greek theta symbol
    '&upsih;':         '\u03d2',  # Greek Upsilon with hook symbol
    '&piv;':           '\u03d6',  # Greek pi symbol
    '&ensp;':          '\u2002',  # en space
    '&emsp;':          '\u2003',  # em space
    '&thinsp;':        '\u2009',  # thin space
    '&zwnj;':          '\u200c',  # zero-width non-joiner
    '&zwj;':           '\u200d',  # zero-width joiner
    '&lrm;':           '\u200e',  # left-to-right mark
    '&rlm;':           '\u200f',  # right-to-left mark
    '&ndash;':         '\u2013',  # en dash
    '&mdash;':         '\u2014',  # em dash
    '&lsquo;':         '\u2018',  # left single quotation mark
    '&rsquo;':         '\u2019',  # right single quotation mark
    '&sbquo;':         '\u201a',  # single low-9 quotation mark
    '&ldquo;':         '\u201c',  # left double quotation mark
    '&rdquo;':         '\u201d',  # right double quotation mark
    '&bdquo;':         '\u201e',  # double low-9 quotation mark
    '&dagger;':        '\u2020',  # dagger
    '&Dagger;':        '\u2021',  # double dagger
    '&bull;':          '\u2022',  # bullet (= black small circle)
    '&hellip;':        '\u2026',  # horizontal ellipsis (= three dot leader)
    '&permil;':        '\u2030',  # per mille sign
    '&prime;':         '\u2032',  # prime (= minutes = feet)
    '&Prime;':         '\u2033',  # double prime (= seconds = inches)
    '&lsaquo;':        '\u2039',  # single left-pointing angle quotation mark
    '&rsaquo;':        '\u203a',  # single right-pointing angle quotation mark
    '&oline;':         '\u203e',  # overline (= spacing overscore)
    '&frasl;':         '\u2044',  # fraction slash (= solidus)
    '&euro;':          '\u20ac',  # euro sign
    '&image;':         '\u2111',  # black-letter capital I (= imaginary part)
    '&weierp;':        '\u2118',  # script capital P (= power set = Weierstrass p)
    '&real;':          '\u211c',  # black-letter capital R (= real part symbol)
    '&trade;':         '\u2122',  # trademark sign
    '&alefsym;':       '\u2135',  # alef symbol (= first transfinite cardinal)
    '&larr;':          '\u2190',  # leftwards arrow
    '&uarr;':          '\u2191',  # upwards arrow
    '&rarr;':          '\u2192',  # rightwards arrow
    '&darr;':          '\u2193',  # downwards arrow
    '&harr;':          '\u2194',  # left right arrow
    '&crarr;':         '\u21b5',  # downwards arrow with corner leftwards (= carriage return)
    '&lArr;':          '\u21d0',  # leftwards double arrow
    '&uArr;':          '\u21d1',  # upwards double arrow
    '&rArr;':          '\u21d2',  # rightwards double arrow
    '&dArr;':          '\u21d3',  # downwards double arrow
    '&hArr;':          '\u21d4',  # left right double arrow
    '&forall;':        '\u2200',  # for all
    '&part;':          '\u2202',  # partial differential
    '&exist;':         '\u2203',  # there exists
    '&empty;':         '\u2205',  # empty set (= null set = diameter)
    '&nabla;':         '\u2207',  # nabla (= backward difference)
    '&isin;':          '\u2208',  # element of
    '&notin;':         '\u2209',  # not an element of
    '&ni;':            '\u220b',  # contains as member
    '&prod;':          '\u220f',  # n-ary product (= product sign)
    '&sum;':           '\u2211',  # n-ary summation
    '&minus;':         '\u2212',  # minus sign
    '&lowast;':        '\u2217',  # asterisk operator
    '&radic;':         '\u221a',  # square root (= radical sign)
    '&prop;':          '\u221d',  # proportional to
    '&infin;':         '\u221e',  # infinity
    '&ang;':           '\u2220',  # angle
    '&and;':           '\u2227',  # logical and (= wedge)
    '&or;':            '\u2228',  # logical or (= vee)
    '&cap;':           '\u2229',  # intersection (= cap)
    '&cup;':           '\u222a',  # union (= cup)
    '&int;':           '\u222b',  # integral
    '&there4;':        '\u2234',  # therefore
    '&sim;':           '\u223c',  # tilde operator (= varies with = similar to)
    '&cong;':          '\u2245',  # congruent to
    '&asymp;':         '\u2248',  # almost equal to (= asymptotic to)
    '&ne;':            '\u2260',  # not equal to
    '&equiv;':         '\u2261',  # identical to; sometimes used for 'equivalent to'
    '&le;':            '\u2264',  # less-than or equal to
    '&ge;':            '\u2265',  # greater-than or equal to
    '&sub;':           '\u2282',  # subset of
    '&sup;':           '\u2283',  # superset of
    '&nsub;':          '\u2284',  # not a subset of
    '&sube;':          '\u2286',  # subset of or equal to
    '&supe;':          '\u2287',  # superset of or equal to
    '&oplus;':         '\u2295',  # circled plus (= direct sum)
    '&otimes;':        '\u2297',  # circled times (= vector product)
    '&perp;':          '\u22a5',  # up tack (= orthogonal to = perpendicular)
    '&sdot;':          '\u22c5',  # dot operator
    '&lceil;':         '\u2308',  # left ceiling (= APL upstile)
    '&rceil;':         '\u2309',  # right ceiling
    '&lfloor;':        '\u230a',  # left floor (= APL downstile)
    '&rfloor;':        '\u230b',  # right floor
    '&lang;':          '\u2329',  # left-pointing angle bracket (= bra)
    '&rang;':          '\u232a',  # right-pointing angle bracket (= ket)
    '&loz;':           '\u25ca',  # lozenge
    '&spades;':        '\u2660',  # black spade suit
    '&clubs;':         '\u2663',  # black club suit (= shamrock)
    '&hearts;':        '\u2665',  # black heart suit (= valentine)
    '&diams;':         '\u2666',  # black diamond suit
    }

  #---------------------------------------------------------------------------------------------------------
  namedcref_by_chr = dict(
    ( value, name, ) for name, value in chr_by_namedcref.items() )


  #---------------------------------------------------------------------------------------------------------
  # UPDATE: this list has been manually updated to accommodate changes for CJK characters in Unicode 6.0,
  # but not for other scripts; a revised and improved version is pending.

  # This list has been generated with JIZURA/_extra/#populate-jizura-db.py/defined_unicode_cscid_ranges
  # from the Unicode 5.1.0 `http://www.unicode.org/Public/UNIDATA/UnicodeData.txt`. It contains all
  # the start and endpoints of contiguous subranges within the Unicode CID range, `0x0...0x10fffe`. This
  # list is used by `~.is_defined_unicode_cid()`.
  #
  # ###OBS### this list could probably more efficiently computed using this snippet from
  # http://docs.python.org/library/itertools.html#examples ::
  #
  #     >>> # Find runs of consecutive numbers using groupby.  The key to the solution
  #     >>> # is differencing with a range so that consecutive numbers all appear in
  #     >>> # same group.
  #     >>> data = [ 1,  4,5,6, 10, 15,16,17,18, 22, 25,26,27,28]
  #     >>> for k, g in groupby(enumerate(data), lambda (i,x):i-x):
  #     ...     print map(itemgetter(1), g)
  #     ...
  #     [1]
  #     [4, 5, 6]
  #     [10]
  #     [15, 16, 17, 18]
  #     [22]
  #     [25, 26, 27, 28]
  #
  # and combining it with pickling.
  #
  ranges_of_defined_unicode_cids = ( ###OBS### these should be rewritten using the more efficient and versatile urange object
    range( 0x00000000, 0x00000378 ), range( 0x0000037a, 0x0000037f ), range( 0x00000384, 0x0000038b ),
    range( 0x0000038c, 0x0000038d ), range( 0x0000038e, 0x000003a2 ), range( 0x000003a3, 0x00000524 ),
    range( 0x00000531, 0x00000557 ), range( 0x00000559, 0x00000560 ), range( 0x00000561, 0x00000588 ),
    range( 0x00000589, 0x0000058b ), range( 0x00000591, 0x000005c8 ), range( 0x000005d0, 0x000005eb ),
    range( 0x000005f0, 0x000005f5 ), range( 0x00000600, 0x00000604 ), range( 0x00000606, 0x0000061c ),
    range( 0x0000061e, 0x00000620 ), range( 0x00000621, 0x0000065f ), range( 0x00000660, 0x0000070e ),
    range( 0x0000070f, 0x0000074b ), range( 0x0000074d, 0x000007b2 ), range( 0x000007c0, 0x000007fb ),
    range( 0x00000901, 0x0000093a ), range( 0x0000093c, 0x0000094e ), range( 0x00000950, 0x00000955 ),
    range( 0x00000958, 0x00000973 ), range( 0x0000097b, 0x00000980 ), range( 0x00000981, 0x00000984 ),
    range( 0x00000985, 0x0000098d ), range( 0x0000098f, 0x00000991 ), range( 0x00000993, 0x000009a9 ),
    range( 0x000009aa, 0x000009b1 ), range( 0x000009b2, 0x000009b3 ), range( 0x000009b6, 0x000009ba ),
    range( 0x000009bc, 0x000009c5 ), range( 0x000009c7, 0x000009c9 ), range( 0x000009cb, 0x000009cf ),
    range( 0x000009d7, 0x000009d8 ), range( 0x000009dc, 0x000009de ), range( 0x000009df, 0x000009e4 ),
    range( 0x000009e6, 0x000009fb ), range( 0x00000a01, 0x00000a04 ), range( 0x00000a05, 0x00000a0b ),
    range( 0x00000a0f, 0x00000a11 ), range( 0x00000a13, 0x00000a29 ), range( 0x00000a2a, 0x00000a31 ),
    range( 0x00000a32, 0x00000a34 ), range( 0x00000a35, 0x00000a37 ), range( 0x00000a38, 0x00000a3a ),
    range( 0x00000a3c, 0x00000a3d ), range( 0x00000a3e, 0x00000a43 ), range( 0x00000a47, 0x00000a49 ),
    range( 0x00000a4b, 0x00000a4e ), range( 0x00000a51, 0x00000a52 ), range( 0x00000a59, 0x00000a5d ),
    range( 0x00000a5e, 0x00000a5f ), range( 0x00000a66, 0x00000a76 ), range( 0x00000a81, 0x00000a84 ),
    range( 0x00000a85, 0x00000a8e ), range( 0x00000a8f, 0x00000a92 ), range( 0x00000a93, 0x00000aa9 ),
    range( 0x00000aaa, 0x00000ab1 ), range( 0x00000ab2, 0x00000ab4 ), range( 0x00000ab5, 0x00000aba ),
    range( 0x00000abc, 0x00000ac6 ), range( 0x00000ac7, 0x00000aca ), range( 0x00000acb, 0x00000ace ),
    range( 0x00000ad0, 0x00000ad1 ), range( 0x00000ae0, 0x00000ae4 ), range( 0x00000ae6, 0x00000af0 ),
    range( 0x00000af1, 0x00000af2 ), range( 0x00000b01, 0x00000b04 ), range( 0x00000b05, 0x00000b0d ),
    range( 0x00000b0f, 0x00000b11 ), range( 0x00000b13, 0x00000b29 ), range( 0x00000b2a, 0x00000b31 ),
    range( 0x00000b32, 0x00000b34 ), range( 0x00000b35, 0x00000b3a ), range( 0x00000b3c, 0x00000b45 ),
    range( 0x00000b47, 0x00000b49 ), range( 0x00000b4b, 0x00000b4e ), range( 0x00000b56, 0x00000b58 ),
    range( 0x00000b5c, 0x00000b5e ), range( 0x00000b5f, 0x00000b64 ), range( 0x00000b66, 0x00000b72 ),
    range( 0x00000b82, 0x00000b84 ), range( 0x00000b85, 0x00000b8b ), range( 0x00000b8e, 0x00000b91 ),
    range( 0x00000b92, 0x00000b96 ), range( 0x00000b99, 0x00000b9b ), range( 0x00000b9c, 0x00000b9d ),
    range( 0x00000b9e, 0x00000ba0 ), range( 0x00000ba3, 0x00000ba5 ), range( 0x00000ba8, 0x00000bab ),
    range( 0x00000bae, 0x00000bba ), range( 0x00000bbe, 0x00000bc3 ), range( 0x00000bc6, 0x00000bc9 ),
    range( 0x00000bca, 0x00000bce ), range( 0x00000bd0, 0x00000bd1 ), range( 0x00000bd7, 0x00000bd8 ),
    range( 0x00000be6, 0x00000bfb ), range( 0x00000c01, 0x00000c04 ), range( 0x00000c05, 0x00000c0d ),
    range( 0x00000c0e, 0x00000c11 ), range( 0x00000c12, 0x00000c29 ), range( 0x00000c2a, 0x00000c34 ),
    range( 0x00000c35, 0x00000c3a ), range( 0x00000c3d, 0x00000c45 ), range( 0x00000c46, 0x00000c49 ),
    range( 0x00000c4a, 0x00000c4e ), range( 0x00000c55, 0x00000c57 ), range( 0x00000c58, 0x00000c5a ),
    range( 0x00000c60, 0x00000c64 ), range( 0x00000c66, 0x00000c70 ), range( 0x00000c78, 0x00000c80 ),
    range( 0x00000c82, 0x00000c84 ), range( 0x00000c85, 0x00000c8d ), range( 0x00000c8e, 0x00000c91 ),
    range( 0x00000c92, 0x00000ca9 ), range( 0x00000caa, 0x00000cb4 ), range( 0x00000cb5, 0x00000cba ),
    range( 0x00000cbc, 0x00000cc5 ), range( 0x00000cc6, 0x00000cc9 ), range( 0x00000cca, 0x00000cce ),
    range( 0x00000cd5, 0x00000cd7 ), range( 0x00000cde, 0x00000cdf ), range( 0x00000ce0, 0x00000ce4 ),
    range( 0x00000ce6, 0x00000cf0 ), range( 0x00000cf1, 0x00000cf3 ), range( 0x00000d02, 0x00000d04 ),
    range( 0x00000d05, 0x00000d0d ), range( 0x00000d0e, 0x00000d11 ), range( 0x00000d12, 0x00000d29 ),
    range( 0x00000d2a, 0x00000d3a ), range( 0x00000d3d, 0x00000d45 ), range( 0x00000d46, 0x00000d49 ),
    range( 0x00000d4a, 0x00000d4e ), range( 0x00000d57, 0x00000d58 ), range( 0x00000d60, 0x00000d64 ),
    range( 0x00000d66, 0x00000d76 ), range( 0x00000d79, 0x00000d80 ), range( 0x00000d82, 0x00000d84 ),
    range( 0x00000d85, 0x00000d97 ), range( 0x00000d9a, 0x00000db2 ), range( 0x00000db3, 0x00000dbc ),
    range( 0x00000dbd, 0x00000dbe ), range( 0x00000dc0, 0x00000dc7 ), range( 0x00000dca, 0x00000dcb ),
    range( 0x00000dcf, 0x00000dd5 ), range( 0x00000dd6, 0x00000dd7 ), range( 0x00000dd8, 0x00000de0 ),
    range( 0x00000df2, 0x00000df5 ), range( 0x00000e01, 0x00000e3b ), range( 0x00000e3f, 0x00000e5c ),
    range( 0x00000e81, 0x00000e83 ), range( 0x00000e84, 0x00000e85 ), range( 0x00000e87, 0x00000e89 ),
    range( 0x00000e8a, 0x00000e8b ), range( 0x00000e8d, 0x00000e8e ), range( 0x00000e94, 0x00000e98 ),
    range( 0x00000e99, 0x00000ea0 ), range( 0x00000ea1, 0x00000ea4 ), range( 0x00000ea5, 0x00000ea6 ),
    range( 0x00000ea7, 0x00000ea8 ), range( 0x00000eaa, 0x00000eac ), range( 0x00000ead, 0x00000eba ),
    range( 0x00000ebb, 0x00000ebe ), range( 0x00000ec0, 0x00000ec5 ), range( 0x00000ec6, 0x00000ec7 ),
    range( 0x00000ec8, 0x00000ece ), range( 0x00000ed0, 0x00000eda ), range( 0x00000edc, 0x00000ede ),
    range( 0x00000f00, 0x00000f48 ), range( 0x00000f49, 0x00000f6d ), range( 0x00000f71, 0x00000f8c ),
    range( 0x00000f90, 0x00000f98 ), range( 0x00000f99, 0x00000fbd ), range( 0x00000fbe, 0x00000fcd ),
    range( 0x00000fce, 0x00000fd5 ), range( 0x00001000, 0x0000109a ), range( 0x0000109e, 0x000010c6 ),
    range( 0x000010d0, 0x000010fd ), range( 0x00001100, 0x0000115a ), range( 0x0000115f, 0x000011a3 ),
    range( 0x000011a8, 0x000011fa ), range( 0x00001200, 0x00001249 ), range( 0x0000124a, 0x0000124e ),
    range( 0x00001250, 0x00001257 ), range( 0x00001258, 0x00001259 ), range( 0x0000125a, 0x0000125e ),
    range( 0x00001260, 0x00001289 ), range( 0x0000128a, 0x0000128e ), range( 0x00001290, 0x000012b1 ),
    range( 0x000012b2, 0x000012b6 ), range( 0x000012b8, 0x000012bf ), range( 0x000012c0, 0x000012c1 ),
    range( 0x000012c2, 0x000012c6 ), range( 0x000012c8, 0x000012d7 ), range( 0x000012d8, 0x00001311 ),
    range( 0x00001312, 0x00001316 ), range( 0x00001318, 0x0000135b ), range( 0x0000135f, 0x0000137d ),
    range( 0x00001380, 0x0000139a ), range( 0x000013a0, 0x000013f5 ), range( 0x00001401, 0x00001677 ),
    range( 0x00001680, 0x0000169d ), range( 0x000016a0, 0x000016f1 ), range( 0x00001700, 0x0000170d ),
    range( 0x0000170e, 0x00001715 ), range( 0x00001720, 0x00001737 ), range( 0x00001740, 0x00001754 ),
    range( 0x00001760, 0x0000176d ), range( 0x0000176e, 0x00001771 ), range( 0x00001772, 0x00001774 ),
    range( 0x00001780, 0x000017de ), range( 0x000017e0, 0x000017ea ), range( 0x000017f0, 0x000017fa ),
    range( 0x00001800, 0x0000180f ), range( 0x00001810, 0x0000181a ), range( 0x00001820, 0x00001878 ),
    range( 0x00001880, 0x000018ab ), range( 0x00001900, 0x0000191d ), range( 0x00001920, 0x0000192c ),
    range( 0x00001930, 0x0000193c ), range( 0x00001940, 0x00001941 ), range( 0x00001944, 0x0000196e ),
    range( 0x00001970, 0x00001975 ), range( 0x00001980, 0x000019aa ), range( 0x000019b0, 0x000019ca ),
    range( 0x000019d0, 0x000019da ), range( 0x000019de, 0x00001a1c ), range( 0x00001a1e, 0x00001a20 ),
    range( 0x00001b00, 0x00001b4c ), range( 0x00001b50, 0x00001b7d ), range( 0x00001b80, 0x00001bab ),
    range( 0x00001bae, 0x00001bba ), range( 0x00001c00, 0x00001c38 ), range( 0x00001c3b, 0x00001c4a ),
    range( 0x00001c4d, 0x00001c80 ), range( 0x00001d00, 0x00001de7 ), range( 0x00001dfe, 0x00001f16 ),
    range( 0x00001f18, 0x00001f1e ), range( 0x00001f20, 0x00001f46 ), range( 0x00001f48, 0x00001f4e ),
    range( 0x00001f50, 0x00001f58 ), range( 0x00001f59, 0x00001f5a ), range( 0x00001f5b, 0x00001f5c ),
    range( 0x00001f5d, 0x00001f5e ), range( 0x00001f5f, 0x00001f7e ), range( 0x00001f80, 0x00001fb5 ),
    range( 0x00001fb6, 0x00001fc5 ), range( 0x00001fc6, 0x00001fd4 ), range( 0x00001fd6, 0x00001fdc ),
    range( 0x00001fdd, 0x00001ff0 ), range( 0x00001ff2, 0x00001ff5 ), range( 0x00001ff6, 0x00001fff ),
    range( 0x00002000, 0x00002065 ), range( 0x0000206a, 0x00002072 ), range( 0x00002074, 0x0000208f ),
    range( 0x00002090, 0x00002095 ), range( 0x000020a0, 0x000020b6 ), range( 0x000020d0, 0x000020f1 ),
    range( 0x00002100, 0x00002150 ), range( 0x00002153, 0x00002189 ), range( 0x00002190, 0x000023e8 ),
    range( 0x00002400, 0x00002427 ), range( 0x00002440, 0x0000244b ), range( 0x00002460, 0x0000269e ),
    range( 0x000026a0, 0x000026bd ), range( 0x000026c0, 0x000026c4 ), range( 0x00002701, 0x00002705 ),
    range( 0x00002706, 0x0000270a ), range( 0x0000270c, 0x00002728 ), range( 0x00002729, 0x0000274c ),
    range( 0x0000274d, 0x0000274e ), range( 0x0000274f, 0x00002753 ), range( 0x00002756, 0x00002757 ),
    range( 0x00002758, 0x0000275f ), range( 0x00002761, 0x00002795 ), range( 0x00002798, 0x000027b0 ),
    range( 0x000027b1, 0x000027bf ), range( 0x000027c0, 0x000027cb ), range( 0x000027cc, 0x000027cd ),
    range( 0x000027d0, 0x00002b4d ), range( 0x00002b50, 0x00002b55 ), range( 0x00002c00, 0x00002c2f ),
    range( 0x00002c30, 0x00002c5f ), range( 0x00002c60, 0x00002c70 ), range( 0x00002c71, 0x00002c7e ),
    range( 0x00002c80, 0x00002ceb ), range( 0x00002cf9, 0x00002d26 ), range( 0x00002d30, 0x00002d66 ),
    range( 0x00002d6f, 0x00002d70 ), range( 0x00002d80, 0x00002d97 ), range( 0x00002da0, 0x00002da7 ),
    range( 0x00002da8, 0x00002daf ), range( 0x00002db0, 0x00002db7 ), range( 0x00002db8, 0x00002dbf ),
    range( 0x00002dc0, 0x00002dc7 ), range( 0x00002dc8, 0x00002dcf ), range( 0x00002dd0, 0x00002dd7 ),
    range( 0x00002dd8, 0x00002ddf ), range( 0x00002de0, 0x00002e31 ), range( 0x00002e80, 0x00002e9a ),
    range( 0x00002e9b, 0x00002ef4 ), range( 0x00002f00, 0x00002fd6 ), range( 0x00002ff0, 0x00002ffc ),
    range( 0x00003000, 0x00003040 ), range( 0x00003041, 0x00003097 ), range( 0x00003099, 0x00003100 ),
    range( 0x00003105, 0x0000312e ), range( 0x00003131, 0x0000318f ), range( 0x00003190, 0x000031b8 ),
    range( 0x000031c0, 0x000031e4 ), range( 0x000031f0, 0x0000321f ), range( 0x00003220, 0x00003244 ),
    range( 0x00003250, 0x000032ff ), range( 0x00003300, 0x00003400 ), range( 0x00003400, 0x00004db6 ),

    #range( 0x00004dc0, 0x00004e00 ), range( 0x00004e00, 0x00009fc4 ), range( 0x0000a000, 0x0000a48d ),
    range( 0x00004dc0, 0x00004e00 ), range( 0x00004e00, 0x00009fcc ), range( 0x0000a000, 0x0000a48d ),

    range( 0x0000a490, 0x0000a4c7 ), range( 0x0000a500, 0x0000a62c ), range( 0x0000a640, 0x0000a660 ),
    range( 0x0000a662, 0x0000a674 ), range( 0x0000a67c, 0x0000a698 ), range( 0x0000a700, 0x0000a78d ),
    range( 0x0000a7fb, 0x0000a82c ), range( 0x0000a840, 0x0000a878 ), range( 0x0000a880, 0x0000a8c5 ),
    range( 0x0000a8ce, 0x0000a8da ), range( 0x0000a900, 0x0000a954 ), range( 0x0000a95f, 0x0000a960 ),
    range( 0x0000aa00, 0x0000aa37 ), range( 0x0000aa40, 0x0000aa4e ), range( 0x0000aa50, 0x0000aa5a ),
    range( 0x0000aa5c, 0x0000aa60 ), range( 0x0000ac00, 0x0000d7a4 ), range( 0x0000d800, 0x0000db80 ),
    range( 0x0000db80, 0x0000dc00 ), range( 0x0000dc00, 0x0000e000 ), range( 0x0000e000, 0x0000f900 ),
    range( 0x0000f900, 0x0000fa2e ), range( 0x0000fa30, 0x0000fa6b ), range( 0x0000fa70, 0x0000fada ),
    range( 0x0000fb00, 0x0000fb07 ), range( 0x0000fb13, 0x0000fb18 ), range( 0x0000fb1d, 0x0000fb37 ),
    range( 0x0000fb38, 0x0000fb3d ), range( 0x0000fb3e, 0x0000fb3f ), range( 0x0000fb40, 0x0000fb42 ),
    range( 0x0000fb43, 0x0000fb45 ), range( 0x0000fb46, 0x0000fbb2 ), range( 0x0000fbd3, 0x0000fd40 ),
    range( 0x0000fd50, 0x0000fd90 ), range( 0x0000fd92, 0x0000fdc8 ), range( 0x0000fdf0, 0x0000fdfe ),
    range( 0x0000fe00, 0x0000fe1a ), range( 0x0000fe20, 0x0000fe27 ), range( 0x0000fe30, 0x0000fe53 ),
    range( 0x0000fe54, 0x0000fe67 ), range( 0x0000fe68, 0x0000fe6c ), range( 0x0000fe70, 0x0000fe75 ),
    range( 0x0000fe76, 0x0000fefd ), range( 0x0000feff, 0x0000ff00 ), range( 0x0000ff01, 0x0000ffbf ),
    range( 0x0000ffc2, 0x0000ffc8 ), range( 0x0000ffca, 0x0000ffd0 ), range( 0x0000ffd2, 0x0000ffd8 ),
    range( 0x0000ffda, 0x0000ffdd ), range( 0x0000ffe0, 0x0000ffe7 ), range( 0x0000ffe8, 0x0000ffef ),
    range( 0x0000fff9, 0x0000fffe ), range( 0x00010000, 0x0001000c ), range( 0x0001000d, 0x00010027 ),
    range( 0x00010028, 0x0001003b ), range( 0x0001003c, 0x0001003e ), range( 0x0001003f, 0x0001004e ),
    range( 0x00010050, 0x0001005e ), range( 0x00010080, 0x000100fb ), range( 0x00010100, 0x00010103 ),
    range( 0x00010107, 0x00010134 ), range( 0x00010137, 0x0001018b ), range( 0x00010190, 0x0001019c ),
    range( 0x000101d0, 0x000101fe ), range( 0x00010280, 0x0001029d ), range( 0x000102a0, 0x000102d1 ),
    range( 0x00010300, 0x0001031f ), range( 0x00010320, 0x00010324 ), range( 0x00010330, 0x0001034b ),
    range( 0x00010380, 0x0001039e ), range( 0x0001039f, 0x000103c4 ), range( 0x000103c8, 0x000103d6 ),
    range( 0x00010400, 0x0001049e ), range( 0x000104a0, 0x000104aa ), range( 0x00010800, 0x00010806 ),
    range( 0x00010808, 0x00010809 ), range( 0x0001080a, 0x00010836 ), range( 0x00010837, 0x00010839 ),
    range( 0x0001083c, 0x0001083d ), range( 0x0001083f, 0x00010840 ), range( 0x00010900, 0x0001091a ),
    range( 0x0001091f, 0x0001093a ), range( 0x0001093f, 0x00010940 ), range( 0x00010a00, 0x00010a04 ),
    range( 0x00010a05, 0x00010a07 ), range( 0x00010a0c, 0x00010a14 ), range( 0x00010a15, 0x00010a18 ),
    range( 0x00010a19, 0x00010a34 ), range( 0x00010a38, 0x00010a3b ), range( 0x00010a3f, 0x00010a48 ),
    range( 0x00010a50, 0x00010a59 ), range( 0x00012000, 0x0001236f ), range( 0x00012400, 0x00012463 ),
    range( 0x00012470, 0x00012474 ), range( 0x0001d000, 0x0001d0f6 ), range( 0x0001d100, 0x0001d127 ),
    range( 0x0001d129, 0x0001d1de ), range( 0x0001d200, 0x0001d246 ), range( 0x0001d300, 0x0001d357 ),
    range( 0x0001d360, 0x0001d372 ), range( 0x0001d400, 0x0001d455 ), range( 0x0001d456, 0x0001d49d ),
    range( 0x0001d49e, 0x0001d4a0 ), range( 0x0001d4a2, 0x0001d4a3 ), range( 0x0001d4a5, 0x0001d4a7 ),
    range( 0x0001d4a9, 0x0001d4ad ), range( 0x0001d4ae, 0x0001d4ba ), range( 0x0001d4bb, 0x0001d4bc ),
    range( 0x0001d4bd, 0x0001d4c4 ), range( 0x0001d4c5, 0x0001d506 ), range( 0x0001d507, 0x0001d50b ),
    range( 0x0001d50d, 0x0001d515 ), range( 0x0001d516, 0x0001d51d ), range( 0x0001d51e, 0x0001d53a ),
    range( 0x0001d53b, 0x0001d53f ), range( 0x0001d540, 0x0001d545 ), range( 0x0001d546, 0x0001d547 ),
    range( 0x0001d54a, 0x0001d551 ), range( 0x0001d552, 0x0001d6a6 ), range( 0x0001d6a8, 0x0001d7cc ),
    range( 0x0001d7ce, 0x0001d800 ), range( 0x0001f000, 0x0001f02c ), range( 0x0001f030, 0x0001f094 ),

    #range( 0x00020000, 0x0002a6d7 ), range( 0x0002f800, 0x0002fa1e ), range( 0x000e0001, 0x000e0002 ),
    range( 0x00020000, 0x0002a6d7 ),
    range( 0x0002a700, 0x0002b735 ), # u-cjk-extc
    range( 0x0002b740, 0x0002b81e ), # u-cjk-extd
    range( 0x0002f800, 0x0002fa1e ), range( 0x000e0001, 0x000e0002 ),

    range( 0x000e0020, 0x000e0080 ), range( 0x000e0100, 0x000e01f0 ), range( 0x000f0000, 0x000ffffe ),
    range( 0x00100000, 0x0010fffe ), )

  #---------------------------------------------------------------------------------------------------------
  ranges_of_defined_jizura_kanji_cscids = (
    # xrange( 0x000e000, 0x000e0ff ), ###OBS### excluded jzr-misc from valid codepoints
    _urange( 0x10000e100, 0x10000e13f ),
    _urange( 0x10000e141, 0x10000e149 ),
    _urange( 0x10000e14b, 0x10000e14b ),
    _urange( 0x10000e14d, 0x10000e156 ),
    _urange( 0x10000e158, 0x10000e163 ),
    _urange( 0x10000e165, 0x10000e182 ), )

  #---------------------------------------------------------------------------------------------------------
  # updated to Unicode 6.0
  unicode_cjk_cid_ranges = {
    ###OBS### should be extended to cover all Unicode blocks (and other character sets, using CSCIDs!);
    ### to and from should be expressed like UMXes, `from-cid`, from-chr`, `from-cscid` and so on;
    ### also, ranges should be extracted from ``range_names_to_cscid_range`` (which, in turn, should list
    ### ranges by range sigils)
    'Hangul Jamo':                              _urange( 0x1100,  0x11ff  ),
    'CJK Radicals Supplement':                  _urange( 0x2e80,  0x2eff  ),
    'Kangxi Radicals':                          _urange( 0x2f00,  0x2fdf  ),
    'Ideographic Description Characters':       _urange( 0x2ff0,  0x2fff  ),
    'CJK Symbols and Punctuation':              _urange( 0x3000,  0x303f  ),
    'Hiragana':                                 _urange( 0x3040,  0x309f  ),
    'Katakana':                                 _urange( 0x30a0,  0x30ff  ),
    'Bopomofo':                                 _urange( 0x3100,  0x312f  ),
    'Hangul Compatibility Jamo':                _urange( 0x3130,  0x318f  ),
    'Kanbun':                                   _urange( 0x3190,  0x319f  ),
    'Bopomofo Extended':                        _urange( 0x31a0,  0x31bf  ),
    'CJK Strokes':                              _urange( 0x31c0,  0x31ef  ),
    'Katakana Phonetic Extensions':             _urange( 0x31f0,  0x31ff  ),
    'Enclosed CJK Letters and Months':          _urange( 0x3200,  0x32ff  ),
    'CJK Compatibility':                        _urange( 0x3300,  0x33ff  ),
    'CJK Unified Ideographs Extension A':       _urange( 0x3400,  0x4dbf  ),
    'Yijing Hexagram Symbols':                  _urange( 0x4dc0,  0x4dff  ),
    'CJK Unified Ideographs':                   _urange( 0x4e00,  0x9fff  ),
    'Hangul Syllables':                         _urange( 0xac00,  0xd7af  ),
    'CJK Compatibility Ideographs':             _urange( 0xf900,  0xfaff  ),
    'CJK Compatibility Forms':                  _urange( 0xfe30,  0xfe4f  ),
    'Tai Xuan Jing Symbols':                    _urange( 0x1d300, 0x1d35f ),
    'CJK Unified Ideographs Extension B':       _urange( 0x20000, 0x2a6df ),

    'CJK Unified Ideographs Extension C':       _urange( 0x2a700, 0x2b73f ),
    'CJK Unified Ideographs Extension D':       _urange( 0x2b740, 0x2b81f ),

    'CJK Compatibility Ideographs Supplement':  _urange( 0x2f800, 0x2fa1f ),
    'Enclosed Ideographic Supplement':          _urange( 0x1f200, 0x1f2ff ),
    }

  #---------------------------------------------------------------------------------------------------------
  # updated to Unicode 6.0
  unicode_kanji_cid_ranges = {
    'CJK Radicals Supplement':                  _urange( 0x2e80,  0x2eff  ),
    'Kangxi Radicals':                          _urange( 0x2f00,  0x2fdf  ),
    # A selection of codepoints from the ``CJK Symbols and Punctuation`` block:
    'CJK Zero':                                 _urange( 0x3007,  0x3007  ),
    'Ad hoc Group 1':                           _urange( 0x3005,  0x3006  ),
    'Ad hoc Group 2':                           _urange( 0x3021,  0x3029  ),
    'Ad hoc Group 3':                           _urange( 0x3038,  0x3039  ),
    'Ad hoc Group 4':                           _urange( 0x303A,  0x303B  ),
    'Ad hoc Group 5':                           _urange( 0x303D,  0x303D  ),
    'CJK Strokes':                              _urange( 0x31c0,  0x31ef  ),
    'CJK Unified Ideographs Extension A':       _urange( 0x3400,  0x4dbf  ),
    'CJK Unified Ideographs':                   _urange( 0x4e00,  0x9fff  ),
    'CJK Compatibility Ideographs':             _urange( 0xf900,  0xfaff  ),
    'CJK Unified Ideographs Extension B':       _urange( 0x20000, 0x2a6df ),

    'CJK Unified Ideographs Extension C':       _urange( 0x2a700, 0x2b73f ),
    'CJK Unified Ideographs Extension D':       _urange( 0x2b740, 0x2b81f ),

    'CJK Compatibility Ideographs Supplement':  _urange( 0x2f800, 0x2fa1f ), }


  #---------------------------------------------------------------------------------------------------------
  # These names were taken from http://www.unicode.org/Public/UNIDATA/Blocks.txt for Unicode 5.1;
  # CJK Extension C has been added.
  range_names_to_cscid_range = {

    #=======================================================================================================
    # UNICODE
    #-------------------------------------------------------------------------------------------------------
    'Aegean Numbers':                                           _urange(  0x10100,  0x1013F ),
    'Alphabetic Presentation Forms':                            _urange(   0xFB00,   0xFB4F ),
    'Ancient Greek Musical Notation':                           _urange(  0x1D200,  0x1D24F ),
    'Ancient Greek Numbers':                                    _urange(  0x10140,  0x1018F ),
    'Ancient Symbols':                                          _urange(  0x10190,  0x101CF ),
    'Arabic Presentation Forms-A':                              _urange(   0xFB50,   0xFDFF ),
    'Arabic Presentation Forms-B':                              _urange(   0xFE70,   0xFEFF ),
    'Arabic Supplement':                                        _urange(   0x0750,   0x077F ),
    'Arabic':                                                   _urange(   0x0600,   0x06FF ),
    'Armenian':                                                 _urange(   0x0530,   0x058F ),
    'Arrows':                                                   _urange(   0x2190,   0x21FF ),
    'Balinese':                                                 _urange(   0x1B00,   0x1B7F ),
    'Basic Latin':                                              _urange(   0x0000,   0x007F ),
    'Bengali':                                                  _urange(   0x0980,   0x09FF ),
    'Block Elements':                                           _urange(   0x2580,   0x259F ),
    'Bopomofo Extended':                                        _urange(   0x31A0,   0x31BF ),
    'Bopomofo':                                                 _urange(   0x3100,   0x312F ),
    'Box Drawing':                                              _urange(   0x2500,   0x257F ),
    'Braille Patterns':                                         _urange(   0x2800,   0x28FF ),
    'Buginese':                                                 _urange(   0x1A00,   0x1A1F ),
    'Buhid':                                                    _urange(   0x1740,   0x175F ),
    'Byzantine Musical Symbols':                                _urange(  0x1D000,  0x1D0FF ),
    'Carian':                                                   _urange(  0x102A0,  0x102DF ),
    'Cham':                                                     _urange(   0xAA00,   0xAA5F ),
    'Cherokee':                                                 _urange(   0x13A0,   0x13FF ),
    'CJK Compatibility Forms':                                  _urange(   0xFE30,   0xFE4F ),
    'CJK Compatibility Ideographs Supplement':                  _urange(  0x2F800,  0x2FA1F ),
    'CJK Compatibility Ideographs':                             _urange(   0xF900,   0xFAFF ),
    'CJK Compatibility':                                        _urange(   0x3300,   0x33FF ),
    'CJK Radicals Supplement':                                  _urange(   0x2E80,   0x2EFF ),
    'CJK Strokes':                                              _urange(   0x31C0,   0x31EF ),
    'CJK Symbols and Punctuation':                              _urange(   0x3000,   0x303F ),
    'CJK Unified Ideographs Extension A':                       _urange(   0x3400,   0x4DBF ),
    'CJK Unified Ideographs Extension B':                       _urange(  0x20000,  0x2A6DF ),
    'CJK Unified Ideographs Extension C':                       _urange(  0x2A700,  0x2B73F ),
    'CJK Unified Ideographs Extension D':                       _urange(  0x2B740,  0x2B81F ),
    'CJK Unified Ideographs':                                   _urange(   0x4E00,   0x9FFF ),
    'Combining Diacritical Marks for Symbols':                  _urange(   0x20D0,   0x20FF ),
    'Combining Diacritical Marks Supplement':                   _urange(   0x1DC0,   0x1DFF ),
    'Combining Diacritical Marks':                              _urange(   0x0300,   0x036F ),
    'Combining Half Marks':                                     _urange(   0xFE20,   0xFE2F ),
    'Control Pictures':                                         _urange(   0x2400,   0x243F ),
    'Coptic':                                                   _urange(   0x2C80,   0x2CFF ),
    'Counting Rod Numerals':                                    _urange(  0x1D360,  0x1D37F ),
    'Cuneiform Numbers and Punctuation':                        _urange(  0x12400,  0x1247F ),
    'Cuneiform':                                                _urange(  0x12000,  0x123FF ),
    'Currency Symbols':                                         _urange(   0x20A0,   0x20CF ),
    'Cypriot Syllabary':                                        _urange(  0x10800,  0x1083F ),
    'Cyrillic Extended-A':                                      _urange(   0x2DE0,   0x2DFF ),
    'Cyrillic Extended-B':                                      _urange(   0xA640,   0xA69F ),
    'Cyrillic Supplement':                                      _urange(   0x0500,   0x052F ),
    'Cyrillic':                                                 _urange(   0x0400,   0x04FF ),
    'Deseret':                                                  _urange(  0x10400,  0x1044F ),
    'Devanagari':                                               _urange(   0x0900,   0x097F ),
    'Dingbats':                                                 _urange(   0x2700,   0x27BF ),
    'Domino Tiles':                                             _urange(  0x1F030,  0x1F09F ),
    'Enclosed Alphanumerics':                                   _urange(   0x2460,   0x24FF ),
    'Enclosed Ideographic Supplement':                          _urange(  0x1f200,  0x1f2ff ),
    'Enclosed CJK Letters and Months':                          _urange(   0x3200,   0x32FF ),
    'Ethiopic Extended':                                        _urange(   0x2D80,   0x2DDF ),
    'Ethiopic Supplement':                                      _urange(   0x1380,   0x139F ),
    'Ethiopic':                                                 _urange(   0x1200,   0x137F ),
    'General Punctuation':                                      _urange(   0x2000,   0x206F ),
    'Geometric Shapes':                                         _urange(   0x25A0,   0x25FF ),
    'Georgian Supplement':                                      _urange(   0x2D00,   0x2D2F ),
    'Georgian':                                                 _urange(   0x10A0,   0x10FF ),
    'Glagolitic':                                               _urange(   0x2C00,   0x2C5F ),
    'Gothic':                                                   _urange(  0x10330,  0x1034F ),
    'Greek and Coptic':                                         _urange(   0x0370,   0x03FF ),
    'Greek Extended':                                           _urange(   0x1F00,   0x1FFF ),
    'Gujarati':                                                 _urange(   0x0A80,   0x0AFF ),
    'Gurmukhi':                                                 _urange(   0x0A00,   0x0A7F ),
    'Halfwidth and Fullwidth Forms':                            _urange(   0xFF00,   0xFFEF ),
    'Hangul Compatibility Jamo':                                _urange(   0x3130,   0x318F ),
    'Hangul Jamo':                                              _urange(   0x1100,   0x11FF ),
    'Hangul Syllables':                                         _urange(   0xAC00,   0xD7AF ),
    'Hanunoo':                                                  _urange(   0x1720,   0x173F ),
    'Hebrew':                                                   _urange(   0x0590,   0x05FF ),
    'High Private Use Surrogates':                              _urange(   0xDB80,   0xDBFF ),
    'High Surrogates':                                          _urange(   0xD800,   0xDB7F ),
    'Hiragana':                                                 _urange(   0x3040,   0x309F ),
    'Ideographic Description Characters':                       _urange(   0x2FF0,   0x2FFF ),
    'IPA Extensions':                                           _urange(   0x0250,   0x02AF ),
    'Kanbun':                                                   _urange(   0x3190,   0x319F ),
    'Kangxi Radicals':                                          _urange(   0x2F00,   0x2FDF ),
    'Kannada':                                                  _urange(   0x0C80,   0x0CFF ),
    'Katakana Phonetic Extensions':                             _urange(   0x31F0,   0x31FF ),
    'Katakana':                                                 _urange(   0x30A0,   0x30FF ),
    'Kayah Li':                                                 _urange(   0xA900,   0xA92F ),
    'Kharoshthi':                                               _urange(  0x10A00,  0x10A5F ),
    'Khmer Symbols':                                            _urange(   0x19E0,   0x19FF ),
    'Khmer':                                                    _urange(   0x1780,   0x17FF ),
    'Lao':                                                      _urange(   0x0E80,   0x0EFF ),
    'Latin Extended Additional':                                _urange(   0x1E00,   0x1EFF ),
    'Latin Extended-A':                                         _urange(   0x0100,   0x017F ),
    'Latin Extended-B':                                         _urange(   0x0180,   0x024F ),
    'Latin Extended-C':                                         _urange(   0x2C60,   0x2C7F ),
    'Latin Extended-D':                                         _urange(   0xA720,   0xA7FF ),
    'Latin-1 Supplement':                                       _urange(   0x0080,   0x00FF ),
    'Lepcha':                                                   _urange(   0x1C00,   0x1C4F ),
    'Letterlike Symbols':                                       _urange(   0x2100,   0x214F ),
    'Limbu':                                                    _urange(   0x1900,   0x194F ),
    'Linear B Ideograms':                                       _urange(  0x10080,  0x100FF ),
    'Linear B Syllabary':                                       _urange(  0x10000,  0x1007F ),
    'Low Surrogates':                                           _urange(   0xDC00,   0xDFFF ),
    'Lycian':                                                   _urange(  0x10280,  0x1029F ),
    'Lydian':                                                   _urange(  0x10920,  0x1093F ),
    'Mahjong Tiles':                                            _urange(  0x1F000,  0x1F02F ),
    'Malayalam':                                                _urange(   0x0D00,   0x0D7F ),
    'Mathematical Alphanumeric Symbols':                        _urange(  0x1D400,  0x1D7FF ),
    'Mathematical Operators':                                   _urange(   0x2200,   0x22FF ),
    'Miscellaneous Mathematical Symbols-A':                     _urange(   0x27C0,   0x27EF ),
    'Miscellaneous Mathematical Symbols-B':                     _urange(   0x2980,   0x29FF ),
    'Miscellaneous Symbols and Arrows':                         _urange(   0x2B00,   0x2BFF ),
    'Miscellaneous Symbols':                                    _urange(   0x2600,   0x26FF ),
    'Miscellaneous Technical':                                  _urange(   0x2300,   0x23FF ),
    'Modifier Tone Letters':                                    _urange(   0xA700,   0xA71F ),
    'Mongolian':                                                _urange(   0x1800,   0x18AF ),
    'Musical Symbols':                                          _urange(  0x1D100,  0x1D1FF ),
    'Myanmar':                                                  _urange(   0x1000,   0x109F ),
    'New Tai Lue':                                              _urange(   0x1980,   0x19DF ),
    'NKo':                                                      _urange(   0x07C0,   0x07FF ),
    'Number Forms':                                             _urange(   0x2150,   0x218F ),
    'Ogham':                                                    _urange(   0x1680,   0x169F ),
    'Ol Chiki':                                                 _urange(   0x1C50,   0x1C7F ),
    'Old Italic':                                               _urange(  0x10300,  0x1032F ),
    'Old Persian':                                              _urange(  0x103A0,  0x103DF ),
    'Optical Character Recognition':                            _urange(   0x2440,   0x245F ),
    'Oriya':                                                    _urange(   0x0B00,   0x0B7F ),
    'Osmanya':                                                  _urange(  0x10480,  0x104AF ),
    'Phags-pa':                                                 _urange(   0xA840,   0xA87F ),
    'Phaistos Disc':                                            _urange(  0x101D0,  0x101FF ),
    'Phoenician':                                               _urange(  0x10900,  0x1091F ),
    'Phonetic Extensions Supplement':                           _urange(   0x1D80,   0x1DBF ),
    'Phonetic Extensions':                                      _urange(   0x1D00,   0x1D7F ),
    'Private Use Area':                                         _urange(   0xE000,   0xF8FF ),
    'Rejang':                                                   _urange(   0xA930,   0xA95F ),
    'Runic':                                                    _urange(   0x16A0,   0x16FF ),
    'Saurashtra':                                               _urange(   0xA880,   0xA8DF ),
    'Shavian':                                                  _urange(  0x10450,  0x1047F ),
    'Sinhala':                                                  _urange(   0x0D80,   0x0DFF ),
    'Small Form Variants':                                      _urange(   0xFE50,   0xFE6F ),
    'Spacing Modifier Letters':                                 _urange(   0x02B0,   0x02FF ),
    'Specials':                                                 _urange(   0xFFF0,   0xFFFF ),
    'Sundanese':                                                _urange(   0x1B80,   0x1BBF ),
    'Superscripts and Subscripts':                              _urange(   0x2070,   0x209F ),
    'Supplemental Arrows-A':                                    _urange(   0x27F0,   0x27FF ),
    'Supplemental Arrows-B':                                    _urange(   0x2900,   0x297F ),
    'Supplemental Mathematical Operators':                      _urange(   0x2A00,   0x2AFF ),
    'Supplemental Punctuation':                                 _urange(   0x2E00,   0x2E7F ),
    'Supplementary Private Use Area-A':                         _urange(  0xF0000,  0xFFFFF ),
    'Supplementary Private Use Area-B':                         _urange( 0x100000, 0x10FFFF ),
    'Syloti Nagri':                                             _urange(   0xA800,   0xA82F ),
    'Syriac':                                                   _urange(   0x0700,   0x074F ),
    'Tagalog':                                                  _urange(   0x1700,   0x171F ),
    'Tagbanwa':                                                 _urange(   0x1760,   0x177F ),
    'Tags':                                                     _urange(  0xE0000,  0xE007F ),
    'Tai Le':                                                   _urange(   0x1950,   0x197F ),
    'Tai Xuan Jing Symbols':                                    _urange(  0x1D300,  0x1D35F ),
    'Tamil':                                                    _urange(   0x0B80,   0x0BFF ),
    'Telugu':                                                   _urange(   0x0C00,   0x0C7F ),
    'Thaana':                                                   _urange(   0x0780,   0x07BF ),
    'Thai':                                                     _urange(   0x0E00,   0x0E7F ),
    'Tibetan':                                                  _urange(   0x0F00,   0x0FFF ),
    'Tifinagh':                                                 _urange(   0x2D30,   0x2D7F ),
    'Ugaritic':                                                 _urange(  0x10380,  0x1039F ),
    'Unified Canadian Aboriginal Syllabics':                    _urange(   0x1400,   0x167F ),
    'Vai':                                                      _urange(   0xA500,   0xA63F ),
    'Variation Selectors Supplement':                           _urange(  0xE0100,  0xE01EF ),
    'Variation Selectors':                                      _urange(   0xFE00,   0xFE0F ),
    'Vertical Forms':                                           _urange(   0xFE10,   0xFE1F ),
    'Yi Radicals':                                              _urange(   0xA490,   0xA4CF ),
    'Yi Syllables':                                             _urange(   0xA000,   0xA48F ),
    'Yijing Hexagram Symbols':                                  _urange(   0x4DC0,   0x4DFF ),

    #=======================================================================================================
    # JIZURA
    #-------------------------------------------------------------------------------------------------------
    'JZR Miscellaneous':                                        _urange( 0x100000000, 0x10000e0ff ),
    'JZR CJK Figures':                                          _urange( 0x10000e100, 0x10000f0ff ),
    }



  ############################################################################################################
  _range_names_to_range_sigils = {
    #=========================================================================================================
    # UNICODE
    #---------------------------------------------------------------------------------------------------------
    'Aegean Numbers':                                           None,
    'Alphabetic Presentation Forms':                            'u-abc-pf',
    'Ancient Greek Musical Notation':                           None,
    'Ancient Greek Numbers':                                    None,
    'Ancient Symbols':                                          None,
    'Arabic Presentation Forms-A':                              'u-arab-pf-a',
    'Arabic Presentation Forms-B':                              'u-arab-pf-b',
    'Arabic Supplement':                                        'u-arab-s',
    'Arabic':                                                   'u-arab',
    'Armenian':                                                 None,
    'Arrows':                                                   'u-arrow',
    'Balinese':                                                 None,
    'Basic Latin':                                              'u-latn',
    'Bengali':                                                  None,
    'Block Elements':                                           'u-block',
    'Bopomofo Extended':                                        'u-bopo-x',
    'Bopomofo':                                                 'u-bopo',
    'Box Drawing':                                              'u-boxdr',
    'Braille Patterns':                                         'u-brail',
    'Buginese':                                                 None,
    'Buhid':                                                    None,
    'Byzantine Musical Symbols':                                None,
    'Carian':                                                   None,
    'Cham':                                                     None,
    'Cherokee':                                                 None,
    'CJK Compatibility Forms':                                  'u-cjk-cmpf',
    'CJK Compatibility Ideographs Supplement':                  'u-cjk-cmpi2',
    'CJK Compatibility Ideographs':                             'u-cjk-cmpi1',
    'CJK Compatibility':                                        'u-cjk-cmp',
    'CJK Radicals Supplement':                                  'u-cjk-rad2',
    'CJK Strokes':                                              'u-cjk-strk',
    'CJK Symbols and Punctuation':                              'u-cjk-sym',
    'CJK Unified Ideographs Extension A':                       'u-cjk-xa',
    'CJK Unified Ideographs Extension B':                       'u-cjk-xb',
    'CJK Unified Ideographs Extension C':                       'u-cjk-xc',
    'CJK Unified Ideographs Extension D':                       'u-cjk-xd',
    'CJK Unified Ideographs':                                   'u-cjk',
    'Combining Diacritical Marks for Symbols':                  'u-cdm-sy',
    'Combining Diacritical Marks Supplement':                   'u-cdm-s',
    'Combining Diacritical Marks':                              'u-cdm',
    'Combining Half Marks':                                     None,
    'Control Pictures':                                         'u-ctrlp',
    'Coptic':                                                   None,
    'Counting Rod Numerals':                                    None,
    'Cuneiform Numbers and Punctuation':                        None,
    'Cuneiform':                                                None,
    'Currency Symbols':                                         'u-currn',
    'Cypriot Syllabary':                                        None,
    'Cyrillic Extended-A':                                      'u-cyrl-a',
    'Cyrillic Extended-B':                                      'u-cyrl-b',
    'Cyrillic Supplement':                                      'u-cyrl-s',
    'Cyrillic':                                                 'u-cyrl',
    'Deseret':                                                  None,
    'Devanagari':                                               None,
    'Dingbats':                                                 'u-dingb',
    'Domino Tiles':                                             None,
    'Enclosed Alphanumerics':                                   'u-enalp',
    'Enclosed CJK Letters and Months':                          'u-cjk-enclett',
    'Enclosed Ideographic Supplement':                          'u-cjk-encsupp',
    'Ethiopic Extended':                                        None,
    'Ethiopic Supplement':                                      None,
    'Ethiopic':                                                 None,
    'General Punctuation':                                      'u-punct',
    'Geometric Shapes':                                         'u-geoms',
    'Georgian Supplement':                                      None,
    'Georgian':                                                 None,
    'Glagolitic':                                               None,
    'Gothic':                                                   None,
    'Greek and Coptic':                                         'u-grek',
    'Greek Extended':                                           'u-grek-x',
    'Gujarati':                                                 None,
    'Gurmukhi':                                                 None,
    'Halfwidth and Fullwidth Forms':                            'u-halfull',
    'Hangul Compatibility Jamo':                                'u-hang-comp-jm',
    'Hangul Jamo':                                              'u-hang-jm',
    'Hangul Syllables':                                         'u-hang-syl',
    'Hanunoo':                                                  None,
    'Hebrew':                                                   None,
    'High Private Use Surrogates':                              None,
    'High Surrogates':                                          None,
    'Hiragana':                                                 'u-cjk-hira',
    'Ideographic Description Characters':                       'u-cjk-idc',
    'IPA Extensions':                                           'u-ipa-x',
    'Kanbun':                                                   'u-cjk-kanbun',
    'Kangxi Radicals':                                          'u-cjk-rad1',
    'Kannada':                                                  None,
    'Katakana Phonetic Extensions':                             'u-cjk-kata-x',
    'Katakana':                                                 'u-cjk-kata',
    'Kayah Li':                                                 None,
    'Kharoshthi':                                               None,
    'Khmer Symbols':                                            None,
    'Khmer':                                                    None,
    'Lao':                                                      None,
    'Latin Extended Additional':                                'u-latn-xa',
    'Latin Extended-A':                                         'u-latn-a',
    'Latin Extended-B':                                         'u-latn-b',
    'Latin Extended-C':                                         'u-latn-c',
    'Latin Extended-D':                                         'u-latn-d',
    'Latin-1 Supplement':                                       'u-latn-1',
    'Lepcha':                                                   None,
    'Letterlike Symbols':                                       'u-llsym',
    'Limbu':                                                    None,
    'Linear B Ideograms':                                       None,
    'Linear B Syllabary':                                       None,
    'Low Surrogates':                                           None,
    'Lycian':                                                   None,
    'Lydian':                                                   None,
    'Mahjong Tiles':                                            None,
    'Malayalam':                                                None,
    'Mathematical Alphanumeric Symbols':                        None,
    'Mathematical Operators':                                   None,
    'Miscellaneous Mathematical Symbols-A':                     'u-maths-a',
    'Miscellaneous Mathematical Symbols-B':                     None,
    'Miscellaneous Symbols and Arrows':                         None,
    'Miscellaneous Symbols':                                    'u-sym',
    'Miscellaneous Technical':                                  None,
    'Modifier Tone Letters':                                    None,
    'Mongolian':                                                None,
    'Musical Symbols':                                          None,
    'Myanmar':                                                  None,
    'New Tai Lue':                                              None,
    'NKo':                                                      None,
    'Number Forms':                                             'u-num',
    'Ogham':                                                    None,
    'Ol Chiki':                                                 'u-olck',
    'Old Italic':                                               None,
    'Old Persian':                                              None,
    'Optical Character Recognition':                            'u-ocr',
    'Oriya':                                                    None,
    'Osmanya':                                                  None,
    'Phags-pa':                                                 None,
    'Phaistos Disc':                                            None,
    'Phoenician':                                               None,
    'Phonetic Extensions Supplement':                           'u-phon-xs',
    'Phonetic Extensions':                                      'u-phon-x',
    'Private Use Area':                                         'u-pua',
    'Rejang':                                                   None,
    'Runic':                                                    None,
    'Saurashtra':                                               None,
    'Shavian':                                                  None,
    'Sinhala':                                                  None,
    'Small Form Variants':                                      'u-small',
    'Spacing Modifier Letters':                                 'u-sml',
    'Specials':                                                 'u-special',
    'Sundanese':                                                None,
    'Superscripts and Subscripts':                              'u-supsub',
    'Supplemental Arrows-A':                                    'u-arrow-a',
    'Supplemental Arrows-B':                                    'u-arrow-b',
    'Supplemental Mathematical Operators':                      None,
    'Supplemental Punctuation':                                 'u-punct-s',
    'Supplementary Private Use Area-A':                         None,
    'Supplementary Private Use Area-B':                         None,
    'Syloti Nagri':                                             None,
    'Syriac':                                                   None,
    'Tagalog':                                                  None,
    'Tagbanwa':                                                 None,
    'Tags':                                                     None,
    'Tai Le':                                                   None,
    'Tai Xuan Jing Symbols':                                    'u-txj-sym',
    'Tamil':                                                    None,
    'Telugu':                                                   None,
    'Thaana':                                                   None,
    'Thai':                                                     None,
    'Tibetan':                                                  None,
    'Tifinagh':                                                 None,
    'Ugaritic':                                                 None,
    'Unified Canadian Aboriginal Syllabics':                    None,
    'Vai':                                                      None,
    'Variation Selectors Supplement':                           'u-varsl-s',
    'Variation Selectors':                                      'u-varsl',
    'Vertical Forms':                                           'u-vertf',
    'Yi Radicals':                                              None,
    'Yi Syllables':                                             None,
    'Yijing Hexagram Symbols':                                  'u-yijng',

    #=========================================================================================================
    # JIZURA
    #---------------------------------------------------------------------------------------------------------
    'JZR Miscellaneous':                                        'jzr-misc',
    'JZR CJK Figures':                                          'jzr-fig',
    }

  #===========================================================================================================
  range_names_to_range_sigils = dict(
    ( name, rsg, )
      for name, rsg in _range_names_to_range_sigils.items()
        if rsg )
  #-----------------------------------------------------------------------------------------------------------
  range_sigils_to_range_names = dict(
    ( rsg, name, )
      for name, rsg in range_names_to_range_sigils.items() )

  #-----------------------------------------------------------------------------------------------------------
  range_sigils_for_sortcid = [
      'u-cjk',
      'u-cjk-xa',
      'u-cjk-xb',
      'u-cjk-xc',
      'u-cjk-xd',
      'u-cjk-sym',
      'u-cjk-rad1',
      'u-cjk-rad2',
      'u-cjk-strk',
      'u-cjk-cmpi1',
      'u-cjk-cmpi2',
      'u-cjk-cmpf',

      'jzr-fig',
      'jzr-misc',

      'c1',
      'c2',
      'c3',
      'c4',
      'c5',
      'c6',
      'c7',
      'cb',
      'cdp',
      'gt',
      'gtk',
      'hzk1',
      'hzk2',
      'hzk3',
      'hzk4',
      'hzk5',
      'hzk6',
      'hzk7',
      'hzk8',
      'hzk9',
      'hzk10',
      'hzk11',
      'hzk12',
      'j83',
      'j90',
      'jc3',
      'jsp',
      'jx1',
      'jx2',
      'jx3',
      'jzr',
      'mcs',
      'morohashi',
      'rui6',
      'aj',
      'b',

      'u-boxdr',
      'u-bopo',
      'u-geoms',
      'u-halfull', ]


  ############################################################################################################
  u_script_codes_to_script_name = {
    'Arab':   'Arabic',
    'Armi':   'Imperial Aramaic',
    'Armn':   'Armenian',
    'Avst':   'Avestan',
    'Bali':   'Balinese',
    'Batk':   'Batak',
    'Beng':   'Bengali',
    'Blis':   'Blissymbols',
    'Bopo':   'Bopomofo',
    'Brah':   'Brahmi',
    'Brai':   'Braille',
    'Bugi':   'Buginese',
    'Buhd':   'Buhid',
    'Cakm':   'Chakma',
    'Cans':   'Unified Canadian Aboriginal Syllabics',
    'Cari':   'Carian',
    'Cham':   'Cham',
    'Cher':   'Cherokee',
    'Cirt':   'Cirth',
    'Copt':   'Coptic',
    'Cprt':   'Cypriot',
    'Cyrl':   'Cyrillic',
    'Cyrs':   'Cyrillic (Old Church Slavonic variant)',
    'Deva':   'Devanagari (Nagari)',
    'Dsrt':   'Deseret (Mormon)',
    'Egyd':   'Egyptian demotic',
    'Egyh':   'Egyptian hieratic',
    'Egyp':   'Egyptian hieroglyphs',
    'Ethi':   'Ethiopic (Ge?ez)',
    'Geok':   'Khutsuri (Asomtavruli and Nuskhuri)',
    'Geor':   'Georgian (Mkhedruli)',
    'Glag':   'Glagolitic',
    'Goth':   'Gothic',
    'Grek':   'Greek',
    'Gujr':   'Gujarati',
    'Guru':   'Gurmukhi',
    'Hang':   'Hangul (Hangul, Hangeul)',
    'Hani':   'Han (Hanzi, Kanji, Hanja)',
    'Hano':   'Hanunoo (Hanunóo)',
    'Hans':   'Han (Simplified variant)',
    'Hant':   'Han (Traditional variant)',
    'Hebr':   'Hebrew',
    'Hira':   'Hiragana',
    'Hmng':   'Pahawh Hmong',
    'Hrkt':   '(alias for Hiragana + Katakana)',
    'Hung':   'Old Hungarian',
    'Inds':   'Indus (Harappan)',
    'Ital':   'Old Italic (Etruscan, Oscan, etc.)',
    'Java':   'Javanese',
    'Jpan':   'Japanese (alias for Han + Hiragana + Katakana)',
    'Kali':   'Kayah Li',
    'Kana':   'Katakana',
    'Khar':   'Kharoshthi',
    'Khmr':   'Khmer',
    'Knda':   'Kannada',
    'Kore':   'Korean (alias for Hangul + Han)',
    'Kthi':   'Kaithi',
    'Lana':   'Tai Tham (Lanna)',
    'Laoo':   'Lao',
    'Latf':   'Latin (Fraktur variant)',
    'Latg':   'Latin (Gaelic variant)',
    'Latn':   'Latin',
    'Lepc':   'Lepcha (Róng)',
    'Limb':   'Limbu',
    'Lina':   'Linear A',
    'Linb':   'Linear B',
    'Lisu':   'Lisu (Fraser)',
    'Lyci':   'Lycian',
    'Lydi':   'Lydian',
    'Mand':   'Mandaic, Mandaean',
    'Mani':   'Manichaean',
    'Maya':   'Mayan hieroglyphs',
    'Mero':   'Meroitic',
    'Mlym':   'Malayalam',
    'Mong':   'Mongolian',
    'Moon':   'Moon (Moon code, Moon script, Moon type)',
    'Mtei':   'Meitei Mayek (Meithei, Meetei)',
    'Mymr':   'Myanmar (Burmese)',
    'Nkgb':   'Nakhi Geba Naxi Geba)',
    'Nkoo':   'N’Ko',
    'Ogam':   'Ogham',
    'Olck':   'Ol Chiki (Ol Cemet’, Ol, Santali)',
    'Orkh':   'Orkhon',
    'Orya':   'Oriya',
    'Osma':   'Osmanya',
    'Perm':   'Old Permic',
    'Phag':   'Phags-pa',
    'Phli':   'Inscriptional Pahlavi',
    'Phlp':   'Psalter Pahlavi',
    'Phlv':   'Book Pahlavi',
    'Phnx':   'Phoenician',
    'Plrd':   'Miao (Pollard)',
    'Prti':   'Inscriptional Parthian',
    'Qaaa':   'Reserved for private use (start)',
    'Qabx':   'Reserved for private use (end)',
    'Rjng':   'Rejang (Redjang, Kaganga)',
    'Roro':   'Rongorongo',
    'Runr':   'Runic',
    'Samr':   'Samaritan',
    'Sara':   'Sarati',
    'Saur':   'Saurashtra',
    'Sgnw':   'SignWriting',
    'Shaw':   'Shavian (Shaw)',
    'Sinh':   'Sinhala',
    'Sund':   'Sundanese',
    'Sylo':   'Syloti Nagri',
    'Syrc':   'Syriac',
    'Syre':   'Syriac (Estrangelo variant)',
    'Syrj':   'Syriac (Western variant)',
    'Syrn':   'Syriac (Eastern variant)',
    'Tagb':   'Tagbanwa',
    'Tale':   'Tai Le',
    'Talu':   'New Tai Lue',
    'Taml':   'Tamil',
    'Tavt':   'Tai Viet',
    'Telu':   'Telugu',
    'Teng':   'Tengwar',
    'Tfng':   'Tifinagh (Berber)',
    'Tglg':   'Tagalog (Baybayin, Alibata)',
    'Thaa':   'Thaana',
    'Thai':   'Thai',
    'Tibt':   'Tibetan',
    'Ugar':   'Ugaritic',
    'Vaii':   'Vai',
    'Visp':   'Visible Speech',
    'Xpeo':   'Old Persian',
    'Xsux':   'Cuneiform, Sumero-Akkadian',
    'Yiii':   'Yi',
    'Zinh':   'Code for inherited script',
    'Zmth':   'Mathematical notation',
    'Zsym':   'Symbols',
    'Zxxx':   'Code for unwritten documents',
    'Zyyy':   'Code for undetermined script',
    'Zzzz':   'Code for uncoded script', }


UMX_data = UMX_data_000()
