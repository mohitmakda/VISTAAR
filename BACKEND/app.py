from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import google.generativeai as genai


app = Flask(__name__)

template = """is the information true or false,  also give a detailed explanation of it not being true/false, the information is just for information sake, give reply in english until the information is in hindi.
information is: {news}
"""

# Retrieve API key from environment variable (assuming it's named GEMINI_API_KEY)

genai.configure(api_key='gemini_api_key')
model = genai.GenerativeModel('gemini-pro')


def get_fact_check_response(news):
    # Replace with actual Gemini-1.0-Pro API call based on their documentation
    # This example assumes a POST request to a hypothetical endpoint
    content = template.format(news=news)
    fact_response = model.generate_content(content)
    
    
    return str(fact_response.text)

    

@app.route("/sms", methods=['GET', 'POST'])
def sms():
    incoming_message_body = request.values.get('Body', '').lower()
    response = MessagingResponse()
    if incoming_message_body == "hi":
        response.message("hi, I can help you check the truthfulness of news headlines. Just send me the headline!")  # Create a response message directly within the TwiML response
    else:
        news = incoming_message_body
        final = get_fact_check_response(news)
        response.message(final)
        print(final)
        
    return str(response)  # Return the TwiML response

if __name__ == "__main__":
    app.run(debug=True)

