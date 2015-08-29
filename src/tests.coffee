
CND                       = require 'cnd'
rpr                       = CND.rpr
badge                     = 'CHR/tests'
debug                     = CND.get_logger 'debug',     badge
log                       = CND.log.bind CND
echo                      = CND.echo.bind CND
rainbow                   = CND.rainbow.bind CND
CHR                       = require './main'
test                      = require 'guy-test'





@[ 'test # 1' ] = ( T ) ->
  T.eq ( ( '&#123;helo'.match     CHR._first_chr_matcher_ncr )[ 1 .. 3 ] ), [ '', undefined, '123' ]

@[ 'test # 2' ] = ( T ) ->
  T.eq ( ( '&#x123;helo'.match    CHR._first_chr_matcher_ncr )[ 1 .. 3 ] ), [ '', '123', undefined ]

@[ 'test # 3' ] = ( T ) ->
  T.eq ( ( '&#x123;helo'.match    CHR._first_chr_matcher_xncr )[ 1 .. 3 ] ),[ '', '123', undefined ]

@[ 'test # 4' ] = ( T ) ->
  T.eq ( ( '&jzr#123;helo'.match  CHR._first_chr_matcher_xncr )[ 1 .. 3 ] ),[ 'jzr', undefined, '123' ]

@[ 'test # 5' ] = ( T ) ->
  T.eq ( ( '&jzr#x123;helo'.match CHR._first_chr_matcher_xncr )[ 1 .. 3 ] ),[ 'jzr', '123', undefined ]

@[ 'test # 6' ] = ( T ) ->
  T.eq ( ( '𤕣'[ 0 ] + 'x' ).match CHR._first_chr_matcher_plain ), null

@[ 'test # 7' ] = ( T ) ->
  T.eq ( CHR._chr_csg_cid_from_chr '&#97;abc', 'ncr' ),                    [ '&#97;', 'u', 97 ]

@[ 'test # 8' ] = ( T ) ->
  T.eq ( CHR._chr_csg_cid_from_chr '&#97;abc', 'plain' ),                  [ '&', 'u', 38 ]

@[ 'test # 9' ] = ( T ) ->
  T.eq ( CHR._chr_csg_cid_from_chr '&#97;abc', 'xncr' ),                   [ '&#97;', 'u', 97 ]

@[ 'test # 10' ] = ( T ) ->
  T.eq ( CHR._chr_csg_cid_from_chr '&#x61;abc' ),                          [ '&', 'u', 38 ]

@[ 'test # 11' ] = ( T ) ->
  T.eq ( CHR._chr_csg_cid_from_chr '&#x61;abc', 'ncr' ),                   [ '&#x61;', 'u', 97 ]

@[ 'test # 12' ] = ( T ) ->
  T.eq ( CHR._chr_csg_cid_from_chr '&#x61;abc', 'plain' ),                 [ '&', 'u', 38 ]

@[ 'test # 13' ] = ( T ) ->
  T.eq ( CHR._chr_csg_cid_from_chr '&#x61;abc', 'xncr' ),                  [ '&#x61;', 'u', 97 ]

@[ 'test # 14' ] = ( T ) ->
  T.eq ( CHR._chr_csg_cid_from_chr 'abc', 'ncr' ),                         [ 'a', 'u', 97 ]

@[ 'test # 15' ] = ( T ) ->
  T.eq ( CHR._chr_csg_cid_from_chr 'abc', 'plain' ),                       [ 'a', 'u', 97 ]

@[ 'test # 16' ] = ( T ) ->
  T.eq ( CHR._chr_csg_cid_from_chr 'abc', 'xncr' ),                        [ 'a', 'u', 97 ]

@[ 'test # 17' ] = ( T ) ->
  T.eq ( CHR.analyze '&#x24563;'                   ), {'~isa':     'CHR/info',"uchr":"&","chr":"&","csg":"u","cid":38,"fncr":"u-latn-26","sfncr":"u-26","ncr":"&#x26;","xncr":"&#x26;","rsg":"u-latn"}

@[ 'test # 18' ] = ( T ) ->
  T.eq ( CHR.analyze '&#x24563;', input: 'ncr'      ), {'~isa':     'CHR/info',"uchr":"𤕣","chr":"𤕣","csg":"u","cid":148835,"fncr":"u-cjk-xb-24563","sfncr":"u-24563","ncr":"&#x24563;","xncr":"&#x24563;","rsg":"u-cjk-xb"}

