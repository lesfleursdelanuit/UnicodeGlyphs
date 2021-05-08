import math
fonts = ["ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ⓪①②③④⑤⑥⑦⑧⑨",
  "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿",
  "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡",
  "A̶B̶C̶D̶E̶F̶G̶H̶I̶J̶K̶L̶M̶N̶O̶P̶Q̶R̶S̶T̶U̶V̶W̶X̶Y̶Z̶a̶b̶c̶d̶e̶f̶g̶h̶i̶j̶k̶l̶m̶n̶o̶p̶q̶r̶s̶t̶u̶v̶w̶x̶y̶z̶0̶1̶2̶3̶4̶5̶6̶7̶8̶9̶",
  "A͟B͟C͟D͟E͟F͟G͟H͟I͟J͟K͟L͟M͟N͟O͟P͟Q͟R͟S͟T͟U͟V͟W͟X͟Y͟Z͟a͟b͟c͟d͟e͟f͟g͟h͟i͟j͟k͟l͟m͟n͟o͟p͟q͟r͟s͟t͟u͟v͟w͟x͟y͟z͟0͟1͟2͟3͟4͟5͟6͟7͟8͟9͟",
  "𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷օյշՅկՏճԴՑգ",
  "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟օյշՅկՏճԴՑգ",
  "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻0123456789",
  "𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯0123456789",
  "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩⓿➊➋➌➍➎➏➐➑➒",
  "𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝒥𝒦𝐿𝑀𝒩𝒪𝒫𝒬𝑅𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏0123456789",
  "A̷͙ͭͫ̕B̩͎͍̾ͅC̵͉͋̔͞D̶͔̭̪̻Ḛͭ̉̇͟F̘͍͖ͫ͘G̩̱ͩ̏͜Hͥ̽ͣ̃̔I̍̅̀̎̊J̶̳̀́̃K͕͓͌̎̾L̸̖̽̌͂M͉̅ͮ͒ͤN̺̻̔̆ͅO̖̼ͩ͌͐P̧͕̒̊͘Q̦̭̀̾͜R͉̜̎͡͠S̵̙͕̀̃T̨͈͗̌ͥU̠҉̷̙ͦV̘̪͆̂̅W̯ͤ̾ͣ͝X̵̹̬̄̽Ỵ̛̖͋͢Z̟̈́̆̉͜ā̤̓̍͘b̬͖̏́͢c͕͗ͤ̕̕ḑ̴̞͛̒ẹ̿͋̒̕f̵͖̜̉ͅĝ̽̓̀͑ḣ̖̻͛̓ỉ͔͖̜͌j̪̟̮̔ͩḳ̯͍̑ͦl̙͖̑̾ͣḿ̬̏ͤͅṇ̤͛̒̍o̯̱̊͊͢p̞̈͑̚͞q͉ͬ͋̇ͥr̴̨̦͕̝s̠҉͍͊ͅt̲̂̓ͩ̑ư̡͕̭̇v͒̄ͭ̏̇w̦̺̐̐͟x̛̘̠̹͋y҉̃̀̋̑z̼͙̓́ͭ0̗̜͕̅̃1̨̹̦͍̀2̷́̃̉̕3̤̰̺̂̃4̶̣̠̖̳5̷̧̼́͌6͙̜̤ͩ̆7̸̹̲ͮ̒8̯̭̓̇͂9͉̳ͬ̃ͥ",
  "🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉0123456789",
  "🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉0123456789",
  "₳฿₵ĐɆ₣₲ⱧłJ₭Ⱡ₥₦Ø₱QⱤ₴₮ɄV₩ӾɎⱫ₳฿₵ĐɆ₣₲ⱧłJ₭Ⱡ₥₦Ø₱QⱤ₴₮ɄV₩ӾɎⱫ0123456789",
  "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿",
  "αв¢∂єƒgнιנкℓмησρqяѕтυνωχуzαв¢∂єƒgнιנкℓмησρqяѕтυνωχуz0123456789",
  "卂乃匚ᗪ乇千Ꮆ卄丨ﾌҜㄥ爪几ㄖ卩Ɋ尺丂ㄒㄩᐯ山乂ㄚ乙卂乃匚ᗪ乇千Ꮆ卄丨ﾌҜㄥ爪几ㄖ卩Ɋ尺丂ㄒㄩᐯ山乂ㄚ乙0123456789",
  "ᗩᗷᑕᗪEᖴGᕼIᒍKᒪᗰᑎOᑭᑫᖇᔕTᑌᐯᗯ᙭YᘔᗩᗷᑕᗪEᖴGᕼIᒍKᒪᗰᑎOᑭᑫᖇᔕTᑌᐯᗯ᙭Yᘔ0123456789",
  "∀ᙠƆᗡƎℲ⅁HIſ⋊˥WNOԀΌᴚS⊥∩ΛMX⅄Zɐqɔpǝɟɓɥıɾʞlɯuodbɹsʇnʌʍxʎz0⇂ᄅƐㄣގ9ㄥ86",
  "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ０１２３４５６７８９",
  "𝕒Ⓑｃ𝓭𝒆ғﻮĤίĴ𝓚ˡ𝓂几σק𝐐ᖇⓢｔยᐯⓦχ𝔂zⓐｂｃ∂𝐄𝕗𝓖Ｈเנ𝓀𝓛𝐌几𝕆𝕡𝐐ⓡѕт𝐮𝓋ｗχＹℤʘ➀❷➂➃❺➅➆❽❾",
  "A͓̽B͓̽C͓̽D͓̽E͓̽F͓̽G͓̽H͓̽I͓̽J͓̽K͓̽L͓̽M͓̽N͓̽O͓̽P͓̽Q͓̽R͓̽S͓̽T͓̽U͓̽V͓̽W͓̽X͓̽Y͓̽Z͓̽a͓̽b͓̽c͓̽d͓̽e͓̽f͓̽g͓̽h͓̽i͓̽j͓̽k͓̽l͓̽m͓̽n͓̽o͓̽p͓̽q͓̽r͓̽s͓̽t͓̽u͓̽v͓̽w͓̽x͓̽y͓̽z͓̽0͓̽1͓̽2͓̽3͓̽4͓̽5͓̽6͓̽7͓̽8͓̽9͓̽",
  "Ⱥβ↻ᎠƐƑƓǶįلҠꝈⱮហටφҨའϚͲԱỼచჯӋɀąҍçժҽƒցհìʝҟӀʍղօքզɾʂէմѵա×վՀ⊘𝟙ϩӠ५ƼϬ7𝟠९",
  "【A】【B】【C】【D】【E】【F】【G】【H】【I】【J】【K】【L】【M】【N】【O】【P】【Q】【R】【S】【T】【U】【V】【W】【X】【Y】【Z】【a】【b】【c】【d】【e】【f】【g】【h】【i】【j】【k】【l】【m】【n】【o】【p】【q】【r】【s】【t】【u】【v】【w】【x】【y】【z】【0】【1】【2】【3】【4】【5】【6】【7】【8】【9】",
  "A҉B҉C҉D҉E҉F҉G҉H҉I҉J҉K҉L҉M҉N҉O҉P҉Q҉R҉S҉T҉U҉V҉W҉X҉Y҉Z҉a҉b҉c҉d҉e҉f҉g҉h҉i҉j҉k҉l҉m҉n҉o҉p҉q҉r҉s҉t҉u҉v҉w҉x҉y҉z҉0҉1҉2҉3҉4҉5҉6҉7҉8҉9҉",
  "ȺɃȻĐɆFǤĦƗɈꝀŁMNØⱣꝖɌSŦᵾVWXɎƵȺƀȼđɇfǥħɨɉꝁłmnøᵽꝗɍsŧᵾvwxɏƶ01ƻ3456789",
  "ⱭƁƇƊҼƑƓӇӀJƘlⱮƝƠƤQRՏƬƲVⱲXƳȤąɓƈɗҽƒɠɦíᴊƙƖɱղօƥʠɾʂƭʋⱱⱳxყz0123456789",
  "ДБСĎЕҒĞНІЈКLМПОРϘГЅТЦѴШХЧZдбсᴅеғɢ̆ніᴊкʟмпорϙгѕтцѵшхчᴢ0123456789",
  "ƛƁƇƊЄƑƓӇƖʆƘԼMƝƠƤƢƦƧƬƲƔƜҲƳȤƛƁƇƊЄƑƓӇƖʆƘԼMƝƠƤƢƦƧƬƲƔƜҲƳȤ0123456789",
  "ᗩᙖᙅᗪᙓᖴᘜᕼIᒍKᒪᙏᑎOᑭᑫᖇSTᙀᐯᙎ᙭YᘔᗩᙖᙅᗪᙓᖴᘜᕼIᒍKᒪᙏᑎOᑭᑫᖇSTᙀᐯᙎ᙭Yᘔ0123456789",
  "ΔƁCDΣFGHIJƘLΜ∏ΘƤႳΓЅƬƱƲШЖΨZλϐςdεғϑɢнιϳκlϻπσρφгsτυvшϰψz012345678",
  "ค๒ς๔єŦɠђเןкl๓ภ๏թợгรtยvฬxץzค๒ς๔єŦɠђเןкl๓ภ๏թợгรtยvฬxץz0123456789",
  "ⱭƁƇƊҼƑƓӇӀJƘlⱮƝƠƤQRՏƬƲVⱲXƳȤɑҍϲժҽƒցհíᴊƙƖʍղօթqɾsեմѵաxყz0123456789",
  "ᾋϐƇƉἝҒƓἬἿЈḰĿṂƝὋƤQȒṨҬȖVẂẊὛẔᾄвƈḋἔғʛђἷʝќłмᾗὄῥqʀṩҭὗvᾧẋẏẓ0123456789",
  "ABCDEFGHIJKLMNOPQRSTUVWXYZãbĉdêfĝĥĩĵklmñǿpqѓşţʉvŵxŷż0123456789",
  "Ⓐ̣̣̣Ⓑ̣̣̣Ⓒ̣̣̣Ⓓ̣̣̣Ⓔ̣̣̣Ⓕ̣̣̣Ⓖ̣̣̣Ⓗ̣̣̣Ⓘ̣̣̣Ⓙ̣̣̣Ⓚ̣̣̣Ⓛ̣̣̣Ⓜ̣̣̣Ⓝ̣̣̣Ⓞ̣̣̣Ⓟ̣̣̣Ⓠ̣̣̣Ⓡ̣̣̣Ⓢ̣̣̣Ⓣ̣̣̣Ⓤ̣̣̣Ⓥ̣̣̣Ⓦ̣̣̣Ⓧ̣̣̣Ⓨ̣̣̣Ⓩ̣̣̣ⓐ̣̣̣ⓑ̣̣̣ⓒ̣̣̣ⓓ̣̣̣ⓔ̣̣̣ⓕ̣̣̣ⓖ̣̣̣ⓗ̣̣̣ⓘ̣̣̣ⓙ̣̣̣ⓚ̣̣̣ⓛ̣̣̣ⓜ̣̣̣ⓝ̣̣̣ⓞ̣̣̣ⓟ̣̣̣ⓠ̣̣̣ⓡ̣̣̣ⓢ̣̣̣ⓣ̣̣̣ⓤ̣̣̣ⓥ̣̣̣ⓦ̣̣̣ⓧ̣̣̣ⓨ̣̣̣ⓩ̣̣̣⓪̣̣̣①̣̣̣②̣̣̣③̣̣̣④̣̣̣⑤̣̣̣⑥̣̣̣⑦̣̣̣⑧̣̣̣⑨̣̣̣",
  "𝑨̲̅𝑩̲̅𝑪̲̅𝑫̲̅𝑬̲̅𝑭̲̅𝑮̲̅𝑯̲̅𝑰̲̅𝑱̲̅𝑲̲̅𝑳̲̅𝑴̲̅𝑵̲̅𝑶̲̅𝑷̲̅𝑸̲̅𝑹̲̅𝑺̲̅𝑻̲̅𝑼̲̅𝑽̲̅𝑾̲̅𝑿̲̅𝒀̲̅𝒁̲̅𝒂̲̅𝒃̲̅𝒄̲̅𝒅̲̅𝒆̲̅𝒇̲̅𝒈̲̅𝒉̲̅𝒊̲̅𝒋̲̅𝒌̲̅𝒍̲̅𝒎̲̅𝒏̲̅𝒐̲̅𝒑̲̅𝒒̲̅𝒓̲̅𝒔̲̅𝒕̲̅𝒖̲̅𝒗̲̅𝒘̲̅𝒙̲̅𝒚̲̅𝒛̲̅0̲̅1̲̅2̲̅3̲̅4̲̅5̲̅6̲̅7̲̅8̲̅9̲̅",
  "A̲B̲C̲D̲E̲F̲G̲H̲I̲J̲K̲L̲M̲N̲O̲P̲Q̲R̲S̲T̲U̲V̲W̲X̲Y̲Z̲a̲b̲c̲d̲e̲f̲g̲h̲i̲j̲k̲l̲m̲n̲o̲p̲q̲r̲s̲t̲u̲v̲w̲x̲y̲z̲0̲1̲2̲3̲4̲5̲6̲7̲8̲9̲",
  "Ä̤̈B̤̈̈C̤̈̈D̤̈̈Ë̤̈F̤̈̈G̤̈̈Ḧ̤̈Ï̤̈J̤̈̈K̤̈̈L̤̈̈M̤̈̈N̤̈̈Ö̤̈P̤̈̈Q̤̈̈R̤̈̈S̤̈̈T̤̈̈Ṳ̈̈V̤̈̈Ẅ̤̈Ẍ̤̈Ÿ̤̈Z̤̈̈ä̤̈b̤̈̈c̤̈̈d̤̈̈ë̤̈f̤̈̈g̤̈̈ḧ̤̈ï̤̈j̤̈̈k̤̈̈l̤̈̈m̤̈̈n̤̈̈ö̤̈p̤̈̈q̤̈̈r̤̈̈s̤̈̈ẗ̤̈ṳ̈̈v̤̈̈ẅ̤̈ẍ̤̈ÿ̤̈z̤̈̈0̤̈̈1̤̈̈2̤̈̈3̤̈̈4̤̈̈5̤̈̈6̤̈̈7̤̈̈8̤̈̈9̤̤̈",
  "A̸B̸C̸D̸E̸F̸G̸H̸I̸J̸K̸L̸M̸N̸O̸P̸Q̸R̸S̸T̸U̸V̸W̸X̸Y̸Z̸a̸b̸c̸d̸e̸f̸g̸h̸i̸j̸k̸l̸m̸n̸o̸p̸q̸r̸s̸t̸u̸v̸w̸x̸y̸z̸0̸1̸2̸3̸4̸5̸6̸7̸8̸9̸",
  "A͓B͓C͓D͓E͓F͓G͓H͓I͓J͓K͓L͓M͓N͓O͓P͓Q͓R͓S͓T͓U͓V͓W͓X͓Y͓Z͓a͓b͓c͓d͓e͓f͓g͓h͓i͓j͓k͓l͓m͓n͓o͓p͓q͓r͓s͓t͓u͓v͓w͓x͓y͓z͓0͓1͓2͓3͓4͓5͓6͓7͓8͓9͓",
  "ABCDEFGHIJKLMNOPQRSTUVWXYZᾰ♭ḉᖱḙḟ❡ℏ!♩кℓՊℵ✺℘ǭԻṧтṳṽω✘⑂ℨ0123456789",
  "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗",
  "𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧0123456789",
  "A͡B͡C͡D͡E͡F͡G͡H͡I͡J͡K͡L͡M͡N͡O͡P͡Q͡R͡S͡T͡U͡V͡W͡X͡Y͡Z͡a͡b͡c͡d͡e͡f͡g͡h͡i͡j͡k͡l͡m͡n͡o͡p͡q͡r͡s͡t͡u͡v͡w͡x͡y͡z͡0͡1͡2͡3͡4͡5͡6͡7͡8͡9͡",
  "⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵⒪⑴⑵⑶⑷⑸⑹⑺⑻⑼",
  "ᾋϐƇƉἝҒƓἬἿЈḰĿṂƝὋƤQȒṨҬȖVẂẊὛẔᾄвƈḋἔғʛђἷʝќłмᾗὄῥqʀṩҭὗvᾧẋẏẓ0123456789",
  "ABCDEFGHIJKLMNOPQRSTUVWXYZαвcdeғɢнιjĸlмɴopqrѕтυvwхyz0123456789",
  "ABCDEFGHIJKLMNOPQRSTUVWXYZαв¢∂єƒgнιנкℓмησρqяѕтυνωχуz0123456789"
]

