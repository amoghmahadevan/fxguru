from sys import float_repr_style
import pandas as pd

#Script for automating spreadsheets

WIDTHS = {
    'L:L' : 20,
    'B:F' : 9
}

def set_widths(pair, writer):
    worksheet = writer.sheets[pair]
    for k,v in WIDTHS.items():
        worksheet.set_column(k, v)

def get_line_chart(book, start_row, end_row, labels_col, data_col, title, sheetname):
    chart = book.add_chart({'type' : 'line'})
    chart.add_series({
        'categories' : [sheetname, start_row, labels_col, end_row, labels_col],
        'values' : [sheetname, start_row, data_col, end_row, data_col], 
        'line' : {'color' : 'blue'}
    })
    chart.set_title({'name' : title})
    chart.set_legend({'none' : True})
    return chart

def add_chart(pair, cross, df, writer):
    workbook = writer.book
    worksheet = writer.sheets[pair]

    chart = get_line_chart(workbook, 1, df.shape[0], 12, 13, 
                           f"C_GAIN for {pair} {cross}", pair)
    chart.set_size({'x_scale' : 2.5, 'y_scale' : 2.5})
    worksheet.insert_chart('O1', chart)

def add_pair_charts(df_ma_res, df_ma_trades, writer):
    cols = ['time', 'C_GAIN']
    #Data frame with first rows of each table of each pair
    df_temp = df_ma_res.drop_duplicates(subset = "pair")
    
    #All trades which have cross and pair of particular row in dataframe
    for _, row in df_temp.iterrows(): 
        dft = df_ma_trades[(df_ma_trades.cross == row.cross)&
                           (df_ma_trades.PAIR == row.pair)]
        dft[cols].to_excel(writer, sheet_name=row.pair, index=False, startrow=0, startcol=12)
        set_widths(row.pair, writer)
        add_chart(row.pair, row.cross, dft, writer)

def add_pair_sheets(df_ma_res, writer):
    #Write for particular pair the results to a table on its own sheet
    #With name of pair and descending order of total gain
    for p in df_ma_res.pair.unique():
        tdf = df_ma_res[df_ma_res.pair == p]
        tdf.to_excel(writer, sheet_name=p, index=False)

def prepare_data(df_ma_res, df_ma_trades):
    #Pairs to be in alphabetical order, gains in descending order (sorting)
    df_ma_res.sort_values(
        by = ['pair', 'total_gain'], 
        ascending =[True, False],
        inplace = True)
    df_ma_trades['time'] = [x.replace(tzinfo=None) for x in df_ma_trades['time']]

#Process DF data into excel sheet
def process_data(df_ma_res, df_ma_trades, writer):
    prepare_data(df_ma_res, df_ma_trades)
    #MA Cross Tables
    add_pair_sheets(df_ma_res, writer)
    #Charts
    add_pair_charts(df_ma_res, df_ma_trades, writer)

def create_excel(df_ma_res, df_ma_trades, granularity):
    filename = f"ma_sim_{granularity}.xlsx"
    #Pandas comes with excel writer
    writer = pd.ExcelWriter(filename, engine="xlsxwriter")
    process_data( #filter for granularity
        df_ma_res[df_ma_res.granularity == granularity].copy(), 
        df_ma_trades[df_ma_trades.GRANULARITY == granularity].copy(), 
        writer)
    writer.close()

def create_ma_res(granularity):
    df_ma_res = pd.read_pickle("./data/ma_res.pkl")
    df_ma_trades = pd.read_pickle("./data/ma_trades.pkl")
    create_excel(df_ma_res, df_ma_trades, granularity)

if __name__ == "__main__":
    #Creating excel sheet out of dataframes
    df_ma_res = pd.read_pickle("../data/ma_res.pkl")
    df_ma_trades = pd.read_pickle("../data/ma_trades.pkl")

    create_excel(df_ma_res, df_ma_trades, "H1")
    create_excel(df_ma_res, df_ma_trades, "H4")