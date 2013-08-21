
TRM                       = require 'coffeenode-trm'
log                       = TRM.log.bind TRM
echo                      = TRM.echo.bind TRM
rainbow                   = TRM.rainbow.bind TRM
CHR                       = require '../../coffeenode-chr'

# log '&jzr#x123;helo'.match @xncr_kernel_matcher
# log '&jzr#x123;helo'.match @ncr_kernel_matcher
# log '&#x123;helo'.match @xncr_kernel_matcher
# log '&#x123;helo'.match @ncr_kernel_matcher
# log '&#x123;helo'.match @first_chr_matcher_ncr
# log '&#x123;helo'.match @first_chr_matcher_xncr
# log '&#x123;helo'.match @first_chr_matcher_plain
# log '𤕣古文龜'.match @first_chr_matcher_plain

assert = require 'assert'
# assert = require 'better-assert'

assert.deepEqual ( ( '&jzr#x123;helo'.match CHR._first_chr_matcher_xncr )[ 1 .. 3 ] ),[ 'jzr', '123', undefined ]
assert.deepEqual ( ( '&jzr#123;helo'.match  CHR._first_chr_matcher_xncr )[ 1 .. 3 ] ),[ 'jzr', undefined, '123' ]
assert.deepEqual ( ( '&#x123;helo'.match    CHR._first_chr_matcher_xncr )[ 1 .. 3 ] ),[ '', '123', undefined ]
assert.deepEqual ( ( '&#x123;helo'.match    CHR._first_chr_matcher_ncr )[ 1 .. 3 ] ), [ '', '123', undefined ]
assert.deepEqual ( ( '&#123;helo'.match     CHR._first_chr_matcher_ncr )[ 1 .. 3 ] ), [ '', undefined, '123' ]
assert.deepEqual ( CHR._chr_csg_cid_from_chr 'abc', 'plain' ),                       [ 'a', 'u', 97 ]
assert.deepEqual ( CHR._chr_csg_cid_from_chr 'abc', 'ncr' ),                         [ 'a', 'u', 97 ]
assert.deepEqual ( CHR._chr_csg_cid_from_chr 'abc', 'xncr' ),                        [ 'a', 'u', 97 ]
assert.deepEqual ( CHR._chr_csg_cid_from_chr '&#97;abc', 'plain' ),                  [ '&', 'u', 38 ]
assert.deepEqual ( CHR._chr_csg_cid_from_chr '&#97;abc', 'ncr' ),                    [ '&#97;', 'u', 97 ]
assert.deepEqual ( CHR._chr_csg_cid_from_chr '&#97;abc', 'xncr' ),                   [ '&#97;', 'u', 97 ]
assert.deepEqual ( CHR._chr_csg_cid_from_chr '&#x61;abc' ),                          [ '&', 'u', 38 ]
assert.deepEqual ( CHR._chr_csg_cid_from_chr '&#x61;abc', 'plain' ),                 [ '&', 'u', 38 ]
assert.deepEqual ( CHR._chr_csg_cid_from_chr '&#x61;abc', 'ncr' ),                   [ '&#x61;', 'u', 97 ]
assert.deepEqual ( CHR._chr_csg_cid_from_chr '&#x61;abc', 'xncr' ),                  [ '&#x61;', 'u', 97 ]
assert.deepEqual ( CHR.csg_cid_from_chr '&#x24563;' ),                               [ 'u', 38 ]
assert.deepEqual ( CHR.csg_cid_from_chr '&#x24563;', 'plain' ),                      [ 'u', 38 ]
assert.deepEqual ( CHR.csg_cid_from_chr '&#x24563;', 'ncr' ),                        [ 'u', 148835 ]
assert.deepEqual ( CHR.csg_cid_from_chr '&#x24563;', 'xncr' ),                       [ 'u', 148835 ]
assert.deepEqual ( CHR.csg_cid_from_chr '𤕣' ),                                       [ 'u', 148835 ]
assert.deepEqual ( CHR.csg_cid_from_chr '𤕣', 'plain' ),                              [ 'u', 148835 ]
assert.deepEqual ( CHR.csg_cid_from_chr '𤕣', 'ncr' ),                                [ 'u', 148835 ]
assert.deepEqual ( CHR.csg_cid_from_chr '𤕣', 'xncr' ),                               [ 'u', 148835 ]
assert.deepEqual ( ( '𤕣'[ 0 ] + 'x' ).match CHR._first_chr_matcher_plain ), null
assert.throws ( -> CHR._chr_csg_cid_from_chr '𤕣'[ 0 ] ),        /^Error: illegal character sequence/
assert.throws ( -> CHR._chr_csg_cid_from_chr '𤕣'[ 0 ] + 'x' ),  /^Error: illegal character sequence/

