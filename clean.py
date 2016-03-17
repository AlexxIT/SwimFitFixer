import os
import sys


def clean_csv(input_name, output_name, lap_distance=0):
    import csv

    new_rows = []

    with open(input_name, 'rt') as f:
        reader = csv.reader(f, delimiter=',')

        title = reader.next()
        new_rows.append(title)

        total_distance = 0
        total_timer_time = 0
        avg_speed = 0
        num_laps = 0

        for row in reader:
            # ignore unknown message
            if row[2] == 'unknown':
                continue

            # add: Type, Local Number, Message
            new_row = row[0:3]

            for i in range(3, len(row), 3):
                # finish line on empty Field X
                if row[i] == '':
                    break

                # change total_distance and avg_speed if necessary
                if lap_distance > 0:
                    if row[0] == 'Data':
                        if row[2] == 'lap':
                            if row[i] == 'total_distance':
                                total_distance += lap_distance
                                row[i+1] = '%d.0' % lap_distance
                            elif row[i] == 'total_timer_time':
                                total_timer_time = float(row[i+1])
                            elif row[i] == 'avg_speed':
                                lap_speed = lap_distance / total_timer_time
                                avg_speed += lap_speed
                                num_laps += 1
                                row[i+1] = '%.3f' % lap_speed
                            elif row[i] == 'enhanced_avg_speed':
                                row[i+1] = '%.3f' % lap_speed
                        elif row[2] == 'session':
                            if row[i] == 'total_distance':
                                row[i+1] = '%d.0' % total_distance
                            elif row[i] == 'avg_speed' or row[i] == 'enhanced_avg_speed':
                                row[i+1] = '%.3f' % (avg_speed / num_laps)

                    # ignore avg_stroke_distance/total_calories fields if necessary
                    if row[i] not in ['unknown', 'avg_stroke_distance', 'total_calories']:
                        new_row += row[i:i+3]
                else:
                    # ignore unknown fields
                    if row[i] != 'unknown':
                        new_row += row[i:i+3]

            if len(new_row) > 3:
                new_rows.append(new_row)

    with open(output_name, 'wt') as f:
        writer = csv.writer(f, delimiter=',', lineterminator='\n')
        writer.writerows(new_rows)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print "Usage: %s input.csv output.csv [lap_distance]" % os.path.basename(__file__)
        sys.exit(0)

    lap_distance = int(sys.argv[3]) if len(sys.argv) >= 4 else 0

    clean_csv(sys.argv[1], sys.argv[2], lap_distance)
