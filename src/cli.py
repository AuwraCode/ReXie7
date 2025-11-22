import pandas as pd

def get_user_selection(df):
    """
    Interactive function for user to select mark and model.
    """

    #Select mark
    print("\n---SELECT BRAND---")

    #Getting available marks
    available_marks = df['mark'].value_counts()
    unique_marks = available_marks.index.tolist()

    #Display TOP5
    print("Most popular marks:")
    for mark, count in available_marks.head(5).items():
        print(f" -{mark.title()} ({count} units)")
    print("(Type 'ALL' to see all options)")

    selected_mark = "" 
    while True:
        user_input = input("\nEnter mark: ").lower().strip()

        if user_input == "ALL":
            print("\nAll marks: ", unique_marks)
            continue

        if user_input in unique_marks:
            selected_mark = user_input
            break
        else:
            print(f"ERROR: Mark '{user_input}' not found. Try e.g., 'toyota'.")

    #Select model (filtred by mark)
    print(f"\n---MODEL SELECTION ({selected_mark.upper()}---")

    #Filter df to find models for this specific mark
    mark_mask = df['mark'] == selected_mark
    available_models = df[mark_mask]['model'].value_counts()
    unique_models = available_models.index.tolist()

    #Display TOP5 models
    print(f"Most popular {selected_mark.title()} models")
    for model, count in available_models.head(5).items():
        print(f"-{model.title()} ({count} units)")
    print("(Type 'ALL' to see all options)")

    selected_model = ""
    while True:
        user_input = input("\nEnter model: ").lower().strip()

        if user_input == "all":
            print(f"\nALL {selected_mark.upper()} MODELS: ", unique_models)
            continue
        
        if user_input in unique_models:
            selected_model = user_input
            break
        else:
            print(f"ERROR:Model '{user_input}' does not exist for {selected_mark}.")

    return selected_mark, selected_model
