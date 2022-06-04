deck = {
'SD001':{
        'name':'The first event for {stats[player_name]}',
        'text':'This is the text of the first event, for {stats[player_name]}, age: {stats[age]}.',
        'req_type_flr':[],'req_amt_flr':[],
        'req_type_cap':[],'req_amt_cap':[],
        'unique':True,'delay':0,'delay_chance':1,
        'options':{
            'opt1':{
                'text':'Option for {stats[player_name]}','new_cards':['TRFM001'],
                'cost_type':[],'cost_amt':[],
                'rwd_type':['food_production'],'rwd_amt':[10],
                'req_type_flr':[],'req_amt_flr':[],
                'req_type_cap':[],'req_amt_cap':[],
                'time':1
            },
            'opt2':{
                'text':'Option 2','new_cards':['SD003'],
                'cost_type':[],'cost_amt':[],
                'rwd_type':[],'rwd_amt':[],
                'req_type_flr':[],'req_amt_flr':[],
                'req_type_cap':[],'req_amt_cap':[],
                'time':2
            },
            'opt3':{
                'text':'Option 3','new_cards':['SD004'],
                'cost_type':[],'cost_amt':[],
                'rwd_type':[],'rwd_amt':[],
                'req_type_flr':[],'req_amt_flr':[],
                'req_type_cap':[],'req_amt_cap':[],
                'time':4
            }}},


'SD002':{
        'name':'The second event',
        'text':'This is the text of the second event.',
        'req_type_flr':[],'req_amt_flr':[],
        'req_type_cap':[],'req_amt_cap':[],
        'unique':True,'delay':0,'delay_chance':1,
        'options':{
            'opt1':{
                'text':'Option 1','new_cards':['SD003'],
                'cost_type':[],'cost_amt':[],
                'rwd_type':['food_consumption'],'rwd_amt':[5],
                'req_type_flr':[],'req_amt_flr':[],
                'req_type_cap':[],'req_amt_cap':[],
                'time':1
            },
            'opt2':{
                'text':'Option 2','new_cards':['SD003'],
                'cost_type':[],'cost_amt':[],
                'rwd_type':[],'rwd_amt':[],
                'req_type_flr':[],'req_amt_flr':[],
                'req_type_cap':[],'req_amt_cap':[],
                'time':2
            },
            'opt3':{
                'text':'Option 3','new_cards':['SD003'],
                'cost_type':[],'cost_amt':[],
                'rwd_type':[],'rwd_amt':[],
                'req_type_flr':[],'req_amt_flr':[],
                'req_type_cap':[],'req_amt_cap':[],
                'time':3
            }}},


'SD003':{
        'name':'The third event',
        'text':'This is the text of the third event.',
        'req_type_flr':[],'req_amt_flr':[],
        'req_type_cap':[],'req_amt_cap':[],
        'unique':True,'delay':0,'delay_chance':1,
        'options':{
            'opt1':{
                'text':'Option 1','new_cards':['SD004'],
                'cost_type':[],'cost_amt':[],
                'rwd_type':['food_reserves'],'rwd_amt':[100],
                'req_type_flr':[],'req_amt_flr':[],
                'req_type_cap':[],'req_amt_cap':[],
                'time':1
            },
            'opt2':{
                'text':'Option 2','new_cards':['SD004'],
                'cost_type':[],'cost_amt':[],
                'rwd_type':[],'rwd_amt':[],
                'req_type_flr':[],'req_amt_flr':[],
                'req_type_cap':[],'req_amt_cap':[],
                'time':2
            },
            'opt3':{
                'text':'Option 3','new_cards':['SD004'],
                'cost_type':[],'cost_amt':[],
                'rwd_type':[],'rwd_amt':[],
                'req_type_flr':[],'req_amt_flr':[],
                'req_type_cap':[],'req_amt_cap':[],
                'time':72
            }}},


'SD004':{
        'name':'The fourth event',
        'text':'This is the text of the fourth event.',
        'req_type_flr':[],'req_amt_flr':[],
        'req_type_cap':[],'req_amt_cap':[],
        'unique':True,'delay':0,'delay_chance':1,
        'options':{
            'opt1':{
                'text':'Option 1','new_cards':[''],
                'cost_type':[],'cost_amt':[],
                'rwd_type':['food_storage'],'rwd_amt':[200],
                'req_type_flr':[],'req_amt_flr':[],
                'req_type_cap':[],'req_amt_cap':[],
                'time':1
            },
            'opt2':{
                'text':'Option 2','new_cards':[''],
                'cost_type':[],'cost_amt':[],
                'rwd_type':[],'rwd_amt':[],
                'req_type_flr':[],'req_amt_flr':[],
                'req_type_cap':[],'req_amt_cap':[],
                'time':2
            },
            'opt3':{
                'text':'Option 3','new_cards':[''],
                'cost_type':[],'cost_amt':[],
                'rwd_type':[],'rwd_amt':[],
                'req_type_flr':[],'req_amt_flr':[],
                'req_type_cap':[],'req_amt_cap':[],
                'time':4
            }}}
}
