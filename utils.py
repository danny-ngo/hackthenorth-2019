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
    elements = []
    
    element = {
        'title': 'Review',
        'buttons': [
            {
                'type': 'web_url',
                'title': '1',
                'url': 'https://www.facebook.com'
            },
            {
                'type': 'web_url',
                'title': '2',
                'url': 'https://www.facebook.com'
            },
            {
                'type': 'web_url',
                'title': '3',
                'url': 'https://www.facebook.com'
            },
            {
                'type': 'web_url',
                'title': '4',
                'url': 'https://www.facebook.com'
            },
            {
                'type': 'web_url',
                'title': '5',
                'url': 'https://www.facebook.com'
            }
        ],
        'image_url': 'https://images.unsplash.com/photo-1508138221679-760a23a2285b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1567&q=80'
    }
    elements.append(element)
    return elements