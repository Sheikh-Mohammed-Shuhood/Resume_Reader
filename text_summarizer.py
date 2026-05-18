import ollama

def summarize_text(text_to_summarize):
    print("Initializing local Llama 3.2 3B model...")
    print("Using hybrid GPU/CPU processing...")
    
    # Define a strict system prompt to keep the summary focused
    system_instruction = (
        "You are an advanced text summarizer. Provide a clear, concise summary "
        "of the text provided. Use bullet points if necessary. Do not include any "
        "conversational filler, introductions, or conclusions."
    )
    
    # Call the local model
    response = ollama.chat(
        model='llama3.2:3b',
        messages=[
            {'role': 'system', 'content': system_instruction},
            {'role': 'user', 'content': f"Please summarize this text:\n\n{text_to_summarize}"}
        ],
        options={
            'temperature': 0.3, # Low temperature makes the summary more factual and structured
        }
    )
    
    return response['message']['content']