names = ["Circular",
  "All Caps",
  "King's Landing",
  "Strikethrough",
  "Underline",
  "Franktur",
  "Franktur Bold",
  "Italic",
  "Bold Italic",
  "Black Pill",
  "Script",
  "Zalgo",
  "Price is Wrong",
  "Domino",
  "Slipknot",
  "Typewriter",
  "Souvlaki",
  "Wasai",
  "Notebook",
  "Upside Down",
  "Lite",
  "Rando",
  "X-Out",
  "Funky Bunch",
  "Bracket",
  "Freaky Friday",
  "Slicer",
  "Pound Cake",
  "Ruski",
  "Gawd Mode",
  "Wiggle Arms",
  "Its All Greek",
  "Wonky Doodle",
  "Quebec",
  "Spicy ABC",
  "Impression",
  "Balloon",
  "Top Hat",
  "Undermine",
  "Dot Matrix",
  "Slash",
  "X Axis",
  "Notes",
  "Serif Bold",
  "Serif Italic",
  "Hat",
  "Function",
  "WiFi",
  "Short Caps",
  "Fancy Text"
]


def getNumCharsPerSym(alpha, base):
  base_len = len(base)
  num_chars_per_symbol = len(alpha)/base_len
  (frac,whole) = math.modf(num_chars_per_symbol)
  return (frac,whole)