@[ 'test # 19' ] = ( T ) ->
  T.eq ( CHR.analyze '&#x24563;', input: 'xncr'     ), {'~isa':     'CHR/info',"uchr":"𤕣","chr":"𤕣","csg":"u","cid":148835,"fncr":"u-cjk-xb-24563","sfncr":"u-24563","ncr":"&#x24563;","xncr":"&#x24563;","rsg":"u-cjk-xb"}

@[ 'test # 20' ] = ( T ) ->
  T.eq ( CHR.analyze '&jzr#x24563;'                ), {'~isa':     'CHR/info',"uchr":"&","chr":"&","csg":"u","cid":38,"fncr":"u-latn-26","sfncr":"u-26","ncr":"&#x26;","xncr":"&#x26;","rsg":"u-latn"}

@[ 'test # 21' ] = ( T ) ->
  T.eq ( CHR.analyze '&jzr#x24563;', input: 'ncr'   ), {'~isa':     'CHR/info',"uchr":"&","chr":"&","csg":"u","cid":38,"fncr":"u-latn-26","sfncr":"u-26","ncr":"&#x26;","xncr":"&#x26;","rsg":"u-latn"}

@[ 'test # 22' ] = ( T ) ->
  # debug '©BY7x6', JSON.stringify ( CHR.analyze '&jzr#x24563;', input: 'xncr'  )
  T.eq ( CHR.analyze '&jzr#x24563;', input: 'xncr'  ), {'~isa':     'CHR/info',"uchr":"𤕣","chr":"&jzr#x24563;","csg":"jzr","cid":148835,"fncr":"jzr-24563","sfncr":"jzr-24563","ncr":"&#x24563;","xncr":"&jzr#x24563;","rsg":null}

@[ 'test # 22a' ] = ( T ) ->
  debug '©BY7x6', JSON.stringify ( CHR.analyze '&jzr#xe101;', input: 'xncr'  )
  T.eq ( CHR.analyze '&jzr#xe101;', input: 'xncr'  ), {"~isa":"CHR/info","chr":"&jzr#xe101;","uchr":"","csg":"jzr","cid":57601,"fncr":"jzr-fig-e101","sfncr":"jzr-e101","ncr":"&#xe101;","xncr":"&jzr#xe101;","rsg":"jzr-fig"}

@[ 'test # 22b' ] = ( T ) ->
  T.eq ( CHR.analyze '&jzr#e101;', input: 'xncr'  ), {"~isa":"CHR/info","chr":"&","uchr":"&","csg":"u","cid":38,"fncr":"u-latn-26","sfncr":"u-26","ncr":"&#x26;","xncr":"&#x26;","rsg":"u-latn"}

@[ 'test # 23' ] = ( T ) ->
  T.eq ( CHR.analyze 'helo world' ), {'~isa':     'CHR/info',"uchr":"h","chr":"h","csg":"u","cid":104,"fncr":"u-latn-68","sfncr":"u-68","ncr":"&#x68;","xncr":"&#x68;","rsg":"u-latn"}

@[ 'test # 24' ] = ( T ) ->
  T.eq ( CHR.chrs_from_text ''                   ), []

@[ 'test # 25' ] = ( T ) ->
  T.eq ( CHR.chrs_from_text '',                  input: 'ncr'  ), []

@[ 'test # 26' ] = ( T ) ->
  T.eq ( CHR.chrs_from_text '',                  input: 'xncr' ), []

@[ 'test # 27' ] = ( T ) ->
  T.eq ( CHR.chrs_from_text 'abc'                ), [ 'a', 'b', 'c' ]

@[ 'test # 28' ] = ( T ) ->
  T.eq ( CHR.chrs_from_text 'abc',               input: 'ncr'  ), [ 'a', 'b', 'c' ]

@[ 'test # 29' ] = ( T ) ->
  T.eq ( CHR.chrs_from_text 'abc',               input: 'xncr' ), [ 'a', 'b', 'c' ]

