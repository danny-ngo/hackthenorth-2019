def create_response_messages():
    buttons = []
    
    button = {
        'type': 'web_url',
        'title': 'test button',
        'url': 'https://www.facebook.com'
    }
    buttons.append(button)
        
    return buttons
    
def test_messages():
    buttons = [
        {
            'type': 'web_url',
            'title': 'test button1',
            'url': 'https://www.facebook.com'
        },
        {
            'type': 'web_url',
            'title': 'test button2',
            'url': 'https://www.facebook.com'
        },
        {
            'type': 'web_url',
            'title': 'test button3',
            'url': 'https://www.facebook.com'
        }
    ]
        
    return buttons