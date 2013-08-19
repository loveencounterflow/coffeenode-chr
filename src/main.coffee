



############################################################################################################
TRM                       = require 'coffeenode-trm'
rpr                       = TRM.rpr.bind TRM
#...........................................................................................................


#===========================================================================================================
# CONVERTING TO CID
#-----------------------------------------------------------------------------------------------------------
@cid_from_chr = ( chr, mode ) ->
  switch mode
    when 'plain'
      matcher = @first_chr_matcher
    when 'ncr'
      matcher = @first_chr_with_ncr_matcher
    when 'xncr'
      matcher = @first_chr_with_xncr_matcher
    else
      throw new Error "unknown mode: #{rpr mode}"
  #.........................................................................................................
  first_chr = ( match = chr.match matcher )[ 0 ]
  switch first_chr.length
    when 0
      throw new Error "unable to obtain CID from empty string"
    when 1
      return first_chr.charCodeAt 0
    when 2
      hi = first_chr.charCodeAt 0
      lo = first_chr.charCodeAt 1
      return ( hi - 0xD800 ) * 0x400 + ( lo - 0xDC00 ) + 0x10000
    else

#-----------------------------------------------------------------------------------------------------------
@cid_from_ncr = ( ) ->

#-----------------------------------------------------------------------------------------------------------
@cid_from_xncr = ( ) ->

#-----------------------------------------------------------------------------------------------------------
@cid_from_fncr = ( ) ->


#===========================================================================================================
# CONVERTING FROM CID
#-----------------------------------------------------------------------------------------------------------
@fncr_from_cid = ( ) ->

#-----------------------------------------------------------------------------------------------------------
@sfncr_from_cid = ( ) ->

#-----------------------------------------------------------------------------------------------------------
@ncr_from_cid = ( ) ->

#-----------------------------------------------------------------------------------------------------------
@rsg_from_cid = ( ) ->


#===========================================================================================================
# ANALYZE CHARACTER
#-----------------------------------------------------------------------------------------------------------
@analyze_chr = ( chr, mode ) ->
  cid = @cid_from_chr chr, mode
  #.........................................................................................................
  R =
    'chr':      chr
    'fncr':     @fncr_from_cid  cid
    'sfncr':    @sfncr_from_cid cid
    'ncr':      @ncr_from_cid   cid
    'rsg':      @rsg_from_cid   cid
  #.........................................................................................................
  return R


#===========================================================================================================
# SPLIT TEXT INTO CHARACTERS
#-----------------------------------------------------------------------------------------------------------
@chrs_from_text = ( text, mode ) ->



#===========================================================================================================
# PATTERNS
#-----------------------------------------------------------------------------------------------------------
@ncr_kernel_matcher          = /// &               \# (?:     x   [a-f0-9]+     |   [0-9]+   ) ; ///
@ncr_cid_matcher             = /// &               \# (?: (?: x ( [a-f0-9]+ ) ) | ( [0-9]+ ) ) ; ///
@ncr_splitter                = /// ( (?: #{@ncr_kernel_matcher.source} ) | (?: . ) ) ///
@first_chr_matcher           = /// ^   (?: [\ud800-\udbff] . ) | . ///
@first_chr_with_ncr_matcher  = /// ^ ( (?: [\ud800-\udbff] . )                   |
                                                (?: #{@ncr_cid_matcher.source} ) |
                                                (?: . )
                                                ) ///
#...........................................................................................................
@xncr_kernel_matcher         = /// &   [a-z0-9]*   \# (?:     x   [a-f0-9]+     |   [0-9]+   ) ; ///
@xncr_csg_cid_matcher        = /// & ( [a-z0-9]* ) \# (?: (?: x ( [a-f0-9]+ ) ) | ( [0-9]+ ) ) ; ///
@xncr_splitter               = /// ( (?: #{@xncr_kernel_matcher.source} ) | (?: . ) ) ///
@first_chr_with_xncr_matcher = /// ^ ( (?: [\ud800-\udbff] . )                 |
                                       (?: #{@xncr_csg_cid_matcher.source} )   |
                                       (?: . )
                                       ) ///






log                       = TRM.log.bind TRM
echo                      = TRM.echo.bind TRM
rainbow                   = TRM.rainbow.bind TRM

# log '&jzr#x123;helo'.match @xncr_kernel_matcher
# log '&jzr#x123;helo'.match @ncr_kernel_matcher
# log '&#x123;helo'.match @xncr_kernel_matcher
# log '&#x123;helo'.match @ncr_kernel_matcher
# log '&#x123;helo'.match @first_chr_with_ncr_matcher
# log '&#x123;helo'.match @first_chr_with_xncr_matcher
# log '&#x123;helo'.match @first_chr_matcher
# log '𤕣古文龜'.match @first_chr_matcher

log '&jzr#x123;helo'.match @first_chr_with_xncr_matcher
log '&#x123;helo'.match @first_chr_with_xncr_matcher


