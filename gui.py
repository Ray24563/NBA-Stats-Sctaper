import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from analysis import stats_analysis
from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from datetime import datetime

window = Tk()
df = stats_analysis()
now = datetime.now()
date = now.date()

window.geometry("1140x730")
window.resizable(False, False)
window.config(bg="#1C1C1C")
window.title("NBA Stats Scraper: 2024-2025 NBA Preseason Stats")
icon = PhotoImage(file="icons/icon-logo.png")
window.iconphoto(True, icon)
text_widget = ""

def on_enter(e):
  e.widget['background'] = '#1D428A'  # Lighter blue for hover
  e.widget['foreground'] = 'white'

def on_leave(e):
  e.widget['background'] = '#0C2340'  # Original blue color
  e.widget['foreground'] = 'white'

def on_enter_red(e):
  e.widget['background'] = '#E04A5A'  # Lighter blue for hover
  e.widget['foreground'] = 'white'

def on_leave_red(e):
  e.widget['background'] = '#C8102E'  # Original red color
  e.widget['foreground'] = 'white'

def main():
    global button_df, button_info, button_offensive, button_defensive, label, display_date, all_rights

    # Clear all widgets from the main window
    for widget in window.winfo_children():
        widget.place_forget()

    # Ensure text_widget is defined and hide it if it exists
    if 'text_widget' in globals() and text_widget:
        text_widget.place_forget()

    # Create a new date label
    now = datetime.now()
    date = now.date()
    display_date = Label(text=f"Date: {date}", background="#1C1C1C", fg="white")
    display_date.pack(side=TOP, anchor="ne")

    # Create the main title label
    label = Label(text="2024-2025 NBA Season Prediction", bg="#1C1C1C", font=('Helvetica', 30, 'bold'), fg="white")
    label.place(x=320, y=160)

    # Load and display the NBA logo
    nba_logo = Image.open("icons/nba-logo.png")
    resized_image = nba_logo.resize((80, 170), Image.LANCZOS)
    nba_logo_tk = ImageTk.PhotoImage(resized_image)

    image_label = Label(window, image=nba_logo_tk, background="#1C1C1C")
    image_label.image = nba_logo_tk  # Keep a reference to avoid garbage collection
    image_label.place(x=190, y=100)

    # Create buttons for different functionalities
    button_df = Button(text="Scraped Data", padx=20, pady=10, font=("Helvetica", 12), bg="#0C2340", fg="white", command=overall_stats, cursor="hand2", activebackground="#C8102E")
    button_df.bind("<Enter>", on_enter)
    button_df.bind("<Leave>", on_leave)
    button_df.place(x=380, y=270)

    button_info = Button(text="About", padx=45, pady=11, font=("Helvetica", 12), bg="#0C2340", fg="white", command=about, cursor="hand2", activebackground="#C8102E")
    button_info.bind("<Enter>", on_enter)
    button_info.bind("<Leave>", on_leave)
    button_info.place(x=625, y=269)

    button_offensive = Button(text="Offensive Ratings", padx=20, pady=10, font=("Helvetica", 12), bg="#0C2340", fg="white", command=offensive_ratings, cursor="hand2", activebackground="#C8102E")
    button_offensive.bind("<Enter>", on_enter)
    button_offensive.bind("<Leave>", on_leave)
    button_offensive.place(x=368, y=370)

    button_defensive = Button(text="Defensive Ratings", padx=20, pady=10, font=("Helvetica", 12), bg="#0C2340", fg="white", command=defensive_ratings, cursor="hand2", activebackground="#C8102E")
    button_defensive.bind("<Enter>", on_enter)
    button_defensive.bind("<Leave>", on_leave)
    button_defensive.place(x=608, y=370)

    button_save_overall_data = Button(text="Save Overall Data", padx=15, pady=10, font=("Helvetica", 12), bg="#0C2340", fg="white", command=save_all_stats, cursor="hand2", activebackground="#C8102E")
    button_save_overall_data.bind("<Enter>", on_enter)
    button_save_overall_data.bind("<Leave>", on_leave)
    button_save_overall_data.place(x=490, y=470)

    # Footer label
    all_rights = Label(text="©2024 All Rights Reserved  |  v1.0.1", background="#1C1C1C", fg="white")
    all_rights.pack(side=BOTTOM, anchor="se")

