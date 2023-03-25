import streamlit as st
import openai

st.set_page_config(page_title="Where2Travel", page_icon = "✈️")

openai.api_key = st.secrets["API_KEY"]

st.title("Where to go")

destination = st.text_input("Destination")
days = st.number_input("Number of Days", value = 1)


if st.button("Let's hear it!"):
	with st.spinner("Wait for it..."):
		response = openai.ChatCompletion.create(
		    model="gpt-3.5-turbo",
		    messages=[
		            {"role": "system", "content": """
		            
		            You are ChatGPT, a large language model trained by OpenAI. 
		                                    
		            
		            """},
		            {"role": "user", "content": """
		            
		            Imagine you are a travel agent.

		            I will be going to {} for {} days.

		            Give me a detailed itinerary with 2 or 3 activites or attractions for each day.
			    
			    When planning the itinerary, group activities or attractions that are nearby together. 

		            Also, include food recommendations for breakfast, lunch, dinner and dessert that are nearby.
		            
		            """.format(destination, days)},
		        ]
		)

	result = ''

	for choice in response.choices:
	    result += choice.message.content

	st.write(result)
