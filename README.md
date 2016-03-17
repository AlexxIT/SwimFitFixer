SwimFitFixer
===

Watch: Garmin Fenix 3 + HRM: Mio Link = can't store HR data in FIT file with Pool Swim mode.

But you can use Open Water Swim mode with disabled GPS.
Unfortunately, these files are not always loaded to the Garmin Connect.

This script fixes the broken Garmin FIT file.

How it works
---

1. Convert FIT file to CSV with Java Utility from FIT SDK.
2. Remove `unknown` fields from CSV file with Python script.
3. Optionally set `lap_distance` with Python script.
4. Convert CSV file to FIT file.
