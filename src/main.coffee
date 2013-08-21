



############################################################################################################
TYPES                     = require 'coffeenode-types'
TRM                       = require 'coffeenode-trm'
rpr                       = TRM.rpr.bind TRM
#...........................................................................................................
unicode_blocks_data       = require './unicode-blocks-data'
@_names_and_ranges_by_csg = unicode_blocks_data[ 'names-and-ranges-by-csg' ]
binary_interval_search    = require './binary-interval-search'



#===========================================================================================================
# SPLIT TEXT INTO CHARACTERS
#-----------------------------------------------------------------------------------------------------------
@chrs_of = ( text, options ) ->
  return [] if text.length is 0
  #.........................................................................................................
  switch mode = options?[ 'mode' ] ? 'plain'
    when 'plain'  then splitter = @_plain_splitter
    when 'ncr'    then splitter = @_ncr_splitter
    when 'xncr'   then splitter = @_xncr_splitter
    else throw new Error "unknown mode: #{rpr mode}"
  #.........................................................................................................
  return ( text.split splitter ).filter ( element, idx ) -> return element.length isnt 0


#===========================================================================================================
# CONVERTING TO CID
#-----------------------------------------------------------------------------------------------------------
@cid_from_chr = ( chr, options ) ->
  mode = options?[ 'mode' ] ? 'plain'
  return ( @_chr_csg_cid_from_chr chr, mode )[ 2 ]

#-----------------------------------------------------------------------------------------------------------
@csg_cid_from_chr = ( chr, options ) ->
  mode = options?[ 'mode' ] ? 'plain'
  return ( @_chr_csg_cid_from_chr chr, mode )[ 1 .. ]

#-----------------------------------------------------------------------------------------------------------
@_chr_csg_cid_from_chr = ( chr, mode ) ->
  ### Given a text with one or more characters, return the first character, its CSG, and its CID (as a
  non-negative integer). Additionally, a `mode` may be given as either `plain`, `ncr`, or `xncr`. In plain
  mode,
  ###
  #.........................................................................................................
  throw new Error "unable to obtain CID from empty string" if chr.length is 0
  #.........................................................................................................
  mode ?= 'plain'
  switch mode
    when 'plain'  then matcher = @_first_chr_matcher_plain
    when 'ncr'    then matcher = @_first_chr_matcher_ncr
    when 'xncr'   then matcher = @_first_chr_matcher_xncr
    else throw new Error "unknown mode: #{rpr mode}"
  #.........................................................................................................
  match     = chr.match matcher
  throw new Error "illegal character sequence in #{rpr chr}" unless match?
  first_chr = match[ 0 ]
  #.........................................................................................................
  switch first_chr.length
    #.......................................................................................................
    when 1
      return [ first_chr, 'u', first_chr.charCodeAt 0 ]
    #.......................................................................................................
    when 2
      ### thx to http://perldoc.perl.org/Encode/Unicode.html ###
      hi  = first_chr.charCodeAt 0
      lo  = first_chr.charCodeAt 1
      cid = ( hi - 0xD800 ) * 0x400 + ( lo - 0xDC00 ) + 0x10000
      return [ first_chr, 'u', cid ]
    #.......................................................................................................
    else
      [ chr
        csg
        cid_hex
        cid_dec ] = match
      cid = if cid_hex? then parseInt cid_hex, 16 else parseInt cid_dec, 10
      csg = 'u' if csg.length is 0
      return [ first_chr, csg, cid ]


# #-----------------------------------------------------------------------------------------------------------
# @cid_from_ncr = ( ) ->

# #-----------------------------------------------------------------------------------------------------------
# @cid_from_xncr = ( ) ->

# #-----------------------------------------------------------------------------------------------------------
# @cid_from_fncr = ( ) ->


#===========================================================================================================
# CONVERTING FROM CID &c
#-----------------------------------------------------------------------------------------------------------
@as_csg         = ( cid_hint, O ) -> return ( @_csg_cid_from_hint cid_hint, O )[ 0 ]
@as_cid         = ( cid_hint, O ) -> return ( @_csg_cid_from_hint cid_hint, O )[ 1 ]
#...........................................................................................................
@as_chr         = ( cid_hint, O ) -> return @_as_chr.apply        @, @_csg_cid_from_hint cid_hint, O
@as_fncr        = ( cid_hint, O ) -> return @_as_fncr.apply       @, @_csg_cid_from_hint cid_hint, O
@as_sfncr       = ( cid_hint, O ) -> return @_as_sfncr.apply      @, @_csg_cid_from_hint cid_hint, O
@as_xncr        = ( cid_hint, O ) -> return @_as_xncr.apply       @, @_csg_cid_from_hint cid_hint, O
@as_ncr         = ( cid_hint, O ) -> return @_as_xncr.apply       @, @_csg_cid_from_hint cid_hint, O
@as_rsg         = ( cid_hint, O ) -> return @_as_rsg.apply        @, @_csg_cid_from_hint cid_hint, O
@as_range_name  = ( cid_hint, O ) -> return @_as_range_name.apply @, @_csg_cid_from_hint cid_hint, O
#...........................................................................................................
@analyze        = ( cid_hint, O ) -> return @_analyze.apply       @, @_csg_cid_from_hint cid_hint, O