#===========================================================================================================
# SPLITTING TEXTS
#-----------------------------------------------------------------------------------------------------------
assert.deepEqual ( CHR.chrs_of ''                   ), []
assert.deepEqual ( CHR.chrs_of 'abc'                ), [ 'a', 'b', 'c' ]
assert.deepEqual ( CHR.chrs_of '𤕣abc'               ), [ '𤕣', 'a', 'b', 'c' ]
assert.deepEqual ( CHR.chrs_of '𤕣ab𤕣c'              ), [ '𤕣', 'a', 'b', '𤕣', 'c' ]
assert.deepEqual ( CHR.chrs_of '𤕣a&#123;b𤕣c'        ), [ '𤕣', 'a', '&', '#', '1', '2', '3', ';', 'b', '𤕣', 'c' ]
assert.deepEqual ( CHR.chrs_of '𤕣a&jzr#123;b𤕣c'     ), [ '𤕣', 'a', '&', 'j', 'z', 'r', '#', '1', '2', '3', ';', 'b', '𤕣', 'c' ]
assert.deepEqual ( CHR.chrs_of '𤕣a&#x123ab;b𤕣c'     ), [ '𤕣', 'a', '&', '#', 'x', '1', '2', '3', 'a', 'b', ';', 'b', '𤕣', 'c' ]
assert.deepEqual ( CHR.chrs_of '𤕣a&jzr#x123ab;b𤕣c'  ), [ '𤕣', 'a', '&', 'j', 'z', 'r', '#', 'x', '1', '2', '3', 'a', 'b', ';', 'b', '𤕣', 'c' ]
assert.deepEqual ( CHR.chrs_of '',                  'ncr'  ), []
assert.deepEqual ( CHR.chrs_of 'abc',               'ncr'  ), [ 'a', 'b', 'c' ]
assert.deepEqual ( CHR.chrs_of '𤕣abc',              'ncr'  ), [ '𤕣', 'a', 'b', 'c' ]
assert.deepEqual ( CHR.chrs_of '𤕣ab𤕣c',             'ncr'  ), [ '𤕣', 'a', 'b', '𤕣', 'c' ]
assert.deepEqual ( CHR.chrs_of '𤕣a&#123;b𤕣c',       'ncr'  ), [ '𤕣', 'a', '&#123;', 'b', '𤕣', 'c' ]
assert.deepEqual ( CHR.chrs_of '𤕣a&#x123ab;b𤕣c',    'ncr'  ), [ '𤕣', 'a', '&#x123ab;', 'b', '𤕣', 'c' ]
assert.deepEqual ( CHR.chrs_of '𤕣a&jzr#x123ab;b𤕣c', 'ncr'  ), [ '𤕣', 'a', '&', 'j', 'z', 'r', '#', 'x', '1', '2', '3', 'a', 'b', ';', 'b', '𤕣', 'c' ]
assert.deepEqual ( CHR.chrs_of '',                  'xncr' ), []
assert.deepEqual ( CHR.chrs_of 'abc',               'xncr' ), [ 'a', 'b', 'c' ]
assert.deepEqual ( CHR.chrs_of '𤕣abc',              'xncr' ), [ '𤕣', 'a', 'b', 'c' ]
assert.deepEqual ( CHR.chrs_of '𤕣ab𤕣c',             'xncr' ), [ '𤕣', 'a', 'b', '𤕣', 'c' ]
assert.deepEqual ( CHR.chrs_of '𤕣a&#123;b𤕣c',       'xncr' ), [ '𤕣', 'a', '&#123;', 'b', '𤕣', 'c' ]
assert.deepEqual ( CHR.chrs_of '𤕣a&#x123ab;b𤕣c',    'xncr' ), [ '𤕣', 'a', '&#x123ab;', 'b', '𤕣', 'c' ]
assert.deepEqual ( CHR.chrs_of '𤕣a&jzr#x123ab;b𤕣c', 'xncr' ), [ '𤕣', 'a', '&jzr#x123ab;', 'b', '𤕣', 'c' ]


