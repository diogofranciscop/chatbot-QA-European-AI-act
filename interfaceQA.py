import gradio as gr
from preprocess import find_answers


# Create the Gradio interface
iface = gr.Interface(
    fn=find_answers,
    inputs="text",
    outputs="text",
    title="Question-Answering Chatbot",
    description="Ask a question about the European AI act and get an answer!",
    theme="compact"
)

# Launch the interface
iface.launch()