def save_all_stats():
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files","*.xlsx")])

    if file_path:
      try:
        df.to_excel(file_path, index=False)
        messagebox.showinfo("Success", f"Data saved to {file_path}")
      except Exception as e:
         messagebox.showerror("Error", f"Failed to save file: {str(e)}")

def save_overall_stats():
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files","*.xlsx")])

    if file_path:
      try:
        df[['Team', 'GP', 'MPG', 'FGM', 'FGA', 'FG%', '3PM', '3PA', '3P%', 'FTM', 'FTA', 'FT%', 'ORB', 'RPG', 'PF']].to_excel(file_path, index=False)
        messagebox.showinfo("Success", f"Data saved to {file_path}")
      except Exception as e:
         messagebox.showerror("Error", f"Failed to save file: {str(e)}")

def save_offensive_stats():
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files","*.xlsx")])

    if file_path:
      try:
        df[['Team', 'PPG', 'EFG%', 'TS%', 'APG', 'TO Ratio', 'Off Ratings']].sort_values(by="Off Ratings", ascending=False).to_excel(file_path, index=False)
        messagebox.showinfo("Success", f"Data saved to {file_path}")
      except Exception as e:
         messagebox.showerror("Error", f"Failed to save file: {str(e)}")

def save_defensive_stats():
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel Files","*.xlsx")])

    if file_path:
      try:
        df[['Team', 'DRB', 'SPG', 'BPG', 'TOV', 'Def Ratings']].sort_values(by="Def Ratings", ascending=False).to_excel(file_path, index=False)
        messagebox.showinfo("Success", f"Data saved to {file_path}")
      except Exception as e:
         messagebox.showerror("Error", f"Failed to save file: {str(e)}")

def overall_stats():

    for widget in window.winfo_children():
      widget.place_forget()

    if text_widget:
      text_widget.place_forget()
    
    display_date.pack_forget()
    all_rights.pack_forget()

    label.config(text="2024-2025 NBA Pre-Season Stats", font=("Arial", 25, 'bold'))
    label.place(x=315, y=50)

    global frame
    frame = Frame(window)
    frame.place(x=100, y=120)

    # Create a Text widget
    table = tk.Text(frame, height=30, width=113, wrap=tk.NONE, padx=20, pady=20, bg="#1C1C1C", fg="white")
    table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame, command=table.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    table.config(yscrollcommand=scrollbar.set)

    # Insert column headers
    table.insert(tk.END, f"{'Team':<15} | {'GP':<1} | {'MPG':<4} | {'FGM':<4} | {'FGA':<4} | {'FG%':<4} | {'3PM':<4} | {'3PA':<5} | {'3P%':<4} | {'FTM':<4} | {'FTA':<4} | {'FT%':<4} | {'ORB':<4} | {'RPG':<4} | {'PF':<8}\n")
    table.insert(tk.END, "-" * 112 + "\n")  # Separator line

    # Insert teams and stats into the Text widget
    for index, row in df.iterrows():
        table.insert(tk.END, f"{row['Team']:<15} | {row['GP']:<2} | {row['MPG']:<3} | {row['FGM']:<3} | {row['FGA']:<3} | {row['FG%']:<3} | {row['3PM']:<4} | {row['3PA']:<3}  | {row['3P%']:<3} | {row['FTM']:<3} | {row['FTA']:<3} | {row['FT%']:<3} | {row['ORB']:<4} | {row['RPG']:<3} | {row['PF']:<7}\n")
    
    home_button = Button(text="Home", padx=15, pady=2, font=("Helvetica", 11), bg="#0C2340", fg="white", command=main, cursor="hand2", activebackground="#C8102E")
    home_button.bind("<Enter>", on_enter)
    home_button.bind("<Leave>", on_leave)
    home_button.place(x=470, y=670)

    save_button = Button(text="Save", padx=15, pady=2, font=("Helvetica", 11), bg="#0C2340", fg="white", command=save_overall_stats, cursor="hand2", activebackground="#C8102E")
    save_button.bind("<Enter>", on_enter)
    save_button.bind("<Leave>", on_leave)
    save_button.place(x=610, y=670)