#===========================================================================================================
# OBTAINING CIDS
#-----------------------------------------------------------------------------------------------------------
assert.throws ( -> CHR.cid_from_chr '' ), /^Error: unable to obtain CID from empty string$/
assert.throws ( -> CHR.cid_from_chr '', 'ncr' ), /^Error: unable to obtain CID from empty string$/
assert.throws ( -> CHR.cid_from_chr '', 'xncr' ), /^Error: unable to obtain CID from empty string$/
assert.strictEqual ( CHR.cid_from_chr 'a'                 ), 97
assert.strictEqual ( CHR.cid_from_chr 'x'                 ), 120
assert.strictEqual ( CHR.cid_from_chr '&#678;'            ), 38
assert.strictEqual ( CHR.cid_from_chr '&#x678;'           ), 38
assert.strictEqual ( CHR.cid_from_chr '&jzr#678;'         ), 38
assert.strictEqual ( CHR.cid_from_chr '&jzr#x678;'        ), 38
assert.strictEqual ( CHR.cid_from_chr 'a',          'ncr', ), 97
assert.strictEqual ( CHR.cid_from_chr 'x',          'ncr', ), 120
assert.strictEqual ( CHR.cid_from_chr '&#678;',     'ncr', ), 678
assert.strictEqual ( CHR.cid_from_chr '&#x678;',    'ncr', ), 0x678
assert.strictEqual ( CHR.cid_from_chr '&jzr#678;',  'ncr', ), 38
assert.strictEqual ( CHR.cid_from_chr '&jzr#x678;', 'ncr', ), 38
assert.strictEqual ( CHR.cid_from_chr 'a',          'xncr', ), 97
assert.strictEqual ( CHR.cid_from_chr 'x',          'xncr', ), 120
assert.strictEqual ( CHR.cid_from_chr '&#678;',     'xncr', ), 678
assert.strictEqual ( CHR.cid_from_chr '&#x678;',    'xncr', ), 0x678
assert.strictEqual ( CHR.cid_from_chr '&jzr#678;',  'xncr', ), 678
assert.strictEqual ( CHR.cid_from_chr '&jzr#x678;', 'xncr', ), 0x678


# log '-------------------------------'
# log '𤕣a&#123;b𤕣c'.match /// ( #{@ncr_matcher.source} ) ///
# log '𤕣a&#123;b𤕣c'.split /// ( #{@ncr_matcher.source} ) ///
# log 'helo &#xabc1; world'.match /// ( #{@ncr_matcher.source} ) ///
# log 'helo &#xabc1; world'.split /// ( #{@ncr_matcher.source} ) ///

# f = ->
#   Table = require 'cli-table'
#   options =
#     head: [ 'name', 'text', 'match', ]
#     # colWidths: [ 50, 50, 50, ]
#     # chars:
#     #   'mid':        ''
#     #   'left-mid':   ''
#     #   'mid-mid':    ''
#     #   'right-mid':  ''
#   table = new Table options
#   texts = [
#     '&#xabc1;'
#     '&#1234;'
#     '&jzr#xabc1;'
#     '&jzr#1234;'
#     'helo &#xabc1; world'
#     'helo &#1234; world'
#     'helo &jzr#xabc1; world'
#     'helo &jzr#1234; world'
#     ]
#   matcher_names = [
#     'ncr_matcher'
#     'xncr_matcher'
#     'ncr_csg_cid_matcher'
#     'xncr_csg_cid_matcher' ]
#   for name in matcher_names
#     for text in texts
#       match = text.match @[ name ]
#       match = match[ ... ] if match?
#       match = rpr match
#       table.push [ name, text, match, ]
#   log table.toString()

# log @ncr_splitter.source



assert.strictEqual ( CHR._as_xncr 'u', 0x12abc     ), '&#x12abc;'
assert.strictEqual ( CHR._as_xncr 'u', 0x12abc   ), '&#x12abc;'
assert.strictEqual ( CHR._as_xncr 'jzr', 0x12abc ), '&jzr#x12abc;'
assert.strictEqual ( CHR._as_sfncr 'u', 0x12abc   ), 'u-12abc'
assert.strictEqual ( CHR._as_sfncr 'jzr', 0x12abc ), 'jzr-12abc'

