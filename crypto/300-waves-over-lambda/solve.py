#!/usr/bin/env python
import string
from collections import Counter


capture = '''
-------------------------------------------------------------------------------
psqtagxi ylal ui csra wogt - walhrlqpc_ui_p_svla_ogjfeg_gtmqyucsjo
-------------------------------------------------------------------------------
flxmllq ri xylal mgi, gi u ygvl goalgec igue isjlmylal, xyl fsqe sw xyl ilg. fliueli ysoeuqt sra ylgaxi xstlxyla xyasrty osqt blausei sw ilbgagxusq, ux yge xyl lwwlpx sw jgnuqt ri xsolagqx sw lgpy sxyla'i cgaqigqe lvlq psqvupxusqi. xyl ogmclaxyl flix sw soe wloosmiyge, flpgril sw yui jgqc clgai gqe jgqc vuaxrli, xyl sqoc priyusq sq elpn, gqe mgi ocuqt sq xyl sqoc art. xyl gppsrqxgqx yge fasrtyx srx goalgec g fsd sw esjuqsli, gqe mgi xscuqt gapyuxlpxragooc muxy xyl fsqli. jgaosm igx pasii-olttle autyx gwx, olgquqt gtguqix xyl jukklq-jgix. yl yge irqnlq pyllni, g cloosm psjboldusq, g ixagutyx fgpn, gq giplxup giblpx, gqe, muxy yui gaji easbble, xyl bgoji sw ygqei srxmgaei, aliljfole gq ueso. xyl eualpxsa, igxuiwule xyl gqpysa yge tsse ysoe, jgel yui mgc gwx gqe igx esmq gjsqtix ri. ml ldpygqtle g wlm msaei ogkuoc. gwxlamgaei xylal mgi iuolqpl sq fsgae xyl cgpyx. wsa isjl algisq sa sxyla ml eue qsx fltuq xygx tgjl sw esjuqsli. ml wlox jleuxgxuvl, gqe wux wsa qsxyuqt frx bogpue ixgauqt. xyl egc mgi lqeuqt uq g ilalquxc sw ixuoo gqe ldhruiuxl fauoougqpl. xyl mgxla iysql bgpuwupgooc; xyl inc, muxysrx g iblpn, mgi g flqutq ujjlqiuxc sw rqixguqle outyx; xyl vlac juix sq xyl liild jgaiy mgi ounl g tgrkc gqe ageugqx wgfaup, yrqt wasj xyl mssele auili uqogqe, gqe eagbuqt xyl osm iysali uq eugbygqsri wsoei. sqoc xyl tossj xs xyl mlix, fasseuqt svla xyl rbbla algpyli, flpgjl jsal isjfal lvlac juqrxl, gi uw gqtlale fc xyl gbbasgpy sw xyl irq.
'''.strip('\n')


def solve():
    s = capture
    c = Counter(x for x in s if x.isalpha())
    tr = str.maketrans(dict(zip((k for k,_ in c.most_common()), string.ascii_lowercase)))
    print(s.translate(tr))
    # :(

    # https://www.guballa.de/substitution-solver
    # https://quipqiup.com


if __name__ == '__main__':
    solve()