def offensive_ratings():
    # Clear the window and other widgets
    for widget in window.winfo_children():
        widget.place_forget()

    if text_widget:
        text_widget.place_forget()

    display_date.pack_forget()
    all_rights.pack_forget()

    label.config(text="2024-2025 NBA Top Offensive Teams", font=("Arial", 25, 'bold'))
    label.place(x=283, y=50)

    # Placeholder for the plot
    global image_label  # Declare image_label globally to manage it
    placeholder_image = Image.open("icons/Placeholder.png")  # Use a placeholder image
    resized_placeholder = placeholder_image.resize((450, 453), Image.LANCZOS)
    placeholder_tk = ImageTk.PhotoImage(resized_placeholder)

    # Create a label with the placeholder image
    image_label = Label(window, image=placeholder_tk)
    image_label.image = placeholder_tk  # Keep a reference to avoid garbage collection
    image_label.place(x=35, y=125)

    # Dropdown for plot selection
    plot_options = ['Select Plot', 'Histogram', 'Bar Plot', 'Line Plot', 'Heatmap', 'Scatter Plot']
    selected_plot = StringVar(window)
    selected_plot.set(plot_options[0])  # Set default value

    plot_dropdown = OptionMenu(window, selected_plot, *plot_options, command=lambda value: update_plot('offensive', value) if value != 'Select Plot' else None)
    plot_dropdown.place(x=35, y=600)

    # Tooltip for help
    tooltip = Label(window, text='?', bg='blue', fg='white', font=('Arial', 12, 'bold'))
    tooltip.place(x=150, y=603)

    # Tooltip messages based on selected plot
    tooltip_messages = {
    'Select Plot': "Please select a plot type from the dropdown menu.",  
    'Histogram': "This histogram displays the distribution of offensive ratings across all NBA teams. \nEach bar represents the frequency of teams that fall within a specific range of offensive ratings. \nUse this to identify how many teams perform at different levels of offensive efficiency.",
    'Bar Plot': "This bar plot shows the offensive ratings of the top 10 NBA teams. \nThe height of each bar indicates the team's offensive rating, \nallowing for a quick comparison of offensive strength among the leading teams.",
    'Line Plot': "The line plot illustrates the offensive ratings of teams over the course of the season. \nEach point on the line represents a team's offensive rating at a specific time, \nhelping you track performance trends and identify peaks or drops in efficiency.",
    'Heatmap': "This heatmap visualizes the offensive ratings of the top teams in a color-coded format. \nDarker colors indicate higher offensive ratings, allowing for a quick visual assessment of which teams are performing best offensively.",
    'Scatter Plot': "The scatter plot compares offensive ratings against teams. \nEach point represents a team, positioned according to its offensive rating. \nThis plot helps identify any correlations between teams' performance and their ratings."
}

    def update_tooltip(event):
        message = tooltip_messages[selected_plot.get()]
        show_tooltip(event, message)

    tooltip.bind("<Enter>", update_tooltip)
    tooltip.bind("<Leave>", hide_tooltip)

    # Create a frame for the stats table on the right side
    global frame
    frame = Frame(window, width=600, height=500)  # Adjust width and height as needed
    frame.place(x=525, y=125)  # Position for the stats table

    # Create a Text widget for displaying stats
    table = tk.Text(frame, height=26, width=68, wrap=tk.NONE, padx=20, pady=20, bg="#1C1C1C", fg="white")
    table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame, command=table.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    table.config(yscrollcommand=scrollbar.set)

    # Insert column headers
    table.insert(tk.END, f"{'Team':<15} | {'PPG':<5} | {'EFG%':<4} | {'TS%':<4} | {'APG':<4} | {'TO Ratio':<4} | {'Off Ratings':<4}\n")
    table.insert(tk.END, "-" * 69 + "\n")  # Separator line

    sorted_df = df.sort_values(by="Off Ratings", ascending=False)

    # Insert teams and stats into the Text widget
    for index, row in sorted_df.iterrows():
        table.insert(tk.END, f"{row['Team']:<15} | {row['PPG']:<5} | {row['EFG%']:<3} | {row['TS%']:<3} | {row['APG']:<3} | {row['TO Ratio']:<8} | {row['Off Ratings']:<3}\n")

    home_button = Button(text="Home", padx=20, pady= 3, font=("Helvetica", 11), bg="#0C2340", fg="white", command=main, cursor="hand2", activebackground="#C8102E")
    home_button.bind("<Enter>", on_enter)
    home_button.bind("<Leave>", on_leave)
    home_button.place(x=515, y=670)

    save_button = Button(text="Save Data", padx=10, pady=3, font=("Helvetica", 10), bg="#C8102E", fg="white", command=save_offensive_stats, cursor="hand2", activebackground="#0C2340", activeforeground="white")
    save_button.bind("<Enter>", on_enter_red)
    save_button.bind("<Leave>", on_leave_red)
    save_button.place(x=750, y=595)