assert.strictEqual ( CHR.as_ncr 0x12abc        ), '&#x12abc;'
assert.strictEqual ( CHR.as_sfncr 'a'      ), 'u-61'
assert.strictEqual ( CHR.as_rsg 'a'        ), 'u-latn'
assert.strictEqual ( CHR.as_rsg '𤕣'        ), 'u-cjk-xb'
assert.strictEqual ( CHR.as_range_name 'a' ), 'Basic Latin'
assert.strictEqual ( CHR.as_range_name '𤕣' ), 'CJK Unified Ideographs Extension B'

assert.strictEqual ( CHR.as_range_name '&#xe100;',     mode: 'plain' ), 'Basic Latin'
assert.strictEqual ( CHR.as_range_name '&jzr#xe100;',  mode: 'plain' ), 'Basic Latin'
assert.strictEqual ( CHR.as_rsg        '&#xe100;',     mode: 'plain' ), 'u-latn'
assert.strictEqual ( CHR.as_rsg        '&jzr#xe100;',  mode: 'plain' ), 'u-latn'

assert.strictEqual ( CHR.as_range_name '&#xe100;',     mode: 'ncr' ), 'Private Use Area'
assert.strictEqual ( CHR.as_range_name '&jzr#xe100;',  mode: 'ncr' ), 'Basic Latin'
assert.strictEqual ( CHR.as_rsg        '&#xe100;',     mode: 'ncr' ), 'u-pua'
assert.strictEqual ( CHR.as_rsg        '&jzr#xe100;',  mode: 'ncr' ), 'u-latn'

assert.strictEqual ( CHR.as_range_name '&#xe100;',     mode: 'xncr' ), 'Private Use Area'
assert.strictEqual ( CHR.as_range_name '&jzr#xe100;',  mode: 'xncr' ), 'Jizura Character Components'
assert.strictEqual ( CHR.as_rsg        '&#xe100;',     mode: 'xncr' ), 'u-pua'
assert.strictEqual ( CHR.as_rsg        '&jzr#xe100;',  mode: 'xncr' ), 'jzr-cc'

assert.throws ( -> CHR.as_rsg        '&unknown#xe100;',  mode: 'xncr' ), "Error: unknown CSG: 'unknown'"
assert.strictEqual ( CHR.as_rsg      '&jzr#xe100;',  mode:  'xncr', csg: 'u'   ), 'u-pua'
assert.strictEqual ( CHR.as_rsg      '&#xe100;',     mode:  'xncr', csg: 'u'   ), 'u-pua'
assert.strictEqual ( CHR.as_rsg      '&#xe100;',     mode:  'xncr', csg: 'jzr' ), 'jzr-cc'
assert.strictEqual ( CHR.as_rsg      '&#x1;',        mode:  'xncr', csg: 'jzr' ), null
assert.strictEqual ( CHR.as_fncr     '&#x1;',        mode:  'xncr', csg: 'jzr' ), 'jzr-1'
assert.strictEqual ( CHR.as_fncr     '&#xe123;',     mode:  'xncr', csg: 'jzr' ), 'jzr-cc-e123'
assert.strictEqual ( CHR.as_fncr     '𤕣',           mode:  'xncr'             ), 'u-cjk-xb-24563'

assert.strictEqual ( CHR.as_cid      '&jzr#xe100;',  mode: 'xncr'              ), 0xe100
assert.strictEqual ( CHR.as_cid      '&jzr#xe100;',  mode:  'xncr', csg: 'u'   ), 0xe100
assert.strictEqual ( CHR.as_cid      '𤕣',           mode:  'xncr'              ), 0x24563

assert.strictEqual ( CHR.as_csg      '&jzr#xe100;',  mode: 'xncr'              ), 'jzr'
assert.strictEqual ( CHR.as_csg      '&jzr#xe100;',  mode:  'xncr', csg: 'u'   ), 'u'
assert.strictEqual ( CHR.as_csg      '𤕣',           mode:  'xncr'              ), 'u'