@[ 'test # 30' ] = ( T ) ->
  T.eq ( CHR.chrs_from_text '𤕣a&#123;b𤕣c'        ), [ '𤕣', 'a', '&', '#', '1', '2', '3', ';', 'b', '𤕣', 'c' ]

@[ 'test # 31' ] = ( T ) ->
  T.eq ( CHR.chrs_from_text '𤕣a&#123;b𤕣c',       input: 'ncr'  ), [ '𤕣', 'a', '&#123;', 'b', '𤕣', 'c' ]

@[ 'test # 32' ] = ( T ) ->
  T.eq ( CHR.chrs_from_text '𤕣a&#123;b𤕣c',       input: 'xncr' ), [ '𤕣', 'a', '&#123;', 'b', '𤕣', 'c' ]

@[ 'test # 33' ] = ( T ) ->
  T.eq ( CHR.chrs_from_text '𤕣a&#x123ab;b𤕣c'     ), [ '𤕣', 'a', '&', '#', 'x', '1', '2', '3', 'a', 'b', ';', 'b', '𤕣', 'c' ]

@[ 'test # 34' ] = ( T ) ->
  T.eq ( CHR.chrs_from_text '𤕣a&#x123ab;b𤕣c',    input: 'ncr'  ), [ '𤕣', 'a', '&#x123ab;', 'b', '𤕣', 'c' ]

@[ 'test # 35' ] = ( T ) ->
  T.eq ( CHR.chrs_from_text '𤕣a&#x123ab;b𤕣c',    input: 'xncr' ), [ '𤕣', 'a', '&#x123ab;', 'b', '𤕣', 'c' ]

@[ 'test # 36' ] = ( T ) ->
  T.eq ( CHR.chrs_from_text '𤕣a&jzr#123;b𤕣c'     ), [ '𤕣', 'a', '&', 'j', 'z', 'r', '#', '1', '2', '3', ';', 'b', '𤕣', 'c' ]

@[ 'test # 37' ] = ( T ) ->
  T.eq ( CHR.chrs_from_text '𤕣a&jzr#x123ab;b𤕣c'  ), [ '𤕣', 'a', '&', 'j', 'z', 'r', '#', 'x', '1', '2', '3', 'a', 'b', ';', 'b', '𤕣', 'c' ]

@[ 'test # 38' ] = ( T ) ->
  T.eq ( CHR.chrs_from_text '𤕣a&jzr#x123ab;b𤕣c', input: 'ncr'  ), [ '𤕣', 'a', '&', 'j', 'z', 'r', '#', 'x', '1', '2', '3', 'a', 'b', ';', 'b', '𤕣', 'c' ]

@[ 'test # 39' ] = ( T ) ->
  T.eq ( CHR.chrs_from_text '𤕣a&jzr#x123ab;b𤕣c', input: 'xncr' ), [ '𤕣', 'a', '&jzr#x123ab;', 'b', '𤕣', 'c' ]

@[ 'test # 40' ] = ( T ) ->
  T.eq ( CHR.chrs_from_text '𤕣abc'               ), [ '𤕣', 'a', 'b', 'c' ]

@[ 'test # 41' ] = ( T ) ->
  T.eq ( CHR.chrs_from_text '𤕣abc',              input: 'ncr'  ), [ '𤕣', 'a', 'b', 'c' ]

@[ 'test # 42' ] = ( T ) ->
  T.eq ( CHR.chrs_from_text '𤕣abc',              input: 'xncr' ), [ '𤕣', 'a', 'b', 'c' ]

@[ 'test # 43' ] = ( T ) ->
  T.eq ( CHR.chrs_from_text '𤕣ab𤕣c'              ), [ '𤕣', 'a', 'b', '𤕣', 'c' ]

@[ 'test # 44' ] = ( T ) ->
  T.eq ( CHR.chrs_from_text '𤕣ab𤕣c',             input: 'ncr'  ), [ '𤕣', 'a', 'b', '𤕣', 'c' ]

@[ 'test # 45' ] = ( T ) ->
  T.eq ( CHR.chrs_from_text '𤕣ab𤕣c',             input: 'xncr' ), [ '𤕣', 'a', 'b', '𤕣', 'c' ]