def defensive_ratings():
    # Clear the window and other widgets
    for widget in window.winfo_children():
        widget.place_forget()

    if text_widget:
        text_widget.place_forget()

    display_date.pack_forget()
    all_rights.pack_forget()

    label.config(text="2024-2025 NBA Top Defensive Teams", font=("Arial", 25, 'bold'))
    label.place(x=283, y=50)

    # Placeholder for the plot
    global image_label  # Declare image_label globally to manage it
    placeholder_image = Image.open("icons/Placeholder.png")  # Use a placeholder image
    resized_placeholder = placeholder_image.resize((450, 453), Image.LANCZOS)
    placeholder_tk = ImageTk.PhotoImage(resized_placeholder)

    # Create a label with the placeholder image
    image_label = Label(window, image=placeholder_tk)
    image_label.image = placeholder_tk  # Keep a reference to avoid garbage collection
    image_label.place(x=35, y=125)

    # Dropdown for plot selection
    plot_options = ['Histogram', 'Bar Plot', 'Line Plot', 'Heatmap', 'Scatter Plot']
    selected_plot = StringVar(window)
    selected_plot.set(plot_options[0])  # Set default value

    plot_dropdown = OptionMenu(window, selected_plot, *plot_options, command=lambda value: update_plot('defensive', value) if value != 'Select Plot' else None)
    plot_dropdown.place(x=35, y=600)

    # Tooltip for help
    tooltip = Label(window, text='?', bg='red', fg='white', font=('Arial', 12, 'bold'))
    tooltip.place(x=150, y=603)

    # Tooltip messages based on selected plot
    tooltip_messages = {
    'Histogram': "This histogram shows the distribution of defensive ratings across all NBA teams. \nEach bar represents how many teams fall into specific ranges of defensive ratings, \nallowing you to see which ratings are most common among teams.",
    'Bar Plot': "This bar plot displays the defensive ratings of the top 10 NBA teams. \nThe height of each bar represents the team's defensive rating, \nmaking it easy to compare the defensive strength of the leading teams.",
    'Line Plot': "The line plot depicts the defensive ratings of teams over the season. \nEach point on the line corresponds to a team's defensive rating at a given time, \nhelping you observe trends and fluctuations in defensive performance.",
    'Heatmap': "This heatmap provides a color-coded visualization of the defensive ratings of the top teams. \nDarker colors signify higher defensive ratings, allowing for quick visual comparisons of defensive strength.",
    'Scatter Plot': "The scatter plot illustrates the relationship between teams and their defensive ratings. \nEach point represents a team, plotted according to its defensive rating, \nwhich can help identify patterns or outliers in defensive performance."
}

    def update_tooltip(event):
        message = tooltip_messages[selected_plot.get()]
        show_tooltip(event, message)

    tooltip.bind("<Enter>", update_tooltip)
    tooltip.bind("<Leave>", hide_tooltip)

    # Create a frame for the stats table on the right side
    global frame
    frame = Frame(window, width=600, height=500)  # Adjust width and height as needed
    frame.place(x=525, y=125)  # Position for the stats table

    # Create a Text widget for displaying stats
    table = tk.Text(frame, height=26, width=68, wrap=tk.NONE, padx=20, pady=20, bg="#1C1C1C", fg="white")
    table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    scrollbar = tk.Scrollbar(frame, command=table.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    table.config(yscrollcommand=scrollbar.set)

    # Insert column headers
    table.insert(tk.END, f"{'Team':<15} | {'DRB':<5} | {'SPG':<4} | {'BPG':<4} | {'TOV':<4} | {'Def Ratings':<4}\n")
    table.insert(tk.END, "-" * 69 + "\n")  # Separator line

    sorted_df = df.sort_values(by="Def Ratings", ascending=False)

    # Insert teams and stats into the Text widget
    for index, row in sorted_df.iterrows():
        table.insert(tk.END, f"{row['Team']:<15} | {row['DRB']:<5} | {row['SPG']:<4} | {row['BPG']:<3} | {row['TOV'] :<5} | {row['Def Ratings']:<3}\n")

    home_button = Button(text="Home", padx=20, pady=3, font=("Helvetica", 12), bg="#0C2340", fg="white", command=main, cursor="hand2", activebackground="#C8102E")
    home_button.bind("<Enter>", on_enter)
    home_button.bind("<Leave>", on_leave)
    home_button.place(x=515, y=670)

    save_button = Button(text="Save Data", padx=10, pady=3, font=("Helvetica", 10), bg="#C8102E", fg="white", command=save_defensive_stats, cursor="hand2", activebackground="#0C2340", activeforeground="white")
    save_button.bind("<Enter>", on_enter_red)
    save_button.bind("<Leave>", on_leave_red)
    save_button.place(x=750, y=595)

def update_plot(plot_type, selected_plot):
    # Clear the placeholder image
    if 'image_label' in globals():
        image_label.place_forget()  # Remove the placeholder image

    # Create a new figure
    fig = Figure(figsize=(5, 4.5))  # Adjust size as needed
    ax = fig.add_subplot(111)

    # Set font size for axes
    font_size = 5  # Change this value to adjust font size

    if plot_type == 'offensive':
        # Get the top 10 teams based on 'Off Ratings'
        top_teams = df.sort_values(by='Off Ratings', ascending=False).head(10)

        if selected_plot == 'Histogram':
            ax.hist(df['Off Ratings'], bins=10, color='blue', alpha=0.7)
            ax.set_title('Histogram of Offensive Ratings')
            ax.set_xlabel('Offensive Ratings', fontsize=font_size)
            ax.set_ylabel('Frequency', fontsize=font_size)
        
        elif selected_plot == 'Bar Plot':
            sns.barplot(data=top_teams, x='Off Ratings', y='Team', ax=ax)
            ax.set_title('Top 10 Offensive Teams')
            ax.set_xlabel('Offensive Ratings', fontsize=font_size)
            ax.set_ylabel('Teams', fontsize=font_size)
            ax.tick_params(axis='y', labelsize=font_size)  # Set y-axis label size
        
        elif selected_plot == 'Line Plot':
            ax.plot(top_teams['Team'], top_teams['Off Ratings'], marker='o', linestyle='-', color='blue')
            ax.set_title('Top 10 Offensive Ratings Over Teams')
            ax.set_xlabel('Teams', fontsize=font_size)
            ax.set_ylabel('Offensive Ratings', fontsize=font_size)
            ax.tick_params(axis='y', rotation=90, labelsize=font_size)  # Set x-axis label size
        
        elif selected_plot == 'Heatmap':
            heatmap_data = top_teams[['Team', 'Off Ratings']].set_index('Team')
            sns.heatmap(heatmap_data, annot=True, cmap='YlGnBu', cbar=True, ax=ax)
            ax.set_title('Heatmap of Top 10 Offensive Ratings')
        
        elif selected_plot == 'Scatter Plot':
            ax.scatter(top_teams['Team'], top_teams['Off Ratings'], color='blue')
            ax.set_title('Scatter Plot of Top 10 Offensive Ratings')
            ax.set_xlabel('Teams', fontsize=font_size)
            ax.set_ylabel('Offensive Ratings', fontsize=font_size)
            ax.tick_params(axis='y', rotation=90, labelsize=font_size)  # Set x-axis label size

    elif plot_type == 'defensive':
        # Get the top 10 teams based on 'Def Ratings'
        top_teams = df.sort_values(by='Def Ratings', ascending=False).head(10)

        if selected_plot == 'Histogram':
            ax.hist(df['Def Ratings'], bins=10, color='red', alpha=0.7)
            ax.set_title('Histogram of Defensive Ratings')
            ax.set_xlabel('Defensive Ratings', fontsize=font_size)
            ax.set_ylabel('Frequency', fontsize=font_size)
        
        elif selected_plot == 'Bar Plot':
            sns.barplot(data=top_teams, x='Def Ratings', y='Team', palette='viridis', ax=ax)
            ax.set_title('Top 10 Defensive Teams')
            ax.set_xlabel('Defensive Ratings', fontsize=font_size)
            ax.set_ylabel('Teams', fontsize=font_size)
            ax.tick_params(axis='y', labelsize=font_size)  # Set y-axis label size
        
        elif selected_plot == 'Line Plot':
            ax.plot(top_teams['Team'], top_teams['Def Ratings'], marker='o', linestyle='-', color='red')
            ax.set_title('Top 10 Defensive Ratings Over Teams')
            ax.set_xlabel('Teams', fontsize=font_size)
            ax.set_ylabel('Defensive Ratings', fontsize=font_size)
            ax.tick_params(axis='y', rotation=90, labelsize=font_size)  # Set x-axis label size
        
        elif selected_plot == 'Heatmap':
            heatmap_data = top_teams[['Team', 'Def Ratings']].set_index('Team')
            sns.heatmap(heatmap_data, annot=True, cmap='YlGnBu', cbar=True, ax=ax)
            ax.set_title('Heatmap of Top 10 Defensive Ratings')
        
        elif selected_plot == 'Scatter Plot':
            ax.scatter(top_teams['Team'], top_teams['Def Ratings'], color='red')
            ax.set_title('Scatter Plot of Top 10 Defensive Ratings')
            ax.set_xlabel('Teams', fontsize=font_size)
            ax.set_ylabel('Defensive Ratings', fontsize=font_size)
            ax.tick_params(axis='y', rotation=90, labelsize=font_size)  # Set x-axis label size

    # Set font size for tick labels
    ax.tick_params(labelsize=font_size)

    # Create a canvas to embed the figure
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().place(x=15, y=129)      

tooltip_window = None

def show_tooltip(event, message):
    global tooltip_window
    if tooltip_window is not None:  # If a tooltip is already open, do not create a new one
        tooltip_window.destroy()

    tooltip_window = Toplevel(window)
    tooltip_window.wm_overrideredirect(True)
    tooltip_window.wm_geometry(f"+{event.x_root + 10}+{event.y_root + 10}")
    label = Label(tooltip_window, text=message, background="white", relief="solid", borderwidth=1)
    label.pack()

def hide_tooltip(event):
  global tooltip_window
  if tooltip_window is not None:
      tooltip_window.destroy()
      tooltip_window = None  

  tooltip_window.after(2000, hide_tooltip)

def hide_tooltip(event):
    global tooltip_window
    if tooltip_window is not None:
        tooltip_window.destroy()
        tooltip_window = None

def about():
    global text_widget

    for widget in window.winfo_children():
        widget.place_forget()
    
    display_date.pack_forget()
    all_rights.pack_forget()

    label.config(text="About", font=("Arial", 40, 'bold'))
    label.place(x=470, y=80)

    text_widget = tk.Text(window, wrap="word", width=90, height=17, font=("Helvetica", 15), bg="#1C1C1C", fg="white", padx=30, pady=30)
    text_widget.place(x=45 , y=170)

    paragraph = """Welcome to NBA Stats Scraper! Here, you will find pre-season statistics that highlight the top teams in offense and defense for the ongoing NBA Season, along with overall insights into the games of each basketball team.\n\nWe used web scraping techniques to collect all the needed data and imported the Pandas library to manage and analyze it effectively. With this method, we make sure that the predictions from the collected data are accurate for predicting the NBA Season games.\n\nWe will provide and show you all the important data to help you understand which teams are strong contenders this season. Get ready for an exciting ride as we uncover the challenges and surprises of the upcoming NBA Season!\n\nDeveloper:\nEnriquez, Andreiy\nMartinez, Joanna Mae\nOlmedo, Mark Nathan\nPalatino, Raymond Charles\nZamora, Kurt"""
    text_widget.insert("1.0", paragraph)

    # Make the Text widget read-only
    text_widget.config(state="disabled")

    home_button = Button(text="Home", padx=20, pady=3, font=("Helvetica", 11), bg="#0C2340", fg="white", command=main, cursor="hand2", activebackground="#C8102E")
    home_button.bind("<Enter>", on_enter)
    home_button.bind("<Leave>", on_leave)
    home_button.place(x=515, y=660)

main()
window.mainloop()