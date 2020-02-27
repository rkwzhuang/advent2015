import re

input_string = """Vixen can fly 19 km/s for 7 seconds, but then must rest for 124 seconds.
Rudolph can fly 3 km/s for 15 seconds, but then must rest for 28 seconds.
Donner can fly 19 km/s for 9 seconds, but then must rest for 164 seconds.
Blitzen can fly 19 km/s for 9 seconds, but then must rest for 158 seconds.
Comet can fly 13 km/s for 7 seconds, but then must rest for 82 seconds.
Cupid can fly 25 km/s for 6 seconds, but then must rest for 145 seconds.
Dasher can fly 14 km/s for 3 seconds, but then must rest for 38 seconds.
Dancer can fly 3 km/s for 16 seconds, but then must rest for 37 seconds.
Prancer can fly 25 km/s for 6 seconds, but then must rest for 143 seconds."""

reindeer_descriptions = input_string.split("\n")
reindeer_stats = {}
race_stats = {}

pattern = r"(.*) can fly ([0-9]+) km/s for ([0-9]+) seconds, but then must rest for ([0-9]+) seconds."

for reindeer_description in reindeer_descriptions:
    print(reindeer_description)
    parsed_reindeer_description = re.search(pattern, reindeer_description)
    # print(parsed_reindeer_description)
    reindeer_name = parsed_reindeer_description.group(1)
    reindeer_speed = int(parsed_reindeer_description.group(2))
    reindeer_duration = int(parsed_reindeer_description.group(3))
    reindeer_rest_time = int(parsed_reindeer_description.group(4))

    reindeer_stats[reindeer_name] = {
        "speed": reindeer_speed,
        "duration": reindeer_duration,
        "rest_time": reindeer_rest_time
    }

    race_stats[reindeer_name] = {
        "distance": 0,
        "time": 0,
        "run": True,
        "score": 0
    }

print(reindeer_stats)
seconds = 2503
# seconds = 1000



for time in range(0,seconds):
    for reindeer in reindeer_stats.keys():
        if race_stats[reindeer]["run"]:
            race_stats[reindeer]["distance"] += reindeer_stats[reindeer]["speed"]
            race_stats[reindeer]["time"] += 1

            if race_stats[reindeer]["time"] == reindeer_stats[reindeer]["duration"]:
                race_stats[reindeer]["time"] = 0
                race_stats[reindeer]["run"] = False
        else:
            race_stats[reindeer]["time"] += 1
            if race_stats[reindeer]["time"] == reindeer_stats[reindeer]["rest_time"]:
                race_stats[reindeer]["time"] = 0
                race_stats[reindeer]["run"] = True

    max_score = max([race_stats[reindeer]['distance'] for reindeer in race_stats.keys()])

    winning_reindeers = [reindeer for reindeer in race_stats.keys() if race_stats[reindeer]['distance'] == max_score]

    for winning_reindeer in winning_reindeers:
        race_stats[winning_reindeer]["score"] += 1

    
    # if time == 143:
    #     print(race_stats)
    #     break
    
for reindeer in race_stats:
    print(reindeer, "score:", race_stats[reindeer]["score"])