#-----------------------------------------------------------------------------------------------------------
@_analyze = ( csg, cid ) ->
  if csg is 'u'
    chr         = @_unicode_chr_from_cid cid
    ncr = xncr  = @_as_xncr csg, cid
  else
    chr         = @_as_xncr csg, cid
    xncr        = @_as_xncr csg, cid
    ncr         = @_as_xncr 'u', cid
  #.........................................................................................................
  R =
    'chr':      chr
    'csg':      csg
    'cid':      cid
    'fncr':     @_as_fncr  csg, cid
    'sfncr':    @_as_sfncr csg, cid
    'ncr':      ncr
    'xncr':     xncr
    'rsg':      @_as_rsg   csg, cid
  #.........................................................................................................
  return R

#-----------------------------------------------------------------------------------------------------------
@_unicode_chr_from_cid = ( cid ) ->
  return String.fromCharCode cid if cid <= 0xffff
  ### thx to http://perldoc.perl.org/Encode/Unicode.html ###
  hi = ( Math.floor ( cid - 0x10000 ) / 0x400 ) + 0xD800
  lo =              ( cid - 0x10000 ) % 0x400   + 0xDC00
  return ( String.fromCharCode hi ) + ( String.fromCharCode lo )

#-----------------------------------------------------------------------------------------------------------
@_as_fncr = ( csg, cid ) ->
  rsg = ( @_as_rsg csg, cid ) ? csg
  return "#{rsg}-#{cid.toString 16}"

#-----------------------------------------------------------------------------------------------------------
@_as_sfncr = ( csg, cid ) ->
  return "#{csg}-#{cid.toString 16}"

#-----------------------------------------------------------------------------------------------------------
@_as_xncr = ( csg, cid ) ->
  csg = '' if csg is 'u' or not csg?
  return "&#{csg}#x#{cid.toString 16};"

#-----------------------------------------------------------------------------------------------------------
@_as_rsg = ( csg, cid ) ->
  return binary_interval_search @_names_and_ranges_by_csg[ csg ], 'first-cid', 'last-cid', 'rsg', cid

#-----------------------------------------------------------------------------------------------------------
@_as_range_name = ( csg, cid ) ->
  return binary_interval_search @_names_and_ranges_by_csg[ csg ], 'first-cid', 'last-cid', 'range-name', cid


#===========================================================================================================
# ANALYZE ARGUMENTS
#-----------------------------------------------------------------------------------------------------------
@_csg_cid_from_hint = ( cid_hint, options ) ->
  ### This helper is used to derive the correct CSG and CID from arguments as accepted by the `as_*` family
  of methods, such as `CHR.as_fncr`, `CHR.as_rsg` and so on; its output may be directly applied to the
  respective namesake private method (`CHR._as_fncr`, `CHR._as_rsg` and so on). The method arguments should
  obey the following rules:

  * Methods may be called with one or two arguments; the first is known as the 'CID hint', the second as
    'options'.

  * The CID hint may be a number or a text; if it is a number, it is understood as a Unicode CID; if it
    is a text, its interpretation is subject to the `options[ 'mode' ]` setting.

  * Options must be a POD with the optional members `mode` and `csg`. `mode` is *only* observed if the CID
    hint is a text; otherwise, it is without effect. Otherwise, it may take the values of `plain`, `ncr`,
    or `xncr`, as for `CHR.cid_from_chr`.

  * If `csg` is set in the options, then it will override whatever the outcome of `CHR.csg_cid_from_chr`
    w.r.t. CSG is—in other words, if you call `CHR.as_sfncr '&jzr#xe100', mode: 'xncr', csg: 'u'`, you
    will get `u-e100`, with the numerically equivalent codepoint from another character set.

  * Before CSG and CID are returned, they will be validated for plausibility.

  Notice that some functions such as `CHR.as_rsg` may return

  ###
  #.........................................................................................................
  switch type = TYPES.type_of options
    when 'null', 'jsundefined'
      csg_of_options  = null
      mode            = null
    when 'pod'
      csg_of_options  = options[ 'csg' ]
      mode            = options[ 'mode' ]
    else
      throw new Error "expected a POD as second argument, got a #{type}"
  #.........................................................................................................
  switch type = TYPES.type_of cid_hint
    when 'number'
      csg_of_cid_hint = null
      cid             = cid_hint
    when 'text'
      [ csg_of_cid_hint
        cid             ] = @csg_cid_from_chr cid_hint, mode: mode
    else
      throw new Error "expected a text or a number as first argument, got a #{type}"
  #.........................................................................................................
  if csg_of_options?
    csg = csg_of_options
  else if csg_of_cid_hint?
    csg = csg_of_cid_hint
  else
    csg = 'u'
  #.........................................................................................................
  @validate_is_csg csg
  @validate_is_cid cid
  return [ csg, cid, ]