assert.deepEqual ( CHR.analyze 'helo world' ), {"chr":"h","csg":"u","cid":104,"fncr":"u-latn-68","sfncr":"u-68","ncr":"&#x68;","xncr":"&#x68;","rsg":"u-latn"}
assert.deepEqual ( CHR.analyze '&#x24563;'                   ), {"chr":"&","csg":"u","cid":38,"fncr":"u-latn-26","sfncr":"u-26","ncr":"&#x26;","xncr":"&#x26;","rsg":"u-latn"}
assert.deepEqual ( CHR.analyze '&#x24563;', mode: 'ncr'      ), {"chr":"𤕣","csg":"u","cid":148835,"fncr":"u-cjk-xb-24563","sfncr":"u-24563","ncr":"&#x24563;","xncr":"&#x24563;","rsg":"u-cjk-xb"}
assert.deepEqual ( CHR.analyze '&#x24563;', mode: 'xncr'     ), {"chr":"𤕣","csg":"u","cid":148835,"fncr":"u-cjk-xb-24563","sfncr":"u-24563","ncr":"&#x24563;","xncr":"&#x24563;","rsg":"u-cjk-xb"}
assert.deepEqual ( CHR.analyze '&jzr#x24563;'                ), {"chr":"&","csg":"u","cid":38,"fncr":"u-latn-26","sfncr":"u-26","ncr":"&#x26;","xncr":"&#x26;","rsg":"u-latn"}
assert.deepEqual ( CHR.analyze '&jzr#x24563;', mode: 'ncr'   ), {"chr":"&","csg":"u","cid":38,"fncr":"u-latn-26","sfncr":"u-26","ncr":"&#x26;","xncr":"&#x26;","rsg":"u-latn"}
assert.deepEqual ( CHR.analyze '&jzr#x24563;', mode: 'xncr'  ), {"chr":"&jzr#x24563;","csg":"jzr","cid":148835,"fncr":"jzr-24563","sfncr":"jzr-24563","ncr":"&#x24563;","xncr":"&jzr#x24563;","rsg":null}

log CHR.analyze 'helo world'
log CHR.analyze '&#x24563;'
log CHR.analyze '&#x24563;', mode: 'ncr'
log CHR.analyze '&#x24563;', mode: 'xncr'
log CHR.analyze '&jzr#x24563;'
log CHR.analyze '&jzr#x24563;', mode: 'ncr'
log CHR.analyze '&jzr#x24563;', mode: 'xncr'



# @time_it_2 = ->
#   binary_interval_search = require './binary-interval-search'
#   names_and_ranges = [
#     [ 'Basic Latin',                                             0x0000,   0x007f ]
#     [ 'Latin-1 Supplement',                                      0x0080,   0x00ff ]
#     [ 'Latin Extended-A',                                        0x0100,   0x017f ]
#     [ 'Latin Extended-B',                                        0x0180,   0x024f ]
#     [ 'New Tai Lue',                                             0x1980,   0x19df ]
#     [ 'Khmer Symbols',                                           0x19e0,   0x19ff ]
#     [ 'Buginese',                                                0x1a00,   0x1a1f ]
#     [ 'Tai Tham',                                                0x1a20,   0x1aaf ]
#     [ null,                                                     0x104af,  0x10800 ] # undefined CIDs
#     [ 'Miscellaneous Symbols And Pictographs',                  0x1f300,  0x1f5ff ]
#     [ 'Emoticons',                                              0x1f600,  0x1f64f ]
#     [ 'Transport And Map Symbols',                              0x1f680,  0x1f6ff ]
#     [ 'Alchemical Symbols',                                     0x1f700,  0x1f77f ]
#     [ 'Supplementary Private Use Area-A',                       0xf0000,  0xfffff ]
#     [ 'Supplementary Private Use Area-B',                      0x100000, 0x10ffff ]
#     [ null,                                                    0x10ffff, 0x110000 ] # undefined CIDs
#     ]
#   for name_and_range in names_and_ranges
#     [ name
#       first_cid
#       last_cid  ] = name_and_range
#     cid           = first_cid + parseInt ( last_cid - first_cid ) / 2 + 0.5
#     log()
#     # log '##############', first_cid, cid, last_cid
#     log rainbow name, ( '0x' + cid.toString 16 ), binary_interval_search @_names_and_ranges, 1, 2, 0, cid
#     # log binary_interval_search 0x2a000
#     # log binary_interval_search 0x61
#     # log binary_interval_search 0x8f
