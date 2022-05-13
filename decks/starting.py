deck = {
'SD001':{
        'name':'The first event',
        'text':'This is the text of the first event.',
        'unique':True,
        'options':{
            'opt1':{
                'text':'Option 1','new_cards':['TEST001'],
                'cost_type':['settlers_count','babies_count'],'cost_amt':[10,5],
                'rwd_type':['settlers_count','babies_approval'],'rwd_amt':[20,1]
            },
            'opt2':{
                'text':'Option 2','new_cards':['SD003'],
                'cost_type':['settlers_approval'],'cost_amt':[1],
                'rwd_type':['settlers_count'],'rwd_amt':[2]
            },
            'opt3':{
                'text':'Option 3','new_cards':['SD004'],
                'cost_type':['settlers_count'],'cost_amt':[3],
                'rwd_type':['settlers_count'],'rwd_amt':[3]
            }}},
'SD002':{
        'name':'The second event',
        'text':'This is the text of the second event.',
        'unique':True,
        'options':{
            'opt1':{
                'text':'Option 1','new_cards':['SD003'],
                'cost_type':['settlers_count','babies_count'],'cost_amt':[10,5],
                'rwd_type':['settlers_count','babies_approval'],'rwd_amt':[20,1]
            },
            'opt2':{
                'text':'Option 2','new_cards':['SD003'],
                'cost_type':['settlers_approval'],'cost_amt':[1],
                'rwd_type':['settlers_count'],'rwd_amt':[2]
            },
            'opt3':{
                'text':'Option 3','new_cards':['SD003'],
                'cost_type':['settlers_count'],'cost_amt':[3],
                'rwd_type':['settlers_count'],'rwd_amt':[3]
            }}},
'SD003':{
        'name':'The third event',
        'text':'This is the text of the third event.',
        'unique':True,
        'options':{
            'opt1':{
                'text':'Option 1','new_cards':['SD004'],
                'cost_type':['settlers_count','babies_count'],'cost_amt':[10,5],
                'rwd_type':['settlers_count','babies_approval'],'rwd_amt':[20,1]
            },
            'opt2':{
                'text':'Option 2','new_cards':['SD004'],
                'cost_type':['settlers_approval'],'cost_amt':[1],
                'rwd_type':['settlers_count'],'rwd_amt':[2]
            },
            'opt3':{
                'text':'Option 3','new_cards':['SD004'],
                'cost_type':['settlers_count'],'cost_amt':[3],
                'rwd_type':['settlers_count'],'rwd_amt':[3]
            }}},
'SD004':{
        'name':'The fourth event',
        'text':'This is the text of the fourth event.',
        'unique':True,
        'options':{
            'opt1':{
                'text':'Option 1','new_cards':[''],
                'cost_type':['settlers_count','babies_count'],'cost_amt':[10,5],
                'rwd_type':['settlers_count','babies_approval'],'rwd_amt':[20,1]
            },
            'opt2':{
                'text':'Option 2','new_cards':[''],
                'cost_type':['settlers_approval'],'cost_amt':[1],
                'rwd_type':['settlers_count'],'rwd_amt':[2]
            },
            'opt3':{
                'text':'Option 3','new_cards':[''],
                'cost_type':['settlers_count'],'cost_amt':[3],
                'rwd_type':['settlers_count'],'rwd_amt':[3]
            }}}
}
