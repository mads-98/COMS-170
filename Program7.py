# Madison Cronk
# 0582982
# Program #7
# COMS-170-01: Winter 2025
# Due: 04/011/2025
# Program #7 -  Create a program to calculate the statistics of competitors' completion times to aid in choosing new candidates for the MUCSOCS esports team. 
# ------------------------------------------------------------------
# Variable              Type        Purpose
# ------------------------------------------------------------------
# floatFast             float      fastest completion time
# floatSlow             float      slowest completion time
# floatAvg              float      average completion time
# floatVal              float      temporary variable local to calc_stats function that stores user input before adding it to the list comlpetion_times
# times                 list       completion times passed as an argument 
# completion_times      list       completion times collected from user
# 

def get_times():
    completion_times = []
    print("ENTER COMPLETION TIMES IN SECONDS OR ENTER -1 TO STOP")
    floatVal = 0.0
    while floatVal != -1:
        try:
            floatVal = float(input("Enter a completion time: "))
            if floatVal == -1:
                continue
            elif floatVal < 0:
                print("Please enter a positive number or -1 to stop.")
            else:
                completion_times.append(floatVal)
        except ValueError:
            print("Invalid input. Please enter numeric values only.")
        except Exception:
                print("An unexpected error occurred.")
    return completion_times

def calc_stats(times):
    if not times:
        print("No completion times were entered. Cannont calculate statistics.")
        return None, None, None
    floatFast = min(times)
    floatSlow = max(times)
    floatAvg = sum(times) / len(times)
    return floatFast, floatSlow, floatAvg

def display_reults(times, floatFast, floatSlow, floatAvg):
    print(f"The fastest completion time is: {floatFast:.2f} seconds")
    print(f"The slowest completion time is: {floatSlow:.2f} seconds")
    print(f"The average completion time is: {floatAvg:.2f} seconds")
    print("------------------------------------------------------------------")
    print("All completion times are:")
    for time in times:
        print(f"{time:.2f} seconds")
    print("------------------------------------------------------------------")

def main():
    try:
        completion_times = get_times()
        if completion_times:
            floatFast, floatSlow, floatAvg = calc_stats(completion_times)
            display_reults(completion_times, floatFast, floatSlow, floatAvg)
        else:
            print("No completion times were entered.")
    except ValueError:
        print("Invalid input. Please enter numeric values only.")
    except Exception:
        print("An unexpected error occurred.")

main()

# ------------------------------------------------------------------