@[ 'test # 46' ] = ( T ) ->
  T.eq ( CHR.chunks_from_text '1 < 2', output: 'html'                          ), [{"~isa":"CHR/chunk","csg":"u","rsg":"u-latn","text":"1 &lt; 2"}]

@[ 'test # 47' ] = ( T ) ->
  T.eq ( CHR.chunks_from_text '2 > 1', output: 'html'                          ), [{"~isa":"CHR/chunk","csg":"u","rsg":"u-latn","text":"2 &gt; 1"}]

@[ 'test # 48' ] = ( T ) ->
  T.eq ( CHR.chunks_from_text 'ab&#x63;d'                                      ), [{"~isa":"CHR/chunk","csg":"u","rsg":"u-latn","text":"ab&#x63;d"}]

@[ 'test # 49' ] = ( T ) ->
  T.eq ( CHR.chunks_from_text 'ab&#x63;d', input: 'ncr'                        ), [{"~isa":"CHR/chunk","csg":"u","rsg":"u-latn","text":"abcd"}]

@[ 'test # 50' ] = ( T ) ->
  T.eq ( CHR.chunks_from_text 'ab&#x63;d', input: 'xncr'                       ), [{"~isa":"CHR/chunk","csg":"u","rsg":"u-latn","text":"abcd"}]

@[ 'test # 51' ] = ( T ) ->
  T.eq ( CHR.chunks_from_text 'ab&jzr#xe063;d'                                 ), [{"~isa":"CHR/chunk","csg":"u","rsg":"u-latn","text":"ab&jzr#xe063;d"}]

@[ 'test # 52' ] = ( T ) ->
  T.eq ( CHR.chunks_from_text 'ab&jzr#xe063;d', input: 'ncr'                   ), [{"~isa":"CHR/chunk","csg":"u","rsg":"u-latn","text":"ab&jzr#xe063;d"}]

@[ 'test # 53' ] = ( T ) ->
  T.eq ( CHR.chunks_from_text 'ab&jzr#xe063;d', input: 'xncr'                  ), [{"~isa":"CHR/chunk","csg":"u","rsg":"u-latn","text":"ab"},{"~isa":"CHR/chunk","csg":"jzr","rsg":"jzr-fig","text":"&#xe063;"},{"~isa":"CHR/chunk","csg":"u","rsg":"u-latn","text":"d"}]

@[ 'test # 54' ] = ( T ) ->
  T.eq ( CHR.chunks_from_text 'ab&jzr#xe063;d', input: 'xncr', output: 'html'  ), [{"~isa":"CHR/chunk","csg":"u","rsg":"u-latn","text":"ab"},{"~isa":"CHR/chunk","csg":"jzr","rsg":"jzr-fig","text":"&#xe063;"},{"~isa":"CHR/chunk","csg":"u","rsg":"u-latn","text":"d"}]

@[ 'test # 55' ] = ( T ) ->
  T.eq ( CHR.chunks_from_text 'helo wörld'                                     ), [{"~isa":"CHR/chunk","csg":"u","rsg":"u-latn","text":"helo w"},{"~isa":"CHR/chunk","csg":"u","rsg":"u-latn-1","text":"ö"},{"~isa":"CHR/chunk","csg":"u","rsg":"u-latn","text":"rld"}]

@[ 'test # 56' ] = ( T ) ->
  T.eq ( CHR.chunks_from_text 'helo wörld', output: 'html'                     ), [{"~isa":"CHR/chunk","csg":"u","rsg":"u-latn","text":"helo w"},{"~isa":"CHR/chunk","csg":"u","rsg":"u-latn-1","text":"ö"},{"~isa":"CHR/chunk","csg":"u","rsg":"u-latn","text":"rld"}]

@[ 'test # 57' ] = ( T ) ->
  T.eq ( CHR.chunks_from_text 'me & you', output: 'html'                       ), [{"~isa":"CHR/chunk","csg":"u","rsg":"u-latn","text":"me &amp; you"}]

@[ 'test # 58' ] = ( T ) ->
  T.eq ( CHR.chunks_from_text 'me &amp; you', output: 'html'                   ), [{"~isa":"CHR/chunk","csg":"u","rsg":"u-latn","text":"me &amp;amp; you"}]

