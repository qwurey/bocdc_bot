## Generated Story 5914322956106259965
* greet
    - utter_greet
* request_search{"item": "的情况"}
    - slot{"item": "消费"}
    - slot{"item": "的情况"}
    - action_search_consume
* request_search{"item": "消费"}
    - slot{"item": "消费"}
    - action_search_consume
* inform_time{"time": "上个月"}
    - slot{"time": "上个月"}
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_goodbye
    - export

## Generated Story 1131691423643832225
* request_search{"item": "消费"}
    - slot{"item": "消费"}
    - utter_ask_time
* inform_time{"time": "十月份"}
    - slot{"time": "十月份"}
    - action_search_consume
    - utter_ask_morehelp
* thanks
    - utter_thanks
    - export

## Generated Story -6529474466838218787
* greet
    - utter_greet
* request_search{"item": "消费"}
    - slot{"item": "消费"}
    - utter_ask_time
* inform_time{"time": "上月"}
    - slot{"time": "上月"}
    - action_search_consume
    - utter_ask_morehelp
* request_search{"time": "还", "item": "消费"}
    - slot{"time": "还"}
    - slot{"item": "消费"}
    - utter_ask_morehelp
    - utter_ask_time
* inform_time{"time": "十月"}
    - slot{"time": "十月"}
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_goodbye
* request_search{"time": "还", "item": "流量"}
    - slot{"time": "还"}
    - slot{"item": "流量"}
    - utter_ask_time
* inform_time{"time": "八月"}
    - slot{"time": "八月"}
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_goodbye
    - utter_thanks
* greet
    - utter_greet
* goodbye
    - utter_goodbye
    - export

## Generated Story 7046379915386561772
* request_search{"item": "流量"}
    - slot{"item": "流量"}
    - utter_ask_time
* inform_time{"time": "上个月"}
    - slot{"time": "上个月"}
    - action_search_consume
    - utter_ask_morehelp
* request_search{"item": "消费"}
    - slot{"item": "消费"}
    - utter_ask_time
* inform_time{"time": "上个月"}
    - slot{"time": "上个月"}
    - action_search_consume
    - utter_ask_morehelp
* request_search{"time": "还", "item": "号码"}
    - slot{"time": "还"}
    - slot{"item": "消费"}
    - slot{"item": "号码"}
    - utter_ask_time
* inform_time{"time": "上月"}
    - slot{"time": "上月"}
    - action_search_consume
    - utter_ask_morehelp
* confirm
    - utter_ask_morehelp
* deny
    - utter_goodbye
    - export

## Generated Story 3510639764351215934
* greet
    - utter_greet
* request_search{"item": "东西"}
    - slot{"item": "东西"}
    - utter_ask_time
* inform_time{"time": "三月"}
    - slot{"time": "三月"}
    - action_search_consume
* request_search{"item": "流量"}
    - slot{"item": "流量"}
    - utter_ask_time
* inform_time{"time": "四月"}
    - slot{"time": "四月"}
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_goodbye
    - export

## Generated Story -243931094327703933
* request_management{"item": "套餐"}
    - slot{"item": "套餐"}
    - utter_ask_package
* inform_package{"item": "套餐三"}
    - slot{"item": "套餐三"}
    - utter_ack_management
    - utter_ask_morehelp
* request_search{"item": "消费"}
    - slot{"item": "消费"}
    - utter_ask_time
* inform_time{"time": "三月"}
    - slot{"time": "三月"}
    - action_search_consume
    - utter_ask_morehelp
* deny
    - utter_goodbye
    - export


## Generated Story -8627121140811593037
* greet
    - utter_greet
* request_management{"item": "流量"}
    - slot{"item": "流量"}
    - utter_ask_package
* inform_package{"item": "套餐一"}
    - slot{"item": "套餐一"}
    - utter_ack_management
    - utter_ask_morehelp
* deny
    - utter_goodbye
* deny
    - utter_greet
    - export