def splitStringIntoChunks(string, n):
  return [string[i:i+n] for i in range(0, len(string), n)]

id = 200
pairs =[(y,z) for (y,z) in zip(fonts, names)]
base = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
num_chars = len(base)
base = list(base)
triples = {}
search = {}
skip = set(["Franktur", "Franktur Bold", "Script", "Serif Bold", "Serif Italic", "Italic", "Bold Italic", "Balloon", "King's Landing"])
for i, (alpha,name) in enumerate(pairs):
  search[name] = alpha
  (frac,whole) = getNumCharsPerSym(search[name], base)
  if frac == 0.0 and name not in skip:
    alpha_split_by_syms = splitStringIntoChunks(alpha, int(whole))
    triples[name] = [(y,z) for (y,z) in zip(base,alpha_split_by_syms)]

    computer_sensitive_name = name.replace(" ", "_").replace("-","")
    f = open(computer_sensitive_name + ".js", "w")

    string = 'import Font from "../Font.js";\n\n'
    string += "const " + computer_sensitive_name + " = new Font(" + str(id) + ',"' + name + '");\n\n'

    id += 1

    string += computer_sensitive_name + '.initCharacterSet("normal",' + str(id) + ');\n'

    for (c,sym) in triples[name]:
      string += computer_sensitive_name + '.character_sets["normal"].setCharacter(null,"' + c + '","' + sym + '");\n'

    id += 1

    string += "\nexport default " + computer_sensitive_name + ";"

    f.write(string)
    f.close()

f = open('allFonts.js', 'w')
string = ""
good = []
for name in names: 
  if name not in skip:
    good.append(name)
    name = name.replace(" ","_").replace("-","")
    string += 'import ' + name + ' from "./' + name + '.js";\n'

string += 'let extraFonts = {'
for g in good:
  string += '"' + g + '" : ' + g.replace(" ","_").replace("-","") + ','

string += '};\n\n'

good.append("extraFonts")

string += 'export {' + ",".join([g.replace(" ","_").replace("-","") for g in good]) + '};'

f.write(string)
f.close()


