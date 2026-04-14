import gradio as gr
import time
import random

# Merge sort algorithm 
def sort(playlist_list, logs): # Divides the playlist in two halves
    if len(playlist_list) <= 1:
        return playlist_list
    
    mid = len(playlist_list) // 2
    left_half = sort(playlist_list[:mid], logs)
    right_half = sort(playlist_list[mid:], logs)
    
    return merge(left_half, right_half, logs)

def merge(left, right, logs): # Merges the lists based on energy level
    playlist_sorted = []
    i = 0
    j = 0
    
    # Visual simulation: capturing the names of songs being merged
    left_names = [song["name"] for song in left]
    right_names = [song["name"] for song in right]
    logs.append(f"Merging: {left_names} , {right_names}")

    while i < len(left) and j < len(right):  # Comparison based on energy level 
        if left[i]['energy'] <= right[j]['energy']:
            playlist_sorted.append(left[i])
            i += 1
        else:
            playlist_sorted.append(right[j])
            j += 1
            
    playlist_sorted.extend(left[i:])
    playlist_sorted.extend(right[j:])
    return playlist_sorted

#Interface

# Variable to store songs before sorting
playlist_data = []

def add_song(name, artist, energy):
    if not name or not artist:
        return gr.update(), "Please fill in all fields."
    
    new_song = {
        "name": name,
        "artist": artist,
        "energy": int(energy)
    }
    playlist_data.append(new_song)
    
    # Format the current list for the display box
    list_display = ""
    for s in playlist_data:
        list_display += f" {s['name']} - {s['artist']} (Energy: {s['energy']})\n"
    
    return list_display, f"'{name}' added successfully."

def run_sorting_process():
    if not playlist_data:
        return "The list is empty.", "Nothing to sort."
    
    simulation_logs = []
    # Calling Merge Sort algorithm
    sorted_playlist = sort(playlist_data, simulation_logs)
    
    # Formatting the simulation log text
    log_text = "\n".join(simulation_logs)
    
    # Formatting the final sorted list
    final_output = "SORTED PLAYLIST (Vibe: Low -> High):\n\n"
    for s in sorted_playlist:
        final_output += f"✨ Energy: {s['energy']} | {s['name']} ({s['artist']})\n"
        
    return log_text, final_output

# GRADIO GUI

with gr.Blocks(theme=gr.themes.Soft()) as demo:
    gr.Markdown("#Playlist Vibe Builder")
    gr.Markdown("Add your favorite songs and organize them by energy level using the Merge Sort algorithm.")
    
    with gr.Row():
        with gr.Column():
            gr.Markdown("### 1. Input Song Details")
            name_input = gr.Textbox(label="Song Title", placeholder="e.g., Runaway")
            artist_input = gr.Textbox(label="Artist Name", placeholder="e.g., Kanye West")
            energy_slider = gr.Slider(0, 100, label="Energy Level", step=1)
            btn_add = gr.Button("Add Song", variant="secondary")
        
        with gr.Column():
            gr.Markdown("### 2. Current Unsorted Playlist")
            monitor_box = gr.Textbox(label="Songs in Queue", lines=8)
            status_msg = gr.Markdown("*Ready to add songs...*")

    gr.Markdown("---")
    btn_sort = gr.Button(" RUN MERGE SORT", variant="primary")
    
    with gr.Row():
        with gr.Column():
            log_display = gr.Textbox(label="Algorithm Simulation: Merging Steps", lines=10)
        with gr.Column():
            result_display = gr.Textbox(label="Final Sorted Output", lines=10)

    # UI Event Handling
    btn_add.click(
        add_song, 
        inputs=[name_input, artist_input, energy_slider], 
        outputs=[monitor_box, status_msg]
    )
    
    btn_sort.click(
        run_sorting_process, 
        outputs=[log_display, result_display]
    )

if __name__ == "__main__":
    demo.launch()
