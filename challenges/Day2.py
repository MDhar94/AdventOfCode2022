import pandas as pd

from params import LOCAL_DATA_PATH

data_path = LOCAL_DATA_PATH + '/Day2_data.csv'

df = pd.read_csv(data_path
            , delim_whitespace=True
            , header=None
            , names=['Opponent','Response'])

def part1(df):

    choice_dict = {'A':'Rock'
               , 'B':'Paper'
               ,'C':'Scissors'
               ,'X':'Rock'
               ,'Y':'Paper'
               ,'Z':'Scissors'}

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
    pass

if __name__ == '__main__':

    part1_output = part1(df)

    print(part1_output)
