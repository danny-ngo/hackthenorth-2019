def create_buttons(id):
    buttons = [
        {
            'type': 'postback',
            'title': 'Not good',
            'payload': id
        },
        {
            'type': 'postback',
            'title': 'Neither good nor bad',
            'payload': id
        },
        {
            'type': 'postback',
            'title': 'Good',
            'payload': id
        }
    ]
        
    return buttons
    
    
def create_quick_replies():
    quick_replies = [
        {
            "content_type":"text",
            "title":"Bad",
            "payload":"bad",
        },
        {
            "content_type":"text",
            "title":"Somewhat Bad",
            "payload":"somewhat_bad",
        },
        {
            "content_type":"text",
            "title":"Neither Good nor Bad",
            "payload":"neutral",
        },
        {
            "content_type":"text",
            "title":"Somewhat Good",
            "payload":"somewhat_good",
        },
        {
            "content_type":"text",
            "title":"Good",
            "payload":"good",
        }
    ]
    
    return quick_replies
    
    '''
    {
        'object': 'page', 
        'entry': [{'id': '113171420070464', 
            'time': 1568511823390, 
            'messaging': [{
                'sender': {'id': '2470284623018202'}, 
                'recipient': {'id': '113171420070464'}, 
                'timestamp': 1568511821021, 
                'postback': {'title': 'Good', 'payload': 'good'}
            }]
        }]
    }
    '''