#===========================================================================================================
# PATTERNS
#-----------------------------------------------------------------------------------------------------------
# G: grouped
# O: optional
name                      = ( /// (?:     [a-z][a-z0-9]*     ) /// ).source
# nameG                     = ( /// (   (?: [a-z][a-z0-9]* ) | ) /// ).source
nameO                     = ( /// (?: (?: [a-z][a-z0-9]* ) | ) /// ).source
nameOG                    = ( /// (   (?: [a-z][a-z0-9]* ) | ) /// ).source
hex                       = ( /// (?: x   [a-fA-F0-9]+       ) /// ).source
hexG                      = ( /// (?: x  ([a-fA-F0-9]+)      ) /// ).source
dec                       = ( /// (?:     [      0-9]+       ) /// ).source
decG                      = ( /// (?:    ([      0-9]+)      ) /// ).source
#...........................................................................................................
@_csg_matcher             = /// ^ #{name} $ ///
@_ncr_matcher             = /// (?: &           \# (?: #{hex}  | #{dec}  ) ; ) ///
@_xncr_matcher            = /// (?: & #{nameO}  \# (?: #{hex}  | #{dec}  ) ; ) ///
@_ncr_csg_cid_matcher     = /// (?: & ()        \# (?: #{hexG} | #{decG} ) ; ) ///
@_xncr_csg_cid_matcher    = /// (?: & #{nameOG} \# (?: #{hexG} | #{decG} ) ; ) ///
#...........................................................................................................
### Matchers for surrogate sequences and non-surrogate, 'ordinary' characters: ###
@_surrogate_matcher       = /// (?: [  \ud800-\udbff ] [ \udc00-\udfff ] ) ///
@_nonsurrogate_matcher    = ///     [^ \ud800-\udbff     \udc00-\udfff ]   ///
#...........................................................................................................
### Matchers for the first character of a string, in three modes (`plain`, `ncr`, `xncr`): ###
@_first_chr_matcher_plain = /// ^ (?: #{@_surrogate_matcher.source}     |
                                      #{@_nonsurrogate_matcher.source}    ) ///
@_first_chr_matcher_ncr   = /// ^ (?: #{@_surrogate_matcher.source}     |
                                      #{@_ncr_csg_cid_matcher.source}   |
                                      #{@_nonsurrogate_matcher.source}    ) ///
@_first_chr_matcher_xncr  = /// ^ (?: #{@_surrogate_matcher.source}     |
                                      #{@_xncr_csg_cid_matcher.source}  |
                                      #{@_nonsurrogate_matcher.source}    ) ///
#...........................................................................................................
@_plain_splitter          = /// ( #{@_surrogate_matcher.source}     |
                                  #{@_nonsurrogate_matcher.source}    ) ///
@_ncr_splitter            = /// ( #{@_ncr_matcher.source}           |
                                  #{@_surrogate_matcher.source}     |
                                  #{@_nonsurrogate_matcher.source}    ) ///
@_xncr_splitter           = /// ( #{@_xncr_matcher.source}          |
                                  #{@_surrogate_matcher.source}     |
                                  #{@_nonsurrogate_matcher.source}    ) ///


#===========================================================================================================
# VALIDATION
#-----------------------------------------------------------------------------------------------------------
@validate_is_csg = ( x ) ->
  TYPES.validate_isa_text x
  throw new Error "not a valid CSG: #{rpr x}" unless ( x.match @_csg_matcher )?
  throw new Error "unknown CSG: #{rpr x}"     unless @_names_and_ranges_by_csg[ x ]?
  return null

#-----------------------------------------------------------------------------------------------------------
@validate_is_cid = ( x ) ->
  TYPES.validate_isa_number x
  throw new Error "expected a non-negative integer, got #{x}" if x < 0 or ( parseInt x ) != x
  return null






# console.log name for name of @
# console.log String.fromCharCode 0x61
# console.log String.fromCharCode 0x24563



