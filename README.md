# Friday AI ChatBot 🤖

A voice-enabled AI chatbot powered by Microsoft's DialoGPT model, capable of speech recognition, text-to-speech, and intelligent responses with Wikipedia and Google search integration.

## Features

- **Voice Recognition**: Converts speech to text using Google Speech Recognition
- **Text-to-Speech**: Responds with natural-sounding voice using Google Text-to-Speech
- **AI Conversations**: Powered by Microsoft's DialoGPT-medium model for contextual responses
- **Wikipedia Integration**: Fetches information from Wikipedia on demand
- **Google Search**: Searches the web for current information
- **Wake Word Detection**: Responds to the name "Fawks"
- **Time Queries**: Provides current time information
- **Conversational Memory**: Maintains context during conversations

## Prerequisites

- Python 3.7 or higher
- Microphone for voice input
- Internet connection for API calls
- Google Custom Search API key and Search Engine ID

## Installation

1. **Clone the repository**
   ```bash
   git clone <your-repository-url>
   cd "AI ChatBot"
   ```

2. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API credentials**
   - Get a Google Custom Search API key from [Google Cloud Console](https://console.cloud.google.com/)
   - Create a Custom Search Engine at [Google CSE](https://cse.google.com/)
   - Update the `api_key` and `cse_id` variables in `Friday.py` with your credentials

## Dependencies

- `numpy` - Numerical computing library
- `speech_recognition` - Speech recognition library
- `gtts` - Google Text-to-Speech
- `transformers` - Hugging Face transformers library
- `tensorflow` - Machine learning framework
- `pydub` - Audio manipulation library
- `wikipediaapi` - Wikipedia API wrapper
- `requests` - HTTP library for API calls

## Usage

1. **Run the chatbot**
   ```bash
   python Friday.py
   ```

2. **Interact with the bot**
   - Say "Fawks" to wake up the bot
   - Ask questions or have conversations
   - Use commands like:
     - "Tell me about [topic]" - Get Wikipedia information
     - "Search Google for [query]" - Search the web
     - "What time is it?" - Get current time
     - "Thank you" - Receive acknowledgment
     - "Exit" or "Close" - End the conversation

## Voice Commands

| Command | Description | Example |
|---------|-------------|---------|
| `Fawks` | Wake word to activate the bot | "Hey Fawks" |
| `Tell me about [topic]` | Get Wikipedia summary | "Tell me about artificial intelligence" |
| `Search Google for [query]` | Web search | "Search Google for latest news" |
| `What time is it?` | Current time | "What time is it?" |
| `Thank you` | Acknowledgment | "Thanks" |
| `Exit/Close` | End conversation | "Exit" |

## Configuration

### API Keys
Update these variables in `Friday.py`:
```python
self.api_key = 'YOUR_GOOGLE_API_KEY'
self.cse_id = 'YOUR_CUSTOM_SEARCH_ENGINE_ID'
```

### Model Cache
The DialoGPT model is cached in the `transformers_cache/` directory to improve loading times.

### Audio Settings
- Default language: English (`en`)
- Audio format: MP3
- Speech recognition: Google Speech Recognition API

## Project Structure

```
AI ChatBot/
├── Friday.py              # Main chatbot application
├── transformers_cache/    # Cached AI models
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
├── .gitignore           # Git ignore rules
└── LICENSE              # Project license
```

## How It Works

1. **Initialization**: Loads the DialoGPT model and sets up APIs
2. **Speech Recognition**: Listens for voice input via microphone
3. **Wake Word Detection**: Activates when "Fawks" is detected
4. **Intent Recognition**: Determines the type of request (Wikipedia, Google, time, etc.)
5. **Response Generation**: Uses appropriate service or AI model to generate response
6. **Text-to-Speech**: Converts response to speech and plays it back

## Troubleshooting

### Common Issues

1. **Microphone not working**
   - Check microphone permissions
   - Ensure microphone is not being used by other applications

2. **Model loading errors**
   - Check internet connection for initial model download
   - Verify sufficient disk space for model cache

3. **API errors**
   - Verify API keys are correct and active
   - Check API quotas and usage limits

4. **Audio playback issues**
   - Install audio codecs if needed
   - Check system audio settings

### Error Messages

- `"Sorry, I did not understand that."` - Speech recognition failed
- `"Sorry, I couldn't find information on that topic."` - No results from Wikipedia/Google

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature/new-feature`)
5. Create a Pull Request

## Privacy Notice

This application:
- Uses your microphone for speech input
- Sends voice data to Google for speech recognition
- Makes API calls to Wikipedia and Google for information retrieval
- Caches AI models locally

No personal data is stored permanently by the application.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Microsoft DialoGPT](https://github.com/microsoft/DialoGPT) for the conversational AI model
- [Hugging Face Transformers](https://huggingface.co/transformers/) for the ML framework
- [Google Speech Recognition API](https://cloud.google.com/speech-to-text) for speech processing
- [Wikipedia API](https://wikipedia.readthedocs.io/) for knowledge retrieval

## Version History

- **v0.4** - Current version with Google search integration
- **v0.3** - Added Wikipedia integration
- **v0.2** - Implemented voice recognition and TTS
- **v0.1** - Basic text-based chatbot

---

**Note**: Remember to keep your API keys secure and never commit them to version control.
