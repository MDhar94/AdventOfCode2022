import pandas as pd

from params import LOCAL_DATA_PATH

data_path = LOCAL_DATA_PATH + '/Day2_data.csv'

df = pd.read_csv(data_path
            , delim_whitespace=True
            , header=None
            , names=['Opponent','Response'])

choice_dict2 = {'A':'Rock'
               , 'B':'Paper'
               ,'C':'Scissors'
               ,'X':'Lose'
               ,'Y':'Draw'
               ,'Z':'Win'}

choice_dict = {'A':'Rock'
               , 'B':'Paper'
               ,'C':'Scissors'
               ,'X':'Rock'
               ,'Y':'Paper'
               ,'Z':'Scissors'}

def part1(df):

    df = df.replace({'Opponent':choice_dict
            ,'Response':choice_dict})

    def score_calculator(row):

        combo_dict = {'loss':['RockPaper','PaperScissors','ScissorsRock'],
                    'draw':['RockRock','PaperPaper','ScissorsScissors'],
                    'win':['PaperRock','ScissorsPaper','RockScissors']}

        choice_score_dict = {'Rock':1,'Paper':2,'Scissors':3}
        combination = row['Response'] + row['Opponent']

        score = 0

        if combination in combo_dict['win']:
            score += 6 + choice_score_dict[row['Response']]

        elif combination in combo_dict['draw']:
            score += 3 + choice_score_dict[row['Response']]

        elif combination in combo_dict['loss']:
            score += 0 + choice_score_dict[row['Response']]

        return score

    df['Score'] = df.apply(lambda row: score_calculator(row),axis=1)

    return df.Score.sum()

def part2(df):

    df2 = df.rename(columns={'Response':'Result'}).replace({'Opponent':choice_dict
                                                        ,'Result':choice_dict2})

    def score_calculator2(row):

        combo_dict = {'RockLose':'Scissors', 'RockDraw':'Rock','RockWin':'Paper'
                    ,'ScissorsLose':'Paper','ScissorsDraw':'Scissors','ScissorsWin':'Rock'
                    ,'PaperLose':'Rock','PaperDraw':'Paper','PaperWin':'Scissors'}

        score_dict = {'Win':6,'Draw':3,'Lose':0}

        choice_score_dict = {'Rock':1,'Paper':2,'Scissors':3}

        combination = row['Opponent'] + row['Result']

        sign_played = combo_dict[combination]

        sign_score = choice_score_dict[sign_played]
        round_score = score_dict[row['Result']]

        return sign_score + round_score

    df2['score'] = df2.apply(lambda row: score_calculator2(row),axis=1)

    return df2['score'].sum()

if __name__ == '__main__':

    part1_output = part1(df)
    part2_output = part2(df)


    print(part1_output)

    print(part2_output)
