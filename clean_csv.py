cat > clean_csv.py <<'PY'
# clean_csv.py
import sys
import pandas as pd

def clean_csv(infile, outfile):
    df = pd.read_csv(infile)
    # drop rows where all values are missing
    df = df.dropna(how='all')
    # trim whitespace from string columns
    for c in df.select_dtypes(include='object').columns:
        df[c] = df[c].str.strip()
    # drop exact duplicate rows
    df = df.drop_duplicates()
    # if an 'id' column exists, drop rows missing id
    if 'id' in df.columns:
        df = df[df['id'].notna()]
    # write cleaned file and print basic summary
    df.to_csv(outfile, index=False)
    print(f'Input rows: {len(pd.read_csv(infile))}, Cleaned rows: {len(df)}')
    print("Columns:", list(df.columns))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python3 clean_csv.py input.csv output.csv')
    else:
        clean_csv(sys.argv[1], sys.argv[2])
PY