@[ 'test # 59' ] = ( T ) ->
  T.eq ( CHR.chunks_from_text '種果〇𤕣カタカナ'                                       ), [{"~isa":"CHR/chunk","csg":"u","rsg":"u-cjk","text":"種果"},{"~isa":"CHR/chunk","csg":"u","rsg":"u-cjk-sym","text":"〇"},{"~isa":"CHR/chunk","csg":"u","rsg":"u-cjk-xb","text":"𤕣"},{"~isa":"CHR/chunk","csg":"u","rsg":"u-cjk-kata","text":"カタカナ"}]

@[ 'test # 60' ] = ( T ) ->
  T.eq ( CHR.csg_cid_from_chr '&#x24563;' ),                               [ 'u', 38 ]

@[ 'test # 61' ] = ( T ) ->
  T.eq ( CHR.csg_cid_from_chr '&#x24563;', input: 'ncr' ),                        [ 'u', 148835 ]

@[ 'test # 62' ] = ( T ) ->
  T.eq ( CHR.csg_cid_from_chr '&#x24563;', input: 'plain' ),                      [ 'u', 38 ]

@[ 'test # 63' ] = ( T ) ->
  T.eq ( CHR.csg_cid_from_chr '&#x24563;', input: 'xncr' ),                       [ 'u', 148835 ]

@[ 'test # 64' ] = ( T ) ->
  T.eq ( CHR.csg_cid_from_chr '𤕣' ),                                       [ 'u', 148835 ]

@[ 'test # 65' ] = ( T ) ->
  T.eq ( CHR.csg_cid_from_chr '𤕣', input: 'ncr' ),                                [ 'u', 148835 ]

@[ 'test # 66' ] = ( T ) ->
  T.eq ( CHR.csg_cid_from_chr '𤕣', input: 'plain' ),                              [ 'u', 148835 ]

@[ 'test # 67' ] = ( T ) ->
  T.eq ( CHR.csg_cid_from_chr '𤕣', input: 'xncr' ),                               [ 'u', 148835 ]

@[ 'test # 68' ] = ( T ) ->
  T.eq ( CHR._as_sfncr 'jzr', 0x12abc ), 'jzr-12abc'

@[ 'test # 69' ] = ( T ) ->
  T.eq ( CHR._as_sfncr 'u', 0x12abc   ), 'u-12abc'

@[ 'test # 70' ] = ( T ) ->
  T.eq ( CHR._as_xncr 'jzr', 0x12abc ), '&jzr#x12abc;'

@[ 'test # 71' ] = ( T ) ->
  T.eq ( CHR._as_xncr 'u', 0x12abc     ), '&#x12abc;'

@[ 'test # 72' ] = ( T ) ->
  T.eq ( CHR._as_xncr 'u', 0x12abc   ), '&#x12abc;'

@[ 'test # 73' ] = ( T ) ->
  T.eq ( CHR.as_cid      '&jzr#xe100;',  input:  'xncr', csg: 'u'   ), 0xe100

@[ 'test # 74' ] = ( T ) ->
  T.eq ( CHR.as_cid      '&jzr#xe100;',  input: 'xncr'              ), 0xe100

@[ 'test # 75' ] = ( T ) ->
  T.eq ( CHR.as_cid      '𤕣',           input:  'xncr'              ), 0x24563

@[ 'test # 76' ] = ( T ) ->
  T.eq ( CHR.as_csg      '&jzr#xe100;',  input:  'xncr', csg: 'u'   ), 'u'

@[ 'test # 77' ] = ( T ) ->
  T.eq ( CHR.as_csg      '&jzr#xe100;',  input: 'xncr'              ), 'jzr'

@[ 'test # 78' ] = ( T ) ->
  T.eq ( CHR.as_csg      '𤕣',           input:  'xncr'              ), 'u'

@[ 'test # 79' ] = ( T ) ->
  T.eq ( CHR.as_fncr     '&#x1;',        input:  'xncr', csg: 'jzr' ), 'jzr-1'

@[ 'test # 80' ] = ( T ) ->
  T.eq ( CHR.as_fncr     '&#xe123;',     input:  'xncr', csg: 'jzr' ), 'jzr-fig-e123'

@[ 'test # 81' ] = ( T ) ->
  T.eq ( CHR.as_fncr     '𤕣',           input:  'xncr'             ), 'u-cjk-xb-24563'

