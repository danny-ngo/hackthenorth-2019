def create_buttons():
    buttons = [
        {
            'type': 'postback',
            'title': 'Not good',
            'payload': 'not_good'
        },
        {
            'type': 'postback',
            'title': 'Neither good nor bad',
            'payload': 'neutral'
        },
        {
            'type': 'postback',
            'title': 'Good',
            'payload': 'good'
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