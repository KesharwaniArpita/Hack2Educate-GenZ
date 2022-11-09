def classify(video_key):
    
    data = list(video_key.keys())

    count={'coding':0,'business':0,'FnA':0,'it':0,'op':0,'pd':0,'design':0,'marketing':0,'ls':0,'photo':0,'HnF':0,'music':0}
    coding=['abstraction','active record','ajax','algorithm','angular.js','Apache','api','argument','arithmetic operators','array','ascii','asssignment operators',
            'Asynchronous Programming Languages','augmented reality','Autonomous','Back End','binary','backbone.js','bit','Block-based Programming Language','blockly',
            'boolean','bootstrap','bug','byte','c++','call','camel case','char','class','html','css','cloud','code','coding','code review','coding',
            'command','comman-line','compile','compilation','compiler','computation','computer','science','conditional',
            'constants','crowdsourcing','cyber','security','data','structures','database','dbms','database','management','debuging',
            'declaration','define','definition','deployment','digital','footprint','django','dns','domain','name','service','double-click','drag','drop','dry','dsl','else',
            'else statement','else condition','endless loop','event','event handler','exeption','exeption','handling','express.js','expression','flask','for loop',
            'framework','front end','full','stack','developer','function','haml','hardcode','high','level','language','http','ide','integrated','development',
            'environment','if','statement','input','inheritance','intellij','internet','ios','swift','ip','address','iteration','java','javascript','json','jquery',
            'junior','notation','object','oriented','programming','key','keywords','lamp','linter','linux','local','loop','low','machine','learning','main','mean',
            'micro','xml','mongodb','mvc','mysql','sql','nosql','neural','networks','node.js','null','oop','oops','related','objects','online','open','source',
            'operand','software','operator','os','operating','system','output','package','method','module','library','packets','pair','parameter','pattern','matching',
            'persistant','php','pixel','pointer','postgresql','program','project','based','python','r','react','native','fortran','applets','applet','relation',
            'relational','rdbms','rest','represtational','state','transfer','ruby','rails','run','runtime','sass','scratch','script','scripts','scripting','server',
            'host','side','sprint','sprites','structured','query','synchronous','asynchronous','syntax','tensor','flow','token','terminal','train','training','url',
            'testing','reusability','usability','user','ux','interface','username','variable','type','in-built','version','control','website','while','whiteboarding',
            'wi-fi','xcode','restraints','try','catch']
    business=['roi','incentivize','monetize','deliverable','margin','accounts','shareholders','payable','recievable','capital','fixed','cost','costs','gross','net','benchmarking',
              'swot','kpi','metrics','performance','review','r$d','research','development','business','b2b','b2c','c2b','c2c','scalable','responsive','competency',
              'sell','selling','propositions','marketing','management','content','customer','relationship','cpl','per','lead','demographics','digital','aquisition',
              'actuary','administration','affiliate','annual','equivalent','annuity','arbitrage','asset','assets','audit','shipping','commissions','wages','strengths',
              'weaknesses','opportunities','threats','contingency','theory','mass','niche','inbound','sales','user','benchmarking','bond','break-even','point','capital',
              'expenditure','copyright','corporate','social','responsibility','csr','critical','success','factor','diversification','enterprise','investment','strategy',
              'trade','export','fairtrade','Valuation','idea','continuity','plan','proposal','outline','fund','dunds','funding','turnover','','','','','','']
    #FnA=[Amortization,Assets,Current,Fixed,Allocation,Bonds,Stocks,maturity,Balance,Sheet,Cash,Equivalents,Equation,Capital,Gain,investors,Mutual,funds,Hedge,Flow,Operating,
     #    Investing,Financing,Compound,Interest,Depreciation,EBITDA,Equity,Income,Statement,profit,loss,P&L,liabilities,accounts,payable,Current,Long-Term,Liquidity,Net,Worth,
      #   Margin,Return,Investment,ROI,Valuation,Working,MisstatementInconsequential,Abatement,Absorption,Costing,Receivable,Receivable,Accountant,Accounting,Change,estimate,
       #  Cycle,APB,Accrual,Expense,Acid-Test,Acquisition,Actuary,Gross,subsidiary,Journal,Trial,Balance,Entry,AICPA,Allowance,Resolution,Alternative,Tax,Dispute,Depository,
        # Receipt,ADR,AICPA,Anti-Dilution,Annuity,Appreciation,Financial,Assertion,Audit,Documentation,Sampling,Auditor,Authorized,Shares,Inventory,Average-Cost,Withholding,Debt,
         #,Debt,Reconciliation, bankruptcy,Value,Bequest,Beta,Bid,Laws,Board,Bond,Discount,,,,,,,,,,,,,,,,,,,,,,,]
    FnA=[]
    it=['access','accessibility','activex','adress','alias','anonymous','ftp','anti','spam','applet','ascii','file','at','command','set','attachment','authentication',
        'backbone','bandwidth','bcp','bi','intelligence','binary','binhex','blended','f2f','learning','blog','bluetooth','bmp','bookmark','boolean','logic','bounce','bridge'
        ,'broadband','connection','browser','buffer','buffered','byod','byte','cable','modem','cache','captcha','carrier','dataprise','case-sensitive','cbt','cdr','drive','cd'
        'rom','ram','disk','rw','cd-r','cd-rom','cd-rw','cgi','gateway','chat','client','server','client-server','technology','cloud','computing','compress','connect','cookie',
        'cookies','courseware','cpu','central','processing','unit','csp','provider','cyberspace','daas','daemon','desktop','data','database','center','decompress','defragmentation',
        'degauss','dhcp','dynamic','host','configuration','protocol','dialog','dial-up','digital','digitize','dual','memory','dimm','directory','drm','distance','education','dither',
        'group','dns','download','dpi','draas','dvd','dvd-rw','dvd-r','disk','eap','extensible','authentication','ega','elearning','e-,ail','archive','archiving','emulation',
        'encryption','eps','emoticon','ethernet','card','extension','female','field','filter','finger','firewall','firewire','flash','folder','font','frames','ftp','transfer',
        'graphic','interchange','format','greyware','gui','interface','handshaking','hardware','header','application','home','page','hypertext','http','hypervisor','hyperlink',
        'iaas','icon','ics','ieee','port','image','map','imap','message','explorer','radio','internat','ip','irq','isp','iv&v','jpeg','kbps','mbps','kerberos','kerning','kilobyte',
        'base','local','network','lan','man','wan','leading','laser','printer','devices','device','lms','system','processor','linux','listserv','listserver','log','secure','security',
        'maac','mac','macintosh','mail','mailing','list','mainframe','male','malware','virus','trojen','worms','worm','trojens','workstations','mapi','mobile','megabyte','gigabyte',
        'mhz','menu','microsoft','windows','moderator','modem','monitor','mouse','mpeg','mrb','remote','msp','multimedia','multitasking','naas','maneserver','nat','adapter','hub',
        'monitoring','ocr','recogniton','on-site','on-cloud','online','opentype','paas','platform','palette','parallel','page','www','web','website','webpage','pda','assitant',
        'pdf','perl','pgp','privacy','ph','phishing','ping','packet','pixel','pop','post','postscript','proxy','ppp','point-to-point','software','pull','push','qos','quicktime',
        'ram','record','registry','backup','login','rgb','rj-45','connector','read','router','rtf','saas','mode','san','storage','sata','transmission','screen','engine','search',
        'secure','section','self-extracting','token','serial','shareware','simm','signature','smtp','spam','ssid','streaming','spyware','subdirectory','svga','t-3','10base-t','table',
        'tcp/ip','telnet','telephony','terminal','tiff','toolbar','horse','twitter','twisted','pair','optical','fibre','unix','upload','usb','username','utility','uuencode','vdi',
        'virtual','classroom','virtualization','hosting','reality','voip','vpn','vt100','wais','wap','wirelass','wep','wi-fi','window','wlan','workstation','world','wide','web','wpa',
        'wysiwyg','x2','xml','xhtml','html','ccss','zero-day','zip','zoom']
    op=[]
    pd=[]
    design=[]
    marketing=['marketing','digital','brand','positioning','awareness','generation','revenue','performance','inbound','lead','crm','cms','sales','services','operations',
               'revenue','qualified','attribution','retention','expansion','success','support','service','satisfaction','product','gtm','go-to-market','product-fit',
               'minimum','viable','total','addressable','tam','plg','product-led','pql','product-qualified','conversion','rate','optimization','cro','market','penetration',
               'analysis','buyer','persona','a/b','testing','analytics','brand','rate','ctr','bounce','conversion','customer']
    ls=[]
    photo=[]
    HnF=[]
    music=[]
    for word in data:
        if word in coding:
            count[coding]+=1
        elif word in business:
            count[business]+=1
        elif word in FnA:
            count[FnA]+=1
        elif word in it:
            count[it]+=1
        elif word in op:
            count[op]+=1
        elif word in pd:
            count[pd]+=1
        elif word in design:
            count[design]+=1 
        elif word in marketing:
            count[marketing]+=1   
        elif word in ls:
            count[ls]+=1
        elif word in photo:
            count[photo]+=1
        elif word in HnF:
            count[HnF]+=1
        elif word in music:
            count[music]+=1
        #else:
         #   print("The video does not belong to any of the sub categories of beyond exams" )
    #Keymax = max(zip(count.values(), count.keys()))[1]
    #print(count.keys[v.index(max(count.values))])
    if (all(x==0 for x in count.values())==True):
        print("The video does not belong to any of the sub categories of beyond exams")
    else:
        print("This video is related to ",count.keys[count.index(max(count.values))])