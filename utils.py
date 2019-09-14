from pymessenger import Button
        
def create_response_messages():
    buttons = []
    
    for i in range(1, 6):
        button = Button(title=str(i), type='web_url', url='https://www.facebook.com')
        buttons.append(button)
        
    return buttons