@[ 'test # 82' ] = ( T ) ->
  T.eq ( CHR.as_ncr 0x12abc        ), '&#x12abc;'

@[ 'test # 83' ] = ( T ) ->
  T.eq ( CHR.as_range_name '&#xe100;',     input: 'ncr' ), 'Private Use Area'

@[ 'test # 84' ] = ( T ) ->
  T.eq ( CHR.as_range_name '&#xe100;',     input: 'plain' ), 'Basic Latin'

@[ 'test # 85' ] = ( T ) ->
  T.eq ( CHR.as_range_name '&#xe100;',     input: 'xncr' ), 'Private Use Area'

@[ 'test # 86' ] = ( T ) ->
  T.eq ( CHR.as_range_name '&jzr#xe100;',  input: 'ncr' ), 'Basic Latin'

@[ 'test # 87' ] = ( T ) ->
  T.eq ( CHR.as_range_name '&jzr#xe100;',  input: 'plain' ), 'Basic Latin'

@[ 'test # 88' ] = ( T ) ->
  T.eq ( CHR.as_range_name '&jzr#xe100;',  input: 'xncr' ), 'Jizura Character Components'

@[ 'test # 89' ] = ( T ) ->
  T.eq ( CHR.as_range_name 'a' ), 'Basic Latin'

@[ 'test # 90' ] = ( T ) ->
  T.eq ( CHR.as_range_name '𤕣' ), 'CJK Unified Ideographs Extension B'

@[ 'test # 91' ] = ( T ) ->
  T.eq ( CHR.as_rsg        '&#xe100;',     input: 'ncr' ), 'u-pua'

@[ 'test # 92' ] = ( T ) ->
  T.eq ( CHR.as_rsg        '&#xe100;',     input: 'plain' ), 'u-latn'

@[ 'test # 93' ] = ( T ) ->
  T.eq ( CHR.as_rsg        '&#xe100;',     input: 'xncr' ), 'u-pua'

@[ 'test # 94' ] = ( T ) ->
  T.eq ( CHR.as_rsg        '&jzr#xe100;',  input: 'ncr' ), 'u-latn'

@[ 'test # 95' ] = ( T ) ->
  T.eq ( CHR.as_rsg        '&jzr#xe100;',  input: 'plain' ), 'u-latn'

@[ 'test # 96' ] = ( T ) ->
  T.eq ( CHR.as_rsg        '&jzr#xe100;',  input: 'xncr' ), 'jzr-fig'

@[ 'test # 97' ] = ( T ) ->
  T.eq ( CHR.as_rsg      '&#x1;',        input:  'xncr', csg: 'jzr' ), null

@[ 'test # 98' ] = ( T ) ->
  T.eq ( CHR.as_rsg      '&#xe100;',     input:  'xncr', csg: 'jzr' ), 'jzr-fig'

@[ 'test # 99' ] = ( T ) ->
  T.eq ( CHR.as_rsg      '&#xe100;',     input:  'xncr', csg: 'u'   ), 'u-pua'

@[ 'test # 100' ] = ( T ) ->
  T.eq ( CHR.as_rsg      '&jzr#xe100;',  input:  'xncr', csg: 'u'   ), 'u-pua'

@[ 'test # 101' ] = ( T ) ->
  T.eq ( CHR.as_rsg 'a'        ), 'u-latn'

@[ 'test # 102' ] = ( T ) ->
  T.eq ( CHR.as_rsg '𤕣'        ), 'u-cjk-xb'

@[ 'test # 103' ] = ( T ) ->
  T.eq ( CHR.as_sfncr 'a'      ), 'u-61'

@[ 'test # 104' ] = ( T ) ->
  T.eq ( CHR.cid_from_chr '&#678;'            ), 38

@[ 'test # 105' ] = ( T ) ->
  T.eq ( CHR.cid_from_chr '&#678;',     input: 'ncr', ), 678

@[ 'test # 106' ] = ( T ) ->
  T.eq ( CHR.cid_from_chr '&#678;',     input: 'xncr', ), 678

@[ 'test # 107' ] = ( T ) ->
  T.eq ( CHR.cid_from_chr '&#x678;'           ), 38

@[ 'test # 108' ] = ( T ) ->
  T.eq ( CHR.cid_from_chr '&#x678;',    input: 'ncr', ), 0x678

@[ 'test # 109' ] = ( T ) ->
  T.eq ( CHR.cid_from_chr '&#x678;',    input: 'xncr', ), 0x678

@[ 'test # 110' ] = ( T ) ->
  T.eq ( CHR.cid_from_chr '&jzr#678;'         ), 38

@[ 'test # 111' ] = ( T ) ->
  T.eq ( CHR.cid_from_chr '&jzr#678;',  input: 'ncr', ), 38

@[ 'test # 112' ] = ( T ) ->
  T.eq ( CHR.cid_from_chr '&jzr#678;',  input: 'xncr', ), 678

@[ 'test # 113' ] = ( T ) ->
  T.eq ( CHR.cid_from_chr '&jzr#x678;'        ), 38

@[ 'test # 114' ] = ( T ) ->
  T.eq ( CHR.cid_from_chr '&jzr#x678;', input: 'ncr', ), 38

@[ 'test # 115' ] = ( T ) ->
  T.eq ( CHR.cid_from_chr '&jzr#x678;', input: 'xncr', ), 0x678

@[ 'test # 116' ] = ( T ) ->
  T.eq ( CHR.cid_from_chr 'a'                 ), 97

@[ 'test # 117' ] = ( T ) ->
  T.eq ( CHR.cid_from_chr 'a',          input: 'ncr', ), 97

@[ 'test # 118' ] = ( T ) ->
  T.eq ( CHR.cid_from_chr 'a',          input: 'xncr', ), 97

@[ 'test # 119' ] = ( T ) ->
  T.eq ( CHR.cid_from_chr 'x'                 ), 120

@[ 'test # 120' ] = ( T ) ->
  T.eq ( CHR.cid_from_chr 'x',          input: 'ncr', ), 120

@[ 'test # 121' ] = ( T ) ->
  T.eq ( CHR.cid_from_chr 'x',          input: 'xncr', ), 120

@[ 'test # 122' ] = ( T ) ->
  T.eq ( CHR.html_from_text '&jzr#xe101; & you', input: 'xncr'   ), """<span class="jzr-fig">&#xe101;</span><span class="u-latn"> &amp; you</span>"""

@[ 'test # 123' ] = ( T ) ->
  T.eq ( CHR.html_from_text 'helo &#x24563; wörld'               ), """<span class="u-latn">helo &amp;#x24563; w</span><span class="u-latn-1">ö</span><span class="u-latn">rld</span>"""

@[ 'test # 124' ] = ( T ) ->
  T.eq ( CHR.html_from_text 'helo &#x24563; wörld', input: 'xncr'), """<span class="u-latn">helo </span><span class="u-cjk-xb">𤕣</span><span class="u-latn"> w</span><span class="u-latn-1">ö</span><span class="u-latn">rld</span>"""

@[ 'test # 125' ] = ( T ) ->
  T.eq ( CHR.html_from_text 'helo wörld'                         ), """<span class="u-latn">helo w</span><span class="u-latn-1">ö</span><span class="u-latn">rld</span>"""

# assert.throws ( -> CHR._chr_csg_cid_from_chr '𤕣'[ 0 ] ),        /^Error: illegal character sequence/
# assert.throws ( -> CHR._chr_csg_cid_from_chr '𤕣'[ 0 ] + 'x' ),  /^Error: illegal character sequence/
# assert.throws ( -> CHR.as_rsg        '&unknown#xe100;',  input: 'xncr' ), /Error: unknown CSG: 'unknown'/
# assert.throws ( -> CHR.chrs_from_text 'x', input: 'xxx' ),  /^Error: unknown input mode: /
# assert.throws ( -> CHR.chunks_from_text 'ab&jzr#xe063;d', input: 'xncr', output: 'xxx' ), /Error: unknown output mode: 'xxx'/
# assert.throws ( -> CHR.cid_from_chr '' ), /^Error: unable to obtain CID from empty string$/
# assert.throws ( -> CHR.cid_from_chr '', 'ncr' ), /^Error: unable to obtain CID from empty string$/
# assert.throws ( -> CHR.cid_from_chr '', 'xncr' ), /^Error: unable to obtain CID from empty string$/

unless module.parent?
  test @

