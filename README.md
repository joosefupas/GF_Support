# GF Mood Emergency Support

This code is a simple Python script that uses the tkinter library to create a GUI that provides users with emotional support based on their entered mood. 

## Usage

To use this script, simply run it in a Python environment. The GUI will then appear, and users can select their mood on a scale of 1-10. After submitting their mood, a message and a random image will appear offering emotional support. 

## Features

- Mood selection scale
- Emotional support message based on mood range
- Random image generated from the web
- Functionality for popup message

## Dependencies

This script makes use of the following libraries:

- tkinter
- random
- urllib
- PIL

## Code Breakdown

The code uses a few important functions, which are explained below:

### `get_random_image()`

This function makes use of the urllib and PIL libraries to generate a random image from the web. Images are fetched from the Unsplash website via their API.

### `print_mood()`

This function is called when the user clicks the "Click for some love" button. It first fetches the user's mood, then searches the predefined `mood_ranges` list to find the appropriate mood range. Once the corresponding mood message is found, the GUI label is updated with the message, and a random image is generated using the `get_random_image()` function. Finally, `message_popup()` function is called to create a popup message with the mood message.

### `message_popup()`

This function creates a popup message with the mood message displayed on it. It also provides an "OK" button to close the popup message.

## Conclusion

This script is a simple way to provide emotional support for users based on their mood. It can be easily customized to include additional mood ranges and corresponding messages, as well as different image sources.
