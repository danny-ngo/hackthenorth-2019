def create_buttons():
    buttons = [
        {
            'type': 'web_url',
            'title': 'Not good',
            'url': 'https://www.facebook.com'
        },
        {
            'type': 'web_url',
            'title': 'Neither good nor bad',
            'url': 'https://www.facebook.com'
        },
        {
            'type': 'web_url',
            'title': 'Good',
            'url': 'https://www.facebook.com'
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