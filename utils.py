from pymessenger import Button
        
def create_response_messages():
    buttons = []
    
    for i in range(1, 6):
        button = Button(title=str(i), type='web_url', url='https://www.facebook.com')
        buttons.append(button)
        
    return buttons
    
def test_messages():
    elements = []

    for i in range(1, 6):
        element = {
            'title': 'Review',
            'buttons': [{
                'type': 'web_url',
                'title': str(i),
                'url': 'https://www.facebook.com'
            }],
            'image_url': 'https://images.unsplash.com/photo-1508138221679-760a23a2285b?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1567&q=80'
        }
        elements.append(element)
    return elements