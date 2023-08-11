# Vata

The scoring matrix after literature review is this

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

The diet chart is as follows

Vata Score	Category	Food	
0-5	No to Light Vata	"Favor warm, cooked, and easily digestible foods.
Incorporate plenty of healthy fats such as ghee, coconut oil, and olive oil.
Include nourishing and grounding foods like sweet potatoes, whole grains (cooked), cooked vegetables, and lentils.
Drink warm herbal teas (non-caffeinated) like ginger, cinnamon, and licorice.
Reduce raw foods, cold foods, and excessive caffeine."	

5-8	Moderate Vata	"Favor warm, cooked, and easily digestible foods.
Incorporate plenty of healthy fats such as ghee, coconut oil, and olive oil.
Include nourishing and grounding foods like sweet potatoes, whole grains (cooked), cooked vegetables, and lentils.
Drink warm herbal teas (non-caffeinated) like ginger, cinnamon, and licorice.
Reduce raw foods, cold foods, and excessive caffeine.
Include a variety of cooked vegetables, grains, and legumes.
Incorporate small amounts of dairy, if tolerated (e.g., warm milk with spices).
Include foods with mild natural sweetness like ripe fruits (in moderation) and sweet spices.
Hydrate well with warm water, herbal teas, and warm soups."	

>9	Extreme Vata	"Focus on stabilizing and grounding foods.
Opt for cooked, moist, and oily foods.
Prioritize cooked grains like rice and quinoa, well-cooked vegetables, and hearty soups.
Include ample healthy fats from avocados, nuts, seeds, and ghee.
Use warming spices like ginger, cinnamon, and cumin.
Stay hydrated with warm, non-caffeinated herbal teas."


Sources

https://www.banyanbotanicals.com/info/ayurvedic-living/living-ayurveda/health-guides/the-ayurvedic-approach-to-fitness/
https://www.who.int/publications-detail-redirect/9789240015128
https://www.ayurvedacollege.com/blog/ayurveda-and-exercise-how-much-is-too-much/
