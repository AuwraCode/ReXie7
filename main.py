#main.py

#Import biblioteki do zarządzania scieżkami
from pathlib import Path

#Import naszych wlasnych funkcji z folderu scr 
from src.data_loader import load_raw_data, save_processed_data
from src.preprocessing import clean_price_data, filter_target_car

def main():
    print("---[JDM_Forecaster] Start Procesu---")

    #Konfiguracja Celu
    TARGET_MARK = 'honda'
    TARGET_MODEL = 'fit'

    #Definiowanie ścieżek niezależnie od systemu operacyjnego
    #Path.cwd() to "Current Working Directory" 
    project_root = Path.cwd()
    raw_data_path = project_root / 'data' / 'raw' / 'cars_datasets.csv'

    #Ścieżki wyjściowe
    output_filename = f'processed_{TARGET_MARK}_{TARGET_MODEL}.csv'
    processed_data_path = project_root / 'data' / 'processed' / output_filename

    #Weryfikacja czy plik istnieje
    if not raw_data_path.exists():
        print(f"Error: Nie znaleziono pliku pod adresem: {raw_data_path}")
        return
    

    #Wczytywanie zaimportowanych funkcji
    df = load_raw_data(raw_data_path)

    #Czyszczenie
    df_cleaned = clean_price_data(df)

    #filtrowanie
    df_target = filter_target_car(df, TARGET_MARK, TARGET_MODEL)

    #Sprawdzanie czy po filtrowaniu coś zostalo
    if df_target.empty:
        print("Error: Zbiór danych jest pusty po filtrowaniu! Sprawdź nazwy marki/modelu!")
        return

    #Zapisywanie
    save_processed_data(df_target, processed_data_path)

    print("---[JDM_Forecaster] Proces Zakończony sukcesem---")

if __name__ == "__main__":
    main()