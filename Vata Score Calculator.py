import pandas as pd

dataset_filepath = '/content/drive/My Drive/av/Vata_Dataset.csv'
df = pd.read_csv(dataset_filepath)

def calculate_sleep_score(minutes_asleep):
    if minutes_asleep < 360:
        return 2
    elif 360 <= minutes_asleep < 420:
        return 1
    elif 420 <= minutes_asleep < 540:
        return 0
    else:
        return 1

def calculate_bedtime_score(bedtime_routine):
    if 0 <= bedtime_routine < 60:
        return 0
    else:
        return 1

def calculate_sleep_quality_score(sleep_quality):
    if 1 <= sleep_quality <= 1.05:
        return 0
    elif 1.051 <= sleep_quality <= 1.10:
        return 1
    elif 1.101 <= sleep_quality <= 1.15:
        return 2
    else:
        return 3

def calculate_steps_score(steps_per_hour):
    if steps_per_hour < 2500:
        return 3
    elif 2500 <= steps_per_hour < 5000:
        return 2
    elif 5000 <= steps_per_hour < 7500:
        return 1
    elif 7500 <= steps_per_hour < 10000:
        return 0
    elif 10000 <= steps_per_hour < 12500:
        return 1
    else:
        return 2

def calculate_sedentary_score(sedentary_minutes):
    if sedentary_minutes < 240:
        return 1
    elif 240 <= sedentary_minutes <= 480:
        return 0
    elif 481 <= sedentary_minutes <= 660:
        return 1
    else:
        return 2

def calculate_activity_score(active_minutes):
    if active_minutes <= 45:
        return 0
    elif 45 < active_minutes <= 60:
        return 1
    else:
        return 2

df['Vata_Score'] = (
    df.apply(lambda row: calculate_sleep_score(row['TotalMinutesAsleep']), axis=1) +
    df.apply(lambda row: calculate_bedtime_score(row['BedtimeRoutine']), axis=1) +
    df.apply(lambda row: calculate_sleep_quality_score(row['SleepQuality']), axis=1) +
    df.apply(lambda row: calculate_steps_score(row['TotalSteps']), axis=1) +
    df.apply(lambda row: calculate_sedentary_score(row['SedentaryMinutes']), axis=1) +
    df.apply(lambda row: calculate_activity_score(row['ModeratelyActiveMinutes']), axis=1)
)

output_filepath = '/content/drive/My Drive/av/Vata_Dataset_with_Scores.csv'
df.to_csv(output_filepath, index=False)

print("Dataset with Vata Scores saved to:", output_filepath)
