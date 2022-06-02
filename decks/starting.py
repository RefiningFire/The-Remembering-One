deck = {
'SD001':{
        'name':'The first event',
        'text':'This is the text of the first event.',
        'unique':True,
        'options':{
            'opt1':{
                'text':'Option 1','new_cards':['TRFM001'],
                'cost_type':['settler_count','baby_count','teen_count','child_count','settler_approval'],'cost_amt':[10,5,2,30,10],
                'rwd_type':['settler_count','baby_approval'],'rwd_amt':[20,1],
                'time':1
            },
            'opt2':{
                'text':'Option 2','new_cards':['SD003'],
                'cost_type':['settler_approval'],'cost_amt':[1],
                'rwd_type':['settler_count'],'rwd_amt':[2],
                'req_type':['settler_count','baby_count'],'req_amt':[10,1],
                'time':2
            },
            'opt3':{
                'text':'Option 3','new_cards':['SD004'],
                'cost_type':['settler_count'],'cost_amt':[3],
                'rwd_type':['settler_count'],'rwd_amt':[3],
                'time':4
            }}},
'SD002':{
        'name':'The second event',
        'text':'This is the text of the second event.',
        'unique':True,
        'options':{
            'opt1':{
                'text':'Option 1','new_cards':['SD003'],
                'cost_type':['settler_count','baby_count'],'cost_amt':[10,5],
                'rwd_type':['settler_count','baby_approval'],'rwd_amt':[20,1],
                'req_type':['baby_count'],'req_amt':[100],
                'time':1
            },
            'opt2':{
                'text':'Option 2','new_cards':['SD003'],
                'cost_type':['settler_approval'],'cost_amt':[1],
                'rwd_type':['settler_count'],'rwd_amt':[2],
                'time':2
            },
            'opt3':{
                'text':'Option 3','new_cards':['SD003'],
                'cost_type':['settler_count'],'cost_amt':[3],
                'rwd_type':['settler_count'],'rwd_amt':[3],
                'time':3
            }}},
'SD003':{
        'name':'The third event',
        'text':'This is the text of the third event.',
        'unique':True,
        'options':{
            'opt1':{
                'text':'Option 1','new_cards':['SD004'],
                'cost_type':['settler_count','baby_count'],'cost_amt':[10,5],
                'rwd_type':['settler_count','baby_approval'],'rwd_amt':[20,1],
                'req_type':[],'req_amt':[],
                'time':1
            },
            'opt2':{
                'text':'Option 2','new_cards':['SD004'],
                'cost_type':['settler_approval'],'cost_amt':[1],
                'rwd_type':['settler_count'],'rwd_amt':[2],
                'req_type':[],'req_amt':[],
                'time':2
            },
            'opt3':{
                'text':'Option 3','new_cards':['SD004'],
                'cost_type':['settler_count'],'cost_amt':[3],
                'rwd_type':['settler_count'],'rwd_amt':[3],
                'req_type':[],'req_amt':[],
                'time':72
            }}},
'SD004':{
        'name':'The fourth event',
        'text':'This is the text of the fourth event.',
        'unique':True,
        'options':{
            'opt1':{
                'text':'Option 1','new_cards':[''],
                'cost_type':['settler_count','baby_count'],'cost_amt':[10,5],
                'rwd_type':['settler_count','baby_approval'],'rwd_amt':[20,1],
                'req_type':[],'req_amt':[],
                'time':1
            },
            'opt2':{
                'text':'Option 2','new_cards':[''],
                'cost_type':['settler_approval'],'cost_amt':[1],
                'rwd_type':['settler_count'],'rwd_amt':[2],
                'req_type':[],'req_amt':[],
                'time':2
            },
            'opt3':{
                'text':'Option 3','new_cards':[''],
                'cost_type':['settler_count'],'cost_amt':[3],
                'rwd_type':['settler_count'],'rwd_amt':[3],
                'req_type':[],'req_amt':[],
                'time':4
            }}}
}
