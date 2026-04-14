# Playlist Vibe Builder

## Chosen Problem:
I chose the playlist vibe builder because I find it interesting to explore how it works when paired with an appropriate algorithm.

## Chosen Algorithm:
I chose merge sort for the playlist vibe builder because this algorithm creates a copy of the original unsorted list, allowing the user to preserve the initial order while also having a new sorted version. Then the user could also rearrange the playlist in different ways without losing the original order. Additionally, since merge sort uses the divide and conquer strategy, it is highly efficient to sort the playlist based on the energy of the song or even the duration.

## Demo:
Screenshots of all runs and edge cases are presented in the images folder.

## Problem Breakdwon & Computational Thinking:
### Decomposition:
- We receive a unsorted list of songs with a specific energy score from 0 to 100
- We split until we have only one element per sub-list
- We compare and start to sort the list based on the energy score
- We merge the list in a copy of the original list
- We receive a sorted list

### Pattern Recognition:
The Merge sort algorithm follows a pattern where we divide the list into smaller sublists. Then we compare the first element of the left sublist with the first element of the right sublist, then the sublists are combined in the correct order. This splitting and merging pattern repeats until the list is fully sorted.

### Abstraction:
We show the user the final sorted list and a visualization of the merging process. We hide the recursion process process, since the interest of the user is just the output.

### Algorithm Design:
- **Input:** A list of unsorted songs given to gradio.
- **Process:** Use merge sort algorithm to organize the songs based on their energy level into a new list.
- **Output:** A visualization of the merging process, and the new final sorted list.

**Note:** I chose to use a Python list because the merging process is easier to implement compared to a linked list.

### Flowchart:
![Flowchart](images/flowchart.png)

## Steps to Run (local) + requirements.txt:
1. Install requirements:
  - gradio
  - huggingface_hub>=0.19.0
2. Run on app.py on python3

## Hugging Face Link:
https://huggingface.co/spaces/juanbernal22/Playlist-Vibe-Builder

## Testing:
1. A 5 song list: The output shows the list sorted.
2. Empty list: The app asks the user to enter at least one song.
4. Only one song: The sorted list is provided automatically since no merging is involved.
6. No artist name: The app shows an error, and asks the user to enter a name in the artist textbox.

**Note:** TScreenshots of all runs and edge cases are presented in the images folder.

## Author & Acknowledgment:
**Author:** Juan Bernal Guasca

I implemented the merge sort algorithm learned in class and used gemini to guide me through the GUI implementation in Gradio. I added comments, reviewed the code, and modified code looking for simplicity and better understanding for both myself and the person grading this project.
