import pandas as pd

def prepare_scopus(file_name):
    pd.set_option('display.max_columns', 5)
    df_q = pd.read_excel(file_name, sheet_name='Journals Q1Q2', converters={'SourceID':str, 'Year':str})
    print(df_q)
    df_dis = pd.read_excel(file_name, sheet_name='Discontinued', converters={'SourceID':str})
    print(df_dis)
    df_a = pd.read_excel(file_name, sheet_name='Конференции А', converters={'SourceID': str})
    df_a['Year'] = '2016'
    df_a['A* в области компьютерных наук'] = 'Y'

    print(df_a)

    df_q.set_index(['SourceID'], inplace=True)
    df_dis.set_index(['SourceID'], inplace=True)
    df_q_dis = df_q[df_q.index.map(lambda x: x not in df_dis.index)]
    print(df_q_dis)


    # Так тоже работает, но решил оставить первый вариант, чтобы не добавлялись лишние колонки
    # df_q_dis = pd.merge(df_q, df_dis, on='SourceID', how="outer", indicator=True)
    # # print('Merged')
    # # print(df_q_dis)
    # df_q_dis = df_q_dis[df_q_dis['_merge'] == 'left_only']
    # print('Result')
    # print(df_q_dis)
    df_q_a = pd.merge(df_q_dis, df_a, on=['SourceID', 'WOS_SourceTitle', 'Year'], how="outer", indicator=True)
    print('Merged')
    print(df_q_a)
    # df_q_a = df_q_a[df_q_a['_merge'] != 'right_only']
    # print('Result')
    # print(df_q_a)
    df_q_a.to_excel('/home/amator/MEGA/Проекты/Социоцентр/Scopus qa.xlsx')

if __name__ == '__main__':
    prepare_scopus('/home/amator/MEGA/Проекты/Социоцентр/Scopus Q1Q2, Discontinued, ConfA.